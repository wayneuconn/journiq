# journiq
This application is designed as a comprehensive platform for users planning trips, offering features for recording destinations, accommodation arrangements, item management, expense sharing, and settlement.

# backend
```
poetry init
poetry shell
poetry add fastapi uvicorn
poetry export -f requirements.txt --output requirements.txt
```
`docker run --name journiq-postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres`