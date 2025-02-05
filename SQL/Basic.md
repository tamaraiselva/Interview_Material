# SQL Basics

1. **What is SQL?**  
SQL stands for Structured Query Language. It is a standardized programming language used to manage and manipulate relational databases. It enables users to perform a variety of tasks such as querying data, creating and modifying database structures, and managing access permissions. SQL is widely used across various relational database management systems such as MySQL, PostgreSQL, Oracle, and SQL Server.

2. **What are the different types of SQL databases (SQL vs NoSQL)?**  
   - **SQL (Relational Databases)**: Use structured data with predefined schemas, support ACID properties, and employ SQL for querying (e.g., MySQL, PostgreSQL, Oracle).
   - **NoSQL (Non-relational Databases)**: Handle unstructured or semi-structured data, offer flexible schemas, and focus on scalability and performance (e.g., MongoDB, Cassandra, Redis).

3. **What is a relational database?**  
   A relational database is a type of database that stores and organizes data in a structured manner using tables. Each table consists of:
   - **Rows** (also called records or tuples): Represent individual entries, such as a customer or an order.
   - **Columns** (also called attributes or fields): Represent the properties of those entries, such as customer name or order date.

4. **What are the main applications of SQL?**  
   Using SQL, we can:
   - Create, delete, and update tables in a database.
   - Access, manipulate, and modify data in a table.
   - Retrieve and summarize the necessary information from a table or several tables.
   - Add or remove certain rows or columns from a table.

5. **What is schema?**
   A schema is a logical structure in a database that organizes and groups related objects like   tables, views, and indexes.

6. **what is Table?**
   A table is a collection of rows and columns in a database that stores structured data, where each column represents a data attribute and each row represents a record.

7. **What is Database?**  
    A database is an organized collection of data, stored and retrieved digitally from a
 remote or local computer system. Databases can be vast and complex, and such
 databases are developed using fixed design and modeling approaches.

8. **What is DBMS, and what types of DBMS do you know?**  
   DBMS stands for Database Management System. DBMS is a system soware responsible for the creation, retrieval, updation, and management of the database. It ensures that our data is consistent, organized, and is easily accessible by serving as an interface between the database and its end-users or application soware..

   Types of DBMS include:
   - Relational
   - Hierarchical
   - Network
   - Graph
   - Object-oriented

---

### SQL Queries

9. **What is an SQL query, and what types of queries do you know?**

   A query is a piece of code written in SQL to access or modify data from a database. There are two types of SQL queries:
   - **Select queries**: Used to retrieve the necessary data (including limiting, grouping, ordering, and extracting data from multiple tables).
   - **Action queries**: Used to create, add, delete, update, and rename data.

10. **What is the basic structure of an SQL statement?**  
   The basic structure typically includes the following clauses:

   ```sql
   SELECT column1, column2 
   FROM table_name 
   WHERE condition 
   ORDER BY column1;
   ```

   - **SELECT**: Specifies the columns to retrieve.

   - **FROM**: Indicates the table to query.

   - **WHERE**: Filters records based on specified conditions.

   - **ORDER BY**: Sorts the results based on one or more columns.

11. **What is an SQL statement? Give some examples.**
   An SQL statement is a command used to perform specific operations on a database. Here are a few common examples:

   - **SELECT Statement**:

     ```sql
     SELECT first_name, last_name FROM employees WHERE department = 'Sales';
     ```

   - **INSERT Statement**:

     ```sql
     INSERT INTO employees (id, first_name, last_name, department, salary) 
     VALUES (1, 'John', 'Doe', 'Sales', 60000.00);
     ```

   - **UPDATE Statement**:

     ```sql
     UPDATE employees SET salary = 65000.00 WHERE id = 1;
     ```

   - **DELETE Statement**:

     ```sql
     DELETE FROM employees WHERE id = 1;
     ```

   - **CREATE TABLE Statement**:

     ```sql
     CREATE TABLE employees (
         id INT PRIMARY KEY,
         first_name VARCHAR(50),
         last_name VARCHAR(50),
         department VARCHAR(50),
         salary DECIMAL(10, 2)
     );
     ```

12. **What are primary keys and foreign keys?**

    - **Primary Key**: A unique identifier for each record in a table, ensuring no duplicate entries. It cannot be NULL.

    - **Foreign Key**: A field in one table that refers to the primary key of another table, establishing a relationship between the two tables.

13. **What is a unique key?**  
    A unique key is a column (or multiple columns) of a table to which the UNIQUE constraint was imposed to ensure unique values, including a possible NULL value (the only one).

14. **What are indexes and how do they work?**  
    Indexes are data structures that improve the speed of data retrieval operations on a database table by providing quick access to rows based on the values in one or more columns.

### SQL Command Types

15. **What types of SQL commands (or SQL subsets) do you know?**  
    - **Data Definition Language (DDL)**: Defines and modifies the structure of a database.
    - **Data Manipulation Language (DML)**: Accesses, manipulates, and modifies data in a database.
    - **Data Control Language (DCL)**: Controls user access to data and gives or revokes privileges to specific users or groups.
    - **Transaction Control Language (TCL)**: Controls transactions in a database.
    - **Data Query Language (DQL)**: Performs queries on the data to retrieve necessary information.

16. **Examples of common SQL commands of each type:**
    - **DDL**: CREATE, ALTER TABLE, DROP, TRUNCATE, ADD COLUMN
    - **DML**: UPDATE, DELETE, INSERT
    - **DCL**: GRANT, REVOKE
    - **TCL**: COMMIT, SET TRANSACTION, ROLLBACK, SAVEPOINT
    - **DQL**: SELECT

---

### Data Definition Language(DDL)

- **`CREATE:`** This command is used to create a new table, database, index, or view in the database.

```sql
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100) UNIQUE,
    DateOfBirth DATE,
    Salary DECIMAL(10, 2) DEFAULT 50000
);
```

- **`ALTER:`** This command is used to modify an existing database object, such as a table.

```sql
ALTER TABLE Employees
ADD COLUMN PhoneNumber VARCHAR(15);
```

- **`DROP:`** This command is used to delete an existing database object, such as a table or a database.

```sql
DROP TABLE Employees;
```

- **`TRUNCATE`:** This command is used to remove all records from a table, but the table structure remains.

```sql
TRUNCATE TABLE Employees;
```

- **`COLUMN:`** This is not a standalone command but is used with other commands like `ALTER` to add, modify, or drop columns in a table.

```sql
ALTER TABLE Employees
ADD COLUMN Department VARCHAR(50);
```

---

### Data Manipulation Langauage(DML)

- **`INSERT:`** This command is used to add new rows to a table.

```sql
INSERT INTO Employees (EmployeeID, FirstName, LastName, Email, DateOfBirth, Salary)
VALUES (1, 'John', 'Doe', 'john.doe@example.com', '1980-01-01', 60000);
```

- **`UPDATE:`** This command is used to modify existing rows in a table.

```sql
UPDATE Employees
SET Salary = 65000
WHERE EmployeeID = 1;
```

- **`DELETE:`** This command is used to remove existing rows from a table.

```sql
DELETE FROM Employees
WHERE EmployeeID = 1;
```

---

### Data Control Language(DCL)

- **`GRANT:`** This command is used to give users access privileges to the database.

```sql
GRANT SELECT, INSERT, UPDATE ON Employees TO user_name;
```

- **`REVOKE:`** This command is used to remove access privileges that were previously granted to users.

```sql
REVOKE SELECT, INSERT, UPDATE ON Employees FROM user_name;
```

---

### Transaction Control Language(TCL)

- **`COMMIT:`** This command is used to save all the changes made during the current transaction. Once committed, the changes cannot be undone.

```sql
COMMIT;
```

- **`SAVEPOINT:`** This command is used to set a point within a transaction to which you can later roll back. It allows partial rollback of a transaction.

```sql
SAVEPOINT savepoint_name;
```

- **`ROLLBACK:`** This command is used to undo changes made during the current transaction. You can roll back to the beginning of the transaction or to a savepoint.

```sql
ROLLBACK TO savepoint_name;
```

- **`SET TRANSACTION:`** This command is used to set the properties of the current transaction, such as isolation level.

```sql
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
```

### Data Query or Retrival Language (DQL)

- **`SELECT:`** This command is used to fetch data from a database. The data returned is stored in a result table, sometimes called the result set.

```sql
SELECT column1, column2, ...
FROM table_name WHERE condition;
```

---

### Constraints

17. **What is a constraint, and why use constraints?**  
    Constraints are used to specify the rules concerning data in the table. It can be
 applied for single or multiple fields in an SQL table during the creation of the table or
 a er creating using the ALTER TABLE command..

18. **What SQL constraints do you know?**

- **`NOT NULL`** - Restricts NULL value from being inserted into a column.

- **`CHECK`** - Verifies that all values in a field satisfy a condition.

- **`DEFAULT`** - Automatically assigns a default value if no value has been specified
 for the field.

- **`UNIQUE`** - Ensures unique values to be inserted into the field.

- **`INDEX`** - Indexes a field providing faster retrieval of records.

- **`PRIMARY KEY`** - Uniquely identifies each record in a table.

- **`FOREIGN KEY`** - Ensures referential integrity for a record in another table

---

### SQL-Server Joins

19. **What is a join?**

The SQL Join clause is used to combine records (rows) from two or more tables in a SQL database based on a related column between the two.

20. **What types of joins do you know?**  

  - **(INNER) JOIN**: Returns only those records that satisfy a defined join condition in both (or all) tables. It's a default SQL join.

  - **LEFT (OUTER) JOIN**: Returns all records from the left table and those records from the right table that satisfy a defined join condition.
  - **RIGHT (OUTER) JOIN**: Returns all records from the right table and those records from the left table that satisfy a defined join condition.

  - **FULL (OUTER) JOIN**: Returns all records from both (or all) tables, combining left and right joins.

  - **CROSS JOIN**: Returns the Cartesian product of the two tables.

  - **SELF JOIN**: A self join is a regular join but the table is joined with itself.

21. **What is NULL value? How is it different from zero or a blank space?**  
    A NULL value indicates the absence of data for a certain cell in a table. In contrast, zero is a valid numeric value, and an empty string is a legal string of zero length.

---

### SQL-Server Functions

**`Aggregate Functions`**

22. **What are aggregate functions? Give examples.**

Aggregate functions perform calculations on a set of values and return a single value. Examples include:

- **COUNT()**: Counts the total number of records in a specific table or view.
- **SUM()**: Calculates the sum of a collection of values.
- **AVG()**: Calculates the mean of a collection of values.
- **MAX()**:  Calculates the maximum of a collection of values.
- **MIN()**: Calculates the minimum of a collection of values.
- **FIRST()**: Fetches the first element in a collection of values.
- **LAST()**: Fetches the last element in a collection of values.

**COUNT()**
Counts the number of rows that match a specified criterion.

**Example:**

```sql
SELECT COUNT(*) AS total_orders
FROM orders
WHERE order_date >= '2023-01-01';
```

This query counts the total number of orders placed since January 1, 2023.

**SUM()**
Calculates the total sum of a specified numeric column.

**Example:**

```sql
SELECT SUM(order_amount) AS total_sales
FROM orders
WHERE order_date >= '2023-01-01';
```

This query calculates the total sales amount for all orders placed since January 1, 2023.

**AVG()**
Calculates the average value of a specified numeric column.

**Example:**

```sql
SELECT AVG(order_amount) AS average_order_amount
FROM orders;
```

This query computes the average order amount for all orders in the `orders` table.

**MAX()**
Finds the maximum value in a specified column.

**Example:**

```sql
SELECT MAX(order_amount) AS highest_order
FROM orders;
```

This query identifies the highest order amount from all orders.

**MIN()**
Finds the minimum value in a specified column.

**Example:**

```sql
SELECT MIN(order_amount) AS lowest_order
FROM orders;
```

This query determines the lowest order amount from all orders.

---

**`String Functions`**

String functions perform operations on string values and return a string or numeric value.

  - **LEN():** Returns the length of a string.

  ```sql
  SELECT LEN(column_name) FROM table_name;
  ```

  - **SUBSTRING():** Extracts a substring from a string.

  ```sql
  SELECT SUBSTRING(column_name, start, length) FROM table_name;
  ```

  - **CHARINDEX():** Returns the position of a substring in a string.

  ```sql
  SELECT CHARINDEX('substring', column_name) FROM table_name;
  ```

  - **REPLACE():** Replaces all occurrences of a substring with another substring.

  ```sql
  SELECT REPLACE(column_name, 'old_substring', 'new_substring') FROM table_name;
  ```

  - **UPPER() and LOWER():** Converts a string to uppercase or lowercase.

  ```sql
  SELECT UPPER(column_name) FROM table_name;
  SELECT LOWER(column_name) FROM table_name;
  ```

---

**`Date Functions`**

Date functions perform operations on date and time values and return a date, time, or numeric value.

  - **GETDATE():** Returns the current date and time.

  ```sql
  SELECT GETDATE();
  ```

  - **DATEADD():** Adds a specified number of units to a date.

  ```sql
  SELECT DATEADD(day, 10, column_name) FROM table_name;
  ```

  - **DATEDIFF():** Returns the difference between two dates.

  ```sql
  SELECT DATEDIFF(day, start_date, end_date) FROM table_name;
  ```

  - **FORMAT():** Formats a date value according to a specified format.

  ```sql
  SELECT FORMAT(column_name, 'yyyy-MM-dd') FROM table_name;
  ```

---

**`Window Functions`**

Window functions perform calculations across a set of table rows that are related to the current row.

  - **ROW_NUMBER():** Assigns a unique number to each row within a partition.

  ```sql
  SELECT ROW_NUMBER() OVER (ORDER BY column_name) AS row_num FROM table_name;
  ```

  - **RANK():** Assigns a rank to each row within a partition, with gaps in the ranking.

  ```sql
  SELECT RANK() OVER (ORDER BY column_name) AS rank FROM table_name;
  ```

  - **DENSE_RANK():** Assigns a rank to each row within a partition, without gaps in the ranking.

  ```sql
  SELECT DENSE_RANK() OVER (ORDER BY column_name) AS dense_rank FROM table_name;
  ```

  - **NTILE():** Distributes rows into a specified number of groups.

  ```sql
  SELECT NTILE(4) OVER (ORDER BY column_name) AS quartile FROM table_name;
  ```

---

**`System Functions`**

System functions perform operations on and return information about values, objects, and settings in SQL Server.

- **@@IDENTITY:** Returns the last-inserted identity value.

```sql
SELECT @@IDENTITY;
```

- **@@ROWCOUNT:** Returns the number of rows affected by the last statement.

```sql
SELECT @@ROWCOUNT;
```

- **@@VERSION:** Returns the SQL Server version information.

```sql
SELECT @@VERSION;
```

- **DB_NAME():** Returns the name of the current database.

```sql
SELECT DB_NAME();
```

- **USER_NAME():** Returns the database user name.

```sql
SELECT USER_NAME();
```

---

**Combining Aggregate Functions**

**Example:**

```sql
SELECT 
    COUNT(*) AS total_orders,
    SUM(order_amount) AS total_sales,
    AVG(order_amount) AS average_order_amount,
    MAX(order_amount) AS highest_order,
    MIN(order_amount) AS lowest_order
FROM orders
WHERE order_date >= '2023-01-01';
```

