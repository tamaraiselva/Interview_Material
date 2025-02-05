# intermediate

## TOPIC

### Types of Joins

1. **Explain FULL OUTER JOIN, SELF JOIN, and CROSS JOIN with examples**
Here's the information for the tables **employees** and **departments** formatted neatly, along with their respective data:

**Table: employees:**

| employee_id | first_name | last_name | department_id |
|-------------|------------|-----------|---------------|
| 1           | John       | Doe       | 101           |
| 2           | Jane       | Smith     | 102           |
| 3           | Jim        | Brown     | NULL          |

**Table: departments:**

| department_id | department_name |
|---------------|-----------------|
| 101           | HR              |
| 102           | Engineering     |
| 103           | Marketing       |

1. **INNER JOIN**:
   The `INNER JOIN` keyword selects records that have matching values in both tables. It returns only the rows where there is a match in both tables.

   ```sql
   SELECT employees.first_name, employees.last_name, departments.department_name
   FROM employees
   INNER JOIN departments
   ON employees.department_id = departments.department_id;
   ```

   **Result Set:**

   | first_name | last_name | department_name |
   |------------|-----------|-----------------|
   | John       | Doe       | HR              |
   | Jane       | Smith     | Engineering     |

2. **LEFT JOIN**:
   The `LEFT JOIN` (or `LEFT OUTER JOIN`) returns all rows from the left table and the matched rows from the right table. If there is no match, the result is `NULL` on the side of the right table.

   ```sql
   SELECT departments.department_name, employees.first_name
   FROM departments
   LEFT JOIN employees
   ON departments.department_id = employees.department_id;
   ```

   **Result Set:**

   | department_name | first_name |
   |-----------------|------------|
   | HR              | John       |
   | Engineering     | Jane       |
   | Marketing       | NULL       |

3. **RIGHT JOIN**:
   The `RIGHT JOIN` (or `RIGHT OUTER JOIN`) is similar to the `LEFT JOIN`, but returns all rows from the right table and the matched rows from the left table. If there is no match, the result is `NULL` on the side of the left table.

   ```sql
   SELECT employees.first_name, departments.department_name
   FROM employees
   RIGHT JOIN departments
   ON employees.department_id = departments.department_id;
   ```

   **Result Set:**

   | first_name | department_name |
   |------------|-----------------|
   | John       | HR              |
   | Jane       | Engineering     |
   | NULL       | Marketing       |

4. **FULL JOIN**:

The `FULL JOIN` (or `FULL OUTER JOIN`) combines the results of both `LEFT JOIN` and `RIGHT JOIN`. The result set will contain all rows from both tables, with `NULL` in places where there is no match.

   ```sql
   SELECT employees.first_name, departments.department_name
   FROM employees
   FULL JOIN departments
   ON employees.department_id = departments.department_id;
   ```

**Result Set:**

| first_name | department_name |
|------------|-----------------|
| John       | HR              |
| Jane       | Engineering     |
| NULL       | Marketing       |
| Jim        | NULL            |

5. **CROSS JOIN**:

The `CROSS JOIN` returns the Cartesian product of the two tables, meaning it returns all possible combinations of rows from the two tables. This type of join does not require a condition.
  
```sql
  SELECT employees.first_name, departments.department_name
  FROM employees
  CROSS JOIN departments;
```
  
  **Result Set:**
  
   | first_name | department_name |
   |------------|-----------------|
   | John       | HR              |
   | John       | Engineering     |
   | John       | Marketing       |
   | Jane       | HR              |
   | Jane       | Engineering     |
   | Jane       | Marketing       |
   | Jim        | HR              |
   | Jim        | Engineering     |
   | Jim        | Marketing       |

---

### What is the difference between UNION and UNION ALL?

**UNION:**

- **Function**: Combines the results of two or more `SELECT` queries.
- **Duplicates**: Removes duplicate rows from the result set.
- **Performance**: Generally slower than `UNION ALL` because it must perform a check to remove duplicates.
- **Example**:

  ```sql
  SELECT name FROM employees
  UNION
  SELECT name FROM managers;
  ```

- Use `UNION` when you want a distinct set of results with duplicates removed.

**UNION ALL:**

