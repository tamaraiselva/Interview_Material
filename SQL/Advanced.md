# Advanced SQL

###  SQL-Server Stored Procedure

**1. Stored Procedures:**

A stored procedure is a set of SQL statements that you can save and reuse. It's stored in the database and can be executed multiple times with different inputs. Stored procedures are helpful for encapsulating complex logic or repetitive operations, making code more modular and easier to maintain.

```sql
CREATE PROCEDURE GetEmployeeDetails(IN emp_id INT)
BEGIN
    SELECT * 
    FROM Employees
    WHERE EmployeeID = emp_id;
END;
```

---

**2. User-Defined Functions (UDFs).**

A user-defined function (UDF) is similar to a stored procedure but is usually designed to return a single value or table and is typically used within SQL queries. Functions are especially useful for calculations or transformations that you want to apply across rows in a query.

```sql
CREATE FUNCTION CalculateDiscountedPrice(original_price DECIMAL(10, 2), discount_percentage DECIMAL(5, 2))
RETURNS DECIMAL(10, 2)
DETERMINISTIC
BEGIN
    RETURN original_price - (original_price * discount_percentage / 100);
END;
```

**SQL-Server Stored Procedure:**

**Differences between Stored Procedures and Functions.**

| Feature           | Stored Procedures                                             | User-Defined Functions                                    |
|-------------------|----------------------------------------------------------------|-----------------------------------------------------------|
| Return Type       | Do not return values directly; execute operations             | Return a single value or a table                          |
| Usage in Queries  | Cannot be used directly in SELECT queries                     | Can be called in SELECT, WHERE, etc.                      |
| Side Effects      | Can have side effects (like modifying data)                   | Should be free of side effects (read-only)                |
| Error Handling    | Can handle complex error handling and transactions            | Limited to simpler logic without transactions             |
| Calling Syntax    | Use `CALL ProcedureName()`                                    | Use `FunctionName()`                                      |

**`Create Procedure`**

To create a stored procedure, you use the `CREATE PROCEDURE` statement.

```sql
CREATE PROCEDURE procedure_name
AS
BEGIN
    -- SQL statements
END;
```

**`Execute Procedure`**

To execute a stored procedure, you use the `EXEC` or `EXECUTE` statement.

``sql
EXEC procedure_name;
``

**`Alter Procedure`**

If you need to modify an existing stored procedure, you use the `ALTER PROCEDURE` statement.

```sql
ALTER PROCEDURE procedure_name
AS
BEGIN
    -- Modified SQL statements
END;
```

**`Drop Procedure`**

To remove a stored procedure, you use the `DROP PROCEDURE` statement.

```sql
DROP PROCEDURE procedure_name;
```

**`Stored Procedure Parameter`**

You can pass parameters to a stored procedure.

```sql
CREATE PROCEDURE procedure_name
    @parameter_name datatype
AS
BEGIN
    -- SQL statements using @parameter_name
END;
```

**`Stored Procedure Variable`**

You can declare and use variables within a stored procedure.

```sql
CREATE PROCEDURE procedure_name
AS
BEGIN
    DECLARE @variable_name datatype;
    SET @variable_name = value;
    -- SQL statements using @variable_name
END;
```

**`Stored Procedure Output Parameters`**

You can use output parameters to return values from a stored procedure.

```sql
CREATE PROCEDURE procedure_name
    @input_parameter datatype,
    @output_parameter datatype OUTPUT
AS
BEGIN
    -- SQL statements
    SET @output_parameter = value;
END;
```

**`Stored Procedure Handling Exceptions`**

You can handle exceptions in a stored procedure using TRY...CATCH blocks.

```sql
CREATE PROCEDURE procedure_name
AS
BEGIN
    BEGIN TRY
        -- SQL statements that might cause an error
    END TRY
    BEGIN CATCH
        -- Error handling code
        SELECT ERROR_MESSAGE() AS ErrorMessage;
    END CATCH;
END;
```

---

### **SQL-Server Triggers**

### What is a "TRIGGER" in SQL?

A trigger is a set of SQL statements that reside in a system catalog. It is a special type of stored procedure that is invoked automatically in response to an event. It allows us to execute a batch of code when an insert, update or delete command is run against a specific table because the trigger is the set of activated actions whenever DML commands are given to the system.

```sql
CREATE TRIGGER trigger_name      
    (AFTER | BEFORE) (INSERT | UPDATE | DELETE)    
         ON table_name FOR EACH ROW      
         BEGIN      
        --variable declarations      
        --trigger code      
        END;  
```

**`Creating Triggers in SQL Server`**

To create a trigger, you use the `CREATE TRIGGER` statement. Triggers can be defined to execute in response to `INSERT`, `UPDATE`, or `DELETE` operations

```sql
CREATE TRIGGER trigger_name
ON table_name
AFTER INSERT, UPDATE, DELETE
AS
BEGIN
    -- SQL statements
END;
```

**`SQL Server INSTEAD OF Trigger`**

An `INSTEAD OF` trigger is used to override the standard action of the `INSERT`, `UPDATE`, or `DELETE` operation.

```sql
CREATE TRIGGER trigger_name
ON table_name
INSTEAD OF INSERT
AS
BEGIN
    -- SQL statements to execute instead of the standard INSERT operation
END;
```

**`SQL Server DDL Trigger`**

A Data Definition Language (DDL) trigger is used to execute in response to DDL events such as `CREATE`, `ALTER`, or `DROP` statements.

```sql
CREATE TRIGGER trigger_name
ON DATABASE
FOR CREATE_TABLE, ALTER_TABLE, DROP_TABLE
AS
BEGIN
    -- SQL statements
END;
```

**`SQL Server DISABLE TRIGGER`**

To disable a trigger, you use the DISABLE TRIGGER statement.

```sql
DISABLE TRIGGER trigger_name ON table_name;
```

**`SQL Server ENABLE TRIGGER`**

To enable a trigger, you use the ENABLE TRIGGER statement.

```sql
ENABLE TRIGGER trigger_name ON table_name;
```

**`SQL Server MODIFY TRIGGER`**

To modify an existing trigger, you need to drop the existing trigger and create a new one with the desired changes.

```sql
DROP TRIGGER trigger_name;
CREATE TRIGGER trigger_name
ON table_name
AFTER INSERT, UPDATE
AS
BEGIN
    -- Modified SQL statements
END;
```

**`SQL Server DROP TRIGGER`**

