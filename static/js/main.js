/**
 * SimpleWeb - Main JavaScript
 * Handles interactive elements and functionality
 */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all interactive elements
    initNavigation();
    initSmoothScroll();
    initContactForm();
    initAnimations();
});

/**
 * Handles mobile navigation toggle and active states
 */
function initNavigation() {
    // Get all navigation links
    const navLinks = document.querySelectorAll('.main-nav a');
    
    // Add click event listeners to each link
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            // Remove active class from all links
            navLinks.forEach(l => l.classList.remove('active'));
            
            // Add active class to clicked link
            this.classList.add('active');
        });
    });
    
    // Update active link based on scroll position
    window.addEventListener('scroll', function() {
        const scrollPosition = window.scrollY;
        
        // Get all sections
        const sections = document.querySelectorAll('section');
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop - 100;
            const sectionHeight = section.offsetHeight;
            const sectionId = section.getAttribute('id');
            
            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                // Remove active class from all links
                navLinks.forEach(link => link.classList.remove('active'));
                
                // Add active class to corresponding link
                const activeLink = document.querySelector(`.main-nav a[href="#${sectionId}"]`);
                if (activeLink) {
                    activeLink.classList.add('active');
                }
            }
        });
    });
}

/**
 * Implements smooth scrolling for anchor links
 */
function initSmoothScroll() {
    // Get all links that start with #
    const links = document.querySelectorAll('a[href^="#"]');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            // Prevent default anchor behavior
            e.preventDefault();
            
            // Get the target element
            const targetId = this.getAttribute('href');
            
            // Skip if it's just "#"
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                // Scroll to the element
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

/**
 * Handles contact form submission and validation
 */
function initContactForm() {
    const contactForm = document.querySelector('.contact-form');
    
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Basic form validation
            const nameInput = document.getElementById('name');
            const emailInput = document.getElementById('email');
            const messageInput = document.getElementById('message');
            
            let isValid = true;
            
            // Validate name
            if (!nameInput.value.trim()) {
                showError(nameInput, 'Please enter your name');
                isValid = false;
            } else {
                removeError(nameInput);
            }
            
            // Validate email
            if (!emailInput.value.trim()) {
                showError(emailInput, 'Please enter your email');
                isValid = false;
            } else if (!isValidEmail(emailInput.value)) {
                showError(emailInput, 'Please enter a valid email');
                isValid = false;
            } else {
                removeError(emailInput);
            }
            
            // Validate message
            if (!messageInput.value.trim()) {
                showError(messageInput, 'Please enter your message');
                isValid = false;
            } else {
                removeError(messageInput);
            }
            
            // If form is valid, submit it (in this demo, just show success message)
            if (isValid) {
                // In a real application, you would send the form data to a server here
                // For demo purposes, we'll just show a success message
                contactForm.innerHTML = '<div class="success-message">Thank you for your message! We\'ll get back to you soon.</div>';
            }
        });
    }
    
    // Helper function to show error message
    function showError(input, message) {
        const formGroup = input.parentElement;
        let errorElement = formGroup.querySelector('.error-message');
        
        if (!errorElement) {
            errorElement = document.createElement('div');
            errorElement.className = 'error-message';
            formGroup.appendChild(errorElement);
        }
        
        errorElement.textContent = message;
        input.classList.add('error');
    }
    
    // Helper function to remove error message
    function removeError(input) {
        const formGroup = input.parentElement;
        const errorElement = formGroup.querySelector('.error-message');
        
        if (errorElement) {
            formGroup.removeChild(errorElement);
        }
        
        input.classList.remove('error');
    }
    
    // Helper function to validate email format
    function isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }
}

/**
 * Adds scroll animations to elements
 */
function initAnimations() {
    // Add fade-in animation to feature cards
    const featureCards = document.querySelectorAll('.feature-card');
    
    // Create an intersection observer
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-fade-in');
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1
    });
    
    // Observe each feature card
    featureCards.forEach(card => {
        observer.observe(card);
    });
}

// Add CSS for animations
const style = document.createElement('style');
style.textContent = `
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .animate-fade-in {
        animation: fadeIn 0.6s ease forwards;
    }
    
    .feature-card {
        opacity: 0;
    }
    
    .error-message {
        color: #dc3545;
        font-size: 0.875rem;
        margin-top: 5px;
    }
    
    input.error, textarea.error {
        border-color: #dc3545;
    }
    
    .success-message {
        text-align: center;
        color: #28a745;
        padding: 20px;
        font-size: 1.1rem;
    }
`;

document.head.appendChild(style);