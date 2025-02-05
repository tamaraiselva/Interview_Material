# JavaScript Interview_Question

1. **What do you understand about JavaScript?**

JavaScript is a popular web scripting language used for client-side and server-side development. Its code can be inserted into HTML pages and understood and executed by web browsers. JavaScript also supports object-oriented programming abilities.

2. **What’s the difference between JavaScript and Java?**

|                              JavaScript                                  |                                               Java                                      |
|--------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| JavaScript is an object-oriented scripting language.                     | Java is an object-oriented programming language.                                        |
| JavaScript applications are meant to run inside a web browser.           | Java applications are generally made for use in operating systems and virtual machines. |
| JavaScript does not need compilation before running the application code.| Java source code needs a compiler before it can be ready to run in realtime.            |

3. **What are the various data types that exist in JavaScript?**

These are the different types of data that JavaScript supports:

- **Boolean** - For true and false values
- **Null** - For empty or unknown values
- **Undefined** - For variables that are only declared and not defined or initialized
- **Number** - For integer and floating-point numbers
- **String** - For characters and alphanumeric values
- **Object** - For collections or complex values
- **Symbols** - For unique identifiers for objects

4. **What are the features of JavaScript?**
   
These are the features of JavaScript:

- Lightweight, interpreted programming language
- Cross-platform compatible
- Open-source
- Object-oriented
- Integration with other backend and frontend technologies
- Used especially for the development of network-based applications

5. **How do you create an object in JavaScript?**
   
Since JavaScript is essentially an object-oriented scripting language, it supports and encourages the usage of objects while developing web applications.

**Example**

```js
const student = {

    name: 'John',

    age: 17

}
```

6. **What is Array of JavaScript**

An array in JavaScript is a type of global object used to store data. Arrays can store multiple values in a single variable, which can condense and organize our code.

7. **What are some of the built-in methods in JavaScript?**

|               Built-in Method                 |                             Values                              |
|-----------------------------------------------|-----------------------------------------------------------------|
| Date()                                        | Returns the present date and time                               |
| concat()                                      | Joins two strings and returns the new string                    |  
| push()                                        | Adds an item to an array                                        |
| pop()                                         | Removes and also returns the last element of an array           |
| round()                                       | Rounds of the value to the nearest integer and then returns it  |
| length()                                      | Returns the length of a string                                  |

8. **What are the scopes of a variable in JavaScript?**

The scope of a variable implies where the variable has been declared or defined in a JavaScript program. There are two scopes of a variable:

- **Global Scope**: Global variables, having global scope are available everywhere in a JavaScript code.

- **Local Scope**: Local variables are accessible only within a function in which they are defined.

9. **What is the ‘this’ keyword in JavaScript?**

The ‘this’ keyword in JavaScript refers to the currently calling object. It is commonly used in constructors to assign values to object properties.

10. **What are the conventions of naming a variable in JavaScript?**

- Variable names cannot be similar to that of reserved keywords. For example, var, let, const, etc.
- Variable names cannot begin with a numeric value. They must only begin with a letter or an underscore character.
- Variable names are case-sensitive.

11.   **What is Callback in JavaScript?**

In JavaScript, functions are objects and therefore, functions can take other functions as arguments and can also be returned by other functions.

12. **How do you debug a JavaScript code?**

All modern web browsers, such as Chrome, Firefox, etc., have an inbuilt debugger that can be accessed anytime by pressing the relevant key, usually the F12 key. The debugging tools offer several features.
We can also debug JavaScript code inside a code editor that we use to develop a JavaScript application, such as Visual Studio Code, Atom, Sublime Text, etc.

13. **What are the ways of adding JavaScript code in an HTML file?**

We can write JavaScript code within the script tag in the same HTML file; this is suitable when we need just a few lines of scripting within a web page.
We can import a JavaScript source file into an HTML document; this adds all scripting capabilities to a web page without cluttering the code.

14. **What is the difference between Function declaration and Function expression?**

|                       Function declaration                       |                            Function expression                              |
|------------------------------------------------------------------|-----------------------------------------------------------------------------|
| Declared as a separate statement within the main JavaScript code | Created inside an expression or some other construct                        |
| Can be called before the function is defined                     | Created when the execution point reaches it; can be used only after that    |
| Offers better code readability and better code organization      | Used when there is a need for a conditional declaration of a function       | 
| Example:                                                         | Example:                                                                    |
| function abc() {                                                 | var a = function abc() {                                                    |
|     return 5;                                                    |     return 5;                                                               |
| }                                                                | }                                                                           |

15. **What are the ways of adding JavaScript code in an HTML file?**

We can write JavaScript code within the script tag in the same HTML file; this is suitable when we need just a few lines of scripting within a web page.
We can import a JavaScript source file into an HTML document; this adds all scripting capabilities to a web page without cluttering the code.

