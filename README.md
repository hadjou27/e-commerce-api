### Description 
This project is an e-commerce platform built with Django, Django Rest Framework, and PostgreSQL. It allows users to manage stores, products, collections, and media. The platform includes user authentication, CRUD operations (Create, Read, Update, Delete) for products, as well as collection management.

The backend API exposes endpoints to manage products, collections, and user-related data, making it ideal for integration with frontend applications. It also supports pagination for large datasets and is optimized for performance and security.

Additionally, the project is Docker-compatible, enabling developers to easily run and deploy the application in a containerized environment. It uses environment variables to manage sensitive data such as database credentials and API keys.

The system also includes administrative features, allowing store owners and administrators to easily manage products, users, and other associated resources.

Key features include:

    - User registration, login, and profile management
    - Store and collection management
    - Create, update, delete, and retrieve products
    - Media management for products
    - Full Docker setup for simplified deployment
    - API documentation and architecture ready for integration

This project is designed to be scalable, secure, and easy to integrate with other services, making it an ideal solution for any e-commerce platform or inventory management system. 
### Technologies Used 
    - Django: Python framework for backend development
    - Django Rest Framework: Extension of Django to create RESTful APIs
    - PostgreSQL: Relational database used to store data
    - Docker: Containerization for easier deployment
    - PgAdmin: Graphical interface for PostgreSQL management 
### Prerequisites 
Before running the application, make sure you have the following installed:

    - Docker: To run the project in a containerized environment.
    - Docker Compose: To easily set up and manage multi-container applications.
    - Python 3.x: For running the Django application.
    - PostgreSQL: The database system for this project. 

### Installation and Deployment 
    - git clone https://github.com/your-username/ecommerce-platform.git : Clone the repository to your local machine 
    - docker-compose up --build : Build and start the Docker containers
    - docker exec -it youcef- api : Execute a command inside the running Docker container named 'youcef-api'. 
    - python3 manage.py makemgrations : Create new database migrations based on the changes in the models.
    - python3 manage.py migrate : python3 manage.py migrate
    - docker logs -f youcef-api : Execute a command inside the running Docker container named 'youcef-api'.

### Access the App 
    - The backend API will be accessible at http://localhost:8020. 

### API Documentation  

Application Store :

Products :

    - GET /product/: Retrieve a list of all products.
    - POST /product/: Create a new product.
    - GET /product/{id}/: Retrieve a specific product by ID.
    - PUT /product/{id}/: Update a product by ID.
    - DELETE /product/{id}/: Delete a product by ID.  

Collections :

    -  GET /collection/: Retrieve a list of all collections.
    - POST /collection/: Create a new collection.
    - GET /collection/{id}/: Retrieve a specific collection by ID.
    - PUT /collection/{id}/: Update a collection by ID.
    - DELETE /collection/{id}/: Delete a collection by ID.  

Application User :

    - POST /users/register/: Registers a new user.
    - POST /users/login/: Logs in a user.
    - GET /users/profile/: Retrieves the profile of the logged-in user.
    - PUT /users/profile/: Updates the profile of the logged-in user. 

### Future Improvements

    - Add JWT authentication to further secure the API.
    - Integrate cloud storage (AWS S3, Backblaze B2) for media files.
    - Implement a real-time notification system using WebSockets or Celery.
    - Enable password recovery for users.