To remove a trigger, you use the DROP TRIGGER statement.

```sql
DROP TRIGGER trigger_name;
```

---

### Data Types

**Exact Numeric:**

**1. What is the difference between exact numeric data types and approximate numeric data types in databases?**

Exact numeric data types, such as INTEGER, BIGINT, DECIMAL, and NUMERIC, are used when precise values are needed without any rounding errors. These types are commonly used for scenarios involving money, counts, and other data where exact representation is critical. In contrast, approximate numeric data types, like FLOAT and DOUBLE, store values as approximations. They are used when performance and range are more important than precision, as they can introduce small rounding errors due to their storage method. This makes them suitable for scientific calculations but not for financial data.

**2. Write a SQL query to create a table named `Transactions` with the following columns:**

- `TransactionID` as an integer primary key.
- `Amount` as a `DECIMAL` with up to 10 digits and 2 digits after the decimal.
- `TransactionDate` as a `DATE` type.

```sql
CREATE TABLE Transactions (
    TransactionID INT PRIMARY KEY,
    Amount DECIMAL(10, 2),
    TransactionDate DATE
);
```

**3. Write a Python function that accepts a list of prices and returns the total sum as a `decimal.Decimal` to ensure precision.**

```py
from decimal import Decimal

def calculate_total(prices):
    total = Decimal('0.00')
    for price in prices:
        total += Decimal(price)
    return total

# Example usage:
prices = ['19.99', '49.95', '25.50']
total_sum = calculate_total(prices)
print("Total sum:", total_sum)
```

---

**Approximate Numeric:**

**4. Why would you use approximate numeric data types such as FLOAT or DOUBLE PRECISION instead of exact numeric types like DECIMAL?**

Approximate numeric data types, such as FLOAT and DOUBLE PRECISION, are used when dealing with scientific and engineering data where handling a wide range of values is more important than perfect precision. These types are capable of representing very large or very small numbers but may introduce small rounding errors due to their binary storage format. They are ideal for applications involving complex calculations, such as simulations and statistical analysis, where minor imprecision is acceptable. Exact numeric types like DECIMAL are used when precision is crucial, such as in financial calculations.

**5. Write a SQL query to create a table named `ScientificData` with the following columns:**

- `DataID` as an integer primary key.
- `Measurement` as a `DOUBLE PRECISION` type.
- `RecordedAt` as a `TIMESTAMP`.

```sql
CREATE TABLE ScientificData (
    DataID INT PRIMARY KEY,
    Measurement DOUBLE PRECISION,
    RecordedAt TIMESTAMP
);
```

**6. Write a Python function that accepts a list of floating-point numbers and returns their average. Consider that the input list may have very large or very small numbers.**

```py
def calculate_average(numbers):
    if not numbers:
        return 0.0  # Return 0.0 if the list is empty to avoid division by zero.
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage:
numbers = [1.23e3, 4.56e-2, 7.89e5, 1.23e-4]
average = calculate_average(numbers)
print("Average:", average)
```

---

**Date & Time:**

**7. What is the difference between TIMESTAMP and DATE data types in a database?**

The DATE data type is used to store only calendar dates without any time information, in the format YYYY-MM-DD. It's suitable for applications where time details are not required, such as birth dates or deadlines. The TIMESTAMP data type, on the other hand, stores both date and time information in the format YYYY-MM-DD HH:MM:SS, and often supports time zone information in certain database systems (e.g., TIMESTAMPTZ in PostgreSQL). It is used when it’s necessary to record when an event occurs, like logging user activity or tracking changes.

**8. Write a SQL query to create a table named Appointments with the following columns:**

`AppointmentID` as an integer primary key.
`AppointmentDate` as a `DATE` type.
`StartTime` as a `TIME` type.
`EndTime` as a `TIME` type.
`CreatedAt` as a `TIMESTAMP` type with the current timestamp as the default value.

```sql
CREATE TABLE Appointments (
    AppointmentID INT PRIMARY KEY,
    AppointmentDate DATE,
    StartTime TIME,
    EndTime TIME,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**9. Write a Python function that calculates the difference in days between two date objects and returns the result.**

```py
from datetime import date

def days_between_dates(date1, date2):
    difference = date2 - date1
    return difference.days

# Example usage:
date1 = date(2024, 11, 1)
date2 = date(2024, 11, 7)
days_diff = days_between_dates(date1, date2)
print("Difference in days:", days_diff)
```

---

**Character Strings:**

**10. What is the difference between `CHAR` and `VARCHAR` data types? When would you use one over the other?**

The `CHAR` (fixed-length character) data type stores strings of a fixed length. If the string is shorter than the specified length, it will be padded with spaces to meet the required length. For example, `CHAR(10)` will always store 10 characters, padding with spaces if the string is shorter.

The `VARCHAR` (variable-length character) data type, on the other hand, stores strings of variable length. It only uses as much space as necessary to store the actual string, up to the specified limit. For example, `VARCHAR(100)` can store a string of any length from 0 to 100 characters.

**11. Write a SQL query to create a table called `Books` with the following columns:**

`BookID` as an integer primary key.
`Title` as a `VARCHAR` data type with a maximum length of 255 characters.
`Author` as a `VARCHAR` data type with a maximum length of 100 characters.
`PublicationYear` as an `INT`.
`Description` as a `TEXT` data type.

```sql
CREATE TABLE Books (
    BookID INT PRIMARY KEY,
    Title VARCHAR(255),
    Author VARCHAR(100),
    PublicationYear INT,
    Description TEXT
);
```

**12. Write a Python function that accepts a list of book titles (strings) and returns the longest title in the list. If there is a tie, return all the titles with the longest length.**

```py
def longest_book_titles(titles):
    # Find the maximum length of the titles
    max_length = max(len(title) for title in titles)
    
    # Find all titles that match the maximum length
    longest_titles = [title for title in titles if len(title) == max_length]
    
    return longest_titles

# Example usage:
book_titles = ["The Great Gatsby", "Moby Dick", "War and Peace", "The Odyssey", "The Brothers Karamazov"]
longest_titles = longest_book_titles(book_titles)
print("Longest book titles:", longest_titles)
```

---

**Unicode Character Strings:**

**13. What is the difference between CHAR, VARCHAR, and NCHAR, NVARCHAR data types? When would you use NCHAR and NVARCHAR over CHAR and VARCHAR?**

`CHAR:` It is a fixed-length string data type that stores characters. If the string is shorter than the specified length, it will be padded with spaces to meet the fixed length. Use `CHAR` when you know the exact length of the string (e.g., country codes).

`VARCHAR:` It is a variable-length string data type that stores characters, but only uses as much space as necessary. Use `VARCHAR` when the string length can vary (e.g., names, descriptions).

`NCHAR`: Similar to `CHAR`, but it stores Unicode characters. It uses 2 bytes per character, making it suitable for international text and multi-language applications. Use `NCHAR` when you need to store fixed-length Unicode data, such as symbols, or characters from languages like Chinese or Arabic.

`NVARCHAR`: Similar to `VARCHAR`, but it stores Unicode characters. It is more flexible, allowing you to store variable-length Unicode strings, and it uses 2 bytes per character. Use `NVARCHAR` when you need variable-length Unicode text (e.g., user names in multiple languages).

**14. Write a SQL query to create a table named `Employees` with the following columns:**

- `EmployeeID` as an integer primary key.
- `EmployeeName` as an `NVARCHAR` type with a maximum length of 100 characters.
- `JobTitle` as an `NVARCHAR` type with a maximum length of 50 characters.
- `Bio` as an `NTEXT` type for storing a long textual description.
- `DateOfJoining` as a `DATE` type.

```sql
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    EmployeeName NVARCHAR(100),
    JobTitle NVARCHAR(50),
    Bio NTEXT,
    DateOfJoining DATE
);
```

**15. Write a Python function that accepts a list of employee names (strings) and returns the name with the maximum length. If there is a tie, return all the names with the longest length. Ensure that the function can handle names containing Unicode characters.**

```py
def longest_employee_names(names):
    # Find the maximum length of the names
    max_length = max(len(name) for name in names)
    
    # Find all names that match the maximum length
    longest_names = [name for name in names if len(name) == max_length]
    
    return longest_names

# Example usage:
employee_names = ["张伟", "Mário Silva", "José González", "Alice"]
longest_names = longest_employee_names(employee_names)
print("Longest employee names:", longest_names)
```

---

**Binary Strings:**

**16. What is the difference between BINARY, VARBINARY, and BLOB data types? When would you use each?**

- **`BINARY:`** This is a fixed-length binary data type. It stores binary data with a fixed number of bytes. If the data is shorter than the specified length, it will be padded with zero bytes to meet the fixed length.

  - **`Use Case:`** `BINARY` is used when you know the exact size of the binary data, such as storing encryption keys, checksums, or fixed-length binary identifiers.

- **`VARBINARY:`** This is a variable-length binary data type. It stores binary data with a variable length, consuming only the necessary space to store the actual data, up to the maximum defined length.

  - **`Use Case:`** `VARBINARY` is used when the length of the binary data varies. For example, storing files or binary blobs of varying sizes (e.g., images or documents) in a database.

- **`BLOB (Binary Large Object):`** This data type is used for storing large amounts of binary data. It can store large files like images, audio files, or video files.

  - **`Use Case:`** `BLOB` is ideal for storing large binary objects where the size of the data can vary significantly, such as multimedia files.

**17. Write a SQL query to create a table named `Files` with the following columns:**

- `FileID` as an integer primary key.
- `FileName` as a `VARCHAR` type with a maximum length of 255 characters.
- `FileType` as a `VARCHAR` type with a maximum length of 50 characters (for example, "image/jpeg", "application/pdf").
- `FileData` as a `VARBINARY` type to store the binary data of the file (e.g., an image or PDF).
- `UploadDate` as a `DATETIME` type to store the date and time when the file was uploaded.

```sql
CREATE TABLE Files (
    FileID INT PRIMARY KEY,
    FileName VARCHAR(255),
    FileType VARCHAR(50),
    FileData VARBINARY(MAX),
    UploadDate DATETIME
);
```

**18. Write a Python function that accepts a list of binary data (represented as byte arrays) and returns the largest binary data in the list. If there is a tie, return all the binary data with the largest length.**

```py
def largest_binary_data(binary_data_list):
    # Find the maximum length of binary data in the list
    max_length = max(len(binary_data) for binary_data in binary_data_list)
    
    # Find all binary data that match the maximum length
    largest_data = [binary_data for binary_data in binary_data_list if len(binary_data) == max_length]
    
    return largest_data

# Example usage:
binary_data_1 = b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a'  # First few bytes of a PNG file
binary_data_2 = b'\x25\x50\x44\x46\x2d\x31\x2e\x35'  # First few bytes of a PDF file
binary_data_3 = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08'  # 9 bytes of binary data

binary_data_list = [binary_data_1, binary_data_2, binary_data_3]

