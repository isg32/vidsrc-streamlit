import requests
import streamlit as sl

api_url = 'https://vidsrc.xyz/episodes/latest/page-1.json'
response = requests.get(api_url)
cachedBody = []

json_data = response.json()

for i in range(len(json_data["result"])):
    cachedBody.append(json_data["result"][i])

markdown_code = ""

# Iterate through the list
for item in cachedBody:
    markdown_code += f"""
| {item["show_title"]} | {item["season"]} | {item["episode"]} | [Play]({item["embed_url"]}) |
|----------------------|------------------|-------------------|-----------------------------|
"""

sl.title("VidSrc: Display")
sl.write("> Latest Released Episodes Here!")
sl.write(f"""
| Name | Season | Episode | URL|
|------|--------|---------|----|
{markdown_code}
""")

# with sl.expander("Provide values for input features"):
#     for i in range(len(json_data["result"])):
#         print({json_data["result"][i][1]})
