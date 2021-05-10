# QA Backend Exercise

Service for testing RESTful API.


1.	Get a list of users with name filter
	```bash
	curl -X GET http://localhost:8000/user?name=hi | jq
	```
2.	Add user to list
	```bash
	curl -X POST --header "Content-Type: application/json" -d '{"name":"My name"}' http://https://qa-backend-exercise.herokuapp.com/user
	```
3. 	Remove user from list
	```bash
	curl -X DELETE --header "Content-Type: application/json" -d '{"name":"My name"}' https://qa-backend-exercise.herokuapp.com/user
	```

---

[Live](https://qa-backend-exercise.herokuapp.com)