#Simple Flask App

To run the Flask app via Docker Follow the steps below:

1. Build the Docker image via command prompt/terminal
`docker build -t myapp:v1 .`

2. Run the container, be sure to specify the ports:
`docker run -p 5000:5000 myapp:v1`

3. Test the GET method in another command prompt/terminal
`curl -X GET http://localhost:5000`

4. Test the POST method in another command prompt/terminal
`curl -X POST -d "data=test" http://localhost:5000`