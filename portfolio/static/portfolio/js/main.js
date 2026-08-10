document.addEventListener("DOMContentLoaded", () => {
    if (window.lucide) {
        window.lucide.createIcons({ attrs: { "aria-hidden": "true" } });
    }

    const nav = document.querySelector(".portfolio-nav");
    const updateNav = () => nav?.classList.toggle("scrolled", window.scrollY > 24);
    updateNav();
    window.addEventListener("scroll", updateNav, { passive: true });

    const revealItems = document.querySelectorAll(".reveal");
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
        revealItems.forEach((item) => item.classList.add("in-view"));
    } else {
        const observer = new IntersectionObserver(
            (entries) => {
                entries.forEach((entry) => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add("in-view");
                        observer.unobserve(entry.target);
                    }
                });
            },
            { threshold: 0.08, rootMargin: "0px 0px -30px" }
        );
        revealItems.forEach((item) => observer.observe(item));
    }

    const search = document.querySelector("#projectSearch");
    const rows = [...document.querySelectorAll("#projectArchive .archive-row")];
    const resultCount = document.querySelector("#projectResultCount");
    const noResults = document.querySelector("#noResults");

    if (search && rows.length) {
        search.addEventListener("input", () => {
            const query = search.value.trim().toLowerCase();
            let visible = 0;
            rows.forEach((row) => {
                const matches = !query || row.dataset.search.includes(query);
                row.hidden = !matches;
                if (matches) visible += 1;
            });
            if (resultCount) resultCount.textContent = `${visible} ${visible === 1 ? "project" : "projects"}`;
            if (noResults) noResults.hidden = visible !== 0;
        });
    }
});
