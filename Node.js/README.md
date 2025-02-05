# Node.JS Interview Question

1. **What is Node.js?**

  Node.js is an open-source, cross-platform JavaScript runtime environment and library to run web applications outside the client’s browser. It is used to create server-side web applications.

2. **Why use Node.js?**

Node.js is a JavaScript framework that's used for server-side development and has many advantages, including:

- Scalability
- Speed
- Event-driven and non-blocking
- Code reusability and sharing
- Unifies client-side and server-side development
- Open-source
- HTTP is a first-class citizen

3. **How does Node.js work?**

A web server using Node.js typically has a workflow that is quite similar to the diagram illustrated below. Let’s explore this flow of operations in detail.

Node.js Architecture Workflow

- Clients send requests to the webserver to interact with the web application. Requests can be non-blocking or blocking:
- Querying for data
- Deleting data 
- Updating the data
- Node.js retrieves the incoming requests and adds those to the Event Queue
- The requests are then passed one-by-one through the Event Loop. It checks if the requests are simple enough not to require any external resources
- The Event Loop processes simple requests (non-blocking operations), such as I/O Polling, and returns the responses to the corresponding clients

4. **Why is Node.js Single-threaded?**

Node.js is single-threaded for async processing. By doing async processing on a single-thread under typical web loads, more performance and scalability can be achieved instead of the typical thread-based implementation.

5. **If Node.js is single-threaded, then how does it handle concurrency?**

The Multi-Threaded Request/Response Stateless Model is not followed by the Node JS Platform, and it adheres to the Single-Threaded Event Loop Model. The Node JS Processing paradigm is heavily influenced by the JavaScript Event-based model and the JavaScript callback system. As a result, Node.js can easily manage more concurrent client requests. The event loop is the processing model's beating heart in Node.js.

6. **Explain callback in Node.js.**

A callback function is called after a given task. It allows other code to be run in the meantime and prevents any blocking.  Being an asynchronous platform, Node.js heavily relies on callback. All APIs of Node are written to support callbacks.

7. **What are the advantages of using promises instead of callbacks?**

- The control flow of asynchronous logic is more specified and structured.
- The coupling is low.
- We've built-in error handling.
- Improved readability.

8. **How would you define the term I/O?**

- The term I/O is used to describe any program, operation, or device that transfers data to or from a medium and to or from another medium
- Every transfer is an output from one medium and an input into another. The medium can be a physical device, network, or files within a system io

9. **How is Node.js most frequently used?**

Node.js is widely used in the following applications:

- Real-time chats
- Internet of Things
- Complex SPAs (Single-Page Applications)
- Real-time collaboration tools
- Streaming applications
- Microservices architecture

10. **Explain the difference between frontend and backend development?**

|                                           Front-end                                                |                                            Back-end                                             |
|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| Frontend refers to the client-side of an application                                               | Backend refers to the server-side of an application                                             |
| It is the part of a web application that users can see and interact with                           | It constitutes everything that happens behind the scenes                                        |
| It typically includes everything that attributes to the visual aspects of a web application        | It generally includes a web server that communicates with a database to serve requests          |
| HTML, CSS, JavaScript, AngularJS, and ReactJS are some of the essentials of frontend development   | Java, PHP, Python, and Node.js are some of the backend development technologies                 |

11. **What is NPM?**

NPM stands for Node Package Manager, responsible for managing all the packages and modules for Node.js.

Node Package Manager provides two main functionalities:

- Provides online repositories for node.js packages/modules, which are searchable on search.nodejs.org
- Provides command-line utility to install Node.js packages and also manages Node.js versions and dependencies  

12.  **What are the modules in Node.js?**

Modules are like JavaScript libraries that can be used in a Node.js application to include a set of functions. To include a module in a Node.js application, use the require() function with the parentheses containing the module's name.

Node.js has many modules to provide the basic functionality needed for a web application. Some of them include:

|       Core Modules        |                               Description                                         |            
|---------------------------|-----------------------------------------------------------------------------------|
| HTTP                      | Includes classes, methods, and events to create a Node.js HTTP server             |
| util                      | Includes utility functions useful for developers                                  |
| fs                        | Includes events, classes, and methods to deal with file I/O operations            |
| url                       | Includes methods for URL parsing                                                  |
| query string              | Includes methods to work with query string                                        |
| stream                    | Includes methods to handle streaming data                                         |
| zlib                      | Includes methods to compress or decompress files                                  |

13. **What is the purpose of the module .Exports?**

In Node.js, a module encapsulates all related codes into a single unit of code that can be parsed by moving all relevant functions into a single file. You may export a module with the module and export the function, which lets it be imported into another file with a needed keyword.

14. **Why is Node.js preferred over other backend technologies like Java and PHP?**

