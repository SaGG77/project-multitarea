(function () {
    const root = document.documentElement;
    const toggleBtns = document.querySelectorAll(".themeToggle");
    
    const getPreferredTheme = () => localStorage.getItem("theme") || "light";

    const setTheme = (theme) => {
    root.setAttribute("data-bs-theme", theme);
        toggleBtns.forEach(btn => {
            const icon = btn.querySelector("i");

            if (icon) {
                icon.className =theme === "dark" ? "bi bi-sun" : "bi bi-moon-stars" ;
            }
        });

     localStorage.setItem("theme", theme);
    };
    
    setTheme(getPreferredTheme());


    toggleBtns.forEach(btn => {
            btn.addEventListener('click', function () {
                const current = root.getAttribute("data-bs-theme") || "light";
                setTheme(current === "dark" ? "light" : "dark");
            });
        });
})();