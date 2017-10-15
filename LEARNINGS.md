1. What is the function of the following technologies in your assignment:
HTML: Provide structure/content
CSS: Provide styling for the HTML elements
JavaScript: Validate the contact form (stop if not all fields are filled/continue with POST request if all filled)
Python: Acts as a server
Flask: Flask is a Python microframework to help service get/post requests for my site
HTTP: protocol to request particular resources
GET and POST requests: GET requests resources, POST can modify/put resources

2. How does HTML, CSS, and JavaScript work together in the browser for this assignment?
HTML provides the content which is styled by CSS. JavaScript waits for the contact form submission to go through then validates it with a validation function.

3. How does Python and Flask work together in the server for this assignment?
Python is the language which the server is written in. Flask is a framework which handles GET and POST requests and serves the appropriate HTML/CSS/JS files.

4. List all of the possible GET and POST requests that your server returns a response for and describes what happens for each GET and POST request
GET: All the links to the webpages in the header/footer and the blogposts are all GET requests. They request the particular HTML file associated with the link.
POST: The only post request is the contact form submission. In this case, a user submits (posts) information.