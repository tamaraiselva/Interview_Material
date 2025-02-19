# Advance Interview & Questions

1. **Explain the function of exit code in Node.js.**

Exit codes are a collection of specific codes whose function is to complete a specific process. Examples of exit codes are fatal error, unused, internal JavaScript evaluation failure, etc.

2. **What causes server latency and prevents scalability in Node.js?**

Several factors can cause server latency and prevent scalability in Node.js. Some of the most common ones include:

- **Blocking I/O**: Blocking I/O operations can cause the server to become unresponsive while waiting for I/O operations to complete. This can be especially problematic in Node.js, which is designed to handle many concurrent connections. To avoid this, Node.js provides non-blocking I/O operations.
 
- **Inefficient code**: Inefficient code can cause unnecessary processing and slow down the server. This can be caused by poor algorithmic choices, excessive use of synchronous operations, or inefficient data structures.

- **Insufficient hardware resources**: Insufficient hardware resources, such as CPU, memory, or network bandwidth, can cause the server to become overloaded and unresponsive. This can be especially problematic in high traffic scenarios.

- **Improper configuration**: Improperly configured servers can cause performance issues. This can be caused by incorrect network settings, improper load balancing, or other misconfigurations.

3. **How does Node.js convert JavaScript code to C++?**

Node.js uses the Google V8 JavaScript engine to convert JS code to C++.

4. **Define event programming.**

Event programming is programming paradigm that uses events to trigger actions. An event can be generated by the user, by the system, or by the program itself.

5. **How is Ajax different from Node.js?**

Ajax is a client-side technology used to make web pages more interactive and dynamic, while Node.js is a server-side technology used to build scalable, high-performance web applications.

6. **Explain non-blocking in Node.js.**

Non-blocking in Node.js means that the program can continue to execute other code even while waiting for I/O operations to complete.

7. **In which packages are dependencies stored in Node.js?**

Dependencies are present in the package.json file.

8. **Define control function in Node.js.**

A control function manages and manipulates the flow of asynchronous code execution.

- Node.js is designed to handle asynchronous I/O operations, which means that multiple I/O operations can be executed simultaneously without blocking the execution of other code. However, managing the flow of asynchronous code can be challenging, especially when multiple operations need to be executed in a particular order.

- Control functions provide a solution to this problem by allowing developers to define the order in which asynchronous operations should be executed. They can be used to perform tasks such as error handling, callback management, and flow control.

9. **When do you use modularization in Node.js?**

Modularization in Node.js provides scalability when developing complex applications. The modularization option can be used to execute the import of objects, classes, functions, modules, and external files.

10. **What is the call-back function used for?**

The call-back function is used to execute a function after a certain event has occurred.

11. **Explain how blocking is prevented in Node.js.**

Because of the event mechanism in Node.js, a callback function is called every time an event starts. This prevents blocking in Node.js.

12. **How many layers are there in Node.js application architecture?**

There are three layers in the application architecture - API, service, and integration layers.

13. **Name input arguments for asynchronous queue.**

Two input arguments for asynchronous queue are concurrency value and task function.

14. **Does Node.js applications buffer data?**

No. Node.js applications do not buffer data.

15. **What is a Boolean data type in Node.js?**

The Boolean data type in Node.js can have one of two values: true or false.

16. **Is it possible to run external processes with Node.js?**

It is possible to run external processes with Node.js. This can be done with the help of the child_process module.

17. **Is it possible to avoid callback hells and how?**

It is possible to avoid callback hells by using promises; they can help to make the code more readable and easier to debug. You can also avoid callback hells using async/wait, libraries, and modularization.

18. **What is the function of the fs module?**

The fs module is used to create and manipulate files. It also provides an API for interacting with the file system.

19. **Define os module in Node.js?**

The os module provides a set of tools for interacting with the operating system. It provides an API for getting information about the system including memory, processor, file system, and network interfaces.

20. **Are duplex streams readable and writable?**

Duplex streams are both readable and writable. This means that they can be used to read data from a source and write data to a destination.

