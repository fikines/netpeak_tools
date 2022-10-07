from pprint import pprint
from oauth2client.service_account import ServiceAccountCredentials
import httplib2
import json

JSON_KEY_FILE = "token.json"
 
SCOPES = [ "https://www.googleapis.com/auth/indexing" ]
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
 
# Authorize credentials
credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE, scopes=SCOPES)
HTTP = credentials.authorize(httplib2.Http())

def indexing(url):
    content = {
        'url': url,
        'type': "URL_UPDATED"
    }
    json_content = json.dumps(content)
    
    response, content = HTTP.request("https://indexing.googleapis.com/v3/urlNotifications:publish", method="POST", body=json_content)

    status = response['status']
    pprint(response)
    print('---------------')
    if status != '200':
        return 1

    return 0


def main(links): 

    for link in links:
        response = indexing(link)
        if response:
            return 1

