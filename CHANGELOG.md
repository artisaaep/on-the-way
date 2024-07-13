# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).



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
- Modified `handlers/start.py` to integrate with state machine for user interaction during registration.
- Improved `index.html` with basic HTML structure for future web integration.

### Removed
- Removed redundant imports and unused code sections.

## 0.5.0 - 2024-06-13

### Added
- Implemented database functionality in `database.py`:
  - Created `Database` class with methods `exists`, `create_profile`, and `update_profile` for interacting with SQLite database (`db.db`).
  - Added SQLite database file `db.db`.
  - Introduced database interaction in `form.py` and `handlers/start.py` using `Database` class methods.

### Changed
- Updated `main.py` to include `form.router` in Dispatcher setup for routing.
- Modified `handlers/start.py` to utilize `Database` class methods for user profile creation and existence checks.

## 0.4.0 - 2024-06-12

### Added
- Implemented database functions in `database.py`:
  - `exists`: Checks if a user ID already exists in the database.
  - `create_profile`: Creates a new user profile in the database.
  - `update_profile`: Updates existing user profile data.

### Changed
- Updated `handlers/start.py` to include:
  - Greeting message for new users, guiding them through registration or providing startup instructions.
  - Utilized `exists` function from `database` module to check user existence during startup.

## 0.3.2 - 2024-06-11

### Changed
- Updated keyboard button text in `handlers/start.py` for the CommandStart message handler.

### Removed
- Removed redundant message response in the CommandStart message handler in `handlers/start.py`.

## 0.3.1 - 2024-06-08

### Added
- Added `.venv` to `.gitignore` to exclude virtual environment files from version control.

### Changed
- Modified `main.py`:
  - Updated import statements to include `asyncio`.
  - Updated `start` function in message handler to include a customized keyboard button text.

### Removed
- Removed unnecessary entries from `.gitignore` related to project directories (`__pycache__`, `.idea`).

### Fixed
- Fixed the `main.py` script to correctly handle asynchronous operations using `asyncio.run(main())`.

## 0.3.0 - 2024-06-08

### Removed
- Removed `.gitignore` entries and configuration files from `.idea/` directory.
  - Deleted `.idea/.gitignore` to stop ignoring specific project files and directories.
  - Removed `.idea/inspectionProfiles/Project_Default.xml` for project inspection profiles.
  - Deleted `.idea/inspectionProfiles/profiles_settings.xml` related to inspection profile settings.
  - Removed `.idea/misc.xml` for miscellaneous project settings.
  - Deleted `.idea/modules.xml` that defines project modules.
  - Removed `.idea/on-the-way.iml` used for project-specific module configuration.
  - Deleted `.idea/vcs.xml` used for version control system directory mappings.
  - Removed `__pycache__/config_reader.cpython-312.pyc` Python bytecode file.

## 0.2.0 - 2024-06-08

### Added
- Added `.gitignore` file to ignore virtual environment files (`venv`).
- Updated `.idea/.gitignore` to exclude project-specific files and directories from version control.
- Updated `.idea` configuration files to optimize project settings and ignore unnecessary files.
- Modified `main.py` to fix type hinting and import issues in command handler.
- Updated `requirements.txt` with specific library versions required for the project.

## 0.1.0 - 2024-06-08

### Added
- Initialized project with basic Telegram bot setup.
  - Integrated `pydantic_settings` for secure token management.
  - Setup environment configuration with `.env` file support.
  - Created initial bot setup using `aiogram`.
  - Implemented `/start` command handler with a basic reply keyboard.