# HTML Interview Question

1. **What is HTML?**

HTML stands for Hypertext Markup Language, the language of the Internet. It is the standard text formatting language used for creating and displaying pages on the Internet.

HTML documents comprise the elements and the tags that format it for proper page display.

2. **What are HTML tags?**

We use HTML tags to place the elements in the proper and appropriate format. Tags use the symbols < and > to set them apart from the HTML content.
The HTML tags need not always be closed. For example, in the case of images, the closing tags are not required as `<img>` tags.

3. **What is a marquee in HTML?**

Marquee is used for scrolling text on a web page. It automatically scrolls the image or text up, down, left, or right. 
You must use </marquee> tags to apply for a marquee.

**Example**

```html
<marquee>This text will scroll from right to left</marquee>
<marquee direction="up">This text will scroll from bottom to top</marquee>
<marquee
  direction="down"
  width="250"
  height="200"
  behavior="alternate"l̥
  style="border:solid">
  <marquee behavior="alternate">This text will bounce</marquee>
</marquee>
```

**Output**

![Images](../HTML%20Interview_Question/Images/Screenshot%202024-10-08%20093742.png)

4. **How do you separate a section of text in HTML?**

We separate a section of text in HTML using the below tags:

- `<br>` tag – It separates the line of text. It breaks the current line and shifts the flow of the text to a new line.

**Example**

```html
<p>Be not afraid of greatness.<br>
Some are born great,<br>
some achieve greatness,<br>
and others have greatness thrust upon them.</p>
<p><em>-William Shakespeare</em></p>
```

**Output**

![Images](../HTML%20Interview_Question/Images/Screenshot%202024-10-08%20095523.png)

- `<p>` tag–This tag is used to write a paragraph of text.

**Example**

```html
<p>This is some text in a paragraph.</p>
```

**Output**

![images](../HTML%20Interview_Question/Images/Screenshot%202024-10-08%20095714.png)

- `<blockquote>` tag–This tag defines large quoted sections.

**Example**

```html
<p>Here is a quote from WWF's website:</p>

<blockquote cite="http://www.worldwildlife.org/who/index.html">
For 50 years, WWF has been protecting the future of nature. The world's leading conservation organization, WWF works in 100 countries and is supported by 1.2 million members in the United States and close to 5 million globally.
</blockquote>
```

**Output**

![Images](../HTML%20Interview_Question/Images/Screenshot%202024-10-08%20095911.png)

5. **Define the list types in HTML.**
  
The list types in HTML are as follows:

  - **Ordered list** – The ordered list uses `<ol>` tag and displays elements in a numbered format.

**Example**

```HTML
<! DOCTYPE html>
<html>
<head>
    <title>HTML Lists</title>
</head>
<body>
<h2>Months</h2>
    <ul>
        <li>January</li>
        <li>February</li>
        <li>March</li>
        <li>April</li>
    </ul>
</body>
</html>
```

**Output**

![images](../HTML%20Interview_Question/Images/Screenshot%202024-10-08%20101602.png)

  - **Unordered list** – The unordered list uses `<ul>` tag and displays elements in a bulleted format.
    
**Example**

```HTML
<html>
<head>
    <title>HTML Lists</title>
</head>
<body>
<h2>Months</h2>
    <ol>
        <li>January</li>
        <li>February</li>
        <li>March</li>
        <li>April</li>
    </ol>
</body>
</html>
```

**Output**

![images](../HTML%20Interview_Question/Images/Screenshot%202024-10-08%20101056.png)

  - **Definition list** – The definition list uses `<dl>`, `<dt>`, `<dd>` tags and displays elements in definition form like in a dictionary.

**Example**

```HTML
<html>
<head>
    <title>HTML Lists</title>
</head>
<body>
<h2>Months</h2>
    <dl>
        <dt>January</dt>
            <dd>First Months</dd>
        <dt>February</dt>
            <dd>Second Months</dd>
        <dt>March</dt>
            <dd>Third Months</dd>
        <dt>April</dt>
            <dd>Fourth Months</dd>
    </dl>
</body>
</html>
```

**Output**

![Images](../HTML%20Interview_Question/Images/Screenshot%202024-10-08%20102227.png)

6. **How do you align list elements in an HTML file?**
  
We can align the list elements in an HTML file using indents. If you indent each nested list further than the 
parent list, you can easily align and determine the various lists and their elements.