This query provides a summary of the total number of orders, total sales, average order amount, highest order, and lowest order for orders placed since January 1, 2023.

---

23. **How do you use string functions such as CONCAT, SUBSTRING, and LENGTH?**  

    - **CONCAT**: Combines two or more strings. Example:

      ```sql
      SELECT CONCAT(first_name, ' ', last_name) FROM employees;
      ```

    - **SUBSTRING**: Extracts a portion of a string. Example:

      ```sql
      SELECT SUBSTRING(name, 1, 3) FROM employees;
      ```

    - **LENGTH**: Returns the length of a string. Example:

      ```sql
      SELECT LENGTH(name) FROM employees;
      ```

24. **What date functions are available?**  
    Common date functions include:
    - **NOW()**: Returns the current date and time.
    - **CURDATE()**: Returns the current date.
    - **DATEDIFF()**: Returns the difference between two dates.

### Subqueries

25. **What is a subquery?**  
    A subquery is a SQL query nested inside another SQL query. It is used to retrieve data that will be used in the main query and can be employed in various clauses, such as SELECT, FROM, or WHERE, returning single or multiple values.

26. **Examples of Subqueries:**
    - **Using a Subquery in the WHERE Clause:**

      ```sql
      SELECT first_name, last_name FROM employees 
      WHERE department_id = (SELECT id FROM departments WHERE name = 'Sales');
      ```

    - **Using a Subquery in the FROM Clause:**

      ```sql
      SELECT AVG(salary) FROM (SELECT salary FROM employees WHERE department = 'Sales') AS sales_salaries;
      ```

### Performance

27. **How to improve SQL query performance?**  
    - Use indexes on frequently queried columns.
    - Limit the number of rows returned with a WHERE clause.
    - Optimize JOINs by minimizing the number of joins and filtering data as early as possible.
    - Avoid using SELECT * and specify only the required columns.
    - Regularly analyze and optimize the database.

### Transactions

28. **What is a transaction?**  
    A transaction is a sequence of one or more SQL operations treated as a single logical unit. A transaction follows the ACID properties:
    - **Atomicity**: Ensures all operations succeed or none at all.
    - **Consistency**: Maintains database integrity.
    - **Isolation**: Ensures transactions are isolated from each other.
    - **Durability**: Ensures the results of a transaction persist after completion.

29. **What are the transaction control commands?**  
    Transaction control commands include:
    - **COMMIT**: Saves all changes made during the current transaction.
    - **ROLLBACK**: Reverts changes made during the current transaction.
    - **SAVEPOINT**: Sets a point in a transaction to which you can later roll back.

30. **What are the differences between SQL, MySQL, and SQL Server?**

| SQL                                    | MySQL                                            | SQL Server                                      |
|----------------------------------|----------------------------------------|--------------------------------------------------|
 SQL or Structured Query Language is useful for managing our relational databases. It is used to query and operate the database.  | MySQL is the popular database management system used for managing the relational database. It is a fast, scalable, and easy-to-use database.                  | SQL Server is an RDBMS database system mainly developed for the Windows system to store, retrieve, and access data requested by the developer.                 |
| SQL first appeared in 1974.       | MySQL first appeared on May 23, 1995.                    | SQL Server first appeared on April 24, 1989.         |
|  SQL was developed by IBM Corporation.                                   | MySQL was developed by Oracle Corporation.                                     | SQL Server was developed by Microsoft Company.                                  |
| SQL is a query language for managing databases.                       | MySQL is database software that uses SQL language to conduct with the database.                               | SQL Server is also a software that uses SQL language to conduct with the database.                                       |
| SQL has no variables.                   | MySQL can use variables constraints and data types.                       | SQL Server can use variables constraints and data types.                      |
| SQL is a programming language, so that it does not get any updates. Its commands are always fixed and remain the same.                              | MySQL is software, so it gets frequent updation.                                   | SQL Server is also software, so it gets frequent updation.                               |

