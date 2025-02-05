# Intermediate FastApi

## Table of Contents

1. [Asynchronous Programming](#asynchronous-programming)

2. [Path Operations and Type Annotations](#path-operations-and-type-annotations)

3. [Authentication & Authorization](#authentication-&-authorization)

## Asynchronous Programming

### 1. What is asynchronous programming, and why is it beneficial in web applications?

Asynchronous programming allows code execution to proceed without waiting for certain tasks (especially I/O-bound tasks) to complete. In web applications, this approach is beneficial because it enables handling multiple requests concurrently, improving performance and responsiveness under high loads. By using asynchronous functions, applications can avoid blocking the main thread while waiting for tasks like database queries or external API calls, making better use of resources and enhancing the user experience.

### 2. How does FastAPI handle asynchronous routes, and when should you use async `def` vs `def`?

FastAPI allows defining asynchronous routes using the `async def` syntax, which supports the `await` keyword to run asynchronous tasks. `async def` routes are optimal for I/O-bound tasks like database queries or network requests, as they do not block the server while waiting for these operations. In contrast, synchronous routes (defined with `def`) are preferable for CPU-bound tasks, where the benefits of asynchronous programming are limited. FastAPI can efficiently serve both types of routes, but asynchronous routes are generally better for scalability and performance under concurrent loads.

### 3. Can you mix synchronous and asynchronous functions within a FastAPI route? If so, how?

Yes, you can mix synchronous and asynchronous functions within a FastAPI route, but it requires some care. In an `async def` route, you can call synchronous code by using FastAPI’s `run_in_threadpool` helper, which prevents blocking the main asynchronous loop. This way, you can execute CPU-bound synchronous code within an asynchronous route without compromising concurrency. However, it’s recommended to keep the entire flow asynchronous when possible to maximize performance.

```python
from fastapi import FastAPI
from time import sleep
from fastapi.concurrency import run_in_threadpool

app = FastAPI()

@app.get("/mixed-endpoint")
async def mixed_route():
    await run_in_threadpool(sleep, 2)  # Call synchronous sleep function in a threadpool
    return {"message": "This is a mixed route"}
```

### 4. Write a FastAPI route `/get-data` that simulates fetching data from a database using a mock asynchronous function. This function should take 3 seconds to complete and then return a message indicating data retrieval success.

```python
from fastapi import FastAPI
import asyncio

app = FastAPI()

async def mock_fetch_data():
    # Simulate an asynchronous data fetch (e.g., database query)
    await asyncio.sleep(3)  # Mock 3-second delay
    return "Data fetched successfully!"

@app.get("/get-data")
async def get_data():
    message = await mock_fetch_data()
    return {"message": message}
```

### 5. Implement two FastAPI routes, `/sync-wait` and `/async-wait`, where both routes introduce a 2-second delay before returning a response. Use synchronous sleep for the first route and asynchronous sleep for the second.

```python
from fastapi import FastAPI
import time
import asyncio

app = FastAPI()

# Synchronous route
@app.get("/sync-wait")
def sync_wait():
    time.sleep(2)  # Blocking delay of 2 seconds
    return {"message": "Completed sync wait"}

# Asynchronous route
@app.get("/async-wait")
async def async_wait():
    await asyncio.sleep(2)  # Non-blocking delay of 2 seconds
    return {"message": "Completed async wait"}
```

### 6. **What is the difference between synchronous (`def`) and asynchronous (`async def`) endpoints in FastAPI?**

The main difference between **synchronous (`def`)** and **asynchronous (`async def`)** endpoints in FastAPI lies in how they handle concurrent tasks:

- **Synchronous (def)**: Executes in a blocking manner. If the function performs a long-running I/O operation (like a database call or API request), it blocks the event loop until the operation is completed, meaning no other request can be processed in the meantime.
  
  Example:

  ```python
  @app.get("/sync/")
  def sync_endpoint():
      return {"message": "This is a synchronous endpoint"}
  ```

- **Asynchronous (async def)**: Executes in a non-blocking manner. It uses Python’s `asyncio` library to pause the function during I/O-bound operations and allow other requests to be processed in the meantime. This is more efficient when handling multiple I/O-bound tasks like database access or network calls.

  Example:

  ```python
  @app.get("/async/")
  async def async_endpoint():
      return {"message": "This is an asynchronous endpoint"}
  ```

The **key difference** is that asynchronous routes (`async def`) allow FastAPI to handle multiple I/O-bound operations concurrently without blocking, making the application more scalable.


### 7. **What is `await` and how does it work in asynchronous FastAPI routes?**

`await` is used in asynchronous functions (`async def`) to pause the execution of the function until an asynchronous operation (like I/O) completes. This allows the event loop to continue handling other requests during the wait time, making the application non-blocking.

In FastAPI, you use `await` to call other asynchronous functions or I/O-bound operations, such as:

```python
@app.get("/data/")
async def get_data():
    result = await some_async_operation()  # Pause execution until operation is done
    return {"data": result}
```

Without `await`, the asynchronous function would not properly handle non-blocking operations, reducing the efficiency of the asynchronous code.

---

## Path Operations and Type Annotations

### 1. What is the purpose of using type annotations in Python, and how does FastAPI leverage them?

Type annotations in Python allow developers to specify the expected data types of variables, function parameters, and return values. They improve code readability and maintainability, providing a way for IDEs and static type checkers to validate data types before runtime. FastAPI leverages type annotations to perform automatic validation and serialization of request and response data, enabling it to generate JSON schemas, validate input data, and return detailed error messages if types don't match.

### 2. Explain the difference between path parameters, query parameters, and body fields in FastAPI.

In FastAPI, path parameters are part of the URL and are required (`e.g., /items/{item_id}`). Query parameters are optional and are specified after a question mark in the URL (`e.g., ?q=search_term`). Body fields are parts of the request body, typically used in `POST` and `PUT` requests to send structured data as JSON.

### 3. Why might you use default values for query parameters or body fields in FastAPI?

Default values for query parameters and body fields allow parameters to be optional, providing flexibility to the API user. For instance, an endpoint may have optional filters or settings that enhance the user experience without making them required inputs. Default values simplify usage by assuming typical values if none are provided.

### 4. Write a FastAPI endpoint to manage a list of `Book` items in a library. The endpoint should allow a user to retrieve a book by `book_id` using a `GET` request and to create a new book using a `POST` request. Each `Book` should have a title (required), an author (required), and an optional summary (default to `"No summary available"`). The `book_id` parameter should be an integer in the path.

```python
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Book Model
class Book(BaseModel):
    title: str
    author: str
    summary: Optional[str] = "No summary available"

# In-memory book storage for demonstration purposes
books = {}

# GET endpoint to retrieve a book by its ID
@app.get("/books/{book_id}")
async def get_book(book_id: int):
    book = books.get(book_id)
    if book:
        return book
    return {"error": "Book not found"}

# POST endpoint to create a new book
@app.post("/books/{book_id}")
async def create_book(book_id: int, book: Book):
    books[book_id] = book
    return {"book_id": book_id, "book": book}

# Example usage:
# GET /books/1 -> Retrieve the book with ID 1
# POST /books/1 with JSON body -> {"title": "Book Title", "author": "Author Name"} to create a book
```

### 5. Modify the POST endpoint to return an error if a book with the given book_id already exists.

```python
@app.post("/books/{book_id}")
async def create_book(book_id: int, book: Book):
    if book_id in books:
        return {"error": "Book with this ID already exists"}
    books[book_id] = book
    return {"book_id": book_id, "book": book}
```

## Authentication & Authorization

### 1. Can you explain the OAuth2 Password Grant flow and when it should be used?

The OAuth2 Password Grant flow is a process where a trusted client app directly requests access tokens by sending a username and password to the authorization server. This flow is ideal for first-party applications or legacy systems where it’s safe for the app to handle the user’s credentials directly. It is generally not recommended for third-party apps because it involves sharing user credentials with the client app.

### 2. What is a JWT, and how does it help in securing APIs?

A JSON Web Token (JWT) is a compact, URL-safe token used for securely transmitting information between parties. It consists of three parts: the header, payload, and signature. JWTs are signed using a secret or a public/private key, making them tamper-proof. They help secure APIs by allowing stateless authentication; once a token is issued, it can be verified without requiring session storage on the server, making it efficient and scalable for authentication purposes.

### 3. What is the role of the `Depends` dependency in FastAPI, and how can it be used for securing endpoints?

In FastAPI, `Depends` is a dependency injection tool that allows us to define shared functionality or services that can be injected into routes. For securing endpoints, `Depends` can be used to enforce authentication checks by requiring a token validation function that ensures the requester has a valid token before accessing the endpoint. This helps centralize and streamline access control in an application.

### 4. Write a function in Python to generate a JWT token with a specific expiration time. The function should accept a payload, secret key, algorithm, and expiration in minutes

```python
from datetime import datetime, timedelta
import jwt

def create_jwt_token(payload: dict, secret_key: str, algorithm: str, expires_in_minutes: int):
    to_encode = payload.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_in_minutes)
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, secret_key, algorithm=algorithm)
    return token

# Example usage:
payload = {"user_id": "123"}
secret_key = "your_secret_key"
algorithm = "HS256"
token = create_jwt_token(payload, secret_key, algorithm, expires_in_minutes=30)
print("JWT Token:", token)
```

### 5. Given a FastAPI endpoint, secure it by validating the JWT token using a dependency. The token should be decoded, and if valid, the user information should be returned

```python
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return {"username": username}
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.get("/protected-route")
async def protected_route(current_user: dict = Depends(get_current_user)):
    return {"message": "Access granted", "user": current_user}
```

### 6. Create a function to hash a password and another to verify a password against the hashed version. Use the `passlib` library for hashing

```python
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Example usage
plain_password = "secure_password"
hashed = hash_password(plain_password)
print("Hashed Password:", hashed)
print("Password Match:", verify_password("secure_password", hashed))  # Should return True
```

### 7.  Write a FastAPI route to log in a user using the OAuth2 Password Grant flow, authenticate with a token, and access a protected resource

```python
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta
import jwt

app = FastAPI()
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

fake_user_db = {
    "johndoe": {
        "username": "johndoe",
        "hashed_password": "$2b$12$KIXQ9a7GpqMgB1grPEfA/OTLO9z.eYdSwOznYoEtgg/jYeWUcPI6S",  # hashed version of "password123"
    }
}

def authenticate_user(username: str, password: str):
    user = fake_user_db.get(username)
    if not user:
        return False
    if not pwd_context.verify(password, user["hashed_password"]):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": user["username"]}, expires_delta=timedelta(minutes=30))
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/protected")
async def read_protected(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return {"user": username}
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
```

### 8. Can you explain how you would implement authentication and authorization in FastAPI?

FastAPI provides a security module to implement authentication and authorization. For authentication, OAuth2PasswordBearer is used which requires a URL that the client will use for token retrieval. The get_current_user function uses Depends to inject dependencies, where it decodes the token and fetches user data. If invalid, HTTPException is raised.

For authorization, FastAPI offers Security Scopes. Each route can have a list of scopes as dependencies. When a request comes in, FastAPI checks if the current user has required scopes. If not, an error is returned.

```py
from fastapi import Depends, FastAPI, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer, SecurityScopes

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(security_scopes: SecurityScopes, token: str = Depends(oauth2_scheme)):
    # decode token and fetch user data here
    raise HTTPException(status_code=403, detail="Not authenticated")

app = FastAPI()

@app.get("/items/", dependencies=[Depends(Security(get_current_user, scopes=["items:read"]))])
async def read_items():
    return [{"item": "Foo", "value": "Bar"}]
```

### 9. How would you handle exception handling and custom error responses in FastAPI?

FastAPI provides built-in exception handling. To handle exceptions, use the HTTPException class from fastapi.exceptions module. This class accepts status_code and detail parameters to define HTTP status code and error message respectively.

For custom error responses, create a subclass of HTTPException and override its attributes. You can also customize the validation error response body by creating a route operation function that raises RequestValidationError from fastapi.exceptions and catch it in an exception handler.

```py
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": f"Oops! {exc.detail}"},
    )

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
```
