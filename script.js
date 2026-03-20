document.addEventListener('DOMContentLoaded', function() {
    // Smooth scrolling for navigation links
    const navLinks = document.querySelectorAll('nav a');

    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            // Only apply smooth scroll for on-page links (those that start with #)
            if (link.getAttribute('href').startsWith('#')) {
                e.preventDefault();
                const targetId = this.getAttribute('href');
                const targetSection = document.querySelector(targetId);

                if (targetSection) {
                    targetSection.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });

    // Testimonial Carousel
    const slides = document.querySelectorAll('.testimonial-slide');
    if (slides.length > 0) {
        let currentSlide = 0;
        const slideInterval = 5000; // Switch every 5 seconds

        function nextSlide() {
            // Remove active class from current slide
            slides[currentSlide].classList.remove('active');
            
            // Move to next slide
            currentSlide = (currentSlide + 1) % slides.length;
            
            // Add active class to new slide
            slides[currentSlide].classList.add('active');
        }

        setInterval(nextSlide, slideInterval);
    }
    // Square Pay Button Integration
    const payBtn = document.getElementById('nav-pay-btn');
    if (payBtn) {
        payBtn.addEventListener('click', function(e) {
            e.preventDefault();
            const url = this.getAttribute('data-url');
            const title = 'Square Payment Links';
            const topWindow = window.top ? window.top : window;
            const dualScreenLeft = topWindow.screenLeft !== undefined ? topWindow.screenLeft : topWindow.screenX;
            const dualScreenTop = topWindow.screenTop !== undefined ? topWindow.screenTop : topWindow.screenY;
            const width = topWindow.innerWidth ? topWindow.innerWidth : document.documentElement.clientWidth ? document.documentElement.clientWidth : screen.width;
            const height = topWindow.innerHeight ? topWindow.innerHeight : document.documentElement.clientHeight ? document.documentElement.clientHeight : screen.height;
            const h = height * .75;
            const w = 500;
            const systemZoom = width / topWindow.screen.availWidth;
            const left = (width - w) / 2 / systemZoom + dualScreenLeft;
            const top = (height - h) / 2 / systemZoom + dualScreenTop;
            const newWindow = window.open(url, title, `scrollbars=yes, width=${w / systemZoom}, height=${h / systemZoom}, top=${top}, left=${left}`);
            if (window.focus) newWindow.focus();
        });
    }
});