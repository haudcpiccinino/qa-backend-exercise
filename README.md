# QA Backend Exercise


Add user to list
```bash
curl -X POST --header "Content-Type: application/json" -d '{"name":"My name"}' http://localhost:8000/user
```

Remove user from list

```bash
curl -X DELETE --header "Content-Type: application/json" -d '{"name":"My name"}' http://localhost:8000/user
```

---

[Link](https://qa-backend-exercise.herokuapp.com)