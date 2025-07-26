# 🔗 Connect Python with Redis using Docker Compose

This project demonstrates how to connect a **Python application** with a **Redis in-memory data store** using **Docker Compose**. The Python client writes a key-value pair to Redis and retrieves it for display.

---

## 📁 Project Structure

redis-python-app/
├── app/
│ ├── Dockerfile # Builds the Python client image
│ └── main.py # Python script that interacts with Redis
├── docker-compose.yml # Defines and connects Redis and Python services
└── README.md

## 🚀 How It Works

- A Redis container is created using the official lightweight `redis:alpine` image.
- A custom Python container is built using `python:3.10-alpine`.
- The Python script waits 3 seconds (to ensure Redis is up), then:
  - Stores `name = "Yash"` in Redis.
  - Retrieves the value and prints it.


You should see:
python_client  | Stored value from Redis: Yash

Services Used
Redis: Key-value store for caching and fast data operations.

Python (redis-py): Client that communicates with Redis.

Docker Compose: Tool to run multi-container Docker apps easily.

Docker Images
Redis: redis:alpine

Python: Built from python:3.10-alpine, installs redis package.


Author
Yash

Email
shankyash11.com

🏷️ Tags
#Python #Redis #DockerCompose #Docker #Microservices #DevOps
