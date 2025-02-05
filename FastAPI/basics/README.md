# Fastapi

## Table of Contents

- [Introduction to FastAPI](#Introduction-to-FastAPI)

- [Routes and Path Parameters](#Routes-and-Path-Parameters)

- [Request Body](#request-body)

## Introduction to FastAPI

### 1. **What is FastAPI?**

**Answer:** FastAPI is a modern, high-performance web framework for building APIs with Python 3.6+ based on standard Python type hints. It is built on top of Starlette for the web parts and Pydantic for data validation and settings management.


### 2. **How does FastAPI differ from Flask or Django?**

**Answer:** FastAPI is asynchronous by nature and supports asynchronous routes natively, which makes it more performant, especially for 
I/O-bound operations like querying databases or handling requests. It also comes with automatic request validation, serialization, and interactive API documentation (Swagger UI and ReDoc). Flask is synchronous by default and lightweight, while Django is a full-fledged web framework offering more than just API development (e.g., ORM, admin panel).


### 3. **What are the key features of FastAPI?**

**Answer:** Some key features include:

- **Asynchronous support**: Built for async and sync code with high concurrency handling.
- **Type hinting**: Leveraging Python type hints for automatic data validation and serialization.
- **Automatic docs generation**: Interactive API documentation with Swagger UI and ReDoc.
- **Fast performance**: One of the fastest Python frameworks, close to NodeJS and Go in speed.


### 4. **What is ASGI, and why is it important in FastAPI?**

**Answer:** ASGI (Asynchronous Server Gateway Interface) is the successor to WSGI, designed to handle asynchronous requests. FastAPI is an ASGI framework, meaning it can handle asynchronous web requests natively, offering better performance in applications that require handling multiple requests simultaneously.


### 5. **How does FastAPI handle request data validation?**

**Answer:** FastAPI uses **Pydantic** for data validation. By using Python type hints, FastAPI automatically validates incoming request data and provides detailed error messages if the data does not match the expected format.


### 6. **What types of interactive API documentation does FastAPI provide?**

**Answer:** FastAPI automatically generates interactive API documentation using **Swagger UI** and **ReDoc**. Swagger UI is available at `/docs`, and ReDoc is available at `/redoc` by default. These allow developers to explore and test the API directly from the browser.


### 7. **How do you create an asynchronous route in FastAPI?**

**Answer:**To create an asynchronous route, you can define the route function with the `async` keyword:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/async-route")
async def async_route():
    return {"message": "This is an asynchronous route"}
```


### 8. **What is the role of Pydantic in FastAPI?**

**Answer:** Pydantic is used for data parsing and validation in FastAPI. It allows FastAPI to use Python's type hints to validate request bodies, query parameters, and response models, ensuring the data conforms to the specified types.


### 9. **What is the significance of type hints in FastAPI?**

**Answer:** Type hints in FastAPI are significant because they:
- Enable automatic validation of request and response data.
- Allow FastAPI to generate automatic API documentation.
- Improve code readability and maintainability by clearly defining input and output types.

---

## Routes and Path Parameters


### 1. **How do you create a basic route in FastAPI?**

**Answer:** To create a basic route in FastAPI, you define a path operation using decorators such as `@app.get()`, `@app.post()`, etc. 

For example:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI"}
```

In this example, `@app.get("/")` defines a GET request for the root path (`/`). The `read_root()` function is executed when this route is called, and it returns a JSON response.

---

### 2. **What are path parameters, and how are they used in FastAPI?**

**Answer:** Path parameters are dynamic parts of a URL that allow you to capture values from the path of a request. In FastAPI, you define path parameters by including curly braces in the URL path.

For example:

```python
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}
```

Here, `item_id` is a path parameter, and the value from the URL (e.g., `/items/42`) will be passed as the argument `item_id`.



### 3. **What are query parameters in FastAPI? How do they differ from path parameters?**

**Answer:**
- **Query parameters** are parameters that are appended to the URL after the `?` symbol. They are used to filter or refine results but are not part of the URL path itself.
- **Path parameters**, on the other hand, are part of the URL structure.

For example:

```python
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}
```

Here, `item_id` is a path parameter, while `q` is a query parameter. If you visit `/items/42?q=fastapi`, `item_id` would be `42` and `q` would be `"fastapi"`.

---

### 4. **How do you validate path parameters in FastAPI?**

**Answer:**In FastAPI, you can use the `Path()` function to validate path parameters by setting constraints like minimum or maximum values. 

For example:

```python
from fastapi import Path

@app.get("/items/{item_id}")
def read_item(item_id: int = Path(..., title="The ID of the item", ge=1)):
    return {"item_id": item_id}
```

In this case, `item_id` is a required parameter (`...`) with a title `"The ID of the item"`, and it must be greater than or equal to 1 (`ge=1`). FastAPI will automatically validate the parameter and return an error if the condition is not met.

---

### 5. **How do you validate query parameters in FastAPI?**

**Answer:** You can use the `Query()` function to add validation rules for query parameters, such as minimum/maximum length, default values, etc. 

For example:

```python
from fastapi import Query

@app.get("/items/")
def read_items(q: str = Query(None, min_length=3, max_length=50)):
    return {"query": q}
```

Here, `q` is a query parameter with a minimum length of 3 characters and a maximum length of 50 characters. If the validation fails, FastAPI automatically returns a detailed error message.


### 6. **Can you combine path and query parameter validation in FastAPI?**

**Answer:**
Yes, you can combine both path and query parameter validation in a single route. For example:

```python
from fastapi import Path, Query

@app.get("/items/{item_id}")
def read_item(
    item_id: int = Path(..., ge=1),
    q: str = Query(None, min_length=3, max_length=50)
):
    return {"item_id": item_id, "query": q}
```

In this example, the path parameter `item_id` is required and must be greater than or equal to 1. The query parameter `q` must have a length between 3 and 50 characters. FastAPI validates both parameters before handling the request.


### 7. **What is the role of `Path()` and `Query()` in FastAPI?**

**Answer:**
- **`Path()`**: Used to validate path parameters and provide metadata. You can specify constraints (e.g., `ge=1`), default values, and titles.
- **`Query()`**: Used to validate query parameters. You can set default values, constraints (e.g., `min_length`, `max_length`), and metadata for query parameters.

These functions improve code readability, automatically validate input, and generate detailed API documentation.


### 8. **What happens if a path or query parameter does not meet the validation criteria in FastAPI?**

**Answer:** If a path or query parameter does not meet the validation criteria, FastAPI automatically generates and returns a **422 Unprocessable Entity** error with a detailed description of what went wrong. This helps ensure data integrity and provides useful feedback to the API client.


### 9. **How can you provide default values for path or query parameters in FastAPI?**

**Answer:** You can provide default values by simply assigning them in the function signature. For query parameters, use `Query()`, and for path parameters, use `Path()`.

For example:

```python
@app.get("/items/")
def read_items(q: str = Query("default")):
    return {"query": q}
```

In this case, if no query parameter is provided, `q` will have the default value `"default"`.

---


##  Request Body

### 1. **How do you send and receive data using the request body in FastAPI?**

**Answer:**In FastAPI, you can send and receive data using the request body by defining function parameters that represent the data to be received. FastAPI automatically parses and validates the request body (usually sent as JSON) into the corresponding Python data type.

Example:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
def create_item(item: Item):
    return {"name": item.name, "price": item.price}
```

In this example:
- The client can send a JSON object in the request body, which FastAPI will parse into an instance of the `Item` model.
- The request body contains the fields `name` and `price`, which are extracted using the `item: Item` parameter.


### 2. **What is Pydantic, and how does FastAPI use it for request body validation?**

**Answer:** Pydantic is a data validation library that FastAPI uses to automatically validate and parse request bodies. Pydantic models are used to define the structure and types of the expected data, and FastAPI ensures that the incoming request data adheres to this structure.

For example:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
def create_item(item: Item):
    return {"name": item.name, "price": item.price}
```

- **Pydantic models** (like `Item`) enforce type validation, ensuring that fields like `name` are strings and `price` is a float.
- If the request body doesn't match the model (e.g., sending a string instead of a float for `price`), FastAPI will return a **422 Unprocessable Entity** error with details about the validation failure.


### 3. **What are the benefits of using Pydantic models for request body validation in FastAPI?**

**Answer:**
- **Automatic Validation**: FastAPI automatically checks the request body against the Pydantic model, ensuring the data conforms to the expected types and constraints.
- **Clear Error Messages**: When validation fails, FastAPI returns detailed error messages indicating what went wrong, such as missing fields or incorrect types.
- **Data Parsing**: Pydantic models automatically parse the incoming data into Python types, so developers don’t need to manually convert data from strings or JSON formats.
- **Data Integrity**: Pydantic helps enforce data integrity by ensuring that only valid data enters the system.


### 4. **How can you define optional fields in a Pydantic model?**

**Answer:** In Pydantic, you can define optional fields using the `Optional` type from the `typing` module or by providing a default value of `None`. This indicates that the field is not required.

Example:

```python
from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
```

In this example:
- `description: Optional[str] = None` means the `description` field is optional and can be omitted from the request body. If omitted, it will default to `None`.


### 5. **How do you add field-level validation in a Pydantic model?**

**Answer:** You can add field-level validation in a Pydantic model by using Pydantic's built-in validation mechanisms like `constr`, `conint`, `confloat`, or by defining custom validators.

Example using constraints:

```python
from pydantic import BaseModel, constr

class Item(BaseModel):
    name: constr(min_length=3, max_length=50)
    price: float
```

In this example:
- The `name` field must be a string with a minimum length of 3 and a maximum length of 50 characters. If the validation fails, FastAPI will return a 422 error with a detailed message.

---

### 6. **How do you define custom validation logic in a Pydantic model?**

**Answer:** You can define custom validation logic in a Pydantic model by using the `@validator` decorator. This allows you to add more complex validation rules that go beyond simple type constraints.

Example:

```python
from pydantic import BaseModel, validator

class Item(BaseModel):
    name: str
    price: float

    @validator('price')
    def price_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError('Price must be greater than 0')
        return value
```

In this example:
- The custom validator `price_must_be_positive` ensures that the `price` field is a positive number. If `price` is less than or equal to zero, a `ValueError` is raised.


### 7. **How can you handle nested data structures in the request body using Pydantic models?**

**Answer:** Pydantic models can be nested inside other models to represent more complex data structures. FastAPI will automatically handle the validation of these nested models.

Example:

```python
from pydantic import BaseModel

class Address(BaseModel):
    city: str
    country: str

class User(BaseModel):
    name: str
    age: int
    address: Address  # Nested Pydantic model

@app.post("/users/")
def create_user(user: User):
    return {"name": user.name, "city": user.address.city}
```

In this example:
- The `User` model includes a nested `Address` model. FastAPI will validate both models when the request is received.
- A client can send a JSON body with nested data, such as:

```json
{
  "name": "John",
  "age": 30,
  "address": {
    "city": "New York",
    "country": "USA"
  }
}
```


### 8. **How do you handle default values in a Pydantic model?**
**Answer:**You can define default values for fields in a Pydantic model by simply assigning the default value in the model declaration.

Example:

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True  # Default value

@app.post("/items/")
def create_item(item: Item):
    return item
```

In this example:
- The `in_stock` field has a default value of `True`. If the client doesn't provide this field in the request body, it will default to `True`.

---

### 9. **What happens if the request body does not match the Pydantic model in FastAPI?**

**Answer:** If the request body does not match the Pydantic model (e.g., missing required fields, wrong data types, or failed validation), FastAPI automatically responds with a **422 Unprocessable Entity** status code. The response includes detailed error messages that explain which part of the request body failed validation.

Example of validation error:

```json
{
  "detail": [
    {
      "loc": ["body", "price"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

This error indicates that the `price` field is missing from the request body.


### 10. **How can you handle a request body with multiple Pydantic models in FastAPI?**

**Answer:** You can define multiple Pydantic models in a request body by passing more than one model as function parameters. FastAPI will parse and validate each model independently.

Example:

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float

class User(BaseModel):
    username: str
    email: str

@app.post("/orders/")
def create_order(item: Item, user: User):
    return {"item": item, "user": user}
```

In this case, the request body must include data for both the `Item` and `User` models. FastAPI will validate both models before proceeding with the request.