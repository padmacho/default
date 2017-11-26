# Introduction to html
- HTML stands for HyperText Markup Language.
- It is an angle based structure language that allows you to define different parts of a page, some visible to the users and some not visible to the users
- It is derived from the SGML language

# Simple HTML Document
```HTML
<html>
  <head>
    <title>Hello Title</title>
  </head>
  <body>
    <h1>Hello World</h1>
  </body>
</html>
```
- **head** contains meta data
- **body** contains visual data what user would see
- Mark up is **Not case sensitive**
- Few tags doesn't have body

# Document Object Model (DOM)
- HTML relies on DOM
- It is an hierarchy of elements
- It represents object graph at runtime
![Dom](dom.png)
# Elements
- Element is a name of an object and it's surrounded by two angle brackets
-  To end an element you're going to start with that same greater than and less than with the same names we have here, but you're going to start it with a **slash** in front of it.

```html
<element>Element body</element>
<bar/> <!-- Element with out body -->

<foo /> <!-- Foo and bar is sibling relationship -->
<bar />


<foo>
  <bar/> <!-- hierarchy relationship -->
</foo>

```
# Div Tag
A div is a basic unit in HTML that says this is a portion of my webpage
```HTML
<div>
  <img />
  <p>Hello world</p>
</div>
```
# Attributes
Attributes are **name value** pairs. An attribute either modifies the default functionality of an element type or provides functionality to certain element types unable to function correctly without them
```HTML
<div id="top">
  <img src="abc.img" alt="abc image"/>
  <p>Hello world</p>
</div>
```
# [Web dev Home](index.html)
