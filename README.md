## Flask Todo (Docker)

A Dockarizied flask application with CRUD features. 

## Tech stack
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

## Project Setup
+ Clone the repository
```bash
git clone https://github.com/nikhil25803/flask_docker.git
```

+ Create and activate a virtual environment
```bash
python -m venv env
```

```bash
env\scripts\activate
```

+ Install the dependencies
```
pip install -r requirements.txt
```

## Run the program
```bash
python main.py
```
Or start a flask server

```bash
flask --app main --debug run
```

Running one of these command will create a `task.db` databse in the root directory to store data.

## Docker Image