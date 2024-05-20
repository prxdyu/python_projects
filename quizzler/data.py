import requests
api_endpoint="https://opentdb.com/api.php"
parameters={"amount":10,"type":"boolean"}
response=requests.get(url=api_endpoint,params=parameters)
question_data=response.json()["results"]
