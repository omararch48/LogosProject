(() => {
    
    
    'use strict'
    
    
    let navBar = document.querySelector('.sidebar-menu');
    let videosVector = document.querySelectorAll('.logos-video');
    const buttonClicked = document.querySelector('.fa-bars');


    buttonClicked.addEventListener('click', () => {
        videosVector.forEach(element => {
            if (element.hasAttribute('controls')) {
                element.removeAttribute('controls');
                element.style.display = 'none';
            } else {
                element.setAttribute('controls', 'default');
                element.style.display = 'block';
            }
        });
        navBar.classList.toggle('active');
    });
    
    
    document.addEventListener('keydown', ({key}) => {
        if (key === 'Escape' && navBar.classList.contains('active')) {
            navBar.classList.toggle('active');
            videosVector.forEach(element => {
                if (element.hasAttribute('controls')) {
                    element.removeAttribute('controls');
                    element.style.display = 'none';
                } else {
                    element.setAttribute('controls', 'default');
                    element.style.display = 'block';
                }
            });
        }
    });


})();