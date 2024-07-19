window.onload = inv;
function isDarkColor(color) {
    const rgb = parseColorToRgb(color);
    const luminance = (0.2126 * rgb[0] + 0.7152 * rgb[1] + 0.0722 * rgb[2]) / 255;
    return luminance < 0.5;
}

function parseColorToRgb(color) {
    let r, g, b;
    if (color.startsWith('#')) {
        if (color.length === 7) {
            r = parseInt(color.slice(1, 3), 16);
            g = parseInt(color.slice(3, 5), 16);
            b = parseInt(color.slice(5, 7), 16);
        } else if (color.length === 4) {
            r = parseInt(color[1] + color[1], 16);
            g = parseInt(color[2] + color[2], 16);
            b = parseInt(color[3] + color[3], 16);
        }
    } else if (color.startsWith('rgb')) {
        const rgbValues = color.match(/\d+/g);
        r = parseInt(rgbValues[0]);
        g = parseInt(rgbValues[1]);
        b = parseInt(rgbValues[2]);
    }
    return [r, g, b];
}

function again() {
    window.location.href = "createtrip.html";
}
function inv() {
    const tg = window.Telegram.WebApp;
    if (tg.themeParams.bg_color && isDarkColor(tg.themeParams.bg_color)) {
        document.getElementById('car').style.filter = 'invert(1)';
        document.body.style.setProperty('background-color', '#1c1c1d');
    }
}
Telegram.WebApp.onEvent('themeChanged', function() {
    const tg = window.Telegram.WebApp;
    if (tg.themeParams.bg_color && isDarkColor(tg.themeParams.bg_color)) {
        document.getElementById('car').style.filter = 'invert(1)';
        document.body.style.setProperty('background-color', '#1c1c1d');
    } else {
        document.getElementById('car').style.filter = 'none';
        document.body.style.setProperty('background-color', '#f0eff5');
    }
});