- **Function**: Combines the results of two or more `SELECT` queries.
- **Duplicates**: Includes all rows from both queries, including duplicates.
- **Performance**: Typically faster than `UNION` because it does not require duplicate removal.
- **Example**:

  ```sql
  SELECT name FROM employees
  UNION ALL
  SELECT name FROM managers;
  ```

- Use `UNION ALL` when you want to include all records from both queries, including duplicates, which can improve performance.

---

### INTERSECT and EXCEPT in SQL

**INTERSECT** and **EXCEPT** are set operations in SQL that allow you to compare the results of two queries. These operations are used to find commonalities and differences between two result sets.

#### INTERSECT

The `INTERSECT` operator returns the common rows between two result sets. Only the rows that appear in both result sets are included in the final result.

**Example:**
Let's assume we have two tables, `employees` and `contractors`.

**Table: `employees`.**

| employee_id | name      | department_id |
|-------------|-----------|---------------|
| 1           | John Doe  | 101           |
| 2           | Jane Smith| 102           |
| 3           | Jim Brown | 103           |

**Table: `contractors`.**

| contractor_id | name      | department_id |
|---------------|-----------|---------------|
| 1             | Alice Blue| 101           |
| 2             | Jane Smith| 102           |
| 3             | Jack White| 104           |

**Query:**

```sql
SELECT name, department_id
FROM employees
INTERSECT
SELECT name, department_id
FROM contractors;
```

**Result:**

| name       | department_id |
|------------|---------------|
| Jane Smith | 102           |

#### EXCEPT

The `EXCEPT` operator returns the rows from the first result set that are not present in the second result set. It is useful for finding differences between two result sets.

**Example:**
Using the same `employees` and `contractors` tables from above:

**Query:**

```sql
SELECT name, department_id
FROM employees
EXCEPT
SELECT name, department_id
FROM contractors;
```

**Result:**

| name      | department_id |
|-----------|---------------|
| John Doe  | 101           |
| Jim Brown | 103           |

**Conversely, if we switch the order of the tables:**

**Query:**

```sql
SELECT name, department_id
FROM contractors
EXCEPT
SELECT name, department_id
FROM employees;
```

**Result:**

| name       | department_id |
|------------|---------------|
| Alice Blue | 101           |
| Jack White | 104           |

#### Key Points

- **INTERSECT** returns only the rows that are present in both result sets.
- **EXCEPT** returns only the rows from the first result set that are not present in the second result set.

---

### Question 1: What is the purpose of the GROUP BY clause in SQL?

The **GROUP BY** clause is used to arrange identical data into groups. It is often used with aggregate functions like **COUNT**, **SUM**, **AVG**, **MAX**, and **MIN** to perform calculations on each group.

**Example:**

```sql
SELECT department_id, COUNT(*) AS employee_count
FROM employees
GROUP BY department_id;
```

This query groups employees by their department and counts how many employees are in each department.

---

### Question 2: What is the purpose of the HAVING clause in SQL?

The **HAVING** clause is used to filter records after aggregation has been performed. It allows you to specify conditions on aggregate functions, unlike the **WHERE** clause, which cannot filter on aggregates.

**Example:**

```sql
SELECT department_id, COUNT(*) AS employee_count
FROM employees
GROUP BY department_id
HAVING COUNT(*) > 5;
```

This query retrieves departments that have more than 5 employees after grouping.

---

### Main Differences Between HAVING and WHERE Clauses

| **HAVING** | **WHERE** |
|------------|------------|
| The **HAVING** clause is used to filter groups of rows after grouping. It operates on the results of aggregate functions applied to grouped columns. | The **WHERE** clause is used to filter rows before grouping. It operates on individual rows in the table and is applied before grouping and aggregation. |
| The **HAVING** clause is typically used with `GROUP BY` queries. It filters groups of rows based on conditions involving aggregated values. | The **WHERE** clause can be used with any SQL query, whether it involves grouping or not. It filters individual rows based on specified conditions. |
| In the **HAVING** clause, you generally use aggregate functions (e.g., SUM, COUNT) to reference grouped columns and apply conditions to groups of rows. | In the **WHERE** clause, you can reference columns directly and apply conditions to individual rows. |

---

