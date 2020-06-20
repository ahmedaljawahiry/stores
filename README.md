## Overview

Full stack project with a backend API feeding a simple frontend. Features
include pagination, searchable-api, and debouncing.

## Backend

### Stack 

- [FastAPI](https://fastapi.tiangolo.com/) 
- [pytest](https://docs.pytest.org/en/stable/)
- Prerequisites:
    1. Python - only tested with v3.8.
    2. pip.
    3. [venv](https://docs.python.org/3/library/venv.html), if you wish. 

### Usage

In the `backend/` directory:
1. Run `pip install -r requirements.txt` to install dependencies.
2. Run `uvicorn api:app` to start the app on port 8000.

The app should now be running at [http://localhost:8000](http://localhost:8000). 
Go to `/docs` to check out the API docs.

To run tests, simply run `pytest` in the `backend/` directory.

## Frontend

### Stack

- Bootstrapped with [Create React App](https://create-react-app.dev/)
- [React](https://reactjs.org/)
- [Typescript](https://www.typescriptlang.org/)
- Prerequisites:
    1. [yarn](https://classic.yarnpkg.com/en/docs/install/).
    2. A relatively modern browser.
    
### Usage

In the `frontend/` directory:
1. Run `yarn install` to install dependencies.
2. Run `yarn start` to start the app on port 3000.

The app should now be running at [http://localhost:3000](http://localhost:3000).

### Features

- Lazy loading on page scroll: 
    hit search without entering anything to bypass any filtering, then
    scroll inside the results container. The "fetch url" at the top of the
    page shows the API calls being made.

- 100ms debounce: this is hard to see when set to 100ms - you can increase
    the time in `App.tsx` to better see the effect.
