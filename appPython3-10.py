# JUST A TEMPLATE.
# WILL NOT BE USED UNTIL GUNICORN SUPPORTS PYTHON 3.10


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
        return None
    return response["links"][0]["a"]


@app.route('/', methods=['GET', 'POST'])
def returnDL():
    match request.method:
        case "GET":
            return render_template('homepage.html')
        case "POST":
            response = dict()
            response["code"] = 500
            response["error"] = "API requests should be made to /api endpoint"
            response["message"] = "API Endpoint tutorial at t774.herokuapp.com/api"
            return response


@app.route('/api', methods=["GET", "POST"])
def apiPage():
    match request.method:
        case "GET":
            return redirect("/api/docs")
        case "POST":
            post_data = request.get_json()
            response = dict()
            if "url" not in post_data:
                response["message"] = "Please ensure a url is entered."
                response["error"] = "No URL Detected."
            else:
                tiktok_url = post_data["url"]
                downloadData = grabDownloadUrl(tiktok_url)
                match downloadData:
                    case [downloadUrl, responseCode, errorMessage]:
                        response["error"] = errorMessage
                        response["code"] = responseCode
                        response["message"] = "Problem with grabbing download link."
                    case [downloadUrl, responseCode]:
                        response["url"] = downloadUrl
                        response["code"] = responseCode
            return response


@app.route('/api/docs')
def docs():
    return render_template('docs.html')


@app.route('/error/<int:code>', methods=["GET"])
def error(code):
    return render_template('error.jinja2', error_code=code)
