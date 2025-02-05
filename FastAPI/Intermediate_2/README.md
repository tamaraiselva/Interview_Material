# Intermediate FastApi

## Table of Contents

1. [JWT token generation and verification Database Integration](#JWT_token_generation_and_verification_Database_Integration)

2. [Pydantic and Data Validation](#Pydantic_and_Data_Validation)

3. [Middleware](#Middleware)

4. [Testing FastAPI Applications](#Testing_FastAPI_Applications)

## JWT token generation and verification Database Integration

### 1. What is JWT, and how does it work in the context of securing a FastAPI application?

JWT (JSON Web Token) is a compact, URL-safe token used for securely transmitting information between parties as a JSON object. It consists of three parts: the header (algorithm and token type), payload (user data), and signature (ensuring data integrity). In FastAPI, JWT is typically used for authentication by generating a token after a user successfully logs in, which is then sent in HTTP headers for subsequent requests to secure endpoints. The server verifies the token using the secret key to ensure it's valid and hasn't been tampered with.

### 2. How do you implement token expiration in JWT in FastAPI?

Token expiration is managed by including an "exp" (expiration) field in the JWT payload. In FastAPI, the expiration can be set during token creation using the `datetime` module. The `jwt.encode()` method accepts an expiration time, which is verified when decoding the token using `jwt.decode()`. If the token has expired, a `JWTError` will be raised, and access will be denied.

### 3. Why is it important to hash passwords in your FastAPI application?

A: Password hashing is crucial because it ensures that plaintext passwords are not stored directly in the database, preventing potential attackers from accessing them in case of a data breach. By using a strong hashing algorithm like `bcrypt`, even if attackers get access to the hashed password, it’s computationally expensive and difficult to reverse-engineer the original password.

### 4. How do you set up a SQLAlchemy session in FastAPI?

In FastAPI, you typically set up a SQLAlchemy session by creating an `engine`, `SessionLocal`, and `Base` classes. The `get_db()` function is defined as a dependency to manage the session lifecycle. This ensures that each request gets a fresh database session, and it closes after the request is completed. This is typically implemented using a `yield` statement to manage session cleanup after execution.

### 5. Explain how FastAPI supports asynchronous operations with MongoDB

FastAPI natively supports asynchronous operations by using async functions. MongoDB can be integrated using the `motor` library, which provides an asynchronous MongoDB client. Operations like querying or inserting data are performed using `await`, which ensures non-blocking, asynchronous communication with the MongoDB server. This approach allows the application to handle a high number of I/O-bound operations efficiently.

### 6. What is the role of dependency injection in database management in FastAPI?

Dependency injection in FastAPI ensures that components like database sessions or collections are provided as dependencies to the routes or services that need them. It allows centralized management of resources, improving code organization, reusability, and maintainability. This pattern ensures clean and isolated code and provides lifecycle management for resources like database connections.

### 7. What is dependency injection, and why is it important in FastAPI?

Dependency injection in FastAPI is a technique where objects are provided to parts of the code as dependencies, allowing for better separation of concerns. Dependencies such as database sessions, JWT verifications, or configuration settings can be injected into routes or services. It promotes modularity, testability, and flexibility since dependencies can easily be replaced or mocked in testing.

### 8. How does FastAPI handle validation for request parameters and data?

A: FastAPI uses Pydantic for data validation. When defining request body models or query parameters, you can specify expected data types using Pydantic models. FastAPI automatically validates the incoming data, ensuring it conforms to the schema. If the data is invalid, FastAPI returns a 422 status code with detailed error messages.

### 9. Implement a FastAPI application with a login endpoint that generates a JWT token. The app should also have a protected route (/profile) that allows access only if the token is valid

**`Answer:`**

```python
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

app = FastAPI()

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

fake_users_db = {
    "alice": {"username": "alice", "hashed_password": pwd_context.hash("password")}
}

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def authenticate_user(username: str, password: str):
    user = fake_users_db.get(username)
    if not user or not pwd_context.verify(password, user['hashed_password']):
        return False
    return user

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": user["username"]}, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/profile")
async def read_profile(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"message": f"Welcome, {username}!"}
```

### 10. Write a FastAPI application that allows creating a new user and fetching a user from a PostgreSQL database using SQLAlchemy?

**`Answer:`**

```python
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

app = FastAPI()

SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/")
async def create_user(username: str, email: str, db: Session = Depends(get_db)):
    new_user = User(username=username, email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get("/users/{user_id}")
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
```

### 11. Write a FastAPI app that allows adding a user to a MongoDB collection and retrieving the user by their ID?

**`Answer:`**

```python
from fastapi import FastAPI, HTTPException, Depends
from motor.motor_asyncio import AsyncIOMotorClient
from bson.objectid import ObjectId

app = FastAPI()

client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client.mydatabase
users_collection = db.get_collection("users")

async def get_users_collection():
    return users_collection

@app.post("/users/")
async def create_user(username: str, email: str, users_collection = Depends(get_users_collection)):
    user = {"username": username, "email": email}
    result = await users_collection.insert_one(user)
    return {"id": str(result.inserted_id)}

@app.get("/users/{user_id}")
async def get_user(user_id: str, users_collection = Depends(get_users_collection)):
    user = await users_collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
```

## Pydantic and Data Validation

### 1. What is Pydantic, and why is it used?

**`Answer:`**

Pydantic is a Python library that provides data validation and settings management using Python type annotations. It helps ensure that the data you’re working with meets certain expectations (e.g., type, format, constraints). Pydantic is commonly used in frameworks like FastAPI for request and response validation because of its performance, simplicity, and ease of integration with modern Python typing.

### 2. How does Pydantic perform data validation?

**`Answer:`**

Pydantic performs data validation using Python's type hints. When a model is created, it automatically checks that the input data matches the types defined in the model. It also allows setting constraints such as length, value ranges, and patterns using validators or through the `Field` function.

### 3. How does Pydantic differ from traditional data validation libraries?

**`Answer:`**

Pydantic emphasizes type hints to perform validation, offering a clean and declarative way to enforce validation rules. Unlike many traditional validation libraries, Pydantic converts data to the expected types where possible (e.g., turning a string into an integer if possible), and raises errors when data cannot be coerced. Additionally, it is fast, taking advantage of modern Python type annotations and features like `dataclasses`.

### 4. Can you explain the use of `Field` in Pydantic?

**`Answer:`**

`Field` is used in Pydantic models to add metadata, constraints, and default values to model attributes. It allows you to specify constraints like minimum and maximum values, string length, and regular expressions, and also provides metadata (e.g., `description`, `title`) that can be used for documentation generation (like in OpenAPI for FastAPI).

```python
from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str = Field(..., min_length=3, max_length=100, description="Product name must be 3-100 characters")
    price: float = Field(..., gt=0, description="Price must be greater than 0")
```

### 5. What are Pydantic custom validators, and how do you use them?

**`Answer:`**

Custom validators in Pydantic allow you to add more specific validation logic to fields in your model. These are defined using the @validator decorator on methods, which accept the value of the field and can raise errors or modify the value before it is assigned.

```python
from pydantic import BaseModel, validator

class User(BaseModel):
    age: int

    @validator('age')
    def check_age(cls, v):
        if v < 0:
            raise ValueError('Age must be positive')
        return v
```

### 6. What is the difference between @validator and @root_validator in Pydantic?

**`Answer:`**

- **`@validator:`** This decorator is used to validate individual fields. You can apply it to one or more fields, and it will run after all fields are parsed.

**`@root_validator:`** This is used to validate multiple fields at once, usually for cross-field validation, where the logic depends on the values of several fields. It processes either before (`pre=True`) or after (`pre=False`) the individual field validators.

### 7. Write a Pydantic model that validates user input for a form that includes name, age, and email. Ensure that?

- `name` is a string with a length between 3 and 50 characters.
- `age` is an integer greater than or equal to 18.
- `email` is a valid email format.

**`Answer:`**

```python
from pydantic import BaseModel, Field, EmailStr, validator

class User(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="Name must be between 3 and 50 characters")
    age: int = Field(..., ge=18, description="Age must be 18 or older")
    email: EmailStr = Field(..., description="Must be a valid email address")

    @validator('name')
    def no_special_chars(cls, v):
        if not v.isalnum():
            raise ValueError('Name cannot contain special characters')
        return v

# Example Usage
try:
    user = User(name="JohnDoe", age=25, email="john.doe@example.com")
    print(user)
except Exception as e:
    print(e)
```

### 8. Create a Pydantic model for a product, with the following constraints?

- `product_name:` Required string field, minimum length of 5.

- `price:` A float that must be greater than 0.

- `stock:` An integer that must be greater than or equal to 0.

- Add a custom validator to ensure the `price` is reasonable (e.g., less than $10,000).

**`Answer:`**

```python
from pydantic import BaseModel, Field, validator

class Product(BaseModel):
    product_name: str = Field(..., min_length=5, description="Product name must be at least 5 characters long")
    price: float = Field(..., gt=0, description="Price must be greater than zero")
    stock: int = Field(..., ge=0, description="Stock must be zero or greater")

    @validator('price')
    def reasonable_price(cls, v):
        if v > 10000:
            raise ValueError('Price is too high; must be less than $10,000')
        return v

# Example Usage
try:
    product = Product(product_name="Laptop", price=9999.99, stock=100)
    print(product)
except Exception as e:
    print(e)
```

### 9. Write a Pydantic model that validates a form submission for a user registration. The form includes a password and a confirmation password field. Ensure that both passwords match and follow these rules?

- Password must be at least 8 characters long.
- Password must contain at least one uppercase letter, one lowercase letter, and one digit.

**`Answer:`**

```python
from pydantic import BaseModel, Field, validator

class UserRegistration(BaseModel):
    password: str = Field(..., min_length=8, description="Password must be at least 8 characters long")
    confirm_password: str

    @validator('password')
    def password_complexity(cls, v):
        if not any(char.isupper() for char in v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not any(char.islower() for char in v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not any(char.isdigit() for char in v):
            raise ValueError('Password must contain at least one digit')
        return v

    @validator('confirm_password')
    def passwords_match(cls, v, values):
        if 'password' in values and v != values['password']:
            raise ValueError('Passwords do not match')
        return v

# Example Usage
try:
    user = UserRegistration(password="StrongPass1", confirm_password="StrongPass1")
    print(user)
except Exception as e:
    print(e)
```

## Middleware

### 1. What is middleware in FastAPI?

**`Answer:`** Middleware in FastAPI is a function that runs before and after each request. It sits between the client and the application, allowing developers to process requests before they reach the endpoint and modify responses before they are sent back to the client. Middleware is often used for logging, adding headers, CORS (Cross-Origin Resource Sharing), authentication, and more.

### 2. How is middleware implemented in FastAPI?

**`Answer:`** Middleware in FastAPI is implemented by decorating an asynchronous function with `@app.middleware("http")`. This function takes a `Request` object as input and passes it to the next middleware or request handler using the `call_next()` function. The result of `call_next()` is a `Response` object that can be modified before sending it back to the client.

### 3. What are some common use cases for middleware in web applications?

**`Answer:`** Common use cases for middleware include:

- Logging incoming requests and outgoing responses.

- Handling Cross-Origin Resource Sharing (CORS).
Compressing responses (e.g., with GZip).

- Adding or modifying headers for security, like `Content-Security-Policy`.

- Handling authentication and authorization checks.

- Tracking performance or metrics (e.g., request processing time).

### 4. What is CORS, and how would you implement CORS in FastAPI middleware?

**`Answer:`** CORS (Cross-Origin Resource Sharing) is a mechanism that allows servers to specify which domains are allowed to access their resources. In FastAPI, CORS can be implemented using the built-in `CORSMiddleware`. Alternatively, it can be handled by creating custom middleware to add the appropriate CORS headers like `Access-Control-Allow-Origin`, `Access-Control-Allow-Methods`, and `Access-Control-Allow-Headers`.

### 5. What is the difference between middleware and dependency injection in FastAPI?

**`Answer:`** Middleware applies globally to all requests and responses, allowing for pre- and post-processing at the application level. Dependency injection, on the other hand, allows you to inject logic into specific route functions. Middleware typically handles cross-cutting concerns like logging, CORS, or security, while dependency injection is often used for injecting configurations, database connections, or service objects into specific route handlers.

### 6. Implement a logging middleware that logs the request method, URL, and the time taken to process each request. The log should look like:`Method: GET, URL: /items/, Time taken: 0.0021 seconds`

**`Answer:`**

```python
from fastapi import FastAPI, Request
import time
import logging

# Initialize the FastAPI application
app = FastAPI()

# Setup basic logging
logging.basicConfig(level=logging.INFO)

# Custom Logging Middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    
    # Log request details
    logging.info(f"Method: {request.method}, URL: {request.url}")
    
    # Process request and get response
    response = await call_next(request)
    
    # Calculate processing time
    process_time = time.time() - start_time
    logging.info(f"Time taken: {process_time:.4f} seconds")
    
    return response

# Example route
@app.get("/items/")
def get_items():
    return {"items": ["item1", "item2", "item3"]}
```

### 7. Write a custom middleware for FastAPI that adds the following CORS headers

- Access-Control-Allow-Origin: *
- Access-Control-Allow-Methods: GET, POST, PUT, DELETE
- Access-Control-Allow-Headers: Content-Type

**`Answer:`**

```python
from fastapi import FastAPI, Request

# Initialize the FastAPI application
app = FastAPI()

# Custom CORS Middleware
@app.middleware("http")
async def add_cors_headers(request: Request, call_next):
    # Process the request
    response = await call_next(request)
    
    # Add CORS headers to the response
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    
    return response

# Example route
@app.get("/items/")
def get_items():
    return {"items": ["item1", "item2", "item3"]}
```

### 8. Write a custom middleware that compresses all responses using GZip for responses larger than 500 bytes?

**`Answer:`**

```python
import gzip
from fastapi import FastAPI, Request, Response

app = FastAPI()

# Custom GZip Compression Middleware
@app.middleware("http")
async def gzip_compression_middleware(request: Request, call_next):
    # Process request and get response
    response = await call_next(request)
    
    # Check if the response is larger than 500 bytes
    if len(response.body) > 500:
        compressed_body = gzip.compress(response.body)
        response = Response(content=compressed_body, 
                            status_code=response.status_code,
                            headers=response.headers, 
                            media_type=response.media_type)
        response.headers["Content-Encoding"] = "gzip"
    
    return response

# Example route
@app.get("/large-data/")
def get_large_data():
    return {"data": "x" * 1000}  # Large response
```

## Testing FastAPI Applications

### 1. What is FastAPI, and why would you choose it over other web frameworks like Flask or Django?

**`Answer:`** FastAPI is a modern, high-performance web framework for building APIs using Python 3.6+ standard type hints. It’s designed to be fast, efficient, and easy to use, especially for building asynchronous web applications. The key reasons to choose FastAPI over frameworks like Flask or Django include:

- **`Asynchronous support:`** FastAPI provides native support for asynchronous request handling using `async` and `await`, allowing for better performance in I/O-bound operations (e.g., database calls, external APIs).

- **`Automatic validation:`** FastAPI leverages Python's type hints to automatically validate request data and provide descriptive errors without extra code.

- **`Interactive documentation:`** FastAPI automatically generates interactive API docs (Swagger UI and ReDoc) based on the code and type annotations.

- **`Performance:`** Due to its asynchronous nature and reliance on the Starlette framework and Pydantic for data validation, FastAPI is one of the fastest Python web frameworks.

### 2. How does dependency injection work in FastAPI?

**`Answer:`** Dependency injection in FastAPI is handled through the `Depends` function. It allows you to define and inject dependencies (e.g., database sessions, authentication mechanisms, third-party services) into routes or other dependencies.

For example, if you want to inject a database session into an API route, you would define a function to get the database session and use Depends to inject it into the route:

```python
from fastapi import Depends

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/items/")
def read_items(db: Session = Depends(get_db)):
    return db.query(Item).all()
```

### 3. What is the purpose of Pydantic in FastAPI?

**`Answer:`** Pydantic is a data validation and settings management library used by FastAPI to enforce data validation, parsing, and serialization. It helps to define request body, query parameters, and path parameters using Python’s type hints. Pydantic models validate incoming data automatically, ensuring that types are correct and fields meet certain constraints before being passed to the route handler.

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
```

### 4. How does FastAPI handle asynchronous requests, and why is this useful?

**`Answer:`** FastAPI natively supports asynchronous request handling using Python’s `async` and `await` keywords. By defining a route handler as `async def`, FastAPI ensures that the request is handled asynchronously. This is particularly useful in I/O-bound operations, such as accessing a database or calling external APIs, where the application doesn't need to wait for the operation to complete before continuing to handle other requests.

```python
@app.get("/async-data/")
async def get_data():
    data = await external_api_call()
    return data
```

### 5. How do you test FastAPI applications, and what tools are commonly used?

**`Answer:`** FastAPI applications can be tested using the TestClient provided by FastAPI (built on top of requests) and pytest as the test framework.

To test a FastAPI endpoint:

1. Use TestClient to simulate HTTP requests.

2. Validate the response status code and JSON content.

```python
from fastapi.testclient import TestClient
from myapp import app

client = TestClient(app)

def test_read_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1}
```

### 6. Coding Question

**Problem Statement:**

Create a FastAPI application with an endpoint `/items/{item_id}` that returns an item’s details from a database (you can simulate the database using a list of dictionaries). Write a test for this endpoint that mocks the database interaction and ensures the correct item is returned.

**Requirements:**

- The FastAPI app should have an endpoint `GET /items/{item_id}`.

- The "database" is a simple list of dictionaries.

- Write a unit test that mocks the database call and tests the API response.

**Solution:**

**FastAPI Application:**

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

# Simulating a database with a list of dictionaries
items_db = [
    {"id": 1, "name": "Item One", "description": "The first item"},
    {"id": 2, "name": "Item Two", "description": "The second item"},
]

@app.get("/items/{item_id}")
def read_item(item_id: int):
    item = next((item for item in items_db if item["id"] == item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
```

**`Unit Test:`**

```python
from fastapi.testclient import TestClient
from unittest.mock import patch
from myapp import app

client = TestClient(app)

def test_read_item():
    # Mocking the database interaction
    mock_db = [
        {"id": 1, "name": "Mock Item", "description": "A mocked item"},
    ]

    with patch("myapp.items_db", mock_db):
        response = client.get("/items/1")
        assert response.status_code == 200
        assert response.json() == {"id": 1, "name": "Mock Item", "description": "A mocked item"}

def test_item_not_found():
    mock_db = []
    with patch("myapp.items_db", mock_db):
        response = client.get("/items/99")
        assert response.status_code == 404
        assert response.json() == {"detail": "Item not found"}
```
