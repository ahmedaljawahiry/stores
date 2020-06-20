## Overview

Full stack project with a backend API feeding a simple frontend.

## Backend

In the `backend/` directory:
1. Run `pip install -r requirements.txt` to install dependencies.
2. Run `uvicorn api:app` to start the app on port 8000.

The app should now be running at [http://localhost:8000](http://localhost:8000). 

## Frontend

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