### Example Commands

#### Using HAVING

```sql
SELECT customer_id, SUM(order_total) AS total_order_amount
FROM orders
GROUP BY customer_id
HAVING SUM(order_total) > 1000;
```

This query retrieves customer IDs and their total order amounts, filtering out those customers whose total order amount is greater than 1000 after aggregation.

#### Using WHERE

```sql
SELECT customer_id, order_total
FROM orders
WHERE order_total > 1000;
```

This query retrieves customer IDs and individual order totals, filtering out orders that exceed 1000 before any grouping occurs.

Certainly! Here’s an explanation of the **EXISTS** and **NOT EXISTS** operators in SQL, formatted in Markdown.

---

### EXISTS and NOT EXISTS Operators

#### EXISTS

The **EXISTS** operator checks if a subquery returns any rows. It evaluates to true if the subquery finds one or more rows.

**Example:**

```sql
SELECT employee_id, first_name
FROM employees e
WHERE EXISTS (SELECT 1 FROM departments d WHERE d.department_id = e.department_id);
```

In this example, the query retrieves employee IDs and first names from the **employees** table only if there exists at least one corresponding department in the **departments** table with the same **department_id**.

---

#### NOT EXISTS

The **NOT EXISTS** operator checks if a subquery returns no rows. It evaluates to true if the subquery finds no rows.

**Example:**

```sql
SELECT employee_id, first_name
FROM employees e
WHERE NOT EXISTS (SELECT 1 FROM departments d WHERE d.department_id = e.department_id);
```

In this example, the query retrieves employee IDs and first names from the **employees** table only if there are no corresponding departments in the **departments** table with the same **department_id**.

---

### Window Functions in SQL

Window functions in SQL allow you to perform calculations across a set of rows related to the current row, without collapsing the result set into a single output row. This means each row retains its identity while still benefiting from aggregate calculations.

**Key Characteristics:**

- **Preserves Row Identity**: Unlike traditional aggregate functions, window functions do not group rows.
- **Defined by OVER Clause**: The set of rows (or "window") is defined using the `OVER` clause.

### Examples of Window Functions

#### 1. ROW_NUMBER()

- **Description**: Assigns a unique sequential integer to rows within a partition of a result set, starting at 1 for the first row in each partition.
- **Use Case**: Generating unique row numbers for each row.
- **Example**:

  ```sql
  SELECT employee_id, name, department_id,
         ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY name) as row_num
  FROM employees;
  ```

- **Result**:

  | employee_id | name         | department_id | row_num |
  |-------------|--------------|---------------|---------|
  | 1           | Alice Blue   | 101           | 1       |
  | 3           | John Doe     | 101           | 2       |
  | 2           | Jane Smith   | 102           | 1       |
  | 4           | Jim Brown    | 103           | 1       |

#### 2. RANK()

- **Description**: Assigns a rank to each row within a partition of a result set. Rows with equal values receive the same rank, with gaps in the rank sequence.
- **Use Case**: Ranking rows within a partition based on specific criteria.
- **Example**:

  ```sql
  SELECT employee_id, name, department_id, salary,
         RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) as rank
  FROM employees;
  ```

- **Result**:

  | employee_id | name         | department_id | salary | rank |
  |-------------|--------------|---------------|--------|------|
  | 1           | Alice Blue   | 101           | 90000  | 1    |
  | 3           | John Doe     | 101           | 80000  | 2    |
  | 2           | Jane Smith   | 102           | 95000  | 1    |
  | 4           | Jim Brown    | 103           | 70000  | 1    |

#### 3. DENSE_RANK()

- **Description**: Similar to `RANK()`, but without gaps in the ranking sequence when there are ties. Rows with equal values receive the same rank, and the next rank follows immediately.
- **Use Case**: Ranking rows without gaps in sequences.
- **Example**:

  ```sql
  SELECT employee_id, name, department_id, salary,
         DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) as dense_rank
  FROM employees;
  ```

- **Result**:

  | employee_id | name         | department_id | salary | dense_rank |
  |-------------|--------------|---------------|--------|------------|
  | 1           | Alice Blue   | 101           | 90000  | 1          |
  | 3           | John Doe     | 101           | 80000  | 2          |
  | 2           | Jane Smith   | 102           | 95000  | 1          |
  | 4           | Jim Brown    | 103           | 70000  | 1          |

