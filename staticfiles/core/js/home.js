// Menu toggle functionality
document.querySelector('.menu-toggle').addEventListener('click', function() {
    const dropdownMenu = document.querySelector('.dropdown-menu');
    dropdownMenu.classList.toggle('active');
});

// Close dropdown when clicking outside
document.addEventListener('click', function(e) {
    const menuToggle = document.querySelector('.menu-toggle');
    const dropdownMenu = document.querySelector('.dropdown-menu');
    
    if (!menuToggle.contains(e.target) && !dropdownMenu.contains(e.target)) {
        dropdownMenu.classList.remove('active');
    }
});

// Dropdown item functionality
document.querySelectorAll('.dropdown-item').forEach(item => {
    item.addEventListener('click', function(e) {
        e.preventDefault();
        const action = this.textContent;
        
        switch(action) {
            case 'Home':
                window.scrollTo({ top: 0, behavior: 'smooth' });
                break;
            case 'Login':
                window.location.href = "login.html";
                break;

             case 'Profile':
                window.location.href = "profile.html";
                break;   
           
            case 'Logout':
                alert('You have been logged out!');
                break;
        }
        
        document.querySelector('.dropdown-menu').classList.remove('active');
    });
});

// Search functionality
document.querySelector('.search-bar').addEventListener('keyup', function(e) {
    const searchTerm = e.target.value.toLowerCase();
    const boxes = document.querySelectorAll('.box');
    
    boxes.forEach(box => {
        const title = box.querySelector('h3').textContent.toLowerCase();
        const content = box.querySelector('p').textContent.toLowerCase();
        
        if (title.includes(searchTerm) || content.includes(searchTerm)) {
            box.style.display = 'flex';
        } else {
            box.style.display = 'none';
        }
    });
});

// Footer icon interactions
document.querySelectorAll('.footer-icon').forEach(icon => {
    icon.addEventListener('click', function() {
        const action = this.querySelector('.icon-text').textContent;
        
        
    });
});

// Footer links functionality
document.querySelectorAll('.footer-links a, .social-links a').forEach(link => {
    link.addEventListener('click', function(e) {
        e.preventDefault();
        const linkType = this.textContent || this.getAttribute('aria-label');
        alert('You clicked on ${linkType}');
    });
});

// Make the entire page scrollable
document.addEventListener('DOMContentLoaded', function() {
    // Ensure all content is scrollable
    document.body.style.overflow = 'auto';
});