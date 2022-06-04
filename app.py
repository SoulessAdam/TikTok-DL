from flask import Flask, redirect, url_for, request, render_template
from requests import post

app = Flask(__name__)


def grabDownloadUrl(url):  # Grab download link from lovetik api
    apiUrl = "https://lovetik.com/api/ajax/search"

    req = post(apiUrl,
               data={
                   "query": url
               },
               headers={
                   "Origin": 'https://lovetik.com/',
                   "Referer": 'https://lovetik.com/',
               })

    response = req.json()
    if "links" not in response:
        print(response)
        return [None, 500, response["mess"]]
    return [response["links"][0]["a"], 200]


@app.route('/', methods=['GET', 'POST'])
def returnDL():
    if request.method == "GET":
        return render_template('homepage.html')
    else:
        response = dict()
        response["code"] = 500
        response["error"] = "API requests should be made to /api endpoint."
        response["message"] = "API Endpoint tutorial at t774.herokuapp.com/api."
        return response


@app.route('/api', methods=["GET", "POST"])
def apiPage():
    if request.method == "GET":
        return redirect("/api/docs")
    else:
        post_data = request.get_json()
        response = dict()
        if "url" not in post_data:
            response["error"] = "No URL Detected."
        else:
            tiktok_url = post_data["url"]
            downloadData = grabDownloadUrl(tiktok_url)
            download_url = downloadData[0]
            responseCode = downloadData[1]
            if download_url is None:
                response["message"] = "Problem with grabbing download link. Please check TikTok Link or try again."
                response["error"] = downloadData[3]
            else:
                response["url"] = download_url
        response["code"] = responseCode
        return response


@app.route('/api/docs')
def docs():
    return render_template('docs.html')


@app.route('/error/<int:code>', methods=["GET"])
def error(code):
    return render_template('error.jinja2', error_code=code)


@app.route('/', defaults={'upath': ''})
@app.route('/<path:u_path>', methods=["GET", "POST"])
def incorrectPath(u_path):
    if request.method == "GET":
        return redirect("/error/404")
    elif request.method == "POST":
        response = dict()
        response["error"] = "Incorrect path."
        response["message"] = "Please use the /api endpoint."
        response["code"] = 500
        return response
