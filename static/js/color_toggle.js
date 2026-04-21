(function () {
    const root = document.documentElement;
    const colorInput = document.getElementById("colorToggle");

    if (!colorInput) return;

    const applyColor = (color) => {
        root.style.setProperty("--bs-primary", color);
        localStorage.setItem("accentColor", color);
    };

    const savedColor = localStorage.getItem("accentColor");
    if (savedColor) {
        colorInput.value = savedColor;
        applyColor(savedColor);
    }

    colorInput.addEventListener("input", function () {
        applyColor(this.value);
    });
})();