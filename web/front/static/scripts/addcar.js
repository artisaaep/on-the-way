// document.getElementById('back').onclick = function () {
//     window.location.href = 'profile.html';
// };

let url = "https://d2fd-188-130-155-177.ngrok-free.app";

let model;
let number;
let color;

const addButton = window.document.getElementById('ADDcarBtn');
addButton.onclick = async function (evt) {
    const modelInput = window.document.getElementById('p1');
    const numberInput = window.document.getElementById('p2');
    const colorInput = window.document.getElementById('p3');
    if (!modelInput.value || !numberInput.value || !colorInput.value) {
        window.Telegram.WebApp.showAlert("Not all data is filled");
        return false;
    }
    await fetch(url + "/api/cars/", {
        method: 'POST',
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            "owner_id" : window.Telegram.WebApp.initDataUnsafe.user.id,
            "number"   : numberInput.value,
            "brand"    : modelInput.value,
            "color"    : colorInput.value,
        }),
    }).then(async response => {
        if (response.ok) {
            const bar = document.getElementById("carchoice");
            const response = await (await fetch(url + "/api/users/" + window.Telegram.WebApp.initDataUnsafe.user.id, {
                method: "GET",
            })).json();
            bar.innerHTML = ``;
            response.car_ids.forEach(async(id) => {
                const response = await (await fetch(url + "/api/cars/" + id, {
                    method: "GET",
                })).json();
                bar.innerHTML += `
                    <li>
                        <label for="car${id}">
                            <input  type="radio" id="car${id}" name="${response.brand}">
                            <div class="checkbox__checkmark"></div>
                            ${response.brand}
                        </label>
                    </li>
                `
            });

            const modal = document.getElementById('myModal');
            modal.querySelector('.modal-content').classList.remove('show');
        setTimeout(() => {
            modal.classList.remove('show');
            setTimeout(() => {
                modal.style.display = 'none';
            }, 300);
        }, 10);
        } else {
            window.Telegram.WebApp.showAlert("Something went wrong");
        }
    })

}