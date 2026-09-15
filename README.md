# To-Do API: DevOps Challenge

A lightweight REST API for managing tasks, built with Python (Flask) and containerized with Docker. It includes a GitHub Actions pipeline to verify builds automatically.

---

## 🚀 Quick Start

### 1. Clone the repository##

    git clone https://github.com/ali-waqar22/todo-list-api
    cd todo-list-api

### 2. Build the Docker image

    docker build -t todo-api .

### 3. Run the container

### Maps port 5000 on your local machine to port 5000 inside the container
    docker run -p 5000:5000 todo-api

The API is now accessible at 
    http://localhost:5000.

## 📡 API Endpoints

|    Method     |       Route      |           Description                 |
|---------------|------------------|---------------------------------------|
| GET           | /tasks           |      Returns a list of all tasks      |
| POST          | /tasks           |           Creates a new task          |
| PUT           | /tasks/<id>/done | Marks a specific task status as"done" |
| DELETE        | /tasks/<id>      |       Removes a task from memory      |

## 🧠 Engineering Reflection

### Choices Made

Because my focus is on cloud infrastructure and automation, I chose Python and Flask for the application logic. It is incredibly simple and functions much like a straightforward script, meaning I didn't have to overcomplicate the routing. This let me focus entirely on writing a clean Dockerfile and setting up the CI pipeline. I also strictly followed the prompt to use in-memory storage to avoid the unnecessary complexity of database volume mounts.

### The Trickiest Part

Getting the Docker layer caching right. I made sure to copy the `requirements.txt` and run `pip install` before copying the rest of my application code. This ensures that if I change a single line of Python, Docker doesn't have to re-download the dependencies, saving a lot of time on pipeline builds.

### Future Improvements (With More Time)

1. Swap the in-memory list for a real database like SQLite or Redis.
2. Make the GitHub Action push the final image to a registry like Docker Hub or AWS ECR.
3. Add a check to the POST route to make sure users can't submit an empty task.