---

### Analytical Functions in SQL

Analytical functions enable complex data analysis by performing calculations across a set of rows related to the current row. Two common analytical functions are **LEAD** and **LAG**.

#### LEAD Function

- **Description**: Accesses data from subsequent rows in the result set.
- **Use Case**: Retrieve values from a row that follows the current row.
- **Example**:

  ```sql
  SELECT sale_id, sale_date, amount,
         LEAD(amount, 1, 0) OVER (ORDER BY sale_date) AS next_sale_amount
  FROM sales;
  ```

- **Result**:

  | sale_id | sale_date  | amount | next_sale_amount |
  |---------|------------|--------|------------------|
  | 1       | 2024-01-01 | 100    | 150              |
  | 2       | 2024-01-02 | 150    | 200              |
  | 3       | 2024-01-03 | 200    | 250              |
  | 4       | 2024-01-04 | 250    | 0                |

#### LAG Function

- **Description**: Accesses data from preceding rows in the result set.
- **Use Case**: Retrieve values from a row that precedes the current row.
- **Example**:

  ```sql
  SELECT sale_id, sale_date, amount,
         LAG(amount, 1, 0) OVER (ORDER BY sale_date) AS previous_sale_amount
  FROM sales;
  ```

- **Result**:

  | sale_id | sale_date  | amount | previous_sale_amount |
  |---------|------------|--------|----------------------|
  | 1       | 2024-01-01 | 100    | 0                    |
  | 2       | 2024-01-02 | 150    | 100                  |
  | 3       | 2024-01-03 | 200    | 150                  |
  | 4       | 2024-01-04 | 250    | 200                  |

---

Here’s the content organized without using numbers:

---

### What is a View?

A view in SQL is a virtual table based on the result-set of an SQL statement. A view contains rows and columns, just like a real table. The fields in a view are fields from one or more real tables in the database.

---

### Can We Create a View Based on Another View?

Yes, this is known as **nested views**. However, it is advisable to avoid nesting multiple views as the code can become difficult to read and debug.

---

### Can We Still Use a View if the Original Table Is Deleted?

No, any views based on that table will become invalid after deleting the base table. If we attempt to use such a view, we will receive an error message.

---

### What Types of SQL Relationships Do You Know?

- **One-to-One**: Each record in one table corresponds to only one record in another table.
- **One-to-Many & Many-to-One**: Each record in one table corresponds to several records in another table.
- **Many-to-Many**: Each record in both tables corresponds to several records in another table.
- **Self-Referencing Relationships:** This is used when a table needs to define a relationship with itself.

### What are Entities and Relationships?

- **Entity:** An entity can be a real-world object, either tangible or intangible, that can be easily identifiable. For example, in a college database, students, professors, workers, departments, and projects can be referred to as entities. Each entity has some associated properties that provide it an identity.

- Relationships: Relations or links between entities that have something to do with each other. For example - The employee's table in a company's database can be associated with the salary table in the same database

---

### What Are the Possible Values of a BOOLEAN Data Field?

In some SQL flavors, such as PostgreSQL, the BOOLEAN data type explicitly exists and takes values **TRUE**, **FALSE**, or **NULL**. In other flavors, such as Microsoft SQL Server, the **BIT** datatype is used to store Boolean values as integers 1 (true) or 0 (false).

---

### What Is the CASE() Function?

The **CASE()** function implements if-then-else logic in SQL. It sequentially checks the provided conditions in the **WHEN** clauses and returns the value from the corresponding **THEN** clause when the first condition is satisfied. If none of the conditions are satisfied, the function returns the value from the **ELSE** clause if provided; otherwise, it returns **NULL**.

**Syntax:**

```sql
CASE
    WHEN condition_1 THEN value_1
    WHEN condition_2 THEN value_2
    WHEN condition_3 THEN value_3
    ...
    ELSE value
END;
```

---

### What Is the Difference Between the DELETE and TRUNCATE Statements?

