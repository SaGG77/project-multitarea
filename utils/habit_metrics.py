from __future__ import annotations

from collections import defaultdict
from datetime import date, timedelta

from sqlalchemy import func

from extensions import db
from models.habit import Habit
from models.habit_log import HabitLog


def clamp_range_days(value: int, minimum: int = 1, maximum: int = 365) -> int:
    return max(minimum, min(value, maximum))


def date_series(days: int, end_date: date | None = None) -> list[date]:
    end_date = end_date or date.today()
    start_date = end_date - timedelta(days=days - 1)
    return [start_date + timedelta(days=offset) for offset in range(days)]


def habit_completed_dates(habit_id: int) -> set[date]:
    rows = (
        db.session.query(HabitLog.log_date)
        .filter(
            HabitLog.habit_id == habit_id,
            HabitLog.completed.is_(True),
        )
        .all()
    )
    return {row.log_date for row in rows}


def calculate_streaks(completed_dates: set[date]) -> tuple[int, int]:
    if not completed_dates:
        return 0, 0

    today = date.today()
    current = 0
    cursor = today if today in completed_dates else today - timedelta(days=1)

    while cursor in completed_dates:
        current += 1
        cursor -= timedelta(days=1)

    best = 0
    running = 0
    previous = None

    for log_day in sorted(completed_dates):
        if previous and log_day == previous + timedelta(days=1):
            running += 1
        else:
            running = 1

        best = max(best, running)
        previous = log_day

    return current, best


def habit_completion_rate(habit_id: int, days: int) -> float:
    start_date = date.today() - timedelta(days=days - 1)

    completed = (
        db.session.query(func.count(HabitLog.id))
        .filter(
            HabitLog.habit_id == habit_id,
            HabitLog.completed.is_(True),
            HabitLog.log_date >= start_date,
        )
        .scalar()
    )

    return round((completed / days) * 100, 1) if days else 0.0


def global_completion_rate(user_id: int, days: int) -> float:
    active_habit_ids = [
        row.id
        for row in Habit.query.filter_by(user_id=user_id, is_active=True)
        .with_entities(Habit.id)
        .all()
    ]

    if not active_habit_ids:
        return 0.0

    start_date = date.today() - timedelta(days=days - 1)

    completed_total = (
        db.session.query(func.count(HabitLog.id))
        .filter(
            HabitLog.habit_id.in_(active_habit_ids),
            HabitLog.completed.is_(True),
            HabitLog.log_date >= start_date,
        )
        .scalar()
    )

    denominator = len(active_habit_ids) * days
    return round((completed_total / denominator) * 100, 1) if denominator else 0.0


def global_streaks(user_id: int) -> tuple[int, int]:
    rows = (
        db.session.query(HabitLog.log_date)
        .join(Habit, Habit.id == HabitLog.habit_id)
        .filter(
            Habit.user_id == user_id,
            Habit.is_active.is_(True),
            HabitLog.completed.is_(True),
        )
        .group_by(HabitLog.log_date)
        .all()
    )

    return calculate_streaks({row.log_date for row in rows})


def summary_series_for_user(user_id: int, days: int) -> dict:
    dates = date_series(days)
    labels = [d.isoformat() for d in dates]

    active_habit_ids = [
        row.id
        for row in Habit.query.filter_by(user_id=user_id, is_active=True)
        .with_entities(Habit.id)
        .all()
    ]

    counts_by_date = defaultdict(int)

    if active_habit_ids:
        rows = (
            db.session.query(HabitLog.log_date, func.count(HabitLog.id))
            .filter(
                HabitLog.habit_id.in_(active_habit_ids),
                HabitLog.completed.is_(True),
                HabitLog.log_date >= dates[0],
            )
            .group_by(HabitLog.log_date)
            .all()
        )

        counts_by_date.update({log_day: count for log_day, count in rows})

    values = [counts_by_date[d] for d in dates]

    habits = (
        Habit.query
        .filter_by(user_id=user_id)
        .order_by(Habit.name.asc())
        .all()
    )

    habits_rates = [
        {"name": habit.name, "value": habit_completion_rate(habit.id, days)}
        for habit in habits
    ]

    return {
        "series": {"labels": labels, "values": values},
        "habits": habits_rates,
    }


def weekday_counts_for_user(user_id: int, days: int) -> dict:
    start_date = date.today() - timedelta(days=days - 1)

    rows = (
        db.session.query(HabitLog.log_date)
        .join(Habit, Habit.id == HabitLog.habit_id)
        .filter(
            Habit.user_id == user_id,
            HabitLog.completed.is_(True),
            HabitLog.log_date >= start_date,
        )
        .all()
    )

    labels = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
    values = [0] * 7

    for (log_day,) in rows:
        values[log_day.weekday()] += 1

    return {"labels": labels, "values": values}