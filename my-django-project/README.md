# My Django Project

This is a simple Django project that implements a Notes API. The API allows users to create and retrieve notes without requiring authentication.

## Project Structure

```
my-django-project
├── manage.py
├── notes_api
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── notes
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd my-django-project
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install django djangorestframework
   ```

4. **Run migrations:**
   ```
   python manage.py migrate
   ```

5. **Run the development server:**
   ```
   python manage.py runserver
   ```

## API Endpoints

- **GET /notes/**: Retrieve a list of all notes.
- **POST /notes/**: Create a new note. Requires a JSON body with `title` and `content`.

## Usage

You can use tools like Postman or curl to interact with the API endpoints. 

### Example Request to Create a Note

```
POST /notes/
Content-Type: application/json

{
    "title": "Sample Note",
    "content": "This is a sample note content."
}
```

### Example Request to List Notes

```
GET /notes/
```

Features
Authentication: JWT-based authentication protects all note endpoints.

Access Control: Users can only access their own notes.

Search: Filter notes by searching the title or content via query parameter:

sql
Copy
Edit
GET /notes/?search=keyword
Pagination: Notes list is paginated, 10 notes per page by default.

