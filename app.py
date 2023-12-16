import requests
import streamlit as sl

api_url = 'https://vidsrc.xyz/episodes/latest/page-1.json'
response = requests.get(api_url)
cachedBody = []

json_data = response.json()



sl.title("VidSrc: Display")

sl.write("> Latest Released Episodes Here!")

for i in range(len(json_data["result"])):
    cachedBody.append(json_data["result"][i])
    sl.write(f"""
| Method | Accuracy |
| ----------- | ----------- |
| {json_data["result"][i][1]} | {json_data["result"][i][0]}% |
""")
