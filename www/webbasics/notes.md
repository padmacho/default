# Basics of HTML
# Elements
- DOCTYPE
   - This is strictly not an element that is part of the HTML standard, but it does tell the browser that this is an HTML document and tells it which version of HTML it is written in
- HEAD
   - This can include a title for the document, scripts, styles, metainformation, and more
- BODY
   - The body element that contains everything that you want to be displayed on the screen.

```HTML
<!DOCTYPE html>
<html>
  <head>
    <!--meta information -->
  </head>
  <body>
    <!-- the content of the page -->
  </body>
</html>
```
# Expressive Elements
They explain what they are used for so that the browser can understand them better and search engines know better which parts of the document are actual data and which parts are meta information.
- Header
   - A header element, which represents a container for introductory content or a set of navigational links
   - nav
    - nav tag that defines a set of navigation links
- main
  - Specifies the main content of a document
  - article
    - specifies independent, self-contained content
  - aside
    -  specifies independent, self-contained content
- footer
  - copyright or the address of your company

```HTML
<!DOCTYPE html>
<html>
<head></head>
<body>
  <header>
    <nav />
  </header>
  <main>
    <article />
    <aside />
  </main>
  <footer>
    <address />
  </footer>
</body>
</html>
```
# Interactive HTML Elements
- audio
- canvas
- form
   - input
- video 
