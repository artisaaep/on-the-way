import dotenv from 'dotenv';

dotenv.config();
import {load} from 'ts-dotenv';

export const env = load({
        BOT_TOKEN: String,
        BASE_WEBAPP_URL: String
    },
    "../../../../.env"
);