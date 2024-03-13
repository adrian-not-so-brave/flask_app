#!bin/bash

#test the get method
curl -X GET http://localhost:5000

#test the put method
curl -X POST -d "data=test" http://localhost:5000