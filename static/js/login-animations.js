document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector('.form-container');
    
    form.style.opacity = 0;
    form.style.transform = 'translateY(50px)';
    
    setTimeout(() => {
        form.style.transition = 'opacity 1s ease, transform 1s ease';
        form.style.opacity = 1;
        form.style.transform = 'translateY(0)';
    }, 500);
});
