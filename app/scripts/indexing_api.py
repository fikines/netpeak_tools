from pprint import pprint
from oauth2client.service_account import ServiceAccountCredentials
import httplib2
import json


def indexing(url,http):
    content = {
        'url': url,
        'type': "URL_UPDATED"
    }
    json_content = json.dumps(content)

    try:
        response, content = http.request("https://indexing.googleapis.com/v3/urlNotifications:publish", method="POST", body=json_content)

        status = response['status']
    
        if status == '403':
            return 1
    except:
        pass 

    return 0


def main(links, token): 
    
    SCOPES = [ "https://www.googleapis.com/auth/indexing" ]
    key = json.loads(token, strict=False)


    # Authorize credentials
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(key, scopes=SCOPES)
    http = credentials.authorize(httplib2.Http())

    for link in links:
        response = indexing(link, http)
        if response:
            return 1

    return 0
