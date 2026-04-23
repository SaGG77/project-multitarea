(function () {
    const root = document.documentElement;
    const colorInput = document.getElementById("colorToggle");

    const clamp = (value) => Math.max(0, Math.min(255, value));

    const hexToRgb = (hex) => {
        const clean = hex.replace("#", "");
        const bigint = parseInt(clean, 16);

        return {
            r: (bigint >> 16) & 255,
            g: (bigint >> 8) & 255,
            b: bigint & 255
        };
    };

    const rgbToHex = (r, g, b) => {
        return "#" + [r, g, b]
            .map(value => clamp(value).toString(16).padStart(2, "0"))
            .join("");
    };

    const lighten = (hex, amount) => {
        const { r, g, b } = hexToRgb(hex);
        return rgbToHex(r + amount, g + amount, b + amount);
    };

    const applyColor = (color) => {
        const lighterColor = lighten(color, 30);

        root.style.setProperty("--app-primary", color);
        root.style.setProperty("--app-primary-strong", lighterColor);
        root.style.setProperty("--app-navbar-start", color);
        root.style.setProperty("--app-navbar-end", lighterColor);

        localStorage.setItem("accentColor", color);
    };

    const savedColor = localStorage.getItem("accentColor");
    if (savedColor) {
        applyColor(savedColor);

        if (colorInput) {
            colorInput.value = savedColor;
        }
    }

    if (colorInput) {
        colorInput.addEventListener("input", function () {
            applyColor(this.value);
        });
    }
})();