largest_data = largest_binary_data(binary_data_list)
print("Largest binary data:", largest_data)
```

---

**Other DataTypes:**

### JSON and XML Data Types

**JSON (JavaScript Object Notation):**

JSON data type is commonly used to store structured and semi-structured data in a way that resembles JavaScript objects. JSON is lightweight and flexible, making it an ideal choice for handling complex and nested data within relational databases.

**Creating a JSON Column:**

```sql
CREATE TABLE Orders (
    OrderID INT,
    OrderDetails JSON
);
```

**Inserting JSON Data:**

```sql
INSERT INTO Orders (OrderID, OrderDetails) 
VALUES (1, '{"product": "Laptop", "quantity": 2, "price": 1200}');
```

**Extracting JSON Data:**

- **In MySQL, use `JSON_EXTRACT()`:**

```sql
SELECT JSON_EXTRACT(OrderDetails, '$.product') AS ProductName
FROM Orders;
```

- **In PostgreSQL, use the `->` operator:**

```sql
SELECT OrderDetails->>'product' AS ProductName
FROM Orders;
```

**Updating JSON Fields:**

```sql
UPDATE Orders
SET OrderDetails = JSON_SET(OrderDetails, '$.price', 1100)
WHERE OrderID = 1;
```

---

### XML (Extensible Markup Language)

XML data type is used to store XML data, which is a markup language designed to encode documents in a format that is both human- and machine-readable. While less popular than JSON, XML is widely used in certain industries and supports data hierarchies similar to JSON.

- **Creating an XML Column:**

```sql
CREATE TABLE Products (
    ProductID INT,
    ProductDetails XML
);
```

- **Inserting XML Data:**

```sql
INSERT INTO Products (ProductID, ProductDetails)
VALUES (1, '<product><name>Laptop</name><quantity>2</quantity><price>1200</price></product>');
```

- **Querying XML Data (Example in SQL Server):**

```sql
SELECT ProductDetails.value('(/product/name)[1]', 'VARCHAR(50)') AS ProductName
FROM Products;
```

**What are some other commonly used data types in databases, and when would you use them?**

**`ENUM:`** Use this when a column should only accept one of a predefined set of values, like "Active", "Inactive", or "Pending" for status columns.

**`JSON / JSONB:`** Use for storing semi-structured or hierarchical data like user preferences or configurations, allowing for flexible schemas.

**`XML:`** Ideal for storing structured data in XML format, useful in web services or configurations.

**`UUID:`** When you need globally unique identifiers, especially in distributed systems where data is generated across multiple nodes.

**`ARRAY:`** Use when you want to store multiple values of the same type in a single column, such as tags or multiple phone numbers.

**`Geometric Data Types (POINT, POLYGON, etc.):`** Use these for spatial data applications, such as geographic coordinates or area boundaries in GIS systems.

**`INTERVAL:`** Perfect for storing durations or differences between time values.

**`BIT:`** Efficient for storing binary flags, like yes/no or true/false values.

---

### Arrays and Composite Types

An array data type allows storing multiple values of the same data type in a single field, which is particularly useful for handling data lists (e.g., tags, categories) within a table.

- **Creating an Array Column:**

```sql
CREATE TABLE Students (
    StudentID INT,
    Subjects TEXT[]
);
```

- **Inserting Data into an Array Column:**

```sql
INSERT INTO Students (StudentID, Subjects)
VALUES (1, ARRAY['Math', 'Science', 'History']);
```

- **Querying Data from an Array:**

```sql
SELECT StudentID, Subjects[1] AS FirstSubject
FROM Students;
```

- **Filtering by Array Contents:**

```sql
SELECT * 
FROM Students 
WHERE 'Math' = ANY(Subjects);
```

---

### Composite Types

Composite types allow grouping multiple fields into a single column, essentially creating a mini-record type. This can be useful for modeling entities with multiple attributes as a single unit within a table.

1. **Defining a Composite Type:**

```sql
CREATE TYPE Address AS (
    Street VARCHAR(50),
    City VARCHAR(50),
    ZipCode INT
);
```

2. **Using Composite Types in a Table:**

```sql
CREATE TABLE Customers (
    CustomerID INT,
    Name VARCHAR(50),
    Address Address
);
```

3. **Inserting Data into a Composite Column:**

```sql
INSERT INTO Customers (CustomerID, Name, Address)
VALUES (1, 'John Doe', ('123 Main St', 'Springfield', 12345));
```

4. **Querying Composite Data:**

```sql
SELECT Name, Address.City AS City
FROM Customers;
```

| Data Type | Description                      | Use Cases                                                                                 |
|-----------|----------------------------------|-------------------------------------------------------------------------------------------|
| JSON      | Stores structured JSON data      | Flexible schema, hierarchical data, web applications                                      |
| XML       | Stores structured XML data       | Interoperability with XML-based systems, data validation                                  |
| Array     | Stores multiple values of the same type in one column | Lists of values (tags, skills, categories)                               |
| Composite | Groups multiple fields as a single column value | Address or contact details, complex attributes                             |

---

### Dynamic SQL

Dynamic SQL allows SQL statements to be constructed and executed at runtime rather than being predefined in static queries. This approach is particularly useful when query structure needs to change based on conditions, such as when filtering criteria are determined by user input or when table names or columns vary dynamically.

---

### Building Dynamic SQL Queries

Dynamic SQL queries are usually constructed as strings, then executed using commands that interpret and run them as SQL code.

```sql
DECLARE @tableName NVARCHAR(50) = 'Employees';
DECLARE @columnName NVARCHAR(50) = 'Department';
DECLARE @value NVARCHAR(50) = 'Sales';

DECLARE @sql NVARCHAR(MAX);
SET @sql = 'SELECT * FROM ' + @tableName + ' WHERE ' + @columnName + ' = ''' + @value + '''';

EXEC(@sql);
```

---

### Using EXEC and sp_executesql

1. **EXEC Command**

The `EXEC` command is the simpler of the two and directly executes a string of SQL. It’s commonly used for straightforward dynamic SQL queries but lacks certain features, like parameterization.

```sql
DECLARE @sql NVARCHAR(MAX) = 'SELECT * FROM Employees WHERE Department = ''Sales''';
EXEC(@sql);
```

2. **sp_executesql**

`sp_executesql` is a stored procedure that executes a dynamically built SQL string and allows for parameterization, which improves security and performance. This is generally the preferred method for executing dynamic SQL in SQL Server.

```sql
DECLARE @sql NVARCHAR(MAX);
DECLARE @department NVARCHAR(50) = 'Sales';

SET @sql = N'SELECT * FROM Employees WHERE Department = @Dept';