7. **Differentiate between an Ordered list and an Unordered list.** 

- An unordered list uses `<ul> </ul>` tags, and each element of the list is written between `<li> </li>` tags. 
The list items are displayed as bullets rather than numbers.

- An ordered list uses `<ol> </ol>` tags, and each element of the list is written between `<li> </li>` tags. 
The list items are displayed as numbers rather than bullet points.

**Example**

```HTML
<!DOCTYPE html>
<html>
  <body>
    <h2>HTML List Example</h2>
    <ul>
      <li>Coffee</li>
      <li>Tea</li>
      <li>Milk</li>
    </ul>
    <ol>
      <li>Coffee</li>
      <li>Tea</li>
      <li>Milk</li>
    </ol>
  </body>
</html>
```

**Output**

![images](../HTML%20Interview_Question/Images/html-list-example-23.jpeg)

8. **What is an element in HTML?**
    
An element in HTML is a set of tags that define a specific part of a web page. It consists of a 
start tag, content, and an end tag.

9. **What is the difference between HTML and CSS?**
  
HTML creates a web page's structure and content, while CSS defines its appearance and layout.

10. **What are void elements in HTML?**

Void elements in HTML are tags that do not require a closing tag. They are used to insert images, line breaks, and other content that does not require additional information.

11. **What is the advantage of collapsing white space?**
  
Collapsing white space in HTML can help reduce web pages' size and make them load faster. It involves removing unnecessary white space between HTML elements.

12. **What are HTML Entities?**
  
HTML Entities are special characters used to represent characters that cannot be typed on a keyboard. They are often used to display special symbols and foreign characters.

13. **How do you display a table in an HTML webpage?**
   
The HTML `<table>` tag displays data in a tabular format. It is also used to manage the layout of the page, 
for example, the header section, navigation bar, body content, and footer section. Given below is the list of HTML tags used for displaying a table on an HTML webpage:

|      Tag      |                                    Description                                     |
|---------------|------------------------------------------------------------------------------------|
|  `<table>`    | It defines a table.                                                                |
|  `<tr>`       | It defines a row in a table.                                                       |
|  `<th>`       | It defines a header cell in a table.                                               |
|  `<td>`       | It defines a cell in a table.                                                      |
|  `<caption>`  | It defines the table caption.                                                      |
|  `<colgroup>` | It specifies a group of one or more columns in a table for formatting.             |
|  `<col>`      | It is used with `<colgroup>` element to specify column properties for each column. |
|  `<tbody>`    | It is used to group the body content in a table.                                   |
|  `<thead>`    | It is used to group the header content in a table.                                 |
|  `<tfooter>`  | It is used to group the footer content in a table.                                 |

14. **How would you display the given table on an HTML webpage?**

**Example**

```HTML
<table>
  <tr>
    <td>50 pcs</td>
    <td>100</td>
    <td>500</td>
  </tr>
  <tr>
    <td>10 pcs</td>
    <td>5</td>
    <td>50</td>
  </tr>
</table>
```

**Output**

![Images](../HTML%20Interview_Question/Images/Screenshot%202024-10-08%20102525.png)

15. **How do we insert a comment in HTML?**
    
We can insert a comment in HTML by beginning with a lesser than sign and ending with a greater than sign. For example, “<!-“ and “->.”

16. **How do you insert a copyright symbol in HTML?**
  
To insert a copyright symbol in HTML, you can use the HTML entity &copy or the numeric code `&#169`;

17. **What is white space in HTML?**
   
An empty sequence of space characters is called white space in HTML. It is considered a single-space character.

White space helps the browser merge multiple spaces into one space, making indentation easier. It also helps better organize the content and tags, making them readable and easily understood.

18. **How do you create links to different sections within the same HTML web page?**

We use the `<a>` tag and referencing through the # symbol to create several links to different sections within the same web page.

19. **How do you create a hyperlink in HTML?**
    
We use the anchor tag `<a>` to create a hyperlink in HTML that links one page to another. The hyperlink can be added to images, too.

20. **Define an image map.**
  
An image map in HTML helps link different kinds of web pages using a single image. It can also be used to define shapes in the images used in the image mapping process.

21. **Why do we use a style sheet in HTML?**
    
A style sheet helps create a well-defined, consistent, and portable HTML webpage template. We can link a single style sheet template to various web pages, which makes it easier to maintain and change the website's look.

