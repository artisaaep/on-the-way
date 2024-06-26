document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('myModal');
    const openModalBtn = document.getElementById('addcar');
    const closeModalBtn = document.querySelector('.close');

    // Функция для открытия модального окна
    function openModal() {
        modal.style.display = 'block';
        setTimeout(() => {
            modal.classList.add('show');
            modal.querySelector('.modal-content').classList.add('show');
        }, 10); // Небольшая задержка для запуска анимации
    }

    document.addEventListener('click', function(event) {
        var isClickInside = document.querySelector('.vvod').contains(event.target);

        if (!isClickInside) {
            document.querySelector('.vvod').blur(); // Убираем фокус с текстового поля
        }
    });

    // Функция для закрытия модального окна
    function closeModal() {
        modal.querySelector('.modal-content').classList.remove('show');
        setTimeout(() => {
            modal.classList.remove('show');
            setTimeout(() => {
                modal.style.display = 'none';
            }, 300); // Длительность перехода должна совпадать с CSS transition
        }, 10); // Небольшая задержка для запуска анимации
    }

    // Открываем модальное окно при клике на кнопку
    openModalBtn.addEventListener('click', openModal);

    // Закрываем модальное окно при клике на "X"
    closeModalBtn.addEventListener('click', closeModal);

    // Закрываем модальное окно при клике вне его содержания
    window.addEventListener('click', function(event) {
        if (event.target == modal) {
            closeModal();
        }
    });
});
