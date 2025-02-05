# MongoDB Basic Topics

## Table of Contents

1. [Introduction to MongoDB](#introduction-to-mongodb)

2. [MongoDB Installation and Setup](#mongodb-installation-and-setup)

3. [Data Modeling and Schema Design](#data-modeling-and-schema-design)

4. [CRUD Operations (Create, Read, Update, Delete)](#crud-operations-(create,-read,-update,-delete))

5. [Indexes and Basic Querying](#indexes-and-basic-querying)

6. [Aggregation Framework Overview](#aggregation-framework-overview)

7. [Data Import and Export](#data-import-and-export)

## Introduction to MongoDB

### 1. What is MongoDB, and how is it different from traditional SQL databases?

MongoDB is a NoSQL, document-oriented database that stores data in flexible, JSON-like documents called BSON. Unlike traditional SQL databases that use tables and rows to store data in a structured format, MongoDB is schema-less and allows for variable document structures within a collection. This flexibility is ideal for applications with evolving data models. Additionally, MongoDB supports horizontal scaling with features like sharding, while SQL databases usually rely on vertical scaling.

### 2. Explain the difference between a MongoDB collection and a document

In MongoDB, a collection is similar to a table in a relational database, serving as a container for documents. A document is the basic unit of data within a collection, equivalent to a row in SQL databases. Each document is a JSON-like structure with key-value pairs and can contFain nested arrays and objects, allowing for more complex data representations than a relational database row.

### 3. What is a replica set in MongoDB, and why is it important?

A replica set in MongoDB is a group of MongoDB servers that maintain the same data, providing redundancy and high availability. A replica set consists of a primary node and one or more secondary nodes. The primary node accepts write operations, while secondary nodes replicate data from the primary. If the primary node fails, one of the secondaries can be automatically elected to become the new primary. This setup ensures that data is always available, even in the case of hardware or network failures.

### 4. Describe sharding in MongoDB and its use case

Sharding is MongoDB’s way of distributing data across multiple servers, or shards, to manage large datasets and high request rates. Each shard contains a subset of the data. MongoDB uses a sharding key to distribute documents across shards evenly. This approach allows for horizontal scaling, where additional shards can be added as data grows. Sharding is essential for applications with high data volumes, as it reduces the load on any single server, thus improving performance and availability.

### 5. Write a MongoDB query to find all documents in a users collection where the user's age is greater than 30

```javascript
db.users.find({ age: { $gt: 30 } });
```

### 6. Write a query to update all documents in the products collection, setting the inStock field to true where the quantity is greater than 0

```javascript
db.products.updateMany(
  { quantity: { $gt: 0 } },
  { $set: { inStock: true } }
);
```

### 7. Write a MongoDB aggregation pipeline to find the average age of users grouped by city in the users collection

```javascript
db.users.aggregate([
  { $group: { _id: "$city", averageAge: { $avg: "$age" } } }
]);
```

### 8. Write a query to delete all documents in the orders collection where the status is "cancelled"

```javascript
db.orders.deleteMany({ status: "cancelled" });
```

### 9. Write a query to insert multiple documents into a students collection, including the fields name, age, and grade

```javascript
db.students.insertMany([
  { name: "Alice", age: 20, grade: "A" },
  { name: "Bob", age: 22, grade: "B" },
  { name: "Charlie", age: 23, grade: "A" }
]);
```

### 10 Why mongoDB?

MongoDB is a popular NoSQL database for modern applications, especially when you need flexibility, scalability, and performance with data that may not fit neatly into a traditional relational database schema

### 11. Have you used Atlas Service?

I’m familiar with the general concept of Atlas Service, but it would help to know which specific Atlas Service you’re referring to. There are several services and products named "Atlas" across different industries:

- **MongoDB Atlas** - A popular cloud database service for MongoDB.
- **AWS Atlas Service** - Occasionally used to refer to mapping or geospatial services on Amazon Web Services.
- **Atlassian Atlas** - A project and goal tracking tool, part of Atlassian’s suite for team collaboration.
- **Healthcare Atlas Services** - Used in healthcare or biomedical fields for data analysis and research.

### 12. What is the difference between Enterprise and community version of MongoDB?

**`Community Edition:`**

- `License:` Open-source under the Server Side Public License (SSPL).

- `Cost:` Free to use.

- `Support:` Community-driven support through forums and online resources.

- `Features:` Includes essential database management features like document storage, queries, indexing, aggregation, and basic sharding.

- `Use Cases:` Ideal for development, testing, and small-scale production applications.

**`Enterprise Edition:`**

- `License:` Commercial license with proprietary features.

- `Cost:` Requires a paid subscription.

- `Support:` Official support from MongoDB, Inc., with access to dedicated support teams and enterprise-level service level agreements (SLAs).

- `Features:` Offers advanced security features (Kerberos authentication, LDAP integration, auditing), data encryption, advanced management tools, and increased scalability.

- `Compliance:` Provides features that assist with regulatory compliance, including auditing and monitoring tools.

- `Use Cases:` Targeted at larger organizations that require robust support, advanced security features, compliance with regulations, and high availability for mission-critical applications.

### 13. Have you worked with in premises or cloud hosting of MongoDB?

**`On-Premises Hosting`**

- `Control:` Full control over hardware, software, and security configurations.

- `Customization:` Tailor the environment to specific needs and compliance requirements.

- `Cost:` Higher upfront costs for hardware and ongoing maintenance.

- `Scalability:` Requires planning and investment to scale.

**`Cloud Hosting`**

- `Flexibility:` Easily scalable with pay-as-you-go pricing models.

- `Maintenance:` Managed services reduce the burden of maintenance and updates.

- `Availability:` High availability and disaster recovery options.

- `Integration:` Seamless integration with other cloud services.

### 14. What are the most powerful features of MongoDB?

MongoDB is a powerful NoSQL database that provides a range of features designed to support modern application development. Its flexibility, scalability, and performance make it suitable for various use cases, from small projects to large enterprise applications.

### 15. Have you used Stitch MongoDB Service?

MongoDB Stitch, now known as MongoDB Realm, is a serverless application platform that allows developers to build applications quickly and easily by integrating various services and managing their MongoDB databases.

### 16. What are the Best practices in MongoDB ?

Implementing best practices in MongoDB can significantly enhance the performance, scalability, security, and maintainability of your applications.

### 17. Can MongoDB and Redis work together?

Yes, MongoDB and Redis can work together, and they are often used in tandem to take advantage of their complementary strengths. While MongoDB is a powerful NoSQL database that excels in storing large amounts of semi-structured data, Redis is an in-memory data store known for its ultra-fast read and write capabilities, making it ideal for caching and real-time applications.

### 18. How will you create a Database? and What are the considerations before creating a database?

Creating a database in MongoDB is straightforward and can be done through the MongoDB shell, a programming language driver, or GUI tools.

**1. Connect to MongoDB:** First, you need to start your MongoDB server and connect to it using the MongoDB shell. You can do this by running:

```bash
mongo
```

**2. Switch to or Create a Database:** Use the use command to switch to a database. If the database does not exist, MongoDB will create it when you first store data in it.

```javascript
use myDatabase
```

Replace myDatabase with your desired database name.

**3. Create Collections:** Once you are in the desired database, you can create collections. Collections are similar to tables in relational databases.

```javascript
db.createCollection("myCollection")
```

Again, replace `myCollection` with your desired collection name. Alternatively, collections are created automatically when you insert the first document.

**4. Insert Data:** After creating a collection, you can insert documents into it.

```javascript
db.myCollection.insertOne({ name: "Alice", age: 30 })
```

**Considerations Before Creating a Database**
Before creating a database in MongoDB, consider the following factors:

**1. `Database Design:`**

- `Data Model:` Understand the data structure and how documents will relate to one another. Consider whether to use embedded documents or references, and plan your collections accordingly.

- `Schema Design:` Although MongoDB is schema-less, having a schema design in mind helps maintain consistency and eases querying.

**2. `Indexes:`**

- `Performance:` Plan your indexes to optimize query performance. Indexes can significantly speed up read operations but may slow down writes. Consider which fields will be frequently queried.

- `Compound Indexes:` If you anticipate complex queries, consider creating compound indexes that involve multiple fields.

**3. `Scalability:`**

- `Sharding:` If you expect high data volumes or traffic, plan for sharding (horizontal scaling) from the beginning. Identify sharding keys that will help distribute data evenly across shards.

**4. `Access Control:`**

- `User Roles and Permissions:` Determine how you will manage users and permissions. Use MongoDB’s built-in role-based access control (RBAC) to restrict access to sensitive data.

**5. `Backup and Recovery:`**

- `Data Backup:` Establish a backup strategy to prevent data loss. Consider using MongoDB’s built-in backup tools or third-party solutions.
Disaster Recovery: Plan for disaster recovery and ensure that you can restore data in case of failure.

**6. `Performance Monitoring:`**

- `Monitoring Tools:` Use tools like MongoDB Atlas, MongoDB Cloud Manager, or other monitoring solutions to track performance metrics and optimize the database as necessary.

**7. `Compliance and Security:`**

- `Data Encryption:` Consider encrypting sensitive data at rest and in transit. Use MongoDB's Encrypted Storage Engine if necessary.

- `Compliance Requirements:` Understand any regulatory requirements regarding data storage and privacy that may impact how you design your database.

**8. `Environment:`**

- `Development vs. Production:` Separate your development and production environments. Use different databases for testing, development, and production to avoid accidental data loss or corruption.

### 19. How will you create a Collection? and What are the considerations before creating a database?

Creating a collection in MongoDB is a straightforward process, similar to creating a database. Collections are analogous to tables in relational databases and are used to store documents (records) within a database.

**1. Connect to MongoDB:** Start the MongoDB shell by running:

```bash
mongo
```

**2. Switch to the Desired Database:** Use the `use` command to switch to the database where you want to create the collection. If the database does not exist, MongoDB will create it when you first add data.

```javascript
use myDatabase
```

**3. Create a Collection:** o create a collection explicitly, you can use the `createCollection()` method:

```javascript
db.createCollection("myCollection")
```

Replace "myCollection" with your desired collection name.

Alternatively, you can create a collection implicitly by inserting a document into it

```javascript
db.myCollection.insertOne({ name: "Alice", age: 30 })
```

**Considerations Before Creating a Database**
Before creating a database in MongoDB, consider the following factors:

**1. `Data Model Design:`**

- `Document Structure:` Define the structure of the documents that will be stored in the collection. Decide whether to use a flat structure or nested documents based on your application's requirements.

- `Schema Design:` While MongoDB is schema-less, having a planned schema helps in maintaining consistency and optimizing queries.

**2. `Indexes:`**

- `Indexing Strategy:` Plan how you will index the collection to optimize query performance. Determine which fields will be frequently queried and consider creating appropriate indexes.

- `Compound Indexes:` If your queries often involve multiple fields, consider creating compound indexes to enhance performance.

**3. `Data Size and Growth:`**

- `Anticipated Size:` Consider the expected size of the collection and its growth over time. This can help inform decisions about sharding (distributing data across multiple servers) and indexing.

- `Document Size:` Keep in mind the BSON document size limit of 16 MB when designing your documents.

**4. `Access Patterns:`**

- `Query Patterns:` Understand how your application will access the data. Identify common query patterns to ensure the collection and its indexes are optimized for those access patterns.

- `Read vs. Write:` Determine if your application will be read-heavy or write-heavy, as this may influence how you design your collection and indexes.

**5. `Collection Naming:`**

- `Naming Conventions:` Use meaningful and consistent naming conventions for your collections. This makes it easier for developers to understand the purpose of each collection.

- `Avoid Reserved Words:` Avoid using MongoDB reserved words or special characters in collection names to prevent potential issues.

**6. `Sharding and Scalability:`**

- `Future Scalability:` If you anticipate the need to scale out your database, consider how to shard your collections effectively. Identify potential shard keys that will distribute data evenly.

**7. `Backup and Recovery:`**

- `Backup Strategy:` Establish a backup plan for your collection to ensure data can be restored in case of loss or corruption.

- `Disaster Recovery:` Plan for disaster recovery and how you will handle data restoration.

**8. `Performance Monitoring:`**

- `Monitoring Tools:` Use monitoring tools to track performance metrics and identify bottlenecks. This helps in optimizing collections and indexes over time.

**9. Compliance and Security:**

- `Data Security:` Consider any necessary security measures, including user authentication and authorization, to control access to the collection.

- `Compliance Requirements:` Ensure that your data handling practices comply with relevant regulations and standards, especially if you are working with sensitive data.

### 20. What is Vertical and Horizontal scaling?

| Feature             | Vertical Scaling (Scaling Up)                      | Horizontal Scaling (Scaling Out)               |
|---------------------|---------------------------------------------------|------------------------------------------------|
| Definition          | Adding resources to a single server               | Adding more servers to distribute load         |
| Implementation      | Upgrading hardware on one machine                  | Deploying multiple machines and load balancing  |
| Cost                | Can be expensive; limited by hardware prices      | Often more cost-effective; allows gradual scaling |
| Performance Limits  | Limited by the maximum capacity of the server     | Greater potential for scaling indefinitely      |
| Complexity          | Easier to manage; single instance                  | More complex due to multiple instances          |
| Fault Tolerance     | Single point of failure                            | Higher availability with redundancy             |

### 21.  What are some of the advantages of MongoDB?

Some advantages of MongoDB are as follows:

- MongoDB supports field, range-based, string pattern matching type queries. for

- searching the data in the database 
MongoDB support primary and secondary index on any fields

- MongoDB basically uses JavaScript objects in place of procedures

- MongoDB uses a dynamic database schema

- MongoDB is very easy to scale up or down

- MongoDB has inbuilt support for data partitioning (Sharding).

## MongoDB Installation and Setup

### 1. What is MongoDB, and why would you choose it over relational databases?

MongoDB is a NoSQL document-oriented database that stores data in flexible, JSON-like documents instead of rigid tables. It’s well-suited for applications that require scalability, fast performance, and flexibility in data structure, as it allows for a schema-less design. MongoDB is a good choice over relational databases when dealing with large amounts of unstructured data, as it can easily scale horizontally with features like sharding, which divides data across multiple servers. Additionally, MongoDB’s query language is highly expressive and supports complex queries, aggregation, and indexing.

### 2. Explain the structure of a MongoDB document

A MongoDB document is a JSON-like structure composed of key-value pairs. Each document represents a record in a collection and can have fields with different data types, including strings, numbers, arrays, and even nested documents. Documents in a collection don’t have to adhere to a strict schema, meaning each document can have a unique structure. However, documents in the same collection are typically related, so they often share similar fields.

### 3. What is a replica set in MongoDB,and why is it important?

A replica set in MongoDB is a group of MongoDB servers that maintain the same data, providing redundancy and high availability. A replica set typically includes a primary server that handles client operations and secondary servers that replicate the data from the primary. If the primary server fails, a secondary can automatically take over as the new primary, minimizing downtime. This setup is crucial in production environments to ensure data availability and durability.

### 4. How does MongoDB handle transactions?

MongoDB supports multi-document transactions to ensure data consistency, similar to transactions in relational databases. In a transaction, multiple read and write operations are grouped together, and either all succeed, or none are applied (atomicity). Transactions in MongoDB follow ACID properties within a single replica set, and starting with MongoDB 4.2, they can also span multiple shards in a sharded cluster. Transactions can be started using session.`startTransaction()` and are typically committed with `session.commitTransaction()` or aborted with `session.abortTransaction()`.

### 5. Write a MongoDB query to retrieve all documents from a collection named employees where the employee has a "salary" field greater than 50,000 and is working in the "Sales" department. The results should be sorted by the "salary" field in descending order

Sample Document Structure in `employees` Collection:

```json
{
  "name": "Alice",
  "salary": 60000,
  "department": "Sales",
  "hireDate": "2022-03-12"
}
```

**Answer:**

```javascript
db.employees.find(
  { 
    salary: { $gt: 50000 }, 
    department: "Sales" 
  }
).sort({ salary: -1 })
```

### 6. You need to update all documents in the employees collection where the department is "Engineering". Increase each employee's salary in that department by 10%

```javascript
db.employees.updateMany(
  { department: "Engineering" },
  { $mul: { salary: 1.1 } }
)
```

### 7. What are the validation levels in Mongodb?

MongoDB provides two levels of validation for documents: strict and moderate

### 8. Does MongoDB supports Views?

Yes, MongoDB does support views. Views in MongoDB are similar to views in relational databases. They allow you to create a virtual collection based on the results of a query.

### 9. How to create views in MongoDB?

Creating views in MongoDB is straightforward and can be done using the db.createView() method. Views are read-only and are defined using the MongoDB aggregation framework.

### 10. What's the GUI client you used and What are its frequently used features?

One popular GUI client for MongoDB that many developers use is MongoDB Compass. It's an official tool provided by MongoDB, Inc., and offers a user-friendly interface to interact with MongoDB databases. There are also other GUI clients, such as Studio 3T, Robo 3T, and NoSQLBooster.

- Schema Exploration and Data Visualization: Schema explorers help understand the structure of collections.

- Aggregation and Query Builders: Useful for building complex queries and pipelines without needing command-line proficiency.

- CRUD Operations and Index Management: Basic yet essential for managing data and improving query performance.

- Performance Monitoring and Statistics: Real-time metrics help users monitor MongoDB’s resource usage and health.

- SQL Support (in some clients): SQL query translation or direct SQL querying capabilities make MongoDB more accessible for users with SQL backgrounds.

### 11. How can you lock a Database in MongoDB?

In MongoDB, you can lock a database using the `fsync` command with the `lock` option. This is typically used for maintenance tasks, such as backups, where you need to ensure that no write operations occur during the process.

```js
// Lock the database
db.fsyncLock()

// Perform your maintenance tasks here

// Unlock the database
db.fsyncUnlock()
```

### 12. What is BSONdump?

`bsondump` is a utility provided by MongoDB that converts BSON (Binary JSON) files into a readable JSON or Extended JSON format. BSON is the binary encoding format MongoDB uses to store documents and make data retrieval and storage faster. However, BSON files are not human-readable, so `bsondump` is used to translate BSON data files into JSON format, making it easier to review, debug, or transfer data.

### 13. What is a Document in MongoDB?

A Document in MongoDB is an ordered set of keys with associated values. It is represented by a map, hash, or dictionary. In JavaScript, documents are represented as objects:

```mongodb
{"greeting" : "Hello world!"}
```

Complex documents will contain multiple key/value pairs:

```db
 {"greeting" : "Hello world!", "views" : 3}
```

## Data Modeling and Schema Design

### 1. What is the difference between embedded documents and referencing documents in MongoDB, and when would you use each approach?

- **Embedded Documents:** Store related data in a single document, useful when data is typically accessed together. For example, a user profile document with an embedded address object is suitable if the address is rarely accessed independently.

- **References:** Store data in separate collections and use references (usually the `_id` of another document) to link them. This is preferred for complex, reusable relationships or if the related data is large. For instance, storing user IDs in an orders collection allows multiple orders to reference a single user without redundancy.

`When to use:`

- Use embedding for one-to-few relationships, where related data is mostly read together (e.g., user and address).

- Use references for one-to-many or many-to-many relationships, or when data needs to be shared across multiple documents (e.g., users and roles).

### 2. Explain how sharding works in MongoDB and when you would consider implementing it

- Sharding is MongoDB’s approach to distributing data across multiple servers to support large datasets and high-throughput operations. It works by dividing data across shards based on a chosen shard key, which evenly distributes data to balance the load and improve performance.

- Sharding is appropriate when a single server cannot handle the storage requirements or when query/transaction load is very high, as it enables horizontal scaling.

`When to implement:`

- When the dataset size approaches a single machine's capacity or read/write operations per second exceed its capability.

- If query performance drops significantly due to high data volume and indexing alone doesn’t resolve it.

### 3. Describe the MongoDB aggregation framework and its use cases

- The aggregation framework in MongoDB is a powerful tool to perform data processing and transformation within the database. It provides operations like `$match`, `$group`, `$sort`, `$lookup`, and `$project`, allowing for complex data manipulations similar to SQL’s GROUP BY, JOIN, etc.

- Use cases: Suitable for reporting and data analytics, generating summary reports, calculating averages, totals, and finding trends within the data.

### 4. Write a MongoDB query to find the top 5 most expensive products in a `products` collection and return only the `name` and `price` fields for each

`Collection Structure (products):`

```json
{
   "_id": ObjectId("..."),
   "name": "Laptop",
   "category": "Electronics",
   "price": 1200,
   "stock": 30
}
```

**Answer:**

```javascript
db.products.aggregate([
    { $sort: { price: -1 } },
    { $limit: 5 },
    { $project: { _id: 0, name: 1, price: 1 } }
]);
```

### 5. Write a query to update the stock quantity of a product by a given amount, but only if the stock quantity is greater than zero

```javascript
db.products.updateOne(
    { _id: ObjectId("..."), stock: { $gt: 0 } },
    { $inc: { stock: -5 } }
);
```

### 6. Whats is the alternative for $in operator?

In MongoDB, the `$in` operator is used to match documents where the value of a field is equal to any value in a specified array. While `$in` is a powerful and frequently used operator, there are alternatives that can achieve similar functionality, depending on the context of the query

### 7. What does $unset does?

In MongoDB, the `$unset` operator is used to remove a specific field from a document. When you apply `$unset` to a field, that field will be deleted from the document entirely, which means that it will no longer be present in the document's structure.

```js
db.collection.update(
   { <query> },
   { $unset: { <field1>: "", <field2>: "" } }
)
```

### 8.How will you get the current date in mongodb? $currentDate

In MongoDB, you can get the current date using the `$currentDate` operator, which is particularly useful within update operations. The `$currentDate` operator allows you to set a field to the current date or timestamp during an update operation. This is often used to track when documents are created or modified.

```js
db.collection.update(
   { <query> },
   { $currentDate: { <field>: true | { $type: "date" | "timestamp" } } } }
)
```

### 9. What does the difference between update and upsert?

| Aspect                       | Update                                                                | Upsert                                                               |
|------------------------------|-----------------------------------------------------------------------|----------------------------------------------------------------------|
| Purpose                      | Modify existing documents only.                                       | Modify existing documents or insert new ones if none match.        |
| Effect on Non-Matching Documents | No action taken if no documents match.                              | Inserts a new document if no matching documents exist.              |
| Use Case                     | When you want to change values in existing documents without creating new ones. | When you want to ensure that a document is present with certain values, creating it if necessary. |
| Performance                  | Generally faster if you are certain the document exists.             | May incur additional overhead due to the possibility of insertion.  |

### 10. How will you append a Value to an Array? $push

In MongoDB, you can append a value to an array using the `$push` operator. This operator allows you to add one or more elements to the end of an existing array field within a document. If the specified field is not an array, MongoDB will create a new array containing the value.

```js
db.collection.update(
   { <query> },                     // Query to select the document(s) to update
   { $push: { <arrayField>: <value> } }  // Update operation to append the value
)
```

### 11. What does $addToSet does?

In MongoDB, the $addToSet operator is used to add a value to an array only if that value does not already exist in the array.

```js
db.collection.update(
   { <query> },                          // Query to select the document(s) to update
   { $addToSet: { <arrayField>: <value> } }  // Operation to add the value to the array
)
```

### 12. What's the difference between $pull and $pullall?

| Feature    | $pull                                                | $pullAll                                   |
|------------|-----------------------------------------------------|--------------------------------------------|
| Purpose    | Removes all instances of a specific value or values matching a condition. | Removes multiple specified values from an array. |
| Input      | Takes a single value or a condition.                | Takes an array of values to be removed.   |
| Use Case   | Use when you need to remove a specific element (or elements matching a query). | Use when you want to remove multiple elements in one operation. |

- **$pull**

```js
db.collection.update(
   { <query> },                      // Query to select the document(s) to update
   { $pull: { <arrayField>: <value> } }  // Remove elements matching the value
)
```

- **$pullAll**

```js
db.collection.update(
   { <query> },                           // Query to select the document(s) to update
   { $pullAll: { <arrayField>: [<value1>, <value2>, ...] } }  // Remove multiple values
)
```

### 13. How will you upload images into mongodb? explain the architecture

Uploading images into MongoDB typically involves using the GridFS specification, which is designed for storing and retrieving files that exceed the BSON-document size limit of 16 MB. GridFS splits files into smaller chunks and stores each chunk as a separate document. This makes it suitable for handling large files, such as images, videos, and other types of binary data.

**Architecture of GridFS:**

GridFS is built on top of MongoDB and utilizes two main collections to manage files:

- `fs.files:` This collection stores metadata about the files. Each document in this collection contains information such as the filename, upload date, file length, and a unique identifier (the ObjectId).

- `fs.chunks:` This collection stores the actual binary data. Each document in this collection contains a chunk of the file, along with a reference to the file it belongs to (using the file's ObjectId) and the chunk's sequence number.

### 14. What are the storage engines used by MongoDB?

MongoDB supports several storage engines, each designed for different use cases and providing various features for data management, performance, and reliability. The choice of storage engine can significantly impact the performance and behavior of a MongoDB deployment.

### 15. What is ObjectId?

- **Unique Identifier:** An `ObjectId` is a 12-byte identifier that is generated by MongoDB to uniquely identify documents within a collection.

- **Default _id Field:** When you insert a document into a MongoDB collection without specifying an `_id` field, MongoDB automatically creates an `ObjectId` for that field.

### 16. What are the alternatives to MongoDB?

MongoDB is a popular NoSQL database known for its flexibility, scalability, and ease of use. However, there are several alternatives available, each with its own strengths and suitable use cases.

## CRUD Operations (Create, Read, Update, Delete)

### 1. What is MongoDB, and how does it differ from traditional relational databases?

MongoDB is a NoSQL database that stores data in flexible, JSON-like documents (BSON). Unlike traditional relational databases that use tables and fixed schemas, MongoDB allows for dynamic schemas, meaning documents in the same collection can have different structures. This flexibility supports unstructured data and enables rapid development and scaling.

### 2. Explain the CRUD operations in MongoDB

CRUD operations in MongoDB refer to the four basic functions:

- **Create:** Insert new documents into a collection.

- **Read:** Retrieve documents from a collection.

- **Update:** Modify existing documents in a collection.

- **Delete:** Remove documents from a collection.

### 3. How do you insert a document in MongoDB? Can you provide an example?

You can insert a document using the `insertOne()` or`insertMany()` methods.

`Example:`

```javascript
db.users.insertOne({ name: "Alice", age: 25, city: "New York" });
```

### 4. What method would you use to find all documents in a collection?

You can use the `find()` method to retrieve all documents in a collection. If you want all documents without any filter, you can call `find()` without any arguments:

```javascript
db.collectionName.find();
```

### 5. How can you update multiple documents in a MongoDB collection?

You can use the updateMany() method to update multiple documents that match a specified filter.

`Example:`

```javascript
db.users.updateMany({ city: "New York" }, { $set: { state: "NY" } });
```

### 6. Explain the difference between `updateOne()` and `updateMany()`

- **updateOne():** Updates the first document that matches the specified filter.

- **updateMany():** Updates all documents that match the specified filter. If no documents match, no updates occur.

### 7. What is the purpose of the `$set` operator in an update operation?

The `$set` operator is used to specify the fields to update and their new values. It does not replace the entire document; it only modifies the specified fields. For example:

```javascript
db.users.updateOne({ name: "Alice" }, { $set: { age: 26 } });
```

### 8. How can you delete a single document from a collection?

You can use the deleteOne() method to remove the first document that matches a specified filter.

`Example:`

```javascript
db.users.deleteOne({ name: "Alice" });
```

### 9. What is a MongoDB index, and why is it important?

A MongoDB index is a data structure that improves the speed of data retrieval operations on a collection. Indexes are crucial for optimizing query performance, as they allow MongoDB to find documents more quickly rather than scanning every document in a collection.

### 10. Can you explain how to use projections in a read operation?

Projections in MongoDB are used to specify which fields to include or exclude in the returned documents. You can use projections in the find() method as follows:

```javascript
db.users.find({}, { name: 1, age: 1 }); // Returns only the name and age fields of all documents
```

### 11. Write a Node.js function to connect to a MongoDB database, insert a new user document, retrieve all users, update a user's age based on their name, and then delete that user. Provide the complete code

```javascript
const { MongoClient } = require("mongodb");

async function performCRUDOperations() {
  const uri = "mongodb://localhost:27017"; // MongoDB connection string
  const client = new MongoClient(uri);

  try {
    await client.connect();
    const db = client.db("myDatabase");
    const usersCollection = db.collection("users");

    // Create: Insert a new user
    const newUser = { name: "Alice", age: 25, city: "New York" };
    const insertResult = await usersCollection.insertOne(newUser);
    console.log(`New user inserted with id: ${insertResult.insertedId}`);

    // Read: Retrieve all users
    const users = await usersCollection.find().toArray();
    console.log("All users:", users);

    // Update: Update user's age
    await usersCollection.updateOne(
      { name: "Alice" },
      { $set: { age: 26 } }
    );
    console.log("User's age updated.");

    // Read again to verify update
    const updatedUser = await usersCollection.findOne({ name: "Alice" });
    console.log("Updated user:", updatedUser);

    // Delete: Remove the user
    await usersCollection.deleteOne({ name: "Alice" });
    console.log("User deleted.");
  } catch (error) {
    console.error("Error performing CRUD operations:", error);
  } finally {
    await client.close();
  }
}
performCRUDOperations();
```

### 12. List 5 collection methods used for CRUD operation in MongoDB?

1. insertOne()

2. insertMany()

3. find()

4. updateOne() / updateMany()

5. deleteOne() / deleteMany()

### 13.  How would you restrict the size of a collection in MongoDB?

In MongoDB, you can restrict the size of a collection by creating a capped collection. Capped collections are fixed-size collections that automatically enforce size and document count limits, making them efficient for storing high-throughput data like logs or real-time data.

### 14. Explain about ObjectId

An ObjectId is a unique identifier for MongoDB documents, consisting of a 12-byte hexadecimal value that includes a timestamp, machine identifier, process ID, and a counter. ObjectIds are used as default values for `_id` fields in MongoDB.

### 15. What are the alternatives to MongoDB?

Alternatives to MongoDB include *Cassandra*, *Redis*, *Elasticsearch*, *Couchbase*, and *Firebase** for different use cases like high availability, real-time data processing, and large-scale data storage.

### 16. How will you create a database? What are the considerations before creating a database?

To create a database, simply switch to it in MongoDB:
  javascript
    use myDatabase

MongoDB creates the database when data is first inserted. Considerations include setting appropriate storage limits, choosing sharding configurations, and defining user roles.

### 17. How will you create a collection? What are the considerations before creating a collection?

You can create a collection with `db.createCollection("myCollection")`. Considerations include deciding on schema design, indexes, validation rules, and storage options like capped collections or TTL settings.

### 18. What is BSON, and what are the types of BSON?

BSON (Binary JSON) is MongoDB’s data storage format, extending JSON with additional data types like Date and Binary for efficient storage and transport. BSON types include `ObjectId`, `Binary`, `Date`, `RegularExpression`, `Code`, and more.

### 19.  How to do batch operations in MongoDB?

In MongoDB, batch operations allow you to perform multiple write operations in a single request, making it more efficient by reducing network overhead and ensuring atomicity on each operation within the batch.

### 20. What is the difference between save and insert in MongoDB?

**1. Operation Type:**

`insert():` Exclusively inserts new documents into the collection. It will throw an error if a document with the same `_id` already exists.

`save():` Works as both an insert and an update. If the document contains an `_id` that already exists in the collection, `save()` will update the existing document. If no `_id` exists (or if it’s a new `_id`), `save()` will insert a new document.

**2. Upsert Behavior:**

`insert():` Only performs insert operations and will not replace or update an existing document, even if an `_id` conflict occurs.

`save():` Acts like an "upsert" (update or insert). If the `_id` already exists, it updates the document; otherwise, it inserts a new document.

**3. Error Handling on Duplicate IDs:**

`insert():` Throws an error if the document has a duplicate `_id` that already exists in the collection.

`save():` Does not throw an error for a duplicate `_id`. Instead, it will replace the existing document with the new data.

**4. Usage and Best Practices:**

`insert():` Recommended for inserting new documents when you don’t want to unintentionally overwrite existing data.

`save():` Suitable when you want to insert a document if it doesn't exist or update an existing document if it does. However, `save()` is less commonly used in modern MongoDB applications, as `updateOne()` with `upsert: true` provides more control and flexibility.

```js
db.collection.insert({ _id: 1, name: "Alice", age: 25 }); //insert()
```

```js
// save()
db.collection.save({ _id: 1, name: "Alice", age: 25 });
// Inserts the document if _id: 1 doesn't exist; otherwise, updates it.
```

### 21.  How to use regex in MongoDB? Give some examples?

In MongoDB, you can use regular expressions (regex) to match patterns within string fields. MongoDB supports regular expressions in query filters, allowing you to search for documents based on complex string patterns.

```js
db.collection.find({ field: { $regex: /pattern/, $options: 'i' } });
```

### 22. How to print all the users available in MongoDB?

To print all the users available in MongoDB, you can use the `db.getUsers()` command in the MongoDB shell or its equivalent in a programming language like Python. The method of accessing user information may vary slightly depending on whether you are using the MongoDB shell, a GUI tool like MongoDB Compass, or a driver in your application.

## Indexes and Basic Querying

### 1. What is MongoDB, and how does it differ from traditional relational databases

MongoDB is a NoSQL database that stores data in a flexible, JSON-like format called BSON (Binary JSON). Unlike traditional relational databases, which use structured schemas and tables, MongoDB is schema-less, allowing for dynamic data structures. This flexibility enables developers to easily accommodate changes in data types without requiring schema migrations. Additionally, MongoDB supports horizontal scaling through sharding, making it suitable for large datasets and high-traffic applications.

### 2. Explain what an index is and why it is important in MongoDB

An index in MongoDB is a special data structure that improves the speed of data retrieval operations on a database collection. Indexes are critical for enhancing query performance by allowing the database to quickly locate documents without scanning the entire collection. Without indexes, MongoDB would perform a collection scan, which can be slow, especially for large datasets. Different types of indexes (single-field, compound, text, etc.) can be created based on the query patterns of an application.

### 3. What are some common types of indexes in MongoDB?

- **`Single Field Index:`** An index on a single field of a document.

- **`Compound Index:`** An index on multiple fields of a document, useful for queries involving multiple fields.

- **`Text Index:`** Enables text search on string fields.

- **`Geospatial Index:`** Used for efficient querying of geospatial data.

- **`Unique Index:`** Ensures that the indexed field does not contain duplicate values.

### 4. Create a collection and insert multiple documents into it. Write the code in JavaScript (using the MongoDB shell)

```js
// Create a collection called 'students'
db.createCollection("students");

// Insert multiple student documents
db.students.insertMany([
    { name: "Alice", age: 22, major: "Computer Science" },
    { name: "Bob", age: 24, major: "Mathematics" },
    { name: "Charlie", age: 23, major: "Physics" },
    { name: "David", age: 21, major: "Chemistry" }
]);
```

### 5. Write a query to find all students who are older than 22 and sort them by age in descending order

```js
db.students.find({ age: { $gt: 22 } }).sort({ age: -1 });
```

### 6. Write a command to create a compound index on the 'name' and 'age' fields of the 'students' collection

```js
db.students.createIndex({ name: 1, age: -1 }); // 1 for ascending, -1 for descending
```

### 7. Count the number of students majoring in "Computer Science"

```js
db.students.countDocuments({ major: "Computer Science" });
```

### 8. Write a function to retrieve students' names and majors who are older than a given age parameter and return them as an array. Assume you are using Node.js with the MongoDB driver

```js
const { MongoClient } = require("mongodb");

async function getStudentsOlderThan(db, age) {
    const students = await db.collection("students")
        .find({ age: { $gt: age } })
        .project({ name: 1, major: 1 }) // Only retrieve name and major fields
        .toArray();
    
    return students;
}

// Usage Example
async function main() {
    const client = new MongoClient("mongodb://localhost:27017");
    
    try {
        await client.connect();
        const db = client.db("school");
        
        const results = await getStudentsOlderThan(db, 22);
        console.log(results);
    } finally {
        await client.close();
    }
}

main().catch(console.error);
```

### 9. What is a compound index in MongoDB, and when would you use it?

A compound index is an index on multiple fields within a document. It’s particularly useful when queries frequently filter by multiple fields since it allows MongoDB to optimize query performance by scanning a single index. The order of fields in a compound index matters because queries that use a prefix of the indexed fields can still take advantage of the compound index. For example, if you create a compound index on `{ "name": 1, "age": -1 }`, MongoDB can use this index for queries filtering on `name` alone or on both `name` and `age`.

### 10. What are multikey indexes in MongoDB, and how do they work?

Multikey indexes allow indexing of array fields, automatically indexing each element in the array individually. When you index an array field, MongoDB will create an entry for each element, enabling queries to match documents containing any of those values. For example, if you have a field `tags: ["mongodb", "indexing", "database"]` and create a multikey index on `tags`, MongoDB can efficiently query for documents with specific tags like `"indexing"` or `"database"`. Note that MongoDB does not support creating compound multikey indexes on multiple array fields due to storage and performance limitations.

### 11. Explain the difference between partial indexes and sparse indexes in MongoDB

Partial indexes and sparse indexes are both used to reduce the number of indexed documents, but they work in different ways:

- **Partial Index:** A partial index is created with a filter expression to include only documents that meet specific criteria. It is ideal when only a subset of documents should be indexed based on conditions, such as indexing only documents where `"status": "active"`.

- **Sparse Index:** A sparse index only includes documents where the indexed field exists and is non-null. This is useful for optional fields since it excludes documents missing the indexed field, reducing index size and improving write performance.

### 12. How to do a ascending index in Mongodb?

Creating an ascending index in MongoDB is straightforward. You can use the `createIndex()` method to create an index on a specific field in ascending order.

```js
db.users.createIndex({ age: 1 })
```

### 13. How to use partialFilterExpression in MongoDB indexing?

Using `partialFilterExpression` in MongoDB allows you to create indexes that only include documents that match a specified filter. This can be particularly useful for optimizing queries that only target a subset of documents in a collection.

```js
db.orders.createIndex(
   { deliveryDate: 1 }, // Index on the deliveryDate field in ascending order
   { partialFilterExpression: { status: "shipped" } } // Only include documents where status is "shipped"
)
```

### 14. How and When do you do reindexing?

Reindexing in MongoDB is the process of rebuilding indexes for a collection. This can be necessary for various reasons, such as improving performance, addressing index corruption, or after significant data changes.

- The reIndex command rebuilds all indexes on a collection.

```js
db.collection.reIndex()
```

Alternatively, you can manually drop and recreate specific indexes. This approach gives you more control over which indexes to rebuild.

```js
db.collection.dropIndex("indexName")
```

`Performance Degradation:`

If you notice a significant drop in query performance, it might be due to fragmented or inefficient indexes. Reindexing can help optimize the indexes and improve performance.

`Index Corruption:`

In rare cases, indexes can become corrupted. Reindexing can help resolve such issues by rebuilding the indexes from scratch.

`Significant Data Changes:`

After bulk inserts, updates, or deletions, the distribution of data might change significantly. Reindexing can help ensure that the indexes are optimized for the new data distribution.

`Schema Changes:`

If you make significant changes to the schema, such as adding or removing fields, reindexing can help ensure that the indexes are aligned with the new schema.

`Regular Maintenance:`

As part of regular database maintenance, periodic reindexing can help keep the indexes optimized and ensure consistent performance.

### 15. What are Partial Indexes and Why they are used ?

Partial indexes in MongoDB are indexes that only include documents that meet a specified filter condition. This allows you to create more efficient and targeted indexes by excluding documents that do not match the filter criteria.

`Reduced Index Size:`

By indexing only a subset of documents, partial indexes can significantly reduce the size of the index. This leads to lower storage requirements and can improve performance.

`Improved Query Performance:`

Queries that target the indexed subset of documents can be executed more efficiently. Since the index is smaller and more focused, MongoDB can quickly locate the relevant documents.

`Optimized Write Performance:`

Since fewer documents are indexed, write operations (inserts, updates, deletes) can be faster. This is because MongoDB has to update fewer index entries.

`Targeted Indexing:`

Partial indexes allow you to create indexes that are tailored to specific query patterns. For example, you can create an index that only includes active users or orders with a specific status.

## Aggregation Framework Overview

### 1. Explain the difference between `$match` and `$project` stages in MongoDB's Aggregation Framework. When would you use each?

- The `$match` stage filters documents based on specified criteria, similar to a SQL WHERE clause. It is often used early in the pipeline to limit the number of documents processed, which can significantly improve performance by reducing the dataset size.

- The `$project` stage reshapes documents, specifying which fields to include or exclude, similar to a SQL SELECT statement. It can also create new fields by applying transformations to existing fields, enabling complex calculations or formatting.

`When to Use:`

- Use $match to filter records at the start of the pipeline and reduce the workload on subsequent stages.

- Use $project when you need to limit the fields in the output or create new fields by transforming existing data.

### 2. What are some common performance considerations when using the Aggregation Framework in MongoDB?

1. **`Indexing:`** Use indexes to optimize the `$match` and `$sort` stages. `$match` can utilize indexes if placed at the beginning of the pipeline.

2. **`Pipeline Ordering:`** Place `$match` and `$project` stages as early as possible to reduce the number of documents processed by later stages.

3. **`Memory Usage:`** Certain operations, like `$sort` and `$group`, can be memory-intensive, so MongoDB limits RAM usage. For larger data sets, enable `allowDiskUse: true` to temporarily use disk space for operations exceeding the memory limit.

4. **`Aggregation Expressions:`** Minimize the use of complex expressions within the pipeline when possible, as they can slow down processing.

### 3. Write a MongoDB aggregation query to find the top 3 highest-paying customers by their total spending in the `orders` collection. Assume each order document has the fields `customer_id` and `amount`?

```js
db.orders.aggregate([
    { $group: { _id: "$customer_id", totalSpent: { $sum: "$amount" } } },
    { $sort: { totalSpent: -1 } },
    { $limit: 3 },
    {
        $lookup: {
            from: "customers",
            localField: "_id",
            foreignField: "_id",
            as: "customerInfo"
        }
    },
    {
        $project: {
            _id: 0,
            customer_id: "$_id",
            totalSpent: 1,
            customerInfo: { $arrayElemAt: ["$customerInfo", 0] }
        }
    }
])
```

### 4. Explain Aggregation in MongoDB? Why you selected it over Mapreduce?

Explain Aggregation in MongoDB? Why you selected it over Mapreduce?
Aggregation in MongoDB
Aggregation in MongoDB is a powerful framework for data processing and transformation. It allows you to perform complex operations on your data, such as filtering, grouping, and sorting, in a single query. The aggregation framework uses a pipeline approach, where documents pass through a series of stages that transform them into aggregated results

- **`Performance:`** The aggregation framework is optimized for performance and can handle large datasets more efficiently than MapReduce. It leverages indexes and can execute operations in parallel.

- **`Ease of Use:`** Aggregation pipelines are easier to write and understand compared to MapReduce functions. The pipeline stages provide a more intuitive way to express data transformations.

- **`Flexibility:`** The aggregation framework offers a wide range of operators and stages that cover most data processing needs. It also supports complex operations like joins and array manipulations.

- **`Maintenance:`** Aggregation pipelines are easier to maintain and debug compared to MapReduce functions, which require writing custom JavaScript code.

### 5. What is the use of ismaster and freeze in replication?

In MongoDB replication, `ismaster` and `freeze` are commands used to manage replica set behavior, particularly around the roles of primary and secondary members.

### 6. Why we need Query Router?

**`Scalability:`** By distributing queries across multiple shards, the Query Router enables horizontal scaling, allowing the database to handle large volumes of data and high query loads.

**`Performance:`** Efficient query routing and load balancing help maintain high performance, even as the dataset grows.

**`Transparency:`** The Query Router abstracts the complexity of the sharded architecture from the client, providing a unified interface for interacting with the database.

### 7. What's the use of $graphLookup?

In MongoDB, the `$graphLookup` aggregation stage is used to perform recursive or graph-like lookups within a collection. It allows you to traverse relationships between documents, making it especially useful for exploring hierarchical or tree-like structures within data, such as employee reporting structures, category hierarchies, or social network connections.

## Data Import and Export

### 1. What is MongoDB, and how is it different from traditional SQL databases

MongoDB is a NoSQL, document-oriented database that stores data in a flexible, JSON-like format (BSON) rather than the rows and columns of a traditional SQL database. Unlike SQL databases, MongoDB does not require a predefined schema, making it easier to modify data structure. MongoDB is also designed for horizontal scaling, allowing it to handle large volumes of data across distributed architectures, whereas SQL databases rely more on vertical scaling.

### 2. Explain the structure of a MongoDB document. What is BSON?

A MongoDB document is a JSON-like data structure stored in the database as BSON (Binary JSON). BSON includes extensions to JSON, such as support for dates and binary data, making it more efficient for storage and retrieval. Each document in MongoDB represents a record, with fields and values as key-value pairs. The fields can include basic data types, embedded documents, or arrays, making MongoDB highly flexible.

### 3. What are MongoDB collections, and how do they differ from tables in SQL databases?

In MongoDB, collections are equivalent to tables in SQL databases. Collections are containers for documents, grouping similar documents together. Unlike SQL tables, collections do not enforce a strict schema, meaning documents within a collection can have varying structures. This schema flexibility allows for faster iteration and adaptation to changes in the data model.

### 4.  How does MongoDB handle schema flexibility, and what are the pros and cons of this approach?

MongoDB's schema flexibility allows each document in a collection to have a unique structure, providing adaptability and fast development. Pros: It enables handling unstructured or semi-structured data, quick prototyping, and efficient scaling. Cons: Schema flexibility can lead to data inconsistency, increased complexity in querying and validation, and potential challenges with data migration.

### 5. Explain the CAP theorem and how MongoDB adheres to it

The CAP theorem states that a distributed database can provide at most two of three guarantees: Consistency, Availability, and Partition tolerance. MongoDB prioritizes Partition tolerance and Availability by default, with optional consistency configurations. It allows for flexible configuration (like read and write concern levels) so developers can adjust the consistency requirements based on the use case.

### 6. What are indexes in MongoDB, and why are they important?

Indexes in MongoDB are special data structures that store a small portion of the data in a form that’s easy to traverse. They improve query performance by enabling the database to locate data more efficiently, reducing the need for full collection scans. However, indexes require additional storage and can slow down write operations. MongoDB supports various types of indexes, including single-field, compound, and text indexes.

### 7. Describe a replica set in MongoDB. How does it support high availability?

A replica set is a group of MongoDB servers that maintain the same data set, providing redundancy and high availability. It includes a primary node (for write operations) and secondary nodes (which replicate the primary's data). If the primary node fails, an election occurs among secondaries to choose a new primary, ensuring minimal downtime. Replica sets are essential for fault tolerance in MongoDB deployments.

### 8. What is sharding in MongoDB, and why is it used?

Sharding in MongoDB is a method of distributing data across multiple servers to handle large data volumes and high-throughput operations. MongoDB splits data into chunks based on a shard key and distributes them across different shards. This enables horizontal scaling, allowing MongoDB to handle more data and load by adding more servers, thus improving performance and storage capabilities.

### 9. How do you ensure data consistency in MongoDB?

MongoDB provides several mechanisms for consistency, such as write concerns (to control acknowledgment levels for write operations) and read concerns (to define the level of consistency required when reading data). Developers can also use transactions in MongoDB for multi-document consistency. Ensuring consistency in MongoDB depends on configuring these options based on application requirements and deployment architecture.

### 10. Explain the purpose of MongoDB Aggregation Framework

The Aggregation Framework in MongoDB is used for processing data and performing complex queries, such as filtering, grouping, and transforming data. It’s a powerful alternative to `mapReduce`, offering a pipeline-based syntax where multiple stages can be chained together to perform operations on data. Common stages include `$match`, `$group`, `$sort`, and `$project`, allowing for efficient and comprehensive data transformations.

### 11. Write a MongoDB query to find all documents in the employees collection where the employee’s age is greater than 30 and sort them by name in ascending order

```js
db.employees.find({ age: { $gt: 30 } }).sort({ name: 1 })
```

### 12. Suppose you have a sales collection with documents that include product and quantity fields. Write a MongoDB aggregation pipeline to calculate the total quantity sold for each product

```js
db.sales.aggregate([
  {
    $group: {
      _id: "$product",            // Group by product name
      totalQuantity: { $sum: "$quantity" } // Sum the quantity sold for each product
    }
  }
])
```

### 13. What are collection and Documents?

**`Collection`**

- A collection in MongoDB is equivalent to a table in a relational database.

- It is a group of documents that are stored together within a single database.

- Collections do not enforce a strict schema, meaning that documents within a collection can have different structures, fields, or data types.

**`Document`**

- A document in MongoDB is the basic unit of data and is similar to a row in a relational database.

- Each document is stored in BSON (Binary JSON) format, which is MongoDB’s optimized format for JSON-like documents.

- Documents are key-value pairs, where keys are field names, and values can be various data types, including strings, numbers, arrays, and even nested documents.

**Example:**

```json
{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "year_published": 1925,
  "genres": ["Classic", "Novel"],
  "available": true
}
```

### 14. What is the relation between JSON and Documents?

- MongoDB uses a document data model, which is a JSON-like format (specifically BSON) to store documents.

- BSON (Binary JSON) is a binary-encoded format of JSON that MongoDB uses internally to store data efficiently.

- BSON supports more data types than JSON, including Date, Binary Data, and ObjectId, which makes it flexible and optimized for database operations.

- Since documents are stored in a JSON-like format, MongoDB allows for nested structures, arrays, and flexible schemas, making it easy to represent complex data in a single document.

### 15.  What is BSON and why the document is saved as BSON internally and not as JSON?

BSON stands for Binary JSON and is a binary-encoded serialization format developed by MongoDB. It’s similar to JSON in structure but optimized for efficient storage and retrieval of data in MongoDB.

- JSON, as a text-based format, has limited data types (such as string, number, array, object, and boolean).

- BSON introduces additional data types that are commonly used in databases, including:

  - **`Date:`** BSON can store dates as Date objects with millisecond precision, which JSON lacks.
  
  - **`ObjectId:`** BSON includes a specific data type for ObjectId, which MongoDB uses as a unique identifier for each document.

  - **`Binary Data:`** BSON can store binary data, such as images or files, which isn’t possible with plain JSON.

  - **`64-bit integers:`** BSON natively supports 64-bit integers, which JSON lacks.

### 16. How arrays in JSON documents are handled in MongoDB?

In MongoDB, arrays in JSON documents are handled seamlessly and are stored directly within documents as part of the BSON format. MongoDB's document model is flexible, allowing arrays to contain any data type, including other arrays or nested documents.

### 17. How mongoDB can be used for Cache Management?

MongoDB can be effectively used for cache management due to its flexible schema, high performance, and rich query capabilities. Utilizing MongoDB as a caching layer can help optimize application performance by reducing latency and decreasing the load on primary databases or other data sources.

1. In-Memory Storage with MongoDB
2. TTL (Time-To-Live) Indexes
3. Flexible Schema for Caching
4. Replica Sets for High Availability
5. Integration with Application Layer
6. Aggregating and Storing Derived Data
7. Using Change Streams for Cache Updates

### 18. What are the types of BSON?

| Type               | Description                                      | Example                                     |
|--------------------|--------------------------------------------------|---------------------------------------------|
| Double             | 64-bit floating-point number                     | 3.14                                       |
| String             | UTF-8 encoded string                             | "Hello, world!"                            |
| Object             | Embedded document                                | { "name": "Alice", "age": 30 }            |
| Array              | Array of values                                  | [1, 2, 3]                                  |
| Binary Data        | Binary data (e.g., images, files)               | BinData(0, "...")                          |
| Undefined          | Null value (not commonly used)                  | (Not commonly used)                        |
| ObjectId           | Unique identifier for documents                  | ObjectId("507f1f77bcf86cd799439011")      |
| Boolean            | Boolean value (true or false)                   | true                                       |
| Date               | Date and time                                    | ISODate("2024-11-05T00:00:00Z")           |
| Null               | Null value                                       | null                                       |
| Regular Expression  | Represents a regex pattern                       | /^[a-z]+$/                                 |
| JavaScript         | Represents JavaScript code                        | new Code("function() { return true; }")   |
| Timestamp          | BSON timestamp                                   | Timestamp(123456789, 0)                    |
| Decimal128         | High-precision decimal value                     | Decimal128("10.123456789012345678901234567890") |
| Min Key            | Less than all other values                       | MinKey()                                   |
| Max Key            | Greater than all other values                    | MaxKey()                                   |

### 19. How do you Update a Document?

Once a document is stored in the database, it can be changed using one of several update methods: `updateOne` , `updateMany` , and `replaceOne`. `updateOne` and `updateMany` each takes a filter document as their first parameter and a modifier document, which describes changes to make, as the second parameter. `replaceOne` also takes a filter as the first parameter, but as the second parameter `replaceOne` expects a document with which it will replace the document matching the filter.

For example, in order to replace a document:

```db
{
"_id" : ObjectId("4b2b9f67a1f631733d917a7a"),
"name" : "alice",
"friends" : 24,
"enemies" :2
}
```

### 20. How do you Delete a Document?

The CRUD API in MongoDB provides `deleteOne` and `deleteMany` for this purpose. Both of these methods take a filter document as their first parameter. The filter specifies a set of criteria to match against in removing documents.

For example:

```db
> db.books.deleteOne({"_id" : 3})
```