22. **What is semantic HTML?**
  
Semantic HTML is a coding style that uses HTML markup to reinforce the semantics or meaning of the content. 

For example, in semantic HTML, the `<b> </b>` tag is not used for bold statements as well, and the `<i> </i>` tag is not used for italics. Instead of these, we use `<strong></strong>` and `<em></em>` tags.

23. **What is SVG in HTML?**
    
HTML SVG describes vector or raster graphics. SVG images and their behaviors are defined in XML text files. 

We primarily use it for vector-type diagrams like pie charts and 2-dimensional graphs in an X-Y coordinate system.

**Example**

```HTML
<svg width="100" height="100">
  <circle cx="50" cy="50" r="40" stroke="yellow" stroke-width="4" fill="red" />
</svg>
```

**Output**

![images](../HTML%20Interview_Question/Images/Screenshot%202024-10-08%20102745.png)

24. **What would happen without text between the HTML tags?**
  
There would be nothing to format if there is no text present between the tags. Therefore, nothing will appear on the screen. 

Some tags, such as those without a closing tag like the <img> tag, do not require any text between them.

25. **How do you create nested web pages in HTML?**
    
Nested web pages mean a webpage within a webpage. We can create nested web pages in HTML using the built-in iframe tag. The HTML `<iframe>` tag defines an inline frame. For example:

**Example**

```HTML
<!DOCTYPE html>
<html>
  <body>
    <h2>HTML Iframes example</h2>
    <p>
      specify the size of the iframe using the height and width attributes:
    </p>
    <iframe src="https://simplilearn.com/" height="600" width="800"></iframe>
  </body>
</html>
```

**Output**
![Images](../HTML%20Interview_Question/Images/Screenshot%202024-10-08%20131834.png)

26. **How do you add buttons in HTML?**
    
We can use the built-in Button tag in HTML to add buttons to an HTML web page.

**Example**

```HTML
<!DOCTYPE html>
<html>
  <body>
    <h2>HTML Button Tag Example</h2>
    <button name="button" type="button">CLICK ME</button>
  </body>
</html>
```

**Output**

![Images](../HTML%20Interview_Question/Images/Screenshot%202024-10-08%20132219.png)

27. **What are the different types of headings in HTML?**
  
There are six heading tags in HTML, defined with the ``<h1>`` to `<h6>` tags. Each type of heading tag displays a different text size from another. ``<h1>`` is the largest heading tag and `<h6>` is the smallest. For example:

```HTML
<!DOCTYPE html>
<html>
  <body>
    <h1>This is Heading 1</h1>
    <h2>This is Heading 2</h2>
    <h3>This is Heading 3</h3>
    <h4>This is Heading 4</h4>
    <h5>This is Heading 5</h5>
    <h6>This is Heading 6</h6>
  </body>
</html>
```

**output**

![Images](../HTML%20Interview_Question/Images/heading-html.jpeg)

28. **How do you insert an image in the HTML webpage?**
  
You can insert an image in the HTML webpage by using the following code:

```HTML
<!DOCTYPE html>
<html>
  <body>
    <h2>HTML Image Example</h2>
    <img src="tulip.jpeg" />
  </body>
</html>
```

**Output**

![Images](../HTML%20Interview_Question/Images/Screenshot%202024-10-08%20133014.png)

29.  **What is the alt attribute in HTML?**
  
The alt attribute displays text in place of an image whenever the image cannot be loaded due to technical issues.

**Example**

```HTML
<!DOCTYPE html>
<html>
  <body>
    <h2>HTML Alt Example</h2>
    <img src="tulip.jpeg" alt="Tulip Garden" />
  </body>
</html>
```

**Output**

![Images](../HTML%20Interview_Question/Images/Screenshot%202024-10-08%20133413.png)


30.  **How are hyperlinks inserted in the HTML webpage?**
  
You can insert a hyperlink in the HTML webpage by using the following code:

**Example**

```HTML
<!DOCTYPE html>
<html>
  <body>
    <h2>HTML Hyperlink Example</h2>
    <a href="https://github.com/SwayaanTechnologies/InterviewMaterial">link text</a>
  </body>
</html>
```

**Output**

![Images](../HTML%20Interview_Question/Images/Screenshot%202024-10-08%20172712.png)

31.  **How do you add color to the text in HTML?**
  
