import requests


def webex_alert(message):

    url = "https://api.ciscospark.com/v1/messages"

    payload = "{\n  \"roomId\": \"Y2lzY29zcGFyazovL3VzL1JPT00vZGEwMzA3NTAtNTdhNi0xMWU5LTlmYTMtNTU2MTE3YTAyZmQ2\",\n  \"markdown\": \"%s\"\n}\n" % (message)
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer NmNkMjIwZWYtM2Y4OC00NzJmLWEzYWEtZGNiZGNlYWI5NTViMTkwOTlmZTUtYjg5_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f",
        'cache-control': "no-cache",
        'Postman-Token': "0a528c48-53ed-4d1c-ae6f-4cfbdf4e69e0"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)

# NTQyYjlhM2QtYTkwNS00ZWU3LTg0OGYtNmE3OWQ2ZmY0YjNkOTI0Y2I3ZGMtNDEw_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f