- **DELETE** is a reversible DML (Data Manipulation Language) command used to delete one or more rows from a table based on the conditions specified in the **WHERE** clause.
- **TRUNCATE** is an irreversible DDL (Data Definition Language) command used to delete all rows from a table.
- **DELETE** works slower than **TRUNCATE** and cannot be used on a table containing a foreign key.

### What Is the Difference Between the DROP and TRUNCATE Statements?

- **DROP** deletes a table from the database completely, including the table structure, all associated constraints, relationships with other tables, and access privileges.
- **TRUNCATE** deletes all rows from a table without affecting the table structure and constraints.
- **DROP** works slower than **TRUNCATE**. Both are irreversible DDL commands.

---

### How Do You Add a Record to a Table?

Using the **INSERT INTO** statement in combination with **VALUES**.

**Syntax:**

```sql
INSERT INTO table_name
VALUES (value_1, value_2, ...);
```

---

### How to Delete a Record from a Table?

Using the **DELETE** statement.

**Syntax:**

```sql
DELETE FROM table_name
WHERE condition;
```

This syntax can also delete multiple records if they satisfy the provided condition.

---

### How to Add a Column to a Table?

Using the **ALTER TABLE** statement in combination with **ADD**.

**Syntax:**

```sql
ALTER TABLE table_name
ADD column_name datatype;
```

---

### How to Rename a Column of a Table?

Using the **ALTER TABLE** statement in combination with **RENAME COLUMN ... TO ...**.

**Syntax:**

```sql
ALTER TABLE table_name
RENAME COLUMN old_column_name TO new_column_name;
```

---

### How to Delete a Column from a Table?

Using the **ALTER TABLE** statement in combination with **DROP COLUMN**.

**Syntax:**

```sql
ALTER TABLE table_name
DROP COLUMN column_name;
```

---

### How to Select All Even or All Odd Records in a Table?

By checking the remainder of the division by 2. In some SQL versions (e.g., PostgreSQL and MySQL), we use the **MOD** function; in others (Microsoft SQL Server and SQLite), we use the modulo operator (%).

**To select all even records using MOD:**

```sql
SELECT * FROM table_name
WHERE MOD(ID_column, 2) = 0;
```

**To select all even records using %:**

```sql
SELECT * FROM table_name 
WHERE ID_column % 2 = 0;
```

To select all odd records, the syntax is identical, except we would use the inequality operator `<>` instead of `=`.

### How to Prevent Duplicate Records When Making a Query?

Using the **DISTINCT** statement in combination with **SELECT** or creating a unique key for that table.

---

### How to Find the nth Highest Value in a Column of a Table?

Using the **OFFSET** clause. For example, to find the 6th highest value from a column, we would use the following syntax:

```sql
SELECT * FROM table_name
ORDER BY column_name DESC
LIMIT 1
OFFSET 5;
```

---

### How to Find the Values in a Text Column of a Table That Start with a Certain Letter?

Using the **LIKE** operator in combination with the `%` and `_` wildcards. For example, to find all surnames in a table that start with "A":

```sql
SELECT * FROM table_name
WHERE surname LIKE 'A%';
```

---

### How to Find the Last ID in a Table?

Using the **MAX()** function or ordering the IDs.

**Using MAX():**

```sql
SELECT MAX(id) AS last_id
FROM table_name;
```

---

**Or using order by:**

```sql
SELECT id
FROM table_name
ORDER BY id DESC
LIMIT 1;
```

In Microsoft SQL Server:

```sql
SELECT TOP 1 id
FROM table_name
ORDER BY id DESC;
```

---

### How to Select Random Rows from a Table?

Using the **RAND()** function in combination with **ORDER BY** and **LIMIT**. In some SQL flavors, such as PostgreSQL, it’s called **RANDOM()**.

**For MySQL:**

```sql
SELECT * FROM table_name
ORDER BY RAND()
LIMIT 5;
```

---

### What is the First Normal Form (1NF)?

For any relation to be in the first normal form (1NF), the relation should not contain any composite or multi-valued attribute. So a relation will be in first normal form if it contains atomic values. The relation should contain only a single-valued attribute.

| Roll Number | Student Name | Marks |
|-------------|--------------|-------|
| 1           | Abhay        | 96    |
| 2           | Amit         | 78    |
| 3           | Ayushi       | 86    |

