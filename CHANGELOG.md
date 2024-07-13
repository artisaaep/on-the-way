# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 3.0.0 - 2024-07-07 - MVP Version 2

Full-fledged bot communication with the database and refactoring of some web pages

### Added
-

## 2.1.0 - 2024-07-06

### Added 
- Added pipeline features
- Dockerfile for NGINX web server

## 2.0.2 - 2024-07-04

### Added
- Added base for Svelte-framework based front-end in some web pages

### Removed
- Removed unnecessary part of the code of web pages due to migration to Svelte

## 2.0.1 - 2024-07-02

### Added
- Added handling for `car_ids` in user data for trip passengers in `data_models.py`.
- Added enhanced trip rendering in `main` function in `availabletrips.js`.

### Fixed
- Fixed redundant script import in `availabletrips.html`.

### Changed
- Changed `user` retrieval to use `SQLUser` instead of `User` in `data_models.py`.
- Changed `url` variable to point to a new API endpoint in `addcar.js`.
- Changed `url` variable to point to a new API endpoint in `availabletrips.js`.
- Changed `apply` function to handle trip applications with a specific payload in `availabletrips.js`.
- Changed `url` variable to point to a new endpoint in `profile.js`.

## 2.0.0 - 2024-06-30 - MVP Version 1

The bot is uploaded to the server and partially connected to the database

### Added
- Updated values for `BOT_TOKEN` and `BASE_WEBAPP_URL` in the `.env` file.

### Changed
- Fixed links in `telegram/form.py` for user interaction with the web application.
- Updated instructions for compiling files into the static folder.
- Updated `package-lock.json`.
- Updated `package.json`.
- Added `rollup.config.js` for script compilation.
- Updated scripts and styles in static files.
- Added and updated HTML files and scripts for the web application.

### Removed
- Deleted `index.html` file as it was unnecessary.

## 1.0.3 - 2024-06-27

### Added
- Added `BASE_WEBAPP_URL` to `.env`.
- Integrated web app links in `form.py` for user interaction.

### Changed
- Updated imports across several files for clarity and organization.
- Streamlined user profile creation in `database_class.py`.

### Fixed
- Corrected file path in `web/server.py` for static file handling.

## 1.0.2 - 2024-06-25

### Added
- Added `cars` router to `server.py` for managing car-related endpoints.
- Implemented ORM models `User`, `Trip`, and `TripPassenger` in `base_models.py` using SQLAlchemy.
- Introduced support for SQLAlchemy sessions in `database.py` for user profile management and photo retrieval.
- Included ID generator function in `id_generators.py` for generating unique identifiers.

### Changed
- Enhanced trip handling in `trips.py` by integrating ORM models, optimizing CRUD operations for trips and passengers.
- Updated `server.py` to include new endpoints and routes for car management.

### Fixed
- Fixed file paths for photos in `server.py`, moving them from `photos` directory to `shared/photos`.

### Removed
- Removed redundant imports and unused code from `data_models.py` and `users.py`.

## 1.0.1 - 2024-06-25

### Updated

- Added `cars` router to `server.py` for handling requests related to cars.
- Integrated ORM models `User`, `Trip`, and `TripPassenger` in `base_models.py` for use with SQLAlchemy.
- Enhanced `database.py` to support SQLAlchemy sessions for managing user profiles and fetching photos.
- Improved trip handling in `trips.py` using ORM models, optimizing CRUD operations.
- Added ID generator function in `id_generators.py` for generating unique identifiers for entities.

## 1.0.0 - 2024-06-23 - MVP Version 0

A bot along with a web app that is not connected to the database.

## 0.6.2 - 2024-06-21

### Changed
- Refactored `create_profile` method in `database.py` to simplify and remove unnecessary parameters (`photo` and `bio`).
- Updated `telegram/form.py` to streamline user profile creation flow:
  - Removed `bio` state handling from the form process.
  - Updated `set_sex`, `set_photo`, and `set_finish` handlers to align with the new profile creation logic.
  - Adjusted messages and prompts to improve user interaction and clarity throughout the profile creation process.

## 0.6.1 - 2024-06-20

### Removed
- Removed `bio` state from form handling in `form.py`.
  - Deleted `bio` state handling from the state machine in form processing.
  - Removed conditions related to setting `bio` in the user profile creation flow.
  - Updated `set_sex` and `set_photo` handlers to remove references to `bio` state transitions.
  - Refactored `set_photo` and `set_finish` handlers to no longer expect `bio` state interaction.
  - Updated message handling to exclude prompts related to `bio`.

