
(function () {
    const storageKey = "student-management-theme";
    const root = document.documentElement;

    // Restore the previously selected theme.
    let savedTheme = null;

    try {
        savedTheme = localStorage.getItem(storageKey);
    } catch (error) {
        // The theme still works if storage is unavailable.
    }

    function applyTheme(theme) {
        const isDark = theme === "dark";

        root.classList.toggle("dark-mode", isDark);

        if (toggleButton) {
            toggleButton.textContent = isDark
                ? "☀️ Light mode"
                : "🌙 Dark mode";

            toggleButton.setAttribute(
                "aria-pressed",
                String(isDark)
            );
        }
    }

    let toggleButton = null;

    // Create the same toggle on every connected page.
    function createToggle() {
        toggleButton = document.createElement("button");
        toggleButton.type = "button";
        toggleButton.className = "theme-toggle";
        toggleButton.setAttribute(
            "aria-label",
            "Switch color theme"
        );

        toggleButton.addEventListener("click", function () {
            const isDark = root.classList.contains("dark-mode");
            const newTheme = isDark ? "light" : "dark";

            applyTheme(newTheme);

            try {
                localStorage.setItem(storageKey, newTheme);
            } catch (error) {
                // Theme works for this page without persistence.
            }
        });

        document.body.appendChild(toggleButton);
        applyTheme(root.classList.contains("dark-mode") ? "dark" : "light");
    }

    // Apply the saved theme before displaying the toggle.
    applyTheme(savedTheme === "dark" ? "dark" : "light");

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", createToggle);
    } else {
        createToggle();
    }
})();
