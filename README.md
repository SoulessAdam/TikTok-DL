# TikTok-DL
TikTok Video Downloader API. 
<hr>

##### <b>How to setup (iOS):</b>
* Download Scriptable <a href=https://apps.apple.com/us/app/scriptable/id1405459188>here.</a>
* Create new script.
* Copy `ScriptableiOS.js`'s content and paste into your script.
* Enter the scripts settings. *(Bottom left button)*
* Rename your script to anything you want - such as `Download`.
* Tap `Share Sheet Inputs`.
* Click `URLs`.
* Your script is now ready to use! *Guide below.*

##### <b>How to use (iOS):</b>
* Ensure you setup the script w/ above tutorial.
* Goto any TikTok video.
* Tap share.
* Goto the `Other` option and tap.
* Tap Run Script.
* Click on your script setup before.
* Wait for website to load.
* Click Download.
<hr>

##### <b>How to setup server (Heroku):</b>
* Literally just deploy this repository to Heroku.
* Wait for build to complete.
* Grab your URL for your deployed heroku app.
* Update the `apiEndpoint` in the iOS Script.

##### <b>How to setup server (Python):</b>
###### *NOTE THIS IS FOR LOCAL NETWORKS ONLY*
* Download `Server.py`
* Run `Server.py` with `python ./path/to/Server.py`
* Copy the displayed IP on startup
* Update your `apiEndpoint` variable in the iOS Script.