EXEC sp_executesql @sql, N'@Dept NVARCHAR(50)', @Dept = @department;
```

---

### When to Use Dynamic SQL

- The table name, column names, or conditions need to change based on input.

- Multiple queries must be dynamically assembled depending on user requirements.

- There’s a need to execute different SQL operations conditionally (e.g., `INSERT`, `UPDATE`, `DELETE` based on input).

| Method         | Use Case                 | Advantages                                    | Disadvantages                              |
|----------------|---------------------------|-----------------------------------------------|--------------------------------------------|
| EXEC           | Basic dynamic SQL execution | Simple and direct execution                   | No parameterization, vulnerable to SQL injection |
| sp_executesql  | Parameterized dynamic SQL  | Safer, supports parameters, reuses execution plans | Slightly more complex to use             |

---

### Database Design and Normalization

Database normalization is a process used to design a database structure that reduces redundancy and dependency. The goal of normalization is to organize data efficiently, ensuring consistency and reducing the risk of anomalies (errors or inconsistencies) during database operations like inserts, updates, and deletions.

---

### Principles of Database Normalization

1. `Eliminate Redundant Data:` Minimize duplicate data across the database to save space and improve data integrity.

2. `Organize Data into Logical Groups:` Ensure that related data is stored together logically, which enhances data accessibility and clarity.

3. `Reduce Data Anomalies:` Anomalies are inconsistencies that can occur when inserting, updating, or deleting data. Normalization reduces these by establishing rules about data organization.

4. `Simplify Queries and Maintenance:` Organized, well-structured tables are easier to query, update, and maintain.

---

### 1. First Normal Form (1NF)

- All columns contain atomic (indivisible) values.

- Each column contains only one type of data.

- Each row contains unique data (each row can be uniquely identified by a primary key).

1NF ensures that each cell in the table holds only one value, making data retrieval straightforward and eliminating repeating groups within rows.

`Example:` A table that violates 1NF might look like this:

| StudentID | Name  | Subject  |
|-----------|-------|----------|
| 1         | Alice | Math, Science|
| 2         | Bob   | English, History |

To satisfy 1NF, we separate the subjects into individual rows:

| StudentID | Name  | Subject  |
|-----------|-------|----------|
| 1         | Alice | Math     |
| 1         | Alice | Science  |
| 2         | Bob   | English  |
| 2         | Bob   | History  |

---

### 2. Second Normal Form (2NF)

- It is in 1NF.

- All non-key columns are fully functionally dependent on the entire primary key, meaning no partial dependencies exist (a partial dependency occurs when a non-key attribute depends only on a part of a composite primary key).

2NF is especially relevant for tables with composite primary keys. It helps prevent duplicate data by ensuring that each attribute in the table depends on the whole primary key, not just a part of it.

`Example:` Consider an Enrollments table that violates 2NF:

| StudentID | CourseID | StudentName | CourseName |
|-----------|----------|-------------|------------|
| 1         | 101      | Alice       | Math       |
| 2         | 102      | Bob         | Science    |

Here, `StudentName` depends only on `StudentID`, and `CourseName` depends only on `CourseID`. To bring this table to 2NF, we separate it into two tables:

1. **Students table:**

| StudentID | StudentName |
|-----------|-------------|
| 1         | Alice       |
| 2         | Bob         |

2. **Courses table:**

| CourseID | CourseName |
|----------|------------|
| 101      | Math       |
| 102      | Science    |

3. Enrollments table (new):

| StudentID | CourseID |
|-----------|----------|
| 1         | 101      |
| 2         | 102      |

---

### 3. Third Normal Form (3NF)

- It is in 2NF.

- It has no transitive dependencies, meaning non-key columns should not depend on other non-key columns.

3NF further reduces redundancy by ensuring that non-key attributes only depend on the primary key, not on other non-key attributes. This avoids situations where data changes in one place need to be reflected in multiple places.

`Example:` Consider a table that violates 3NF:

| StudentID | StudentName | CourseID | InstructorName |
|-----------|-------------|----------|----------------|
| 1         | Alice       | 101      | Dr. Smith      |
| 2         | Bob         | 102      | Dr. Brown      |

In this case, `InstructorName` depends on `CourseID`, not directly on `StudentID`. To bring this to 3NF, we split the table into two tables:

1. **Students table:**

| StudentID | StudentName |
|-----------|-------------|
| 1         | Alice       |
| 2         | Bob         |

2. **Courses table (including Instructor):**

| CourseID | InstructorName |
|----------|----------------|
| 101      | Dr. Smith      |
| 102      | Dr. Brown      |

---

### 4. Boyce-Codd Normal Form (BCNF)

- It is in 3NF.

- Every determinant (an attribute on which other attributes depend) is a candidate key.

BCNF is used to handle anomalies that can arise even in 3NF, typically in complex scenarios where a table has multiple candidate keys. It ensures that every determinant is a candidate key, reducing the likelihood of redundancy further.

---

### Higher Normal Forms (4NF, 5NF)

- `4NF:` Removes multi-valued dependencies to prevent one-to-many and many-to-many relationships within a single table.

- `5NF:` Ensures tables are decomposed in a way that every join dependency is preserved.

| Normal Form | Requirement                                            | Purpose                                               |
|-------------|--------------------------------------------------------|-------------------------------------------------------|
| 1NF         | Eliminate repeating groups; use atomic values          | Simplifies querying and reduces redundancy            |
| 2NF         | Satisfy 1NF; remove partial dependencies               | Ensures data relates to the whole primary key         |
| 3NF         | Satisfy 2NF; remove transitive dependencies            | Reduces dependency on non-key columns                |
| BCNF        | Satisfy 3NF; all determinants are candidate keys       | Addresses anomalies not covered in 3NF               |
| 4NF         | Eliminate multi-valued dependencies                    | Further removes redundancy                            |
| 5NF         | Ensure decomposition where all join dependencies are preserved | Achieves ultimate data structure efficiency           |

### Advanced Query Optimization

Query optimization plays a crucial role in ensuring that SQL queries are executed as efficiently as possible. Well-optimized queries reduce the load on the database, minimize response times, and improve overall system performance. Indexing is a key aspect of query optimization, and several techniques can be employed to analyze and improve query performance.

1. **Effective Indexing Strategies**

Indexing helps speed up the retrieval of data by creating an efficient lookup structure for the database.

**a. Choose the Right Columns for Indexing:**

1. **`Primary Key Indexes:`** Every table automatically gets an index on its primary key. This index ensures that data retrieval based on the primary key is fast.

2. **`Foreign Key Indexes:`** Adding an index on foreign keys improves the performance of join operations. Foreign key columns are frequently used in `JOIN` queries, so indexing them can reduce lookup times.

3. **`Columns in WHERE Clause:`** Columns that are frequently used in the `WHERE` clause (especially for filtering data) should be indexed. These indexes can significantly speed up query execution by minimizing the number of rows the database needs to scan.

4. **`Columns Used in ORDER BY:`** Indexing columns used in the `ORDER BY` clause can enhance sorting performance, especially for large datasets.

5. **`Composite Indexes:`** When multiple columns are often used together in queries (e.g., in `WHERE` or `JOIN` clauses), creating a composite index on those columns can speed up query performance. For example:

```sql
Copy code
CREATE INDEX idx_composite_name_age ON Employees (LastName, Age);
```

6. **`Full-Text Indexes:`** For text-heavy searches, especially when you need to search for specific words or phrases in a large text field, full-text indexes can improve search performance. In MySQL, you can use `FULLTEXT` indexes, and in SQL Server, you can use `CONTAINS` or `FREETEXT`.

---

**b. Avoid Over-Indexing:**

While indexes improve query performance, too many indexes can negatively impact insert, update, and delete operations because the indexes must be updated whenever the data in the table changes. Always index the most frequently queried columns and avoid indexing columns that don't contribute to query performance.

**c. Index Maintenance:**

Indexes can become fragmented over time, especially with frequent updates. It is essential to rebuild or reorganize indexes periodically to maintain performance.

```sql
-- Rebuilding an index:
ALTER INDEX ALL ON Employees REBUILD;
```

In MySQL, you can use:

```sql
OPTIMIZE TABLE Employees;
```

---

2. **Query Optimization Techniques**

Several techniques can be applied to optimize the performance of SQL queries.

**a. Use Proper Join Types:**

- **`INNER JOIN:`** Use INNER JOIN when you need to retrieve only the matching rows from both tables.

- **`LEFT JOIN/RIGHT JOIN:`** Use LEFT JOIN (or RIGHT JOIN) when you need to return all rows from the left (or right) table, even if there is no match in the other table. However, avoid unnecessary JOINs that increase data volume.

```sql
SELECT * FROM Orders O LEFT JOIN Customers C ON O.CustomerID = C.CustomerID WHERE C.CustomerID IS NOT NULL;
```

```sql
SELECT * FROM Orders O INNER JOIN Customers C ON O.CustomerID = C.CustomerID;
```

**b. Select Only Required Columns:**

Instead of using `SELECT *`, which fetches all columns, specify only the columns you need. This reduces the amount of data returned, improving query performance.

```sql
-- Inefficient:
SELECT * FROM Employees;

