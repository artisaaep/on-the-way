document.addEventListener('DOMContentLoaded', (event) => {
    const comment = document.getElementById('comment');

    document.addEventListener('click', handleClickOutside);
    document.addEventListener('touchstart', handleClickOutside);
    document.addEventListener("touchend", handleClickOutside);
    document.addEventListener("touchcancel", handleClickOutside);
    document.addEventListener("touchmove", handleClickOutside);

    function handleClickOutside(event) {
        console.log('Event type:', event.type);
        if (comment === document.activeElement && !comment.contains(event.target)) {
            console.log('Click outside textarea');
            comment.blur(); 
        }
    }
});

document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('.dir-button');

    buttons.forEach(button => {
        button.addEventListener('click', () => {
            // Сохраняем текущий контент кнопки
            const currentContent = button.innerHTML;

            // Очищаем кнопку
            button.innerHTML = '';

            // Создаем новые кнопки
            const newButton1 = document.createElement('button');
            newButton1.className = 'new-button';
            newButton1.id = 'upper';
            newButton1.textContent = 'Иннополис';

            const newButton2 = document.createElement('button');
            newButton2.className = 'new-button';
            newButton2.id = 'lower';
            newButton2.textContent = 'Казань';

            newButton1.addEventListener('click', () => {
                newButton1.style.backgroundColor = '#969696'; 
            });

            newButton2.addEventListener('click', () => {
                newButton2.style.backgroundColor = '#969696'; 
            });

            button.appendChild(newButton1);
            button.appendChild(newButton2);

            button.setAttribute('disabled', '');
        });
    });
});