## 0.6.0 - 2024-06-17

### Added
- Defined Pydantic data models for Trip, NewTrip, Driver, Passenger, and User.
- Implemented main API entry point with FastAPI in `main.py`.
- Created routers for `trips` and `users` with basic CRUD operations.

## 0.5.1 - 2024-06-15

### Added
- Initialized bot and dispatcher in `bot_init.py` using configuration from `config_reader`.
- Implemented database functionality enhancements in `database.py`:
  - Extended `create_profile` method to include an `alias` parameter for user identification.
  - Added `get_photo` method to retrieve user photo from the database.
- Introduced stateful form handling in `form.py`:
  - Defined `Form` class with states for capturing user profile information.
  - Added message handlers for capturing and updating user profile details using `Database` methods.

### Changed
- Updated `main.py` to import bot and dispatcher from `bot_init.py`.
- Modified `start.py` to integrate with state machine for user interaction during registration.
- Improved `index.html` with basic HTML structure for future web integration.

### Removed
- Removed redundant imports and unused code sections.

## 0.5.0 - 2024-06-13

### Added
- Implemented database functionality in `database.py`:
  - Created `Database` class with methods `exists`, `create_profile`, and `update_profile` for interacting with SQLite database (`db.db`).
  - Added SQLite database file `db.db`.
  - Introduced database interaction in `form.py` and `start.py` using `Database` class methods.

### Changed
- Updated `main.py` to include `form.router` in Dispatcher setup for routing.
- Modified `start.py` to utilize `Database` class methods for user profile creation and existence checks.

## 0.4.0 - 2024-06-12

### Added
- Added the first html file for the web app
- Implemented database functions in `database.py`:
  - `exists`: Checks if a user ID already exists in the database.
  - `create_profile`: Creates a new user profile in the database.
  - `update_profile`: Updates existing user profile data.

### Changed
- Updated `start.py` to include:
  - Greeting message for new users, guiding them through registration or providing startup instructions.
  - Utilized `exists` function from `database` module to check user existence during startup.

## 0.3.2 - 2024-06-11

### Changed
- Updated keyboard button text in `start.py` for the CommandStart message handler.

### Removed
- Removed redundant message response in the CommandStart message handler in `start.py`.

## 0.3.1 - 2024-06-08

### Added
- Added `.venv` to `.gitignore` to exclude virtual environment files from version control.

### Changed
- Modified `main.py`:
  - Updated import statements to include `asyncio`.
  - Updated `start` function in message handler to include a customized keyboard button text.

### Removed
- Removed unnecessary entries from `.gitignore` related to project directories.

### Fixed
- Fixed the `main.py` script to correctly handle asynchronous operations using `asyncio.run(main())`.

## 0.3.0 - 2024-06-08

### Removed
- Eliminated `.gitignore` entries and configuration files from the `.idea/` directory.
  - Deleted `.idea/.gitignore` to stop excluding specific project files and directories from version control.
  - Removed `.idea/inspectionProfiles/Project_Default.xml` used for project inspection profiles.
  - Deleted `.idea/inspectionProfiles/profiles_settings.xml` containing inspection profile settings.
  - Removed `.idea/misc.xml` for miscellaneous project settings.
  - Deleted `.idea/modules.xml` defining project modules.
  - Removed `.idea/on-the-way.iml` used for project-specific module configuration.
  - Deleted `.idea/vcs.xml` defining version control system directory mappings.

## 0.2.0 - 2024-06-08

### Added
- Introduced `.gitignore` file to prevent versioning of virtual environment files (`venv`).
- Enhanced `.gitignore` to exclude project-specific files and directories from being tracked by version control.
- Optimized `.idea` configuration files to improve project settings and remove unnecessary files.
- Resolved type hinting and import issues in the command handler of `main.py`.
- Updated `requirements.txt` to specify exact library versions essential for the project.

## 0.1.0 - 2024-06-08

### Added
- Initiated project setup for a Telegram bot.
  - Integrated `pydantic_settings` for secure token management.
  - Configured environment settings with support for `.env` files.
  - Established initial bot functionality using `aiogram`.
  - Implemented `/start` command handling with a basic reply keyboard.