-- Efficient:
SELECT EmployeeID, FirstName, LastName FROM Employees;
```

**c. Avoid Subqueries in SELECT and WHERE Clauses:**

Subqueries can sometimes result in performance issues, particularly when used in the `SELECT` or `WHERE` clauses. Where possible, try to rewrite the query using `JOINs` instead.

- **Subquery Example:**

```sql
SELECT EmployeeID, FirstName FROM Employees WHERE EmployeeID IN (SELECT EmployeeID FROM Orders WHERE OrderAmount > 1000);
```

- **Optimized using JOIN:**

```sql
SELECT E.EmployeeID, E.FirstName 
FROM Employees E
JOIN Orders O ON E.EmployeeID = O.EmployeeID
WHERE O.OrderAmount > 1000;
```

**d. Use Efficient WHERE Conditions:**

**Avoid Functions on Indexed Columns:** When you use a function on an indexed column in a WHERE clause, it can prevent the database from using the index efficiently.

```sql
SELECT * FROM Employees WHERE YEAR(HireDate) = 2020;
```

`Instead, try:`

```sql
SELECT * FROM Employees WHERE HireDate >= '2020-01-01' AND HireDate < '2021-01-01';
```

- Use `BETWEEN` for Range Queries: Use `BETWEEN` for inclusive range searches, as it's optimized for queries with ranges.

```sql
SELECT * FROM Orders WHERE OrderDate BETWEEN '2023-01-01' AND '2023-12-31';
```

**e. Avoid Using `DISTINCT` and `GROUP BY` Unnecessarily**

- Use `DISTINCT` only when necessary. It removes duplicates and can be resource-intensive.

- `GROUP BY` should be used carefully, especially on large datasets, as it requires sorting and aggregation.

---

3. **How to Analyze and Fix Performance Issues**
Analyzing and fixing performance issues involves understanding where and why a query is performing poorly.

**a. Analyze Execution Plans:**

An execution plan provides insight into how SQL Server (or another DBMS) executes a query. It helps identify inefficiencies such as missing indexes, table scans, or expensive operations.

- **SQL Server:** You can view the execution plan using SQL Server Management Studio (SSMS) or by running:

```sql
SET SHOWPLAN_ALL ON;
SELECT * FROM Employees WHERE Department = 'Sales';
SET SHOWPLAN_ALL OFF;
```

- **MySQL:** Use `EXPLAIN` to view the query execution plan:

```sql
EXPLAIN SELECT * FROM Employees WHERE Department = 'Sales';
```

**b. Optimize Queries Based on Execution Plans:**

- **Missing Indexes:** If the plan shows full table scans, consider adding indexes on the columns used in `WHERE`, `JOIN`, or `ORDER BY` clauses.

- **Inefficient Joins:** Check the join order, and ensure that smaller tables are joined first or use appropriate join types.

- **Sort Operations:** If the query has large sorts, consider indexing the columns involved in sorting.

**c. Use Query Caching:**

Many databases, including MySQL and SQL Server, offer query caching mechanisms. By caching the result of a query, subsequent executions of the same query can return data more quickly. Make sure your database is configured to take advantage of this feature, especially for frequently executed queries that don’t change often.

**d. Review Server Configuration:**

- **Memory Allocation:** Ensure the database server has adequate memory for efficient query processing and caching.

- **Disk I/O:** If queries are slow due to disk access, optimize disk storage (e.g., use SSDs, optimize database layout).

- **Parallel Query Execution:** Some DBMSs support parallel query execution, which divides the work of executing a query across multiple processors.

**e. Regularly Monitor and Tune Queries:**

Use monitoring tools to regularly check query performance over time. In SQL Server, you can use SQL Server Profiler or Extended Events to trace and analyze slow queries.

---

### Working with Large Data Sets

**1. Partitioning Tables.**

Table partitioning is the process of splitting a large table into smaller, more manageable pieces, known as partitions. Each partition is stored separately but treated as part of the whole table by the database engine. Partitioning can improve query performance, especially for queries that focus on specific subsets of the data.

- **a. Types of Partitioning**

**`Range Partitioning:`** Data is divided into partitions based on a range of values from a specific column (typically a date or numeric column).

```sql
CREATE TABLE Sales (
    SaleID INT,
    SaleDate DATE,
    Amount DECIMAL
) PARTITION BY RANGE (YEAR(SaleDate)) (
    PARTITION p2019 VALUES LESS THAN (2020),
    PARTITION p2020 VALUES LESS THAN (2021),
    PARTITION p2021 VALUES LESS THAN (2022)
);
```

**`List Partitioning:`** Data is divided based on a list of predefined values, such as specific categories or regions.

```sql
CREATE TABLE Sales (
    SaleID INT,
    Region VARCHAR(50),
    Amount DECIMAL
) PARTITION BY LIST (Region) (
    PARTITION pNorth VALUES IN ('North'),
    PARTITION pSouth VALUES IN ('South'),
    PARTITION pWest VALUES IN ('West')
);
```

**`Hash Partitioning:`** Data is distributed evenly across partitions based on a hash function, ensuring that data is distributed without regard to any specific order or range.

```sql
CREATE TABLE Customers (
    CustomerID INT,
    CustomerName VARCHAR(100)
) PARTITION BY HASH (CustomerID) PARTITIONS 4;
```

**`Composite Partitioning:`** A combination of two partitioning strategies (e.g., range and hash).

```sql
CREATE TABLE Sales (
    SaleID INT,
    SaleDate DATE,
    Region VARCHAR(50),
    Amount DECIMAL
) PARTITION BY RANGE (YEAR(SaleDate)) 
    SUBPARTITION BY HASH (Region) 
    PARTITIONS 4 (
        PARTITION p2019 VALUES LESS THAN (2020),
        PARTITION p2020 VALUES LESS THAN (2021)
    );
