# XMEME 
### A project for Crio - Winter of Doing

![Crio Banner](XMEME_banner.png)

This project has 2 parts:

- FRONTEND:
    - Contains code for the frontend of the application made using Node and EJS
    - If you want to run on the local machine
        - Go to the "frontend/xmeme" folder
        - Ensure you have node installed with the dependencies in the package.json file
        - Enter 'node app.js' in the terminal
- BACKEND: 
    - Contains code for the API made using Python, FastAPI and SQLite
    - If you want to run on the local machine
        - Go to the "app" folder
        - Install the requirements
        - Enter 'uvicorn main:app --port 8081' in the terminal
- Dockerfile:
    - Used to create the Docker container for the API
- server_run.sh:
    - Used to run the API server
- install.sh:
    -  Used to install all the dependencies required by the API to run
- sleep.sh:
    - Used to sleep the server while the API is starting 

