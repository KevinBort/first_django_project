# Blog Django Project

This is a **Django-based blog** project where users can create, read, update, and delete blog posts. The application follows the Model-View-Template (MVT) pattern of Django and incorporates essential blog functionalities like user authentication, post creation, commenting, and category management.

## Features

- User registration and authentication (login/logout)
- Create, edit, and delete blog posts
- Add comments to blog posts
- Categorize posts by topics
- Pagination for large sets of blog posts
- Admin dashboard for post and user management

## Technologies

- **Backend**: Django 4.x
- **Frontend**: HTML, CSS, JavaScript (with Bootstrap for responsive design)
- **Database**: SQLite (default), easily swappable with PostgreSQL, MySQL, etc.
- **Deployment**: Configured for deployment on platforms like Heroku or DigitalOcean

## Getting Started

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.x
- pip (Python package installer)
- Virtualenv (optional but recommended)

### Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:ararrojas/blog-django.git
   cd blog-django
   ```
   
2. Create a virtual environment (optional but recommended):
   ```bash
   Copy code
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   Copy code
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   Copy code
   python manage.py migrate
   ```

5. Create a superuser (for accessing the Django admin panel):
   ```bash
   Copy code
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   Copy code
   python manage.py runserver
   ```

7. Access the application at http://127.0.0.1:8000/ and the admin panel at http://127.0.0.1:8000/admin.

### Usage
- **Creating Posts**: Logged-in users can create new blog posts and categorize them.
- **Comments**: Users can leave comments on posts.
- **Admin Panel**: Superusers can manage users, posts, comments, and other aspects of the blog via the Django admin interface.
