from crypt import methods
from flask import Flask, redirect, url_for, request
from requests import post

app = Flask(__name__)

def grabDownloadUrl(url): # Grab download link from lovetik api
    apiUrl = "https://lovetik.com/api/ajax/search"

    req = post(apiUrl,
    data = {
            "query": url
    },
    headers = {
        "Origin": 'https://lovetik.com/',
        "Referer": 'https://lovetik.com/',
    })

    return req.json()["links"][0]["a"]


@app.route('/', methods=['POST'])
def returnDL():
    post_data = request.get_json()
    response = dict()
    if "url" not in post_data:
        response["error"] = "No URL Detected."
    else:
        tiktok_url = post_data["url"]
        download_url = grabDownloadUrl(tiktok_url)
        if download_url is None:
            response["error"] = "Problem with grabbing download link. Please check TikTok Link or try again."
        else:
            response["url"] = download_url
    return response
