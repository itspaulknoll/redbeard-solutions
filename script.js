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
    // Square Pay Modal Integration
    const payBtn = document.getElementById('nav-pay-action');
    const squareModal = document.getElementById('square-modal');
    const closeSquareModal = document.getElementById('close-square-modal');

    if (payBtn && squareModal && closeSquareModal) {
        payBtn.addEventListener('click', function(e) {
            e.preventDefault();
            squareModal.style.display = 'flex';
            document.body.style.overflow = 'hidden'; // prevent background scrolling
        });

        closeSquareModal.addEventListener('click', function() {
            squareModal.style.display = 'none';
            document.body.style.overflow = '';
        });

        // Close when clicking outside the modal content
        squareModal.addEventListener('click', function(e) {
            if (e.target === squareModal) {
                squareModal.style.display = 'none';
                document.body.style.overflow = '';
            }
        });
    }
});