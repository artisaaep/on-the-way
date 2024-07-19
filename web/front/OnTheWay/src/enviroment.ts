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
    BOT_TOKEN: "6658030178:AAF7JwKztrDvVQVlzR3lZlSebnf961JUocs",
    BASE_WEBAPP_URL: "https://45d7-188-130-155-149.ngrok-free.app",
}

export const url: string = env.BASE_WEBAPP_URL;

declare global {
    interface Window {
        Telegram: {
            WebApp: any;
        }
    }
}
