# Interview Question

## 1. Can you explain what is MongoDB and where it is typically used?

MongoDB is a source-available, NoSQL database program that uses JSON-like documents with optional schemas. It’s designed for high volume data storage and offers horizontal scalability as its key feature. MongoDB is typically used in big data applications and content management systems where data is diverse and doesn’t fit well into tables. It’s also suitable for real-time analytics and processing massive amounts of queries, thanks to its indexing and querying capabilities.

## 2. How does MongoDB differ from a traditional SQL database in terms of structure and querying capabilities?

MongoDB, a NoSQL database, differs from traditional SQL databases in structure and querying capabilities. Unlike SQL’s table-based relational model, MongoDB uses a flexible, document data model where each record is a document comprising of key-value pairs, similar to JSON objects. This allows for diverse data types within the same collection and nested fields.

In terms of querying, MongoDB offers rich query language with secondary indexes, enabling complex queries. It supports ad-hoc queries, indexing, and real-time aggregation rather than relying on predefined schemas and joins like SQL. However, it lacks support for transactions and joins which are inherent in SQL databases.

Moreover, MongoDB provides horizontal scaling through sharding by distributing data across many servers, unlike SQL’s vertical scaling. This makes MongoDB more suitable for handling large volumes of data and high traffic applications.

## 3. Can you describe how MongoDB achieves high write loads?

MongoDB achieves high write loads through sharding and replication. Sharding is a method of distributing data across multiple machines, allowing MongoDB to meet the demands of data growth. It uses a shard key to distribute data across shards in a cluster, ensuring balanced load. Replication provides redundancy and increases data availability by maintaining multiple copies of data on different database servers. This process involves a primary node that receives all write operations and secondary nodes that replicate the primary node’s oplog and apply the operations to their data sets.

## 4. Please explain the purpose and usage of MongoDB’s Aggregation Framework?

MongoDB’s Aggregation Framework is a powerful tool for data analysis and manipulation. It provides a pipeline where documents pass through multiple stages, each transforming the data in some way. This allows complex queries to be executed efficiently.

The framework uses operators like $match, $group, $sort, etc., which are applied in sequence. For instance, $match filters incoming documents to only let those that match certain criteria pass through. $group then groups these filtered documents by specified fields.

Aggregation can also reshape documents using $project, add new fields with computed values via $addFields, or even join collections together using $lookup.

This framework is particularly useful when dealing with large datasets as it reduces the need for application-level code, making operations faster and more efficient. It’s used extensively in analytics, reporting, or whenever there’s a need to transform data into a format suitable for further processing or visualization.

## 5. What are the differences between MongoDB’s update() and save() functions

MongoDB’s update() and save() functions serve different purposes. The update() function modifies existing documents in a collection based on specified criteria, while the save() function either creates a new document or replaces an entire existing one.

The update() function requires two parameters: the query condition to identify the documents to be updated, and the changes to apply. It can modify multiple documents if the multi parameter is set to true. If no matching document is found, it does nothing unless upsert is set to true, which will create a new document.

On the other hand, save() function takes a document as its parameter. If the document has an _id field, it will replace the existing document with the same_id; otherwise, it inserts a new document. Unlike update(), save() cannot modify multiple documents at once.

## 6. Illustrate a scenario where you would use an Embedded Document in MongoDB

In a blogging platform, an embedded document in MongoDB would be useful. Each blog post could be represented as a document with fields such as title, content, and author. Comments on the blog post can be stored as an array of embedded documents within the main blog post document. Each comment document might contain fields like commenter name, comment text, and timestamp. This structure allows for efficient retrieval of all comments associated with a specific blog post, as they are directly nested within the parent document. It also simplifies updates to individual comments, as each is a distinct document within the array.

## 7. Explain the difference between MongoDB’s findOne() and find() functions

MongoDB’s findOne() and find() functions are both used for retrieving data, but they differ in their usage and output. The findOne() function returns the first document that matches a specified filter or query. It is useful when you know there is only one matching document, or are only interested in the first match. On the other hand, the find() function returns all documents that match the specified filter or query as an array of objects. This makes it suitable for situations where multiple documents may match the criteria. Both functions can accept two optional parameters: a projection object specifying which fields to include or exclude, and options such as sort order.

## 8. Write a piece of code using MongoDB to avoid a situation of dirty read

In MongoDB, to avoid a dirty read situation, we can use the concept of transactions. Transactions ensure that all operations within it are atomic and consistent. Here’s an example:

```db
const session = client.startSession();
session.startTransaction();
try {
  const opts = { session };
  const A = await collection.findOne({ _id: "A" }, opts);
  A.balance -= 100;
  
  const B = await collection.findOne({ _id: "B" }, opts);
  B.balance += 100;
  await collection.updateOne({ _id: "A" }, { $set: A }, opts);
  await collection.updateOne({ _id: "B" }, { $set: B }, opts);
  await session.commitTransaction();
} catch (error) {
  console.error('Error processing transaction', error);
  session.abortTransaction();
}
session.endSession();
```

This code initiates a transaction with startTransaction(), performs two findOne operations to fetch documents, modifies them, then uses updateOne to save changes. If any operation fails, abortTransaction() rolls back changes, ensuring data consistency.