21. **What is a transform stream?**

A transform stream is a type of stream that can be used to modify or transform the data as it is being read or written.

22. **In Node.js, how many Node object methods are available?**

There are a total of 18 Node object methods available. These methods can be used to create, manipulate, and delete objects.

23. **What is the meaning of HTTP status code 504?**

HTTP status code 504 indicates that the server is unable to process the request. This can be due to several reasons, such as an overloaded server or a network issue.

24. **Explain routing in the express.**

Routing is a process where you associate HTTP request to a URL path or specific routes. When a request matches one of these routes, a corresponding handling function is used. Routing is a robust mechanism that enables you to define how an application handles incoming requests.

25. **How to open a file in Node.js?**

A file can be opened in Node.js using the fs.open() method. This method takes two arguments, the path of the file and the flags.

26. **What is the difference between Angular and Node.js?**

Angular is a front-end web application framework. Node.js is a back-end runtime environment.

27. **How does Node.js handle concurrency if it is single-threaded?**

Node.js prevents bottlenecks and aids programmers in easily writing the code because of the single-thread model. Internally, there are several POSIX threads for different I/O operations like File, DNS, etc.

So, when Node receives an I/O request, it uses one of these threads for the I/O operation. Once the operation is complete, the result joins the event queue. Because of the event mechanism, the event loop starts after each event, checks the queue, and if Node’s execution stack is free, then the loop adds the queue result to it, thus managing concurrency.

28. **What is the shortcut for killing a process in Node.js?**

Ctrl + C shortcut is used for terminating processes in Node.js.

29. **What is a Node Inspector?**

A Node-Inspector is a debugging tool that allows developers to inspect and debug the code of an application through a graphical user interface.

30. **Is dgram an in-built module?**

The Dgram is an in-built module. It is useful in implementing UDP datagram packets.

31. **Can we import a buffer class without buffer modules?**

You can import the buffer class without the buffer module.

32. **Which function is used to fire an event?**

The emit() function is used to fire an event.

33. **Explain call back.**

In Node.js, a callback function is a function that is passed as an argument to another function and is called back at a later point in time. The purpose of using a callback function is to handle asynchronous operations.

In asynchronous programming, a function that initiates an asynchronous operation returns immediately while the operation continues in the background. When the operation is completed, the callback function is called with the result of the operation.

34. **Can middleware function execute code?**

Yes, the middleware functions can execute code and they can modify the request or response objects.

35. **How many types of streams are there in Node.js?**

There are four types of streams in Node.js: readable, writable, duplex, and transform.

- **Readable**: The readable streams are used to read data from a specific source.

- **Writable**: These streams are utilized for writing data to the destination.

- **Duplex**: The duplex streams are used for both reading and writing data.

36.  **What is the difference between setImmediate() and setTimeout()?**

The difference between setImmediate() and setTimeout() is that setImmediate() will execute the callback function immediately, while setTimeout() will wait for a specified time before executing the callback function.

37. **What two arguments do async.queue take?**

Task function and concurrency value are the two arguments async.queue takes.

38. **What is the Null data type in Node.js?**

It is a special data type that only takes one value, i.e., null.

39. **What is the difference between an event and a callback?**

The difference between an event and a callback is that an event is a mechanism that signals a change or action that represents a part of the program's behaviour, while a callback is a function that takes data and sends it back to the calling function.

40. **How will you delete a directory?**

To delete a directory, we use fs. rmdir() method.

41. **Is the value of the symbol data type kept private?**

Yes, it is private and used internally.

42. **What is an error-first callback?**

Error-first callbacks are used to pass data and identify if an error has occurred.

43. **What are global objects?**

Global objects are universal objects that are present in every module or file of the application without requiring explicit import statements.

44. **When does the child process occur?**

In Node.js, a child process occurs when a new process is created using the child_process module. This module provides functionality to spawn child processes in a similar way to the fork() system call in Unix.

45. **Can variables defined with let keyword be redeclared?**

No, the let keyword can’t be redeclared and should be declared before use.