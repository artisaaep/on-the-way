// import dotenv from 'dotenv';
//
// dotenv.config();
// import {load} from 'ts-dotenv';
//
// export const env = load({
//         BOT_TOKEN: String,
//         BASE_WEBAPP_URL: String
//     },
//     "../../../.env"
// );

const env = {
    BOT_TOKEN: "6839255641:AAEWqA8xiGYJ2k7z-10wEB3Z1wRJA8JLWVA",
    BASE_WEBAPP_URL: "https://b9be-188-130-155-169.ngrok-free.app",
}

export const url: string = env.BASE_WEBAPP_URL;

declare global {
    interface Window {
        Telegram: {
            WebApp: any;
        }
    }
}
