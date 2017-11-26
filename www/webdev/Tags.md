# Tags
Some important tags in html
# div
- div is a block element
- Div is a section of an html page
- Divs themselves don't have any UI to them unless you tell them to color or add elements
- It represents a rectangle section of the page
- These are commonly used for header, footer and body for the page

# Escape characters or Special characters or HTML Entities
- Reserved characters in HTML must be replaced with character entities
- Characters that are not present on your keyboard can also be replaced by entities
```html
&copy;
&gt;
&lt;
```

# Span
- Span represents inline container
- This means that to use them semantically, divs should be used to wrap sections of a document, while spans should be used to wrap small portions of text, images, etc.

```html
<div>This a large main division, with <span>a small bit</span> of spanned text!</div>
```

# Semantic Tags
- Semantic Tag  is the use of HTML markup to reinforce the semantics, or meaning, of the information in webpages and web applications rather than merely to define its presentation or look
- Semantic HTML is processed by traditional web browsers as well as by many other user agents
- Examples of **non-semantic** elements: <div> and <span> - Tells nothing about its Content
- Examples of semantic elements: <form>, <table>, and <article> - Clearly defines its content


Tag|Description
---|---
header| header of a Page
footer| Footer of a Page
section| element defines section in a document
nav| It defines a set of navigation links.Notice that NOT all links of a document should be inside a <nav> element. The <nav> element is intended only for major block of navigation links

```html
<html>
  <head>
    <title>My title</title>
  </head>
  <body>
  <header>This is header of the page</header>
  <section>Body of the blog</section>
  <footer>This is footer of the page</footer>
  </body>
</html>
```
# Lists
**ordered** list **<ol>** and **unorderd** list **<ul>**
- **<li>** list item
```HTML
<ol>
  <li>mango</li>
  <li>apple</li>
</ol>
<ul>
  <li>mango</li>
  <li>apple</li>
</ul>
```


# [Web dev Home](index.html)
