# Reccomend-on-the-fly

## How to build
- **Run** `docker build -t reccommender .` to build the container
- **Run** `docker run -d --name starlette -p 9999:80 reccommender` to start on localhost:9999

## Example usage
- **Request** localhost:9999/user_id to get reccomendation for user user_id