# Book Review Service API

## Overview
This is a RESTful API for a simple book review service that allows users to register accounts, log in, search for books, add reviews, and retrieve reviews. The API supports basic CRUD operations for books and reviews, as well as user authentication.

## Features
- **User Management**:
  - Register a new user.
  - Log in to get an authentication token.

  - **Books**:
  - Get a list of books
  - Search for books by title or author.
  - View details of a specific book.

  - **Reviews**:
  - Add a review for a book.
  - Add a rating for a book.
  - View all reviews for a specific book.
  - Retrieve a user’s review history.

    ## Tech Stack
    - **Backend Framework**: Django Rest Framework (DRF).
    - **Database**: PostgreSQL.
    - **Authentication**: Token Based Authentication.
    - **Other**: version control GitHub.

    ## Endpoints
    ### 1. **User Registration Endpoint**

    #### POST /auth-app/register

    - Register a new user account.
    - **Request Body**:
     ```json```
    {
        "username": "your_username",
        "email": "your_email",
        "password": "your_password"
    }

    -Response

    {
    "message": "User registered successfully",
    "data": {
        "username": "your_username",
        "email": "your_email",
        "password": "your_password"
    }
    }

    ### 2. **User Login Endpoint**

    #### POST /auth-app//login

    - Log in to get a  authentication token.
    - **Request Body**:
     ```json```
    {
        "email": "your_email",
        "password": "your_password"
    }

    -Response

    {
    "message": "Login successfully",
    "data": {
        "user_id": "user_id",
        "username": "your_username",
        "email": "your_email",
        "token": "token"
    }
    }

    ### 3. **User Logout Endpoint**

    #### POST /auth-app/logout

    - Remove session details.
    - **Request Body**:
     ```json```
    {
        "user_id": "user_id"
    }

    -Response

    {
    "message": "Logout successfully"
    }

    ### 4. **Book Endpoints**

        #### POST /books-app/books

        - Rgister Book details.

        - **Request Body**:
        ```json```
        {
            "title": "book_title",
            "author": "book_author",
            "genre": "boook_genre",
            "summary": "book_description"
        }

        -Response

        {
            "message": "Book added successfully",
            "data": {
                "title": "book_title",
                "author": "book_author",
                "genre": "boook_genre",
                "summary": "book_description"
            }
        }

        #### GET /books-app/books

        - Get all Book details.

        -Response

        {
            "message": "Book details fetched successfully",
            "data": [
            {
                "book_id": "book_id",
                "title": "book_title",
                "author": "book_author",
            },
             {
                "book_id": "book_id",
                "title": "book_title",
                "author": "book_author",
            }
            ]
        }

        #### GET /books-app/books

        - Get Specific Book details by Author ot Title.

        - Parameters
          title or author
        
        - Parameter title

        /books-app/books?title="book_title"

        -Response

        {
            "message": "Book details fetched successfully",
            "data": [
                {
                    "book_id": "book_id",
                    "title": "book_title",
                    "author": "book_author"
                }
                ]
        }

        /books-app/books?author="book_author"

        -Response

        {
            "message": "Book details fetched successfully",
            "data": [
                {
                    "book_id": "book_id",
                    "title": "book_title",
                    "author": "book_author"
                }
                ]
        }

        #### GET /books-app/books/{book_id}

        - Get Specific Book details by Book ID.

        -Response

        {
            "message": "Book details fetched successfully",
             "data": {
                "book_id": "book_id",
                "title": "book_title",
                 "author": "book_author",
                 "genre": "book_genre",
                 "summary": "book_summary"
            }
        }
    
    ### 5. **Review Endpoints**

        #### POST /reviews-app/books/{book_id}/reviews

            - Add book review by user with rating and comments.

            - **Request Body**:
            ```json```
            {
                "rating": "book_rating",
                "comment": "comment"
            }

            -Response

            {
                "message": "Review added successfully"
            }
        

        #### GET /reviews-app/users/{user_id}/reviews

            - Get user specific reviews with optional parameters limit and offset for pagination.

            -Response

            {
                "message": "Reviews fetched successfully",
                "data": [
                    {
                        "user": {
                            "username": "user_name",
                            "email": "user_email",
                        },
                        "book": {
                            "title": "book_title",
                            "author": "book_author",
                            "genre": "book_genre",
                            "summary": "book_summary"
                        },
                        "rating": "book_rating",
                        "comment": "book_comments"
                        }
                        ]
            }
    
    ## Setup Instructions
    1. Clone the repository
    git clone https://github.com/yourusername/book-review.git
    cd book-review

    2. Install Dependencies
    - Create and activate a virtual environment:
       python3 -m venv env
       source env/bin/activate
    - Install required Python packages
      pip install -r requirements.txt
    
    3. Database Setup
    - Installed PostgreSQL
    - Installed PGAdmin

    4. Run the Development Server
    - python manage.py runserver

    5. Access the API
    - http://localhost:8000/api/0.1/

      








