import requests

BASE_URL = 'https://pa2ybxr56j.execute-api.us-east-1.amazonaws.com/master'
headers = {
    "role_id": "admin-role-675833eb-8d30-4e73-b2af-288c59ed5ded",
    "Authorization": "eyJraWQiOiIwXC9VSFNDV0JQUk45aHdvVDdKalpScElSczNOdUVUaFRTcWlpSkFvbEQzUT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIwNzIyZDE4Yi0yOTI5LTQ1ZjktOGU3My1jNjU3ODkxYTc2NmEiLCJhdWQiOiI2ZnZzZGhkNWlqNm44dGVrZTNjZ2xmcm9rdCIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJldmVudF9pZCI6ImExYmMwNDYyLWVmMmItNDhlZS04ZmU2LTY5Njc0NDljNjZmNiIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNTkwOTk1NjI5LCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9XMlBSeDJKdlIiLCJuYW1lIjoiUGl5dXNoIFBhdGVsIiwiY29nbml0bzp1c2VybmFtZSI6InBpeXVzaCIsImV4cCI6MTU5MDk5OTIyOSwiaWF0IjoxNTkwOTk1NjI5LCJlbWFpbCI6InBpeXVzaC5wYXRlbEBjbG91ZHdpY2suY29tIn0.U9mYRNJDtdgWQuVnIW3Jc0wcqHPEEjC8g2IvZ607xdOQOrijKOq0xtlaDQcGgX08VxpH30qf4x2XwHySqj_qRI0p2MgYXZq3PJa665a9QtpkhyYrwE371gjVGlVgK-wJolTuGo2010iCiv_PXIGJLvA2AeI4BnOByzbQ2qPFTd6F_sT_jwf3IKc8VsmHuJou-gC_oF58eDPp7ixkqiACrCcyPpoTFZFg0kgcA5JFv8f8D47ugszMz_dO_mL5V4xCvXKS9hR5j8QEu5m5fCvIkngnfKSiMKCZHnD2_Dcy6DxNXr6UjrSzur3MZL1Q6q40-Ck3Z4dsoNpyeN5FdHoj8A"

    # "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIwYzhlOWZiZC1iMzc2LTQ1MWUtYjUwNS0yYTViNmQ4NjgzOGYiLCJhdWQiOiJkMnhjYWNpNjVwY2x1MyIsImlzcyI6IlBBVF9HRU4iLCJ0b2tlbl91c2UiOiJwYXQiLCJuYW1lIjoicGl5dXNoIiwiY29nbml0bzp1c2VybmFtZSI6InBpeXVzaCIsInJvbGUiOiJyb2xlLTM4OTA0OTg3LTFiOTYtNDVlNS1iYmFjLTgxMjdmMGMwNWFlMyIsImV4cCI6MTU5MzQ5NDc2MCwiZW1haWwiOiJwaXl1c2gucGF0ZWxAY2xvdWR3aWNrLmNvbSIsImlhdCI6MTU5MDk4OTE5N30._IOgnc6DG8dducr1m5JUq7BGXFjaW5Yc5AuJ_WenYofTJeTRy1HeDnMvx7H8YHQ8I52sOE58-YZI-oR-WtUjiA"
}

params = {

    "DatasetName":"api_call_6",
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
print(response.text)

