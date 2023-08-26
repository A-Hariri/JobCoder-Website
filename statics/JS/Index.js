const navbar = document.querySelector("#navbar");

let lastScrollTop = 0;

window.addEventListener(
    "scroll",
    () => {
        console.log("scroll");
        var { pageYOffset } = window;
        if (pageYOffset > lastScrollTop) {
            // downward scroll
            navbar.classList.remove("visible");
        } else if (pageYOffset < lastScrollTop) {
            // upward scroll
            navbar.classList.add("visible");
        } // else was horizontal scroll
        lastScrollTop = pageYOffset <= 0 ? 0 : pageYOffset;
    },
    { passive: true }
);

// ___________________________________________________________________________________________________________________

gsap.registerPlugin(ScrollTrigger);

const sections = gsap.utils.toArray(".panel"),
    container = document.querySelector(".container");

gsap.to(sections, {
    xPercent: -100 * (sections.length - 1),
    ease: "none",
    scrollTrigger: {
        trigger: ".container",
        pin: true,
        scrub: 1,
        snap: 1 / (sections.length - 1),
        end: () => "+=" + container.offsetWidth,
    },
});



function myFunction() {
    var selectedCity = document.querySelector(".options-country li.selected").textContent;
    var selectedJob = document.querySelector(".options-job li.selected").textContent;

    document.getElementById("selectedCityInput").value = selectedCity;
    document.getElementById("selectedJobInput").value = selectedJob;
}

// -------------------------------------------------------------------------------------------------------------------