```

- **b. Benefits of Partitioning**

**`Improved Query Performance:`** Queries that target specific partitions (e.g., a specific date range or region) can run faster since only relevant partitions are scanned.

**`Faster Data Management:`** Partitioned tables allow for easier archiving, data purging, or backup of older data.

**`Improved Indexing:`** Each partition can have its own index, improving the efficiency of searches within each partition.

- **c. Considerations for Partitioning**

**`Maintenance Overhead:`** Partitioning introduces additional complexity in managing the database, especially when dealing with partition pruning (i.e., ensuring queries only access relevant partitions).

**`Balanced Partitions:`** Ensure that partitions are of roughly equal size to avoid hotspots in one partition.

**`Partitioning Key:`** Choose a partitioning key that aligns with your query patterns. For example, range partitioning works well for time-based data.

---

**2. Best Practices for Managing Large Databases.**

Efficiently managing large databases requires a holistic approach, addressing both data storage and query performance.

**a. Indexing Best Practices:**

**`Selective Indexing:`** Index columns that are frequently used in `JOIN` or `WHERE` clauses. Avoid indexing every column, as this can lead to performance degradation during `INSERT`, `UPDATE`, and `DELETE` operations.

**`Composite Indexes:`**When queries frequently use multiple columns for filtering or sorting, create composite indexes. This can help reduce the number of required indexes and improve query performance.

**`Covering Indexes:`** Create indexes that include all the columns needed by a query. This allows the database to retrieve data directly from the index, rather than accessing the table, which improves performance.

**`Index Maintenance:`** Regularly rebuild or reorganize indexes to avoid fragmentation. Use tools like `DBCC DBREINDEX` in SQL Server or `OPTIMIZE TABLE` in MySQL to optimize index performance.

**b. Archiving Old Data:**

**`Archiving:`** For historical data that’s not frequently accessed, consider archiving it to separate tables or even external storage. This can help keep the active data set smaller and improve the overall performance of the system.

**`Partitioning and Archiving:`** You can use partitioning to isolate older data and easily move it to a separate storage system (e.g., cold storage) when it is no longer needed for day-to-day queries.

**c. Data Purging and Cleaning:**

**`Regular Cleanup:`** Implement policies for purging outdated or irrelevant data regularly. This reduces the size of the database, improving performance and reducing backup times.

**`Automated Purging:`** Create automated jobs or scripts that run periodically to delete data that is no longer needed (e.g., logs, temporary data).

**d. Backup and Recovery Strategies:**

**`Incremental Backups:`** Instead of backing up the entire database every time, use incremental backups to capture only changes since the last backup. This reduces backup size and time.

**`Replication and Clustering:`** For high availability and disaster recovery, consider setting up database replication or clustering. This ensures that a standby server can take over in case of failure and helps balance the load for read-heavy applications.

**`Partitioned Backups:`** Backing up partitioned tables can be more efficient, as individual partitions can be backed up and restored independently.

**e. Query Optimization for Large Datasets:**

**`Avoid Full Table Scans:`** Ensure that queries use indexes effectively to avoid full table scans, which are very costly in large datasets.

**`Query Caching:`** Enable query caching to improve performance for frequently executed queries.

**`Avoid Complex Joins:`** Complex joins involving multiple large tables can severely degrade performance. Try to break down complex queries into smaller parts or use intermediate tables where appropriate.

**`Limit Data with LIMIT and OFFSET:`** When retrieving large sets of data for reports or processing, use pagination (LIMIT and OFFSET) to fetch a smaller subset of data at a time.

**f. Data Compression:**

**`Compression:`** Use data compression techniques where possible to reduce the physical storage requirements. Many database management systems (DBMS) like MySQL, SQL Server, and PostgreSQL offer built-in support for table and index compression.

**`Columnar Compression:`** In OLAP systems, use columnar compression to optimize the storage of large datasets, particularly for analytical workloads.

**g. Monitoring and Performance Tuning:**

**`Regular Monitoring:`** Continuously monitor system performance using tools like database logs, query performance monitoring, and system metrics (CPU, disk I/O, memory).

**`Automated Performance Tuning:`** Many modern databases, such as SQL Server and Oracle, offer automatic tuning features that analyze and adjust indexes, queries, and resources.

**`Query Profiling:`** Use query profiling tools to identify slow-running queries and optimize them by changing the query structure or adjusting indexes.

**h. Partition Pruning:**

Partition pruning is a technique where the database engine only scans relevant partitions for a query, avoiding unnecessary scans of data in partitions that do not meet the query criteria. To achieve partition pruning:

  - Ensure partition key usage in queries: Queries should be designed to filter by the partition key to enable partition pruning.

  - Avoid operations that prevent pruning: Avoid functions or expressions that prevent the database from recognizing the partition key in the `WHERE` clause.

---

### Advanced Security in SQL

Securing a SQL database is crucial for protecting sensitive data, ensuring compliance with regulations, and preventing unauthorized access. SQL provides various methods for managing roles and permissions, as well as techniques for encrypting sensitive data to protect it from unauthorized access or breaches. Below are some key concepts and practices related to managing roles, permissions, and data encryption in SQL.

**1. Managing Roles and Permissions in SQL.**

In a relational database, roles and permissions are used to control access to data and operations. By assigning roles to users and controlling what they can access or modify, you can ensure that only authorized users can perform sensitive actions.

**a. What are Roles?**

Roles are a way to group together certain permissions and assign them to users or other roles. A role may represent a specific set of duties, such as database administrators, developers, or analysts. Instead of assigning permissions to individual users, you can assign them to roles and then assign users to those roles.

```sql
-- Creating a role
CREATE ROLE db_writer;

