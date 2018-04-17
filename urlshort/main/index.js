'use strict';

const base_page = `<html>
<body>
<h1>URL Shortener</h1>
<p>Enter a link in the field below, and a short link will be generated for future use</p>
  <form method="POST" action="">
    <label for="uri">Link:</label>
    <input type="text" id="link" name="link" size="40" autofocus />
    <br />
    <br />
    <input type="submit" value="Shorten It" />
  </form>
</body>
</html>`

module.exports.handler = (event, context, callback) => {
    console.log(JSON.stringify(event));
    callback(
        null,
        {
            statusCode: 200,
            body: base_page,
            headers: {'Content-Type': 'text/html'},
        }
    );
}
