
#!/bin/bash


cd backend/app

#Run the fastapi
uvicorn main:app --host 0.0.0.0 --port 8081