-- Assigning permissions to the role
GRANT INSERT, UPDATE ON Employees TO db_writer;
```

**b. Creating and Managing Roles:**

**`Create a Role:`** You create a role with specific permissions, which users can then inherit.

```sql
CREATE ROLE db_admin;
```

**`Assigning Permissions to Roles:`** Once the role is created, you assign the necessary permissions to it. This simplifies the task of granting and revoking permissions across multiple users.

```sql
GRANT SELECT, INSERT, DELETE ON Orders TO db_admin;
```

**`Assigning Roles to Users:`** After a role is defined, you can assign it to a user, and that user will inherit the permissions granted to the role.

```sql
-- Assigning role to a user
EXEC sp_addrolemember 'db_admin', 'JohnDoe';
```

**`Revoking Roles:`** To remove a user from a role or revoke the permissions, use the REVOKE statement:

```sql
EXEC sp_droprolemember 'db_admin', 'JohnDoe';
```

**c. Granting and Revoking Permissions:**

Permissions can be granted to both roles and individual users for specific database objects (e.g., tables, views, procedures).

**1. Granting Permissions:**

```sql
GRANT SELECT ON Employees TO db_reader;
```

**2. Revoking Permissions:**

```sql
REVOKE SELECT ON Employees FROM db_reader;
```

**3. DENY:** In SQL Server, the `DENY` statement explicitly denies a permission, overriding any `GRANT` statements.

```sql
DENY DELETE ON Orders TO db_writer;
```

**d. Permission Hierarchy:**

Permissions in SQL are often hierarchical:

`GRANT:` Allows a user or role to execute a specific action.

`REVOKE:` Removes a granted permission.

`DENY:` Prevents a user or role from performing an action, even if it is granted to other roles.

```sql
-- Create roles
CREATE ROLE db_reader;
CREATE ROLE db_writer;

-- Grant permissions to roles
GRANT SELECT ON Employees TO db_reader;
GRANT INSERT, UPDATE, DELETE ON Employees TO db_writer;

-- Assign roles to users
EXEC sp_addrolemember 'db_reader', 'JaneDoe';
EXEC sp_addrolemember 'db_writer', 'JohnDoe';

-- Revoke permissions
REVOKE DELETE ON Employees FROM db_writer;

-- Deny DELETE operation explicitly
DENY DELETE ON Employees TO db_writer;
```

---

**2. Encryption Techniques to Secure Data:**

Encryption ensures that even if unauthorized users gain access to data, they cannot interpret or use it. There are two main types of encryption used in SQL databases:

**a. Transparent Data Encryption (TDE):**

Transparent Data Encryption (TDE) is a technique that encrypts the entire database, including data files, logs, and backups, without requiring any changes to the application or user queries. The encryption is "transparent" to the users and applications interacting with the database.

```sql
-- Enable encryption on the database
CREATE DATABASE MyDatabase
ENCRYPTION ON;
```

**b. Column-Level Encryption:**

Column-level encryption allows sensitive data, such as credit card numbers or personal information, to be encrypted while leaving other columns unencrypted. This encryption can be applied on a per-column basis and can be symmetric (using the same key for encryption and decryption) or asymmetric (using a public key for encryption and a private key for decryption).

```sql
-- Example of symmetric encryption for storing sensitive data in a column
CREATE SYMMETRIC KEY SensitiveDataKey 
WITH ALGORITHM = AES_256 
ENCRYPTION BY PASSWORD = 'StrongPassword';

-- Encrypt a column value
OPEN SYMMETRIC KEY SensitiveDataKey DECRYPTION BY PASSWORD = 'StrongPassword';
UPDATE Customers SET CreditCardNumber = EncryptByKey(Key_GUID('SensitiveDataKey'), CreditCardNumber);
```

**c. Always Encrypted (SQL Server):**

SQL Server’s Always Encrypted feature allows encryption of sensitive data both at rest and in transit. The data is encrypted on the client side before being sent to the server, ensuring that sensitive data is never exposed to database administrators or even application developers.

```sql
-- Create a column encryption key
CREATE COLUMN ENCRYPTION KEY MyEncryptionKey
WITH VALUES (
    COLUMN MASTER KEY = MyMasterKey,
    ALGORITHM = 'AEAD_AES_256_CBC_HMAC_SHA_256',
    ENCRYPTION TYPE = 'Deterministic'
);
```

**d. Data Masking:**

Data masking involves obscuring sensitive data by replacing it with a similar but non-sensitive value. It's typically used in non-production environments to protect data while allowing testing and development activities.

```sql
-- Create a masked column for a phone number
CREATE TABLE Customers (
    CustomerID INT,
    CustomerName VARCHAR(100),
    PhoneNumber VARCHAR(15) MASKED WITH (FUNCTION = 'default()')
);
```

### What is SQL Injection?

SQL injection is a type of vulnerability in website and web app code that allows attackers to control back-end operations and access, retrieve, and destroy sensitive data from databases. In this technique, malicious SQL statements are inserted into a database entry field, and once they are performed, the database becomes vulnerable to an attacker. This technique is commonly used to access sensitive data and perform administrative activities on databases by exploiting data-driven applications. It is also known as SQLi attack.

Some common examples of SQL injection are:

- Accessing confidential data to modify an SQL query to get desired results.

- UNION attacks to steal data from different database tables.

- Examine the database to extract information regarding the version and structure of the database.

---

### What is the difference between DELETE and TRUNCATE statements in SQL?

The main difference between them is that the delete statement deletes data without resetting a table's identity, whereas the truncate command resets a particular table's identity. The following comparison chart explains it more clearly:

| Feature | DELETE | TRUNCATE |
|---------|--------|----------|
| Operation | Removes single or multiple rows depending on the condition | Deletes the whole contents of a table but preserves the table structure |
| Command Type | DML command | DDL command |
| WHERE Clause | Can use the WHERE clause | Cannot use the WHERE clause |
| Usage | Used to delete a row from a table | Used to remove all rows from a table |
| Speed | Slower because it maintains the log | Faster as it deletes entire data at once without maintaining transaction logs |
| Rollback | Can roll back data | Cannot roll back data |
| Space | Takes more space | Occupies less space |

---

### What are the TRUNCATE, DELETE and DROP statements?

DELETE statement is used to delete rows from a table.

```sql
DELETE FROM Candidates 
WHERE CandidateId > 1000;
```

TRUNCATE command is used to delete all the rows from the table and free the space containing the table

```sql
 TRUNCATE TABLE Candidates;
```

DROP command is used to remove an object from the database. If you drop a table, all the rows in the table are deleted and the table structure is removed from the database.

```sql
DROP TABLE Candidates;
```
