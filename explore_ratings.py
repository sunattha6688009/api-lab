import uuid
import requests

SITE = "https://quickpizza.grafana.com"
s = requests.Session()

user = {"username": "lab-" + uuid.uuid4().hex[:12], "password": "Pizza-2026"}
s.post(SITE + "/api/users", json=user)
token = s.post(SITE + "/api/users/token/login", json=user).json()["token"]
mine = {"Authorization": "token " + token}
pid = s.post(SITE + "/api/pizza", json={}, headers=mine).json()["pizza"]["id"]


def show(label, body, headers):
    res = s.post(SITE + "/api/ratings", json=body, headers=headers)
    print(label, "->", res.status_code, res.text)


show("C2 decimal", {"pizza_id": pid, "stars": 3.5}, mine)
show("C2 text", {"pizza_id": pid, "stars": "3"}, mine)
show("C2 missing", {"pizza_id": pid}, mine)
show("C3 no pizza", {"pizza_id": 999999999, "stars": 3}, mine)
show("C4 no header", {"pizza_id": pid, "stars": 3}, {})
show("C4 short token", {"pizza_id": pid, "stars": 3}, {"Authorization": "token abc"})