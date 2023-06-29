# Phishig Website
This is a phishing website that is meant to emulate the instagram.com login page to phish credentials.

# Technologies
The front end is built in Vue.js and the backend is built in Flask.
When the user attempts to log in, the frontend makes an api call to the Flask server, and the serer appends the user credentials to a text file.
After the user "logs in" they are redirected to the real instagram login page.
