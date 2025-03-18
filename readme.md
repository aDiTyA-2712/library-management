## Library Management System

## Overview
	The Library Management System is a Django-based web application that enables users to manage books, track borrowing and returns, and integrate authentication via Google and GitHub. It includes features like:

		- **Book Management (Create, List, Borrow, Return)
		- **User Authentication via Google & GitHub OAuth
		- **Django Admin Panel for managing books and users
		- **Email Notifications for book borrowing and returns
		
## Project Structure

	library-management/
	│── library/                   # Main Django project folder
	│   ├── settings.py            # Django settings file
	│   ├── urls.py                # URL routing
	│   ├── wsgi.py                # WSGI entry point
	│   ├── asgi.py                # ASGI entry point (for async)
	│── books/                     # Django app for managing books
	│   ├── migrations/            # Database migrations
	│   ├── models.py              # Book model definitions
	│   ├── views.py               # Views for book operations
	│   ├── urls.py                # URL routing for books
	│   ├── serializers.py         # DRF serializers
	│   ├── permissions.py         # Custom permissions
	│── users/                     # Django app for user authentication
	│   ├── models.py              # User model definitions
	│   ├── views.py               # Views for authentication
	│   ├── urls.py                # URL routing for authentication
	│── templates/                 # HTML Templates for Django frontend
	│   ├── base.html              # Base template
	│   ├── book_list.html         # Book listing template
	│── static/                    # Static files (CSS, JS)
	│── .env                       # Environment variables (ignored in Git)
	│── .gitignore                 # Git ignored files
	│── requirements.txt           # Python dependencies
	│── manage.py                  # Django management script


3.1 Clone the Repository

	git clone https://github.com/aDiTyA-2712/library-management.git
	cd library-management
	
3.2 Create a Virtual Environment(if used)

	python -m venv env
	source env/bin/activate  # Mac/Linux
	env\Scripts\activate     # Windows

3.3 Install Dependencies

	pip install -r requirements.txt

3.4 Configure Environment Variables

	Create a .env file in the root directory:
	GOOGLE_CLIENT_ID=your_google_client_id
	GOOGLE_CLIENT_SECRET=your_google_client_secret
	GITHUB_CLIENT_ID=your_github_client_id
	GITHUB_CLIENT_SECRET=your_github_client_secret
	EMAIL_HOST_USER=your_email@gmail.com
	EMAIL_HOST_PASSWORD=your_email_password

	Ensure .env is ignored in .gitignore:
		
3.5 Create a Database ( Here PG is used ) and apply migrations
	
	python manage.py makemigrations
	python manage.py migrate

3.6 Create a Superuser (for Django Admin Panel)

	python manage.py createsuperuser
	then enter your username and password
	
3.7 Run the Development Server	

	python manage.py runserver

    Now, access the application at:

		Frontend (Django Templates) → http://127.0.0.1:8000/
		Admin Panel → http://127.0.0.1:8000/admin/

4. Features & API Endpoints
	4.1 Book Management
		List Books: GET /books/
		Add a Book: POST /books/
		Retrieve a Book: GET /books/<id>/
		Update a Book: PUT /books/<id>/
		Delete a Book: DELETE /books/<id>/
	4.2 Borrow & Return Books
		Borrow a Book: POST /books/<id>/borrow/
		Return a Book: POST /books/<id>/return/
	4.3 Authentication (OAuth Login)
		Google Login: http://127.0.0.1:8000/auth/social/login/google/
		GitHub Login: http://127.0.0.1:8000/auth/social/login/github/	
		
		
5. Running Tests
	5.1 Run Unit Tests

		python manage.py test
		
	5.2 Test Borrow & Return Features
	
		python manage.py test books.tests
	
For Deployement we can do it on different cloud services like AWS,Heroku

Deploying on Heroku
	
	1.Install Heroku CLI:
	
	 pip install gunicorn django-heroku
	
	2.Add Procfile
	
	 web: gunicorn library.wsgi --log-file -
	 
	3.Deploy with Git:
	
	 git add .
	 git commit -m "Deploying to Heroku"
	 heroku create library-management-app
	 git push heroku main
	 
	 


