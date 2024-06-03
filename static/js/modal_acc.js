const customBackdrop = document.querySelector('.custom-backdrop');
    const customModalBtnOpen = document.querySelector('.custom-modal-btn-open');
    const customModalBtnClose = document.querySelector('.custom-modal-btn-close');

    const toggleCustomModal = () => customBackdrop.classList.toggle('is-hidden');

    customModalBtnOpen.addEventListener('click', toggleCustomModal);
    customModalBtnClose.addEventListener('click', toggleCustomModal);

    window.addEventListener('click', (event) => {
        if (event.target === customBackdrop) {
            toggleCustomModal();
        }
    });

// Функція для зміни стану модального вікна








