document.getElementById('back').onclick = function () {
    window.location.href = 'profile.html';
};

let url = process.env["BASE_WEBAPP_URL "];

let model;
let number;
let color;

const modelInput = window.document.getElementById('p1');
const numberInput = window.document.getElementById('p2');
const colorInput = window.document.getElementById('p3');

modelInput.oninput = function (evt) {

}

numberInput.oninput = function (evt) {

}

colorInput.oninput = function (evt) {

}

const addButton = window.document.getElementById('ADD');
addButton.onclick = async function (evt) {
    if (!modelInput.value || !numberInput.value || !colorInput.value) {
        window.Telegram.WebApp.showAlert("Not all data is filled");
        return false;
    }
    await fetch(url + "/api/cars/", {
        method: 'POST',
        body: {
            "owner_id": window.Telegram.WebApp.initDataUnsafe.user.id,
            "number": numberInput.value,
            "color": colorInput.value,
            "model": modelInput.value,
        },
    }).then(response => {
        if (response.ok) {
            window.location.href = "profile.html";
        } else {
            window.Telegram.WebApp.showAlert("Something went wrong");
        }
    })

}