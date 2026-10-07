# 🏋️‍♂️ Workout Tracker

A full-stack web application designed to help users create custom exercises, build workout routines, and track their fitness progress. 

This project demonstrates a modern architecture by separating the frontend UI presentation from the backend business logic, using **Django** to serve templates and **Django REST Framework (DRF)** to handle asynchronous API requests.

## ✨ Key Features

* **Dynamic User Interface:** Seamless, reload-free interactions (creating and deleting exercises) using Vanilla JavaScript and the Fetch API.
* **RESTful API:** Robust backend endpoints built with Django REST Framework to handle CRUD operations and data validation.
* **Custom Exercise Management:** Users can access a global database of core exercises or create their own personalized exercises.
* **Secure Data Access:** Implementation of Django's authentication system and object-level permissions to ensure users only see and modify their own custom data.

## 🛠️ Technology Stack

* **Backend:** Python, Django, Django REST Framework
* **Frontend:** HTML5, CSS3, Vanilla JavaScript (AJAX/Fetch API)
* **Database:** SQLite (Development) / PostgreSQL (Production)
* **Infrastructure:** Docker & Docker Compose

## 🚀 Quick Start (Docker)

To run this project locally using Docker, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   ```

2. Navigate to the project directory:
   ```bash
   cd your-repo-name
   ```

3. Build and start the containers:
   ```bash
   docker-compose up --build
   ```

4. Open your browser and navigate to `http://localhost:8000`