16. **What do you understand about cookies?**

A cookie is generally a small data that is sent from a website and stored on the user’s machine by a web browser that was used to access the website. Cookies are used to remember information for later use and also to record the browsing activity on a website.

17. **How would you create a cookie?**

The simplest way of creating a cookie using JavaScript is as below:

```js
document.cookie = "key1 = value1; key2 = value2; expires = date";
```

18. **How would you read a cookie?**

Reading a cookie using JavaScript is also very simple. We can use the document.cookie string that contains the cookies that we just created using that string.

The document.cookie string keeps a list of name-value pairs separated by semicolons, where ‘name’ is the name of the cookie, and ‘value’ is its value. We can also use the split() method to break the cookie value into keys and values.

19. **How would you delete a cookie?**

To delete a cookie, we can just set an expiration date and time. Specifying the correct path of the cookie that we want to delete is a good practice since some browsers won’t allow the deletion of cookies unless there is a clear path that tells which cookie to delete from the user’s machine.

```js
function delete_cookie(name) {

  document.cookie = name + "=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;";

}
```

20. **What’s the difference between let and var?**

Both let and var are used for variable and method declarations in JavaScript. So there isn’t much of a difference between these two besides that while var keyword is scoped by function, the let keyword is scoped by a block.

21. **What are Closures in JavaScript?**

Closures provide a better, and concise way of writing JavaScript code for the developers and programmers. Closures are created whenever a variable that is defined outside the current scope is accessed within the current scope.

```js
function hello(name) {

  var message = "hello " + name;

  return function hello() {

    console.log(message);

  };

}

//generate closure

var helloWorld = hello("World");

//use closure

helloWorld();
```

22. **What are the arrow functions in JavaScript?**

Arrow functions are a short and concise way of writing functions in JavaScript. The general syntax of an arrow function is as below:

```js
const helloWorld = () => {

  console.log("hello world!");

};
```

23. **What are the different ways an HTML element can be accessed in a JavaScript code?**

Here are the ways an HTML element can be accessed in a JavaScript code:

```js
getElementByClass(‘classname’): Gets all the HTML elements that have the specified classname.
getElementById(‘idname’): Gets an HTML element by its ID name.
getElementbyTagName(‘tagname’): Gets all the HTML elements that have the specified tagname.
querySelector(): Takes CSS style selector and returns the first selected HTML element.
```

24. **What are the ways of defining a variable in JavaScript?**

There are three ways of defining a variable in JavaScript:

- **Var** - This is used to declare a variable and the value can be changed at a later time within the JavaScript code.

- **Const** - We can also use this to declare/define a variable but the value, as the name implies, is constant throughout the JavaScript program and cannot be modified at a later time.

- **Let** - This mostly implies that the values can be changed at a later time within the JavaScript code.

25. **What are Imports and Exports in JavaScript?**

Imports and exports help in writing modular code for our JavaScript applications. With the help of imports and exports, we can split a JavaScript code into multiple files in a project. This greatly simplifies the application source code and encourages code readability.

```js

export const sqrt = Math.sqrt;

export function square(x) {

  return x * x;

}

export function diag(x, y) {

  return sqrt(square(x) + square(y));

}
```
This file exports two functions that calculate the squares and diagonal of the input respectively.

```js

import { square, diag } from "calc";

console.log(square(4)); // 16

console.log(diag(4, 3)); // 5
```

26. **What is the difference between Document and Window in JavaScript?**

- **Document** - The document comes under the windows object and can also be considered as its property.

- **Window** - Window in JavaScript is a global object that holds the structure like variables, functions, location, history, etc.

27. **What are some of the JavaScript frameworks and their uses?**

JavaScript has a collection of many frameworks that aim towards fulfilling the different aspects of the web application development process. Some of the prominent frameworks are:

- **React** - Frontend development of a web application
- **Angular** - Frontend development of a web application
- **Node** - Backend or server-side development of a web application

28. **What is the difference between Undefined and Undeclared in JavaScript?**

- **Undefined** - Undefined means a variable has been declared but a value has not yet been assigned to that variable.

- **Undeclared** - Variables that are not declared or that do not exist in a program or application.

29. **What is the difference between Undefined and Null in JavaScript?**

**Undefined** - Undefined means a variable has been declared but a value has not yet been assigned to that variable.

**Null** - Null is an assignment value that we can assign to any variable that is meant to contain no value.

30. **What is the difference between Session storage and Local storage?**

- **Session storage** - The data stored in session storage gets expired or deleted when a page session ends.

- **Local storage** - Websites store some data in local machine to reduce loading time; this data does not get deleted at the end of a browsing session.

