// Scriptable iOS Script to grab url from share sheet and automatically redirect to download url.
var apiEndpoint = "https://t774.herokuapp.com/api"
var apiResponse = new Request(apiEndpoint)
apiResponse.method = "POST";
apiResponse.headers = {
    "Content-type": "application/json",
    "Accept": "*/*"
}
apiResponse.body = JSON.stringify({
    "url": args.urls[0]
});
var jsonR = await apiResponse.loadJSON();
var url = jsonR["url"]
if(url != undefined) Safari.open(url)
else{
    noti = new Notification()
    noti.title = "Error"
    noti.body += jsonR["error"]
    noti.schedule()
}