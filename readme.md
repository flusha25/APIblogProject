# installation 
### Clone the repository to your local machine:
#### git clone https://github.com/flusha25/API/
### Navigate to the project directory:
#### cd <project_directory>
### Create a virtual environment and activate it:
#### python -m venv venv
#### source venv/bin/activate  # For Linux/Mac
#### Or
#### .\venv\Scripts\activate  # For Windows

### Install the project dependencies:
#### pip install -r requirements.txt

# Usage
## User Login API
### The project includes a user login API endpoint:

#### Endpoint: /login/
#### Method: POST
#### Request Payload: { "username": "your_username" }
#### Response: { "token": "generated_token" }

# Blog Management API
## The project also provides API endpoints for managing blogs:

#### Endpoint: /blogs/
#### GET: Retrieve a list of blogs.
#### POST: Create a new blog. (Requires authenticatio



