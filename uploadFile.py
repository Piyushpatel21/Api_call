import requests
import json
import csv
from io import StringIO

quotedData = StringIO()
BASE_URL = 'https://pa2ybxr56j.execute-api.us-east-1.amazonaws.com/master'
headers = {

    "role_id": "admin-role-675833eb-8d30-4e73-b2af-288c59ed5ded",
    "Authorization":"eyJraWQiOiIwXC9VSFNDV0JQUk45aHdvVDdKalpScElSczNOdUVUaFRTcWlpSkFvbEQzUT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIwNzIyZDE4Yi0yOTI5LTQ1ZjktOGU3My1jNjU3ODkxYTc2NmEiLCJhdWQiOiI2ZnZzZGhkNWlqNm44dGVrZTNjZ2xmcm9rdCIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJldmVudF9pZCI6Ijc2MjJjYTc0LTBiNTctNDI5YS1iYjQ3LTYwYzllYmMzNzU3NSIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNTkwOTg4MzQ1LCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9XMlBSeDJKdlIiLCJuYW1lIjoiUGl5dXNoIFBhdGVsIiwiY29nbml0bzp1c2VybmFtZSI6InBpeXVzaCIsImV4cCI6MTU5MTAyNjE0OSwiaWF0IjoxNTkxMDIyNTQ5LCJlbWFpbCI6InBpeXVzaC5wYXRlbEBjbG91ZHdpY2suY29tIn0.UhBmDNsX6kfmMXgjC7o2C4PQ1XWdhTihxx_mJ4YtYnzKa9kaSgBB7RcCrGls-jfkJVYq5RNvjayw6EKdtqDjZqQddJFRgZGT1273IooneCF8t4BHd-Q1Lpb50qLl4Ueidxixm6QK8GtqgXha3WXF6g9ODCOYE9lLYJjbuKuwYLhUbqFnkY-7tIv8_Mm_ckWoWsYOcJAyE1EJALW0lavzQd0_Shl9wJdUY8Y2aThFqBDTuF4C_p6ykC93u7FM3_2RMOjg9fBUjH7Tq13TKuSqIM6B67nb5MiaehsNZKLNDPSLbPvWSUB1E5d1TJKhps4pABl4GvxqAv_Sss2_Ha8-9w"
    # "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIwYzhlOWZiZC1iMzc2LTQ1MWUtYjUwNS0yYTViNmQ4NjgzOGYiLCJhdWQiOiJkMnhjYWNpNjVwY2x1MyIsImlzcyI6IlBBVF9HRU4iLCJ0b2tlbl91c2UiOiJwYXQiLCJuYW1lIjoicGl5dXNoIiwiY29nbml0bzp1c2VybmFtZSI6InBpeXVzaCIsInJvbGUiOiJyb2xlLTM4OTA0OTg3LTFiOTYtNDVlNS1iYmFjLTgxMjdmMGMwNWFlMyIsImV4cCI6MTU5MzQ5NDc2MCwiZW1haWwiOiJwaXl1c2gucGF0ZWxAY2xvdWR3aWNrLmNvbSIsImlhdCI6MTU5MDk4OTE5N30._IOgnc6DG8dducr1m5JUq7BGXFjaW5Yc5AuJ_WenYofTJeTRy1HeDnMvx7H8YHQ8I52sOE58-YZI-oR-WtUjiA"
}

params = {

    "DatasetId":"6eb6a0a7-1848-47bd-bf12-89bc7fcfdf1f",
    "FileName":"kony_tds_9.csv"
}

response = requests.post(BASE_URL+"/datasets/file", headers=headers, json=params)
y = json.loads(response.text)
S3Url = y["Message"]

print(S3Url)

#//put csv data
f = open("/Users/piyushpatel/Downloads/SGN/kony_data.csv", "r")
#print(f.read())


data=f.read()
print (data)

response = requests.put(S3Url, data=data)
print(response)

