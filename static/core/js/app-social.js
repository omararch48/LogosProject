(() => {


    'use strict'


    let socialSelected = document.querySelector('.modal-container-info-active');
    let socialModal = document.querySelector('.modal-container');
    let closeSelection = document.querySelectorAll('.modal-close');
    let socialGridSelection = document.querySelectorAll('.social-grid-card');
    let socialModalSelection = document.querySelectorAll('.modal-container-info');
    
    
    document.addEventListener('keydown', ({key}) => {
        if (key === 'Escape' && socialModal.style.display === 'flex') {
            socialSelected = document.querySelector('.modal-container-info-active');
            socialSelected.classList.toggle('modal-container-info-active');
            socialSelected.classList.toggle('modal-container-info');
            socialModal = document.querySelector('.modal-container');
            socialModal.style.display = 'none';
        }
    });
    
    
    closeSelection.forEach((closeElement) => {
        closeElement.addEventListener('click', () => {
            for (let i = 0; i < closeSelection.length; i++) {
                if (closeSelection[i] == closeElement) {
                    socialModalSelection[i].classList.toggle('modal-container-info-active');
                    socialModalSelection[i].classList.toggle('modal-container-info');
                    socialModal.style.display = 'none';
                }
    
            }
        })
    });
    
    
    socialGridSelection.forEach((socialElementGrid) => {
        socialElementGrid.addEventListener('click', () => {
            for (let i = 0; i < socialGridSelection.length; i++) {
                if (socialGridSelection[i] == socialElementGrid) {
                    socialModalSelection[i].classList.toggle('modal-container-info');
                    socialModalSelection[i].classList.toggle('modal-container-info-active');
                    socialModal.style.display = 'flex';
                }
    
            }
        })
    });


})();