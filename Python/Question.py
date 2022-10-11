#Modules needed to do this
import requests
import json
import os

#Chose class to handle certain exceptions possibly does nothing
class Request(object):
    """Request object"""
    def __init__(self, request):
        self.request = request
    
    def req(url):
        """Requester"""
        Headers = {
            'Accept': '/*',
        }
        data = {
            "cdn.robinhood.com": {
                "assets": "generated_assets/brand/_next/static"
                }
            }
        
        # json dump the request
        json_val = json.dumps(data).expandtabs(0)
        
        #GET Requester Value
        get_val = requests.request("GET", url=url, headers=Headers, params=data)
        
        #POST Requester Value
        post_val = requests.request("POST", url=url, headers=Headers, params=data)
        
        #checks if the post was successfully processed
        if post_val.status_code != 200:
            raise ConnectionRefusedError("Request returned status code: %s" % post_val)
        #python returns data as a dictionary
        return_val = [json_val,'\nGet Return: %s' % get_val,'\nPost Return: %s' % post_val]
        return print(return_val[0], return_val[1], return_val[2])

def systemConsole(cmd):
    """System Console Command"""
    a = os.system(cmd)
    return a 

def main():
    systemConsole("cls")
    website = input("What Website do you want to connect to?: ")
    Request.req(website)
    return website

if __name__ == "__main__":
    website = main()
    print(f"main(HTTP Requester) called on : %s" % website)
    