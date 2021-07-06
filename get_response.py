import requests
import json

def request_status(response):
    try:
        if (response.status_code < 400):
            y = json.loads(response.text)
            DatasetId = y["DatasetId"]
            Message = y["Message"]
            print("Sucess:  " + str('status code :') + str(response.status_code) + ' ' + str(Message))

        else:
            y = json.loads(response.text)
            print(y)
            Message = y["Message"]
            print("error:  " + str('status code :') + str(response.status_code) + '' + str(Message))
            DatasetId = None

    except requests.ConnectionError:
        print("failed to connect")
    return DatasetId



BASE_URL = 'https://pa2ybxr56j.execute-api.us-east-1.amazonaws.com/master'
headers = {
    "role_id": "admin-role-675833eb-8d30-4e73-b2af-288c59ed5ded",
    "Authorization": "eyJraWQiOiIwXC9VSFNDV0JQUk45aHdvVDdKalpScElSczNOdUVUaFRTcWlpSkFvbEQzUT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIwNzIyZDE4Yi0yOTI5LTQ1ZjktOGU3My1jNjU3ODkxYTc2NmEiLCJhdWQiOiI2ZnZzZGhkNWlqNm44dGVrZTNjZ2xmcm9rdCIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJldmVudF9pZCI6Ijc2MjJjYTc0LTBiNTctNDI5YS1iYjQ3LTYwYzllYmMzNzU3NSIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNTkwOTg4MzQ1LCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9XMlBSeDJKdlIiLCJuYW1lIjoiUGl5dXNoIFBhdGVsIiwiY29nbml0bzp1c2VybmFtZSI6InBpeXVzaCIsImV4cCI6MTU5MTA4MjU4NCwiaWF0IjoxNTkxMDc4OTg0LCJlbWFpbCI6InBpeXVzaC5wYXRlbEBjbG91ZHdpY2suY29tIn0.CYYxe3wNPFoxdMv-u6haavw-6mZg0o8V9UHezmRCvJToPzsTJKfLMRLV-Q4HR45h9-CxQoRRQVUL8SJ6XC8FZk4-JNPEoVfv1hXWlewpStm3jOE0uWjO4He5A_OgSfcj7PFgLhH4-KGgzabEqgRlmmoyEy5KdIc7_pn9gJjieguFj4-jWzgejBxr4wqBQv7vtrmHUxykBWGKK3oWNAQWCUWiTbBZRA0Lf2AA11KSX4SsvBFiChorPjgz_perKpOI5sH_czQdLcmk2SDzoC63cXlBLzGm13UmgrmSR1d50yR3NmC4EVfdBe_VWin6bqAbjy7igbHroCIP4APcGTAKyQ"
    # "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIwYzhlOWZiZC1iMzc2LTQ1MWUtYjUwNS0yYTViNmQ4NjgzOGYiLCJhdWQiOiJkMnhjYWNpNjVwY2x1MyIsImlzcyI6IlBBVF9HRU4iLCJ0b2tlbl91c2UiOiJwYXQiLCJuYW1lIjoicGl5dXNoIiwiY29nbml0bzp1c2VybmFtZSI6InBpeXVzaCIsInJvbGUiOiJyb2xlLTM4OTA0OTg3LTFiOTYtNDVlNS1iYmFjLTgxMjdmMGMwNWFlMyIsImV4cCI6MTU5MzQ5NDc2MCwiZW1haWwiOiJwaXl1c2gucGF0ZWxAY2xvdWR3aWNrLmNvbSIsImlhdCI6MTU5MDk4OTE5N30._IOgnc6DG8dducr1m5JUq7BGXFjaW5Yc5AuJ_WenYofTJeTRy1HeDnMvx7H8YHQ8I52sOE58-YZI-oR-WtUjiA"
}

params = {

    "DatasetName":"api_call_12",
    "DatasetDescription":"SGN_API",
    "Domain":"sgnbidevtest",
    "ConnectionType":"api",
    "DataClassification":["SGNBIhighlyConfidential"],
    "TargetLocation":"s3",
   "Keywords":["Owner:piyush"],
    "TableUpdate":"append",
    "MalwareDetectionOptions":
        {
            "ScanForMalware":False,
            "AllowUnscannableFiles":True
         },
    "FileType":"csv",
    "SkipFileHeader":False,
    "IsDataProfilingEnabled":False
}

response = requests.post(BASE_URL+"/datasets", headers=headers, json=params)

request_status(response)
e

print(response.text)
print(response.status_code)
y = json.loads(response.text)

DatasetId = y["DatasetId"]
Message = y["Message"]
print(DatasetId)
print(Message)
print("##########")