### What is the Second Normal Form (2NF)?

So any relation which contains a single attribute primary key is always in 2NF (second normal form). Thus the relation which contains a composite primary key in order to be in 2NF should not contain any partial dependency.

### Difference Between 1NF and 2NF

| 1NF                                                                                  | 2NF                                                                                                         |
|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| In order to be in 1NF, any relation must be atomic and should not contain any composite or multi-valued attributes. | In order to be in 2NF, any relation must be in 1NF and should not contain any partial dependency.           |
| The identification of functional dependency is not necessary for first normal form.   | The identification of functional dependency is necessary for second normal form.                            |
| First Normal form only deals with the schema of the table and it does not handle the update anomalies. | Second normal form handles the update anomalies.                                                            |
| A relation in 1NF may or may not be in 2NF.                                          | A relation in 2NF is always in 1NF.                                                                         |
| The primary key in case of first normal form can be a composite key.                 | The primary key in case of second normal form cannot be a composite key if it leads to partial dependency.  |
| The main goal of first normal form is to eliminate the redundant data within the table. | The main goal of second normal form is to ensure data dependencies.                                        |
| The first normal form is less strong than the second normal form.                    | The second normal form is comparatively stronger than the first normal form.                                 |

### SQL-Server Views

**`Create View`**

To create a view, you use the CREATE VIEW statement. This allows you to define a virtual table based on a SELECT query.

```sql
CREATE VIEW view_name AS
SELECT column1, column2
FROM table_name
WHERE condition;
```

**`Alter View`**

If you need to modify an existing view, you use the ALTER VIEW statement. This allows you to change the definition of the view without dropping it.

```sql
ALTER VIEW view_name AS
SELECT column1, column2, column3
FROM table_name
WHERE new_condition;
```

**`Drop View`**

To remove a view, you use the DROP VIEW statement. This deletes the view from the database.

```sql
DROP VIEW view_name;
```

### SQL-Server Cursor

A database cursor is a control structure that allows for the traversal of records in a database. Cursors, in addition, facilitates processing a er traversal, such as retrieval, addition, and deletion of database records. They can be viewed as a pointer to one row in a set of rows.

**`Declare a Cursor`**

DECLARE a cursor a er any variable declaration. The cursor declaration must always be associated with a SELECT Statement.

```sql
DECLARE cursor_name CURSOR FOR
SELECT column1, column2
FROM table_name
WHERE condition;
```

**`Opening a Cursor`**

Open cursor to initialize the result set. The OPEN statement must be called before fetching rows from the result set.

```sql
OPEN cursor_name;
```

**`Fetching Data from a Cursor`**

FETCH statement to retrieve and move to the next row in the result set.

```sql
FETCH NEXT FROM cursor_name INTO @variable1, @variable2;
```

**`Looping Through a Cursor`**

You can loop through the result set using a `WHILE` loop.

```sql
WHILE @@FETCH_STATUS = 0
BEGIN
    FETCH NEXT FROM cursor_name INTO @variable1, @variable2;
    -- Perform operations on the fetched data
END;
```

### SQL-Server Control flow Statements

**`SQL Server IF ELSE Statement`**

The IF...ELSE statement is used to execute a block of SQL code based on a condition.

```sql
IF condition
BEGIN
    -- SQL statements if condition is true
END
ELSE
BEGIN
    -- SQL statements if condition is false
END;
```

**`SQL Server WHILE Loop`**

The WHILE loop is used to repeatedly execute a block of SQL code as long as a condition is true.

```sql
WHILE condition
BEGIN
    -- SQL statements to execute repeatedly
END;
```

**`SQL Server BREAK`**

The BREAK statement is used to exit a WHILE loop prematurely.

```sql
WHILE condition
BEGIN
    IF exit_condition
    BEGIN
        BREAK;
    END;
    -- SQL statements to execute repeatedly
END;
```

**`SQL Server CONTINUE`**

The CONTINUE statement is used to skip the rest of the current iteration of a WHILE loop and start the next iteration.

```sql
WHILE condition
BEGIN
    IF skip_condition
    BEGIN
        CONTINUE;
    END;
    -- SQL statements to execute repeatedly
END;
```
