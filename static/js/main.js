// For page load animation
document.addEventListener('DOMContentLoaded', function() {
    const logo = document.querySelector('.logo');
    logo.classList.add('logo-animate');
    
    // Remove the class after animation completes
    setTimeout(() => {
        logo.classList.remove('logo-animate');
    }, 2000);
});

// For scroll-triggered animation (optional)
window.addEventListener('scroll', function() {
    const logo = document.querySelector('.logo');
    if (window.scrollY > 100 && !logo.classList.contains('scrolled')) {
        logo.classList.add('scrolled');
    }
});


// Counter animation for stats
function animateCounters() {
    const counters = document.querySelectorAll('.stat');
    const speed = 200;
    
    counters.forEach(counter => {
        const target = +counter.getAttribute('data-count');
        const count = +counter.innerText;
        const increment = target / speed;
        
        if(count < target) {
            counter.innerText = Math.ceil(count + increment);
            setTimeout(animateCounters, 1);
        } else {
            counter.innerText = target;
        }
    });
}

// Initialize when scrolled to impact section
function initAnimations() {
    const impactSection = document.querySelector('.impact-section');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounters();
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    if (impactSection) {
        observer.observe(impactSection);
    }
}

document.addEventListener('DOMContentLoaded', initAnimations);