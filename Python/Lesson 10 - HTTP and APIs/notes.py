import requests


# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
# print(response.status_code)
# print(response.reason)


# response = requests.get("https://jsonplaceholder.typicode.com/posts/1/posts/1")
# content_type = response.headers.get("Content-Type", "<missing>")
# elapsed_ms = int(response.elapsed.total_seconds() * 1000)

# print(f"Content-Type: {content_type}")
# print(f"Elapsed: {elapsed_ms} ms")


# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# try:
#     data = response.json()

#     print(f"userId: {data['userId']}")
#     print(f"id: {data['id']}")
#     print(f"title: {data['title']}")

# except ValueError:
#     print("Response body was not valid JSON")

# import requests

# params = {"postId": 1}

# response = requests.get(
#     "https://jsonplaceholder.typicode.com/comments",
#     params=params
# )

# comments = response.json()

# print(f"Comments returned: {len(comments)}")

# if comments:
#     print(f"First email: {comments[0]['email']}")
########################################################

from requests.auth import HTTPBasicAuth

BASE_URL = "https://httpbin.org"

response = requests.get(
    f"{BASE_URL}/basic-auth/student/pass123",
    auth=HTTPBasicAuth("student", "pass123"),
)

print(response.status_code)
print(response.json())
###################################################

headers = {"Authorization": "Bearer ayeooo"}
response = requests.get(f"{BASE_URL}/bearer", headers=headers)

print(response.status_code)
print(response.json())

#####################################################

api_key = "key-001"

header_response = requests.get(f"{BASE_URL}/get", headers={"X-API-Key": api_key})
query_response = requests.get(f"{BASE_URL}/get", params={"api_key": api_key})

header_json = header_response.json()
query_json = query_response.json()

print(f"Header API key: {header_json['headers'].get('X-Api-Key')}")
print(f"Query API key: {query_json['args'].get('api_key')}")