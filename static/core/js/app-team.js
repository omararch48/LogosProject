(() => {


    'use strict'

    
    /* Vectors and elements */

    const teamModalContainer = document.querySelector('.team-modal-container');
    const leftArrow = document.querySelector('.left');
    const rightArrow = document.querySelector('.right');
    const infoVector = document.querySelectorAll('.team-info');
    const nameVector = document.querySelectorAll('.team-name-bar h4');
    const modalVector = document.querySelectorAll('.team-modal-info');
    const closeVector = document.querySelectorAll('.team-modal-close');
    let index = 0;


    /* Functions */ 

    const setProperties = function(index) {
        infoVector[index].classList.toggle('display-none');
        infoVector[index].classList.toggle('display-flex');
        nameVector[index].classList.toggle('display-none');
        nameVector[index].classList.toggle('display-block');
    }


    const setPropertiesModal = function(index) {
        teamModalContainer.classList.toggle('display-none');
        teamModalContainer.classList.toggle('display-flex');
        modalVector[index].classList.toggle('display-none');
        modalVector[index].classList.toggle('display-block');
    }


    /* Start selections */ 

    setProperties(index);


    leftArrow.addEventListener('click', () => {
        setProperties(index);
        if (index == 0) {
            index = nameVector.length - 1;
        } else {
            index = index - 1;
        }
        setProperties(index);
    });


    rightArrow.addEventListener('click', () => {
        setProperties(index);
        if (index == nameVector.length - 1) {
            index = 0;
        } else {
            index = index + 1;
        }
        setProperties(index);
    });


    infoVector.forEach(element => {
        element.addEventListener('click', () => {
            setPropertiesModal(index);
        })
    });


    nameVector.forEach(element => {
        element.addEventListener('click', () => {
            setPropertiesModal(index);
        })
    });


    closeVector.forEach(element => {
        element.addEventListener('click', () => {
            setPropertiesModal(index);
        });
    });


    document.addEventListener('keydown', ({key}) => {
        if (key === 'Escape' && modalVector[index].classList.contains('display-block')) {
            setPropertiesModal(index);
        }
    });


})();