You can add color to the text in HTML by using the following code:

**Example**

```HTML
<!DOCTYPE html>
<html>
  <body>
    <h2>HTML Color Text Example</h2>
    <h1 style="color: Red">Hello HTML</h1>
    <p style="color: Blue">Line 1</p>
    <p style="color: Green">Line 2</p>
  </body>
</html>
```

**Output**

![Images](../HTML%20Interview_Question/Images/Screenshot%202024-10-08%20173002.png)

32.  **How do you add CSS styling in HTML?**
    
There are three ways to include the CSS with HTML:

- **Inline CSS:** It is used when less styling is needed or in cases where only a single element has to be styled. To use inline styles add the style attribute in the relevant tag.
- **External Style Sheet:** This is used when the style is applied to many elements or HTML pages. Each page must link to the style sheet using the `<link>` tag:

**Example**

```HTML
<head>
  <link rel="stylesheet" type="text/css" href="style.css" />
</head>
```

**Output**

File connection to CSS in style.css easy to the connected

- **Internal Style Sheet:** It is used when a single HTML document has a unique style, and several elements must be styled to follow the format. Internal styles sheet is added in the head section of an HTML page by using the <style> tag:

**Example**

```HTML
<head>
  <style type="text/css">
    hr {
      color: sienna;
    }
    p {
      margin-left: 20px;
    }
    body {
      background-image: url("images/back40.gif");
    }
  </style>
</head>
```

**Output**

![Images](../HTML%20Interview_Question/Images/Screenshot%202024-10-08%20173754.png)

33.  **What hierarchy do the style sheets follow?**
  
If a single selector includes three different style definitions, the definition closest to the actual tag takes precedence. Inline style takes priority over embedded style sheets, which take priority over external style sheets.

34.  **How do you add JavaScript to an HTML webpage?**
  
JavaScript is used to make HTML web pages more interactive and user-friendly. It is a scripting language that allows you to interact with some aspects of the page based on user input. As with CSS, there are three significant ways of including JavaScript:

**Inline:**
You can add JavaScript to your HTML elements directly whenever a certain event occurs. We can add the JavaScript code using attributes of the HTML tags that support it. Here is an example that shows an alert with a message when the user clicks on it:

**Example**

```HTML
<button onclick="alert('Click the Button!');">
Click!
</button>
```

**Output**

![Images](../HTML%20Interview_Question/Images/Screenshot%202024-10-08%20174229.png)

**Script block:**
You can define a script block anywhere on the HTML code, which will get executed as soon as the browser reaches that part of the document. This is why script blocks are usually added at the bottom of HTML documents.

**Example**

```HTML
<html>
  <script>
    var x = 1;
    var y = 2;
    var result = x + y;
    alert("X + Y is equal to " + result);
  </script>
</html>
```

**Output**

![Images](../HTML%20Interview_Question/Images/Screenshot%202024-10-08%20180550.png)

**External JavaScript file:**
You can also import the JavaScript code from a separate file and keep your HTML code clutter-free. This is especially useful if a large amount of scripting is added to an HTML webpage.

**Example**

```HTML
<html>
  <script src="my-script.js"></script>
</html>
```

35. **What are the different types of lists in HTML?**
 
In HTML, there are three lists: ordered, unordered, and definition. Ordered lists are numbered, unordered lists are bulleted, and definition lists are lists of terms and their definitions.

36. **What is the ‘class' attribute in HTML?**
   
The ‘class' attribute in HTML defines a class for an HTML element. It can be used to apply a specific style to a group of elements on a web page.

37. **What is the difference between the ‘id' and ‘class' attributes of HTML elements?**
   
The ‘id' attribute defines a unique identifier for an HTML element, while the ‘class' attribute defines a class for a group of elements. An ‘id' can only be used once on a page, while a ‘class' can be used multiple times.

38. **What is the difference between HTML and XHTML?**

HTML and XHTML are both markup languages used to create web pages. However, XHTML is stricter than HTML and requires developers to write well-formed code that adheres to specific rules and guidelines. XHTML also requires all tags to be closed and all attributes to be quoted.

39. **What is the difference between HTML and HTML5?**

HTML5 is the latest version of HTML and includes new features and improvements over previous versions. Some key differences between HTML and HTML5 include support for multimedia elements (such as video and audio), improved semantics, and better support for mobile devices.

