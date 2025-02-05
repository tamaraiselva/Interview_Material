# Intermediate FastApi

## Table of Contents

1. [WebSockets](#WebSockets)

2. [Background Tasks](#Background_Tasks)

3. [Dependency Injection (Advanced)](#Dependency_Injection_(Advanced))

4. [Event Handling](#Event_Handling)

5. [API Versioning](#API_Versioning)

6. [Rate Limiting and Throttling](#Rate_Limiting_and_Throttling)

7. [Performance Optimization](#Performance_Optimization)

8. [Security Best Practices](#Security_Best_Practices)

9. [Production Deployment](#Production_Deployment)

10. [API Documentation](#API_Documentation)

## WebSockets

### 1. What are WebSockets, and how do they differ from HTTP?

WebSockets are a protocol that allows for full-duplex communication between client and server over a single, long-lived connection. Unlike HTTP, which is stateless and requires separate requests for each interaction, WebSockets enable persistent connections that support real-time, bidirectional data exchange. This makes WebSockets ideal for applications needing low latency, such as chat apps, notifications, and collaborative tools.

### 2. How does FastAPI support WebSocket connections, and what are the steps to set up a WebSocket endpoint?

FastAPI provides native support for `WebSockets` through its WebSocket class. To create a WebSocket endpoint, we use `@app.websocket()` instead of `@app.get()` or `@app.post()`. Within this endpoint:

- Use await websocket.accept() to start the WebSocket communication.

- Use await websocket.receive_text() to get messages from the client.

- Use await websocket.send_text() to send messages back to the client.

### 3. Describe a scenario where WebSockets would be preferred over HTTP long polling.

In a chat application, WebSockets are preferred because they allow real-time, bidirectional communication with low latency. With HTTP long polling, each client would need to make repeated requests to check for new messages, leading to increased server load and slower response times. WebSockets maintain an open connection, enabling instant message transmission and response with less server overhead.

### 4. What are some challenges when using WebSockets, and how can they be mitigated?

**Some challenges include:**

- **Connection management:** Handling multiple concurrent connections requires efficient resource allocation and may need tools like Redis to manage state in distributed environments.

- **Error handling and reconnections:** If a connection is dropped, reconnecting can be managed by implementing client-side retry logic.

- **Scalability:** WebSocket connections are stateful, so scaling WebSocket applications often requires load balancers capable of handling sticky sessions or specialized servers that support WebSocket connections, like NGINX.

### 5. Implement a WebSocket endpoint in FastAPI that allows clients to connect and receive messages broadcast to all other connected clients. When a client sends a message, it should be shared with every other connected client, including the sender.

```python
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List

app = FastAPI()

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"Message from client: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
```

## Background Tasks

### 1. What are background tasks in FastAPI, and why are they useful?

In FastAPI, background tasks allow certain operations to be performed without blocking the response to the client. The `BackgroundTasks` class can be used to queue tasks that need to run in the background after a client’s request has been processed. Background tasks are especially useful for operations that don't require an immediate response, such as sending emails, processing data, logging information, or notifying third-party services.

### 2. Write a FastAPI endpoint for registering a user. When a new user registers, send a welcome email in the background. Assume that the email sending function is already defined.

```python
from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

# Assume this function sends an email
def send_welcome_email(email_to: str, subject: str, body: str):
    # Simulate email sending (the actual implementation could involve SMTP, etc.)
    print(f"Email sent to {email_to}: {subject} - {body}")

@app.post("/register/")
async def register_user(username: str, email: str, background_tasks: BackgroundTasks):
    # Registration logic (simulated here)
    # This could include saving user details to a database, etc.
    print(f"User {username} registered with email {email}")

    # Add the task to send a welcome email in the background
    background_tasks.add_task(send_welcome_email, email, "Welcome!", f"Hello {username}, thanks for joining us!")

    # Respond immediately to the client
    return {"message": "User registered successfully!"}
```

## Dependency Injection (Advanced)

### 1. How would you manage complex dependencies in a FastAPI application, and why is dependency caching important?

In FastAPI, complex dependencies are often managed by creating modular, layered dependencies where each dependency can rely on other dependencies, forming a dependency tree. This is achieved using FastAPI’s `Depends` mechanism, allowing each dependency to declare its own dependencies. For instance, if a `DatabaseService` depends on a `ConfigurationService` that requires environment-specific settings, `DatabaseService` can use `ConfigurationService` through Depends.

Dependency caching is important in FastAPI as it allows resources to be reused across a single request lifecycle. By default, FastAPI caches dependencies per request, meaning that any given dependency instance is created once and reused in multiple places if called again. This is particularly helpful for resources like database connections, external API clients, or computationally expensive objects. Without caching, these resources would need to be re-initialized every time they are requested, which would degrade performance and increase resource usage.

### 2. Given the following requirements, implement a FastAPI service that demonstrates dependency injection with caching and sub-dependencies.

**Requirements:**

- Create a `Settings` dependency that fetches some configuration settings.

- Implement a `DatabaseService` class that connects to a database using settings from `Settings`.

- Create an `AuthService` class that uses `DatabaseService` to authenticate a user.
Finally, create an endpoint that uses `AuthService` to check user authentication.

```python
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseSettings
from typing import Dict

app = FastAPI()

# Step 1: Define a Settings class to handle configuration
class Settings(BaseSettings):
    database_url: str = "sqlite:///:memory:"  # Default value for demonstration

# Step 2: Define the DatabaseService, which uses Settings as a dependency
class DatabaseService:
    def __init__(self, settings: Settings = Depends()):
        self.connection_string = settings.database_url

    def fetch_user(self, username: str) -> Dict[str, str]:
        # Simulate fetching a user from the database
        if username == "admin":
            return {"username": "admin", "password": "secret"}
        return {}

# Step 3: Define the AuthService, which depends on DatabaseService
class AuthService:
    def __init__(self, db_service: DatabaseService = Depends()):
        self.db_service = db_service

    def authenticate_user(self, username: str, password: str) -> bool:
        user = self.db_service.fetch_user(username)
        if user and user["password"] == password:
            return True
        return False

# Step 4: Define an endpoint that uses AuthService to check authentication
@app.post("/login")
async def login(username: str, password: str, auth_service: AuthService = Depends()):
    if auth_service.authenticate_user(username, password):
        return {"message": "Authenticated successfully"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")

# Run the application (for demonstration only, use `uvicorn` to run in production)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
```

## Event Handling

### 1. Why are startup and shutdown events important in a web application like FastAPI?

Startup and shutdown events are crucial for initializing and cleaning up resources that should persist across multiple requests, enhancing both performance and stability. For example, initializing a database connection pool at startup allows the application to reuse connections across requests, which is more efficient than establishing a new connection each time. Similarly, gracefully closing connections or terminating background jobs during shutdown prevents data loss or corruption. These events help ensure resources are managed correctly, preventing potential memory leaks and resource conflicts.

### 2. How do you handle startup and shutdown events in FastAPI?

FastAPI provides the @app.on_event decorator to define event handlers for both startup and shutdown events. By using @app.on_event("startup"), you can define functions that will run when the application starts, while @app.on_event("shutdown") allows you to define functions that run when the application stops. These decorators enable you to manage resource allocation and cleanup effectively. For example, initializing a database connection pool during startup and closing it on shutdown is a common use case.

### 3. Implement a FastAPI application that initializes a mock database connection at startup and closes it during shutdown. Use this connection to handle a simple request.

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()
database_connected = False  # A mock variable to simulate the database connection state

@app.on_event("startup")
async def startup_event():
    global database_connected
    database_connected = True
    print("Database connection established.")  # Simulating database connection

@app.on_event("shutdown")
async def shutdown_event():
    global database_connected
    database_connected = False
    print("Database connection closed.")  # Simulating closing the database connection

@app.get("/")
async def read_root():
    if not database_connected:
        raise HTTPException(status_code=500, detail="Database connection is not available.")
    return {"message": "Database is connected!"}
```

### 4. How would you handle errors if the database fails to connect during the startup event?

If the database fails to connect during startup, you can handle it with a try-except block to catch exceptions. You could log the error for debugging purposes and potentially retry the connection a certain number of times. If retries fail, you may choose to raise an exception, stopping the application from running with an incomplete setup, which helps avoid unexpected behavior.

**Code Example for Follow-Up**

```python
@app.on_event("startup")
async def startup_event():
    global database_connected
    try:
        # Simulating a connection attempt with potential failure
        database_connected = True
        print("Database connection established.")
    except Exception as e:
        print(f"Failed to connect to database: {e}")
        database_connected = False
```

## API Versioning

### 1. What are the benefits and drawbacks of different API versioning strategies?

Different API versioning strategies serve different purposes. URL Path Versioning is easy to implement, straightforward, and highly visible, making it widely preferred. However, it can lead to duplicate routes and logic. Header Versioning keeps URLs clean but requires clients to manage headers correctly, which might be less intuitive. Query Parameter Versioning provides flexibility and ease of testing but may cause confusion if not documented well. Hostname/Subdomain Versioning allows for complete independence between versions but can be complex to manage and requires additional infrastructure support, like reverse proxies.

### 2. How would you ensure backward compatibility when introducing a new version to an API?

To ensure backward compatibility, I would implement a few key strategies. First, I’d introduce the new version gradually and mark certain features or fields as deprecated in the current version, with clear documentation for clients about the upcoming changes. I’d separate shared logic into modular functions to avoid redundancy across versions, making maintenance easier and safer. I’d also define version-specific schemas to handle any structural changes in the API response. Finally, comprehensive version-specific testing would be essential to catch any potential breaking changes across different API versions.

### 3. Create an API using FastAPI that supports two versions (v1 and v2) for a `GET /items/{item_id}` endpoint. In version 1, return `name` for the item. In version 2, return `title` and an optional `description`.

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Version-specific schemas
class ItemV1(BaseModel):
    id: int
    name: str

class ItemV2(BaseModel):
    id: int
    title: str
    description: str = None

# Mock data
items_data_v1 = {
    1: {"id": 1, "name": "Old Item"},
    2: {"id": 2, "name": "Legacy Item"}
}

items_data_v2 = {
    1: {"id": 1, "title": "New Item", "description": "Updated description"},
    2: {"id": 2, "title": "Refreshed Item", "description": "Improved features"}
}

# v1 endpoint
@app.get("/v1/items/{item_id}", response_model=ItemV1)
async def get_item_v1(item_id: int):
    item = items_data_v1.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found in v1")
    return item

# v2 endpoint
@app.get("/v2/items/{item_id}", response_model=ItemV2)
async def get_item_v2(item_id: int):
    item = items_data_v2.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found in v2")
    return item
```

## Rate Limiting and Throttling

### 1. Can you explain the difference between rate limiting and throttling, and why they are important in modern APIs?

Rate limiting and throttling are techniques to control the flow of requests to an API.

- Rate Limiting sets a cap on the number of requests a client (often identified by IP or API key) can make within a specific period, such as 100 requests per minute. Once the limit is reached, additional requests are denied (often with a 429 Too Many Requests error).

- Throttling also controls the flow of requests but often in a more flexible way, slowing down the request rate instead of outright rejecting requests. For example, after reaching a certain threshold, the system may introduce delays between requests rather than blocking them completely.

### 2. Write a simple middleware function in Python that limits a client to 5 requests per minute, using their IP address as an identifier. Assume that request data can be stored in a dictionary in memory.

```python
from time import time
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory store to keep track of requests per IP
request_counts = {}
RATE_LIMIT = 5  # max requests
WINDOW_SIZE = 60  # window size in seconds

def rate_limit_middleware():
    ip = request.remote_addr
    current_time = time()

    # Initialize request tracking for new IPs
    if ip not in request_counts:
        request_counts[ip] = []

    # Remove requests outside the window
    request_counts[ip] = [t for t in request_counts[ip] if t > current_time - WINDOW_SIZE]

    # Check if the request limit has been reached
    if len(request_counts[ip]) >= RATE_LIMIT:
        return jsonify({"error": "Rate limit exceeded"}), 429

    # Add current request time to the list for this IP
    request_counts[ip].append(current_time)

@app.before_request
def before_request():
    rate_limit_exceeded = rate_limit_middleware()
    if rate_limit_exceeded:
        return rate_limit_exceeded

@app.route("/")
def index():
    return jsonify({"message": "Welcome! You are within the rate limit."})

if __name__ == "__main__":
    app.run(debug=True)
```

### 3. Write a class `RateLimiter` in Python that allows you to specify a maximum number of requests and a time window. This class should provide a method, `allow_request(user_id)`, that returns `True` if the request is allowed and `False` if it exceeds the limit.

```python
from time import time

class RateLimiter:
    def __init__(self, max_requests, window_size):
        self.max_requests = max_requests
        self.window_size = window_size
        self.request_log = {}

    def allow_request(self, user_id):
        current_time = time()

        # Initialize request tracking for new user
        if user_id not in self.request_log:
            self.request_log[user_id] = []

        # Remove old requests outside the window
        self.request_log[user_id] = [
            timestamp for timestamp in self.request_log[user_id] 
            if timestamp > current_time - self.window_size
        ]

        # Check if the request limit has been reached
        if len(self.request_log[user_id]) >= self.max_requests:
            return False

        # Log the current request
        self.request_log[user_id].append(current_time)
        return True

# Example Usage:
rate_limiter = RateLimiter(max_requests=3, window_size=10)  # 3 requests per 10 seconds

# Simulating requests from user_id '123'
print(rate_limiter.allow_request('123'))  # True
print(rate_limiter.allow_request('123'))  # True
print(rate_limiter.allow_request('123'))  # True
print(rate_limiter.allow_request('123'))  # False (limit exceeded)
```

## Performance Optimization

### 1. Explain how FastAPI leverages ASGI and async I/O to enhance performance. How does this differ from traditional synchronous frameworks?

FastAPI uses the ASGI (Asynchronous Server Gateway Interface) specification, which allows for asynchronous request handling. Unlike WSGI, which is synchronous and only supports one request per thread, ASGI enables non-blocking, asynchronous I/O operations. This allows FastAPI to handle multiple requests concurrently using `async` and `await` in Python.

In synchronous frameworks, each request would block the server thread while waiting for I/O operations, like database queries. FastAPI's async support, on the other hand, means the server can continue to process other requests even while waiting for I/O operations to complete, which significantly improves performance for I/O-bound tasks.

### 2. Describe a situation where you optimized an API or service for performance. What steps did you take, and what was the outcome?

In my last project, I worked on optimizing a FastAPI-based application that had performance issues due to high database load. I started by profiling the application with `cProfile` to identify bottlenecks. I noticed that certain database queries were taking longer than expected, especially on frequently accessed endpoints.

To resolve this, I implemented Redis-based caching for some of the endpoint responses, reducing the number of repeated database calls. Additionally, I made sure to use async database queries to take advantage of FastAPI's non-blocking I/O. These changes reduced our response times by 50% and improved the application’s RPS (requests per second) significantly, allowing us to handle more traffic with fewer resources.

### 3. Implement a FastAPI endpoint that fetches a list of books from a database. Assume each book has a title, author, and year. Use Redis caching to store the response for 30 seconds to reduce database load.

**Answer:**

Here's an example of how this could be implemented, assuming we use Redis for caching with `fastapi-cache2` and `aioredis` for Redis support.

1. Install the necessary libraries:

```bash
pip install fastapi-cache2 aioredis
```

2. Implement the endpoint with Redis caching:

```python
from fastapi import FastAPI, Depends
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from pydantic import BaseModel
from redis import asyncio as aioredis
import databases
import sqlalchemy

# Define the database and table setup (assuming SQLite for the example)
DATABASE_URL = "sqlite:///./test.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

books = sqlalchemy.Table(
    "books",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String),
    sqlalchemy.Column("author", sqlalchemy.String),
    sqlalchemy.Column("year", sqlalchemy.Integer),
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

app = FastAPI()

# Pydantic model for a Book
class Book(BaseModel):
    title: str
    author: str
    year: int

@app.on_event("startup")
async def startup():
    # Initialize Redis connection
    redis = aioredis.from_url("redis://localhost:6379")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Caching the endpoint with a 30-second TTL
@app.get("/books", response_model=list[Book])
@cache(expire=30)
async def get_books():
    query = books.select()
    return await database.fetch_all(query)
```

### 4. Modify the above endpoint to accept query parameters (`author` and `year`) and use them to filter the books retrieved from the database. Ensure the caching takes these parameters into account.


```python
from typing import Optional

@app.get("/books", response_model=list[Book])
@cache(expire=30)
async def get_books(author: Optional[str] = None, year: Optional[int] = None):
    query = books.select()
    
    # Build dynamic filtering based on query parameters
    if author:
        query = query.where(books.c.author == author)
    if year:
        query = query.where(books.c.year == year)
    
    return await database.fetch_all(query)
```

## Security Best Practices

### 1. Explain how CSRF (Cross-Site Request Forgery) and CORS (Cross-Origin Resource Sharing) differ. What techniques can be used to prevent CSRF attacks in web applications?

CSRF and CORS are both related to web security but address different aspects of web interactions:

- **CSRF:** CSRF (Cross-Site Request Forgery) is an attack where an unauthorized request is made on behalf of an authenticated user without their consent. It exploits the trust that a site has in the user’s browser, which sends valid cookies along with the request. Attackers trick users into submitting requests they didn’t intend, often via malicious links or embedded forms.

- **CSRF Prevention Techniques:**
  1. **CSRF Tokens:** Use unique tokens that must be sent with each state-changing request, ensuring only genuine requests are accepted.

  2. **Same-Site Cookies:** Set cookies with the `SameSite` attribute to restrict the browser from sending cookies with requests initiated from other sites.

  3. **Double Submit Cookies:** Require the CSRF token to be included both in the request header and as a cookie.

- **CORS:** CORS (Cross-Origin Resource Sharing) is a security feature that restricts resources on a web page to be requested only from the same origin, unless the server explicitly allows requests from other origins. CORS is handled at the server level, where the server specifies which domains, headers, and methods are allowed to access the resources.

### 2. Implement a simple role-based access control (RBAC) system in Python. Write a function that takes a user’s role and a requested action, then returns whether the action is permitted based on predefined role permissions.

Roles and permissions:

Admin: Can perform `read`, `write`, `delete`.
Editor: Can perform `read`, `write`.
Viewer: Can only perform `read`.

```python
# Define the roles and their respective permissions
ROLE_PERMISSIONS = {
    'admin': {'read', 'write', 'delete'},
    'editor': {'read', 'write'},
    'viewer': {'read'}
}

def can_perform_action(role, action):
    """
    Check if the specified role has permission for the requested action.

    Parameters:
        role (str): The user's role (e.g., 'admin', 'editor', 'viewer').
        action (str): The requested action (e.g., 'read', 'write', 'delete').

    Returns:
        bool: True if the action is permitted for the role, False otherwise.
    """
    # Get the permissions for the specified role
    permissions = ROLE_PERMISSIONS.get(role.lower())
    
    # Check if the action is permitted for the role
    return action in permissions if permissions else False

# Test cases
print(can_perform_action('admin', 'delete'))   # Expected: True
print(can_perform_action('editor', 'delete'))  # Expected: False
print(can_perform_action('viewer', 'read'))    # Expected: True
print(can_perform_action('viewer', 'write'))   # Expected: False
```

## Production Deployment

### 1. How would you deploy a FastAPI application in a production environment?

To deploy a FastAPI application in production, I would start by containerizing the application using Docker. I’d write a Dockerfile to package the application and its dependencies into a Docker image. Once the Docker image is built, I would use Kubernetes for deployment, allowing the application to run on multiple replicas, ensuring scalability and high availability.

In Kubernetes, I’d define a Deployment and a Service. The Deployment manages the replicas, while the Service provides load balancing. If it’s a cloud-based deployment, I’d leverage services like AWS EKS, Google GKE, or Azure AKS for managed Kubernetes or use cloud-specific options like AWS Fargate, Google Cloud Run, or Azure App Service, which handle infrastructure management.

### 2. How would you implement logging and monitoring for a FastAPI application in production?

For logging, I would configure structured JSON logs using libraries like `loguru` or `structlog` in FastAPI. I’d send these logs to a centralized logging service, like the ELK Stack (Elasticsearch, Logstash, Kibana) or use cloud logging options like AWS CloudWatch or Google Cloud Logging.

For monitoring, I’d integrate Prometheus and Grafana. Prometheus would scrape metrics from a /`metrics` endpoint in FastAPI, and Grafana would visualize these metrics on dashboards for real-time insights. Additionally, I’d use distributed tracing with tools like OpenTelemetry or Jaeger to capture end-to-end request flows across microservices, helping identify performance bottlenecks.

### 3. What is load balancing, and how can it be set up for a FastAPI application?

Load balancing distributes incoming traffic across multiple instances of an application to prevent any single instance from becoming overwhelmed. In Kubernetes, a Service of type `LoadBalancer` can be set up to manage traffic distribution automatically.

Alternatively, I could configure NGINX or HAProxy as an external load balancer to handle more custom routing rules and traffic distribution. In cloud environments, managed load balancers, like AWS Elastic Load Balancer or Google Cloud Load Balancer, can simplify this setup while providing features such as SSL termination and auto-scaling integration.

### 4. Write a Dockerfile for a FastAPI application that ensures it can be deployed to a production environment with Uvicorn as the server.

```dockerfile
# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Set environment variables for production
ENV UVICORN_HOST=0.0.0.0
ENV UVICORN_PORT=8000
ENV LOG_LEVEL=info

# Run the FastAPI application using Uvicorn
CMD ["uvicorn", "main:app", "--host", "${UVICORN_HOST}", "--port", "${UVICORN_PORT}", "--log-level", "${LOG_LEVEL}"]
```

### 5. Implement a /metrics endpoint in FastAPI that exposes metrics in a format compatible with Prometheus.

```python
from fastapi import FastAPI, Request
from prometheus_client import Counter, generate_latest
from starlette.responses import Response

app = FastAPI()

# Define a counter to track the number of requests
REQUEST_COUNT = Counter('http_requests_total', 'Total number of HTTP requests')

@app.middleware("http")
async def increment_request_count(request: Request, call_next):
    response = await call_next(request)
    REQUEST_COUNT.inc()  # Increment the request count
    return response

@app.get("/metrics")
async def metrics():
    # Return the Prometheus metrics in plain text format
    return Response(generate_latest(), media_type="text/plain")
```

### 6. Describe a time when you faced a challenge with deploying or scaling a web application. How did you approach and resolve it?

In a previous role, we had an issue where our application couldn’t handle a sudden spike in traffic during a product launch. The application was running on a small number of instances, and as traffic increased, latency skyrocketed, affecting user experience.

To resolve this, I restructured the deployment using Kubernetes. I set up a Horizontal Pod Autoscaler to dynamically scale instances based on CPU usage. I also set up a load balancer to evenly distribute traffic across instances. This setup allowed our application to handle increased load smoothly, and it prepared us to handle future traffic spikes with minimal intervention.

## API Documentation

### 1. What are some ways to optimize the performance of a REST API in FastAPI?

To optimize the performance of a REST API in FastAPI, you can:

1. **Use Asynchronous Programming:** FastAPI supports asynchronous I/O, which can help to manage concurrent requests effectively without blocking. Use async and await keywords for I/O-bound operations.

2. **Leverage Caching:** Use in-memory caches like Redis or memory-based caches for frequently accessed data that does not change often.

3. **Database Connection Pooling:** Use connection pooling with libraries like asyncpg or databases when connecting to databases, which reduces the time spent establishing new connections.

4. **Reduce Data Sent Over Network:** Use response models to restrict the fields returned by the API. Avoid sending unnecessary data in responses, minimizing response payloads.

5. **Use Background Tasks for Long-Running Operations:** Offload intensive tasks (like sending emails, or processing large files) using FastAPI's BackgroundTasks.

6. **Implement Pagination and Filtering:** Reduce the number of items returned in API responses by implementing pagination and filtering for large datasets.

7. **Optimize Database Queries:** Avoid N+1 query issues, use indexes, and consider joins or aggregations to reduce the number of queries made per request.

8. **Enable Gzip Compression:** Use FastAPI’s Gzip middleware to compress responses, reducing the response size.

### 2. Write an endpoint in FastAPI to create and retrieve users from an in-memory list. The user should have an ID, name, and email address. Implement the following features?

- An endpoint to add a new user.
- An endpoint to retrieve all users.
- Ensure that each email address is unique.

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List

app = FastAPI()

# In-memory storage for users
users_db = []

# Pydantic model for user
class User(BaseModel):
    id: int
    name: str
    email: EmailStr

# Endpoint to add a new user
@app.post("/users/", response_model=User)
async def create_user(user: User):
    # Check for unique email address
    if any(u['email'] == user.email for u in users_db):
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Add user to database
    users_db.append(user.dict())
    return user

# Endpoint to retrieve all users
@app.get("/users/", response_model=List[User])
async def get_users():
    return users_db
```
