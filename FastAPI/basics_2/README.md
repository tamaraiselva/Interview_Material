# FASTAPI

## Table of Contents

- [1. Response Handling](#Response-Handling)

- [2. Dependency Injection](#Dependency-Injection)

- [3. Error Handling](#Error-Handling)

## Response Handling

### Q1: How does FastAPI handle JSON responses by default?

**`Answer:`** FastAPI automatically serializes Python dictionaries and lists to JSON when returned from an endpoint. The framework handles the conversion of the return value into a JSON-formatted response and sets the appropriate Content-Type: application/json header. For example, returning {"key": "value"} will automatically be serialized into a JSON object.

### Q2: How can you customize the HTTP status code of a FastAPI response?

**`Answer:`** You can customize the HTTP status code of a response by using the `status_code` parameter in the route decorator. For example, to return a 201 status code for a successful POST request:

```python
@app.post("/items/", status_code=201)
async def create_item(item: dict):
    return {"message": "Item created"}
```

Alternatively, you can use constants from `fastapi.status` like `status.HTTP_201_CREATED`.

### Q3: What is the purpose of `JSONResponse` in FastAPI, and when should you use it?

**`Answer:`** `JSONResponse` is a response class that you can use when you need more control over the response being returned. Although FastAPI automatically serializes return values into JSON, `JSONResponse` allows you to explicitly create a JSON response, customize status codes, and add headers or manipulate the structure of the JSON data.

```python
from fastapi.responses import JSONResponse

@app.get("/custom_json/")
async def custom_json():
    return JSONResponse(content={"message": "Custom response"}, status_code=200)
```

### Q4: What is the difference between Response and JSONResponse in FastAPI?

**`Answer:`**

- `Response:` Used for more generic responses where you need to control the raw response, including the content type, headers, and status code. It's useful when returning non-JSON content, like plain text or HTML.

- `JSONResponse:` A specific type of `Response` optimized for returning JSON data. It automatically sets the `Content-Type: application/json` header and serializes Python objects to JSON.

### Q5: How can you return non-JSON content like plain text or HTML in FastAPI?

**`Answer:`** You can use the `Response` class and specify the appropriate `media_type`. For example, to return plain text:

```python
from fastapi import Response

@app.get("/plaintext/")
async def get_plaintext():
    return Response(content="This is plain text", media_type="text/plain")
```

### Q6: Write an endpoint in FastAPI that returns a JSON response with a status code `201 Created`, and adds a custom header called `X-Header`?

**`Answer:`**

```python
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/create-item/")
async def create_item(item: dict):
    headers = {"X-Header": "Custom-Header"}
    return JSONResponse(content={"message": "Item created"}, status_code=201, headers=headers)
```

### Q7: Create a FastAPI endpoint that returns a simple HTML page as a response

**`Answer:`**

```python
from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/html/")
async def get_html():
    html_content = """
    <html>
        <head>
            <title>Sample HTML</title>
        </head>
        <body>
            <h1>Hello, FastAPI!</h1>
        </body>
    </html>
    """
    return Response(content=html_content, media_type="text/html")
```

### Q8: Create an endpoint in FastAPI that always returns a 404 Not Found status code with a custom error message in JSON format

**`Answer:`**

```python
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/not-found/")
async def not_found():
    return JSONResponse(content={"error": "Item not found"}, status_code=404)
```

## Dependency Injection

### Q1: What is Dependency Injection, and why is it important in FastAPI?

**`Answer:`** Dependency Injection (DI) is a design pattern where objects or services (dependencies) are provided to other objects or functions that need them, instead of those objects creating the dependencies themselves. In FastAPI, DI helps in separating concerns by letting you manage external resources like databases, authentication systems, or configuration values outside your business logic.

The benefits of using DI in FastAPI include:

- **`Loose Coupling:`** The code is less dependent on concrete implementations, which makes it easier to modify or extend.

- **`Reusability:`** Dependencies like database connections or authentication mechanisms can be shared across multiple routes.

- **`Testability:`** DI allows for easier mocking of dependencies, making unit testing more straightforward.

- **`Maintainability:`** It promotes clean architecture by separating configuration and infrastructure concerns from the core business logic.

### Q2: Can you explain how `Depends()` works in FastAPI?

**`Answer:`** In FastAPI, `Depends()` is a function that enables Dependency Injection. It allows you to declare a dependency inside a route, and FastAPI will handle the resolution of that dependency automatically. You use `Depends()` to tell FastAPI that a specific parameter in a route (or another dependency) should be provided by calling a specific function or class.

FastAPI automatically manages the lifecycle of the dependencies, including executing the dependency function before the route handler and injecting the return value into the parameter that declares the dependency.

For example, if a route needs to authenticate a user, you can use `Depends(authenticate_user)` to declare the authentication logic as a dependency, and FastAPI will handle the logic of calling the `authenticate_user` function and injecting the result into the route.

### Q3: Write a simple FastAPI route that demonstrates the use of dependency injection. The dependency should return a hardcoded API key, and the route should check if the correct API key was provided in the request?

**`Answer:`**

```python
from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

# Dependency function to return an API key
def get_api_key():
    return "supersecretkey"

# Route that depends on the API key
@app.get("/protected-data")
async def read_protected_data(api_key: str = Depends(get_api_key)):
    if api_key != "supersecretkey":
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return {"message": "You have access to protected data!"}
```

### Q4: Create a FastAPI application that uses a class as a dependency to manage a simple in-memory store of user information. Implement two endpoints: one for adding a user and one for retrieving user information

**`Answer:`**

```python
from fastapi import FastAPI, Depends

app = FastAPI()

# Class to manage an in-memory user store
class UserStore:
    def __init__(self):
        self.users = {}
    
    def add_user(self, user_id: int, username: str):
        self.users[user_id] = {"user_id": user_id, "username": username}
    
    def get_user(self, user_id: int):
        return self.users.get(user_id, {"error": "User not found"})

# Dependency injection using the UserStore class
def get_user_store():
    return UserStore()

# Endpoint to add a user
@app.post("/users/")
async def add_user(user_id: int, username: str, store: UserStore = Depends(get_user_store)):
    store.add_user(user_id, username)
    return {"message": "User added successfully"}

# Endpoint to retrieve user information
@app.get("/users/{user_id}")
async def get_user(user_id: int, store: UserStore = Depends(get_user_store)):
    return store.get_user(user_id)
```

## Error Handling

### Q1: How would you handle errors in a RESTful API? Specifically, how do you use HTTPException to provide custom error messages and status codes?

**`Answer`**

When developing a RESTful API, proper error handling is crucial for enhancing the user experience and debugging processes. Using `HTTPException` is a common way to handle errors in frameworks like FastAPI or Flask. Here's how you can approach error handling:

- **`Understand HTTP Status Codes:`** Familiarize yourself with the various HTTP status codes (like 404 for "Not Found," 400 for "Bad Request," and 500 for "Internal Server Error") and use them appropriately based on the context of the error.

- **`Use HTTPException:`** In FastAPI, you can raise an `HTTPException` with a specific status code and detail. This allows you to provide clear feedback about what went wrong.

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id < 1:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id}
```

- **`Custom Error Handlers:`** You can also define global error handlers to manage specific exceptions in a consistent manner. This allows you to centralize your error handling logic and format responses uniformly.

```python
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": f"Oops! {exc.detail}"},
    )
```

- **`Logging Errors:`** Implement logging to capture error details, which can help in debugging and monitoring the application’s health.

- **`Client-side Handling:`** Ensure that clients consuming your API are prepared to handle errors based on the status codes and messages returned.

### Q2: Implement a simple FastAPI application that includes an endpoint to divide two numbers. Handle division by zero gracefully by returning a custom error message and status code using `HTTPException`

**`Answer`**

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/divide")
async def divide_numbers(x: float, y: float):
    if y == 0:
        # Raise HTTP 400 Bad Request with a custom message
        raise HTTPException(status_code=400, detail="Division by zero is not allowed.")
    
    result = x / y
    return {"result": result}

# To run the application:
# Use the command: uvicorn filename:app --reload
```

### Q3: Create a FastAPI endpoint that divides two numbers. If the second number is zero, return a 400 status code with the message "Cannot divide by zero."

**`Answer`**

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/divide")
async def divide(x: float, y: float):
    if y == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero.")
    return {"result": x / y}
```

### Q4: Write a FastAPI endpoint that accepts a user ID and retrieves user data. If the user ID is less than or equal to zero, raise an HTTPException with a 400 status code and a message "Invalid user ID."

**`Answer`**

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    if user_id <= 0:
        raise HTTPException(status_code=400, detail="Invalid user ID.")
    
    # Assuming we have a function `get_user_data` that fetches user data
    user_data = get_user_data(user_id)  # Placeholder function
    if user_data is None:
        raise HTTPException(status_code=404, detail="User not found.")
    
    return user_data
```

### Q4: What is `HTTPException` in FastAPI, and how can it be used to handle errors in a web application?

**`Answer`**

`HTTPException` is a built-in exception class in FastAPI that allows developers to raise HTTP errors with specified status codes and custom error messages. When an `HTTPException` is raised, FastAPI automatically generates an HTTP response with the appropriate status code and detail message.

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id < 1:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id}
```