Some of the reasons why Node.js is preferred include:

- Node.js is very fast
- Node Package Manager has over 50,000 bundles available at the developer’s disposal
- Perfect for data-intensive, real-time web applications, as Node.js never waits for an API to return data
- Better synchronization of code between server and client due to same code base
- Easy for web developers to start using Node.js in their projects as it is a JavaScript library

15. **What is the difference between Angular and Node.js?**

|                           Angular                             |                                   Node.js                                     |
|---------------------------------------------------------------|-------------------------------------------------------------------------------|
| It is a frontend development framework                        | It is a server-side environment                                               |
| It is written in TypeScript                                   | It is written in C, C++ languages                                             |
| Used for building single-page, client-side web applications   | Used for building fast and scalable server-side networking applications       |
| Splits a web application into MVC components                  | Generates database queries                                                    |


16.  **Which database is more popularly used with Node.js?**

MongoDB is the most common database used with Node.js. It is a NoSQL, cross-platform, document-oriented database that provides high performance, high availability, and easy scalability.

17. **What are some of the most commonly used libraries in Node.js?**

There are two commonly used libraries in Node.js:

- **ExpressJS** - Express is a flexible Node.js web application framework that provides a wide set of features to develop web and mobile applications.
- **Mongoose** - Mongoose is also a Node.js web application framework that makes it easy to connect an application to a database.

18. **What are the pros and cons of Node.js?**

|                                   Node.js Pros                                                |                                            Node.js Cons                                           |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| Fast processing and an event-based model                                                      | Not suitable for heavy computational tasks                                                        |
| Uses JavaScript, which is well-known amongst developers                                       | Using callback is complex since you end up with several nested callbacks                          |   
| Node Package Manager has over 50,000 packages that provide the functionality to an application| Dealing with relational databases is not a good option for Node.js                                |
| Best suited for streaming huge amounts of data and I/O intensive operations                   | Since Node.js is single-threaded, CPU intensive tasks are not its strong suit                     |

19. **What is the command used to import external libraries?**

The “require” command is used for importing external libraries. For example - “var http=require (“HTTP”).”  This will load the HTTP library and the single exported object through the HTTP variable.

Now that we have covered some of the important beginner-level Node.js interview questions let us look at some of the intermediate-level Node.js interview questions.

`var http = require('http');`

## Node.js Interview Questions and Answers For Intermediate Level

20. **What does event-driven programming mean?**

An event-driven programming approach uses events to trigger various functions. An event can be anything, such as typing a key or clicking a mouse button. A call-back function is already registered with the element executes whenever an event is triggered.

21. **What is an Event Loop in Node.js?**

Event loops handle asynchronous callbacks in Node.js. It is the foundation of the non-blocking input/output in Node.js, making it one of the most important environmental features.

22. **Differentiate between process.nextTick() and setImmediate()?**

The distinction between method and product. This is accomplished through the use of nextTick() and setImmediate(). next Tick() postpones the execution of action until the next pass around the event loop, or it simply calls the callback function once the event loop's current execution is complete, whereas setImmediate() executes a callback on the next cycle of the event loop and returns control to the event loop for any I/O operations.

23. **What is an EventEmitter in Node.js?**

EventEmitter is a class that holds all the objects that can emit events
Whenever an object from the EventEmitter class throws an event, all attached functions are called upon synchronously

![node](https://www.simplilearn.com/ice9/free_resources_article_thumb/eventemitter.JPG)

24. **What are the two types of API functions in Node.js?**

The two types of API functions in Node.js are:

- Asynchronous, non-blocking functions
- Synchronous, blocking functions

25. **What is the package.json file?**

The package.json file is the heart of a Node.js system. This file holds the metadata for a particular project. The package.json file is found in the root directory of any Node application or module

This is what a package.json file looks like immediately after creating a Node.js project using the command: npm init

You can edit the parameters when you create a Node.js project.

![alt](https://www.simplilearn.com/ice9/free_resources_article_thumb/node-npm.JPG)

26. **How would you use a URL module in Node.js?**

The URL module in Node.js provides various utilities for URL resolution and parsing. It is a built-in module that helps split up the web address into a readable format.

![alt](https://www.simplilearn.com/ice9/free_resources_article_thumb/varurl.JPG)

27. **What is the Express.js package?**

Express is a flexible Node.js web application framework that provides a wide set of features to develop both web and mobile applications

28. **How do you create a simple Express.js application?**

- The request object represents the HTTP request and has properties for the request query string, parameters, body, HTTP headers, and so on
- The response object represents the HTTP response that an Express app sends when it receives an HTTP request

![alt](https://www.simplilearn.com/ice9/free_resources_article_thumb/varex.JPG)
