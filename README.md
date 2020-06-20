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
    

### Questions

1. Which test did you complete? (backend or full-stack)

    **Answer:** Full-stack

2. If you had chosen to spend more time on this test, what would you have done differently?

    **Answer:** Definitely add frontend tests with [React testing library](https://testing-library.com/docs/react-testing-library/intro),
    Dockerise the app to simplify setup, and add some (in-code) documentation. 
    Maybe use Vue.js, to see what thats like - this is my first
    go with FastAPI and I'm really impressed. Could test performance by using a much larger dataset,
    but I'm not a fan of premature-optimisation; the current code satisfies the requirement.

3. What part did you find the hardest? What part are you most proud of? In both cases, why?

   **Answer:** Pagination was tricky to implement because of the slicing but easy to test, so not too bad overall. 
   Debouncing was probably the hardest, and I can imagine it'd be relatively difficult to test. The implementation only
   looks simple thanks to React's built-in [hooks](https://reactjs.org/docs/hooks-effect.html). 
   I'm probably most proud of the lazy-loading; it just looks really satisfying when you're
   scrolling and watching the requests in the network console!

4. What is one thing we could do to improve this test?

   **Answer:** I cant actually think of anything! It's a fair challenge and, refreshingly, relevant to
   most day-to-day work. I've learnt a few things so it's been a pleasant experience
   overall. I 100% prefer spending time on something like this, over spending hours memorising
   a bunch of algorithms. 

