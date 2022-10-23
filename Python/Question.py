#Modules needed to do this
from time import sleep
import requests
import json
import os

#Chose class to handle certain exceptions possibly does nothing
class Request(object):
    """Request object"""
    # i think useless the way I used it here
    def __init__(self, request):
        self.request = request
    
    def req(url):
        """Requester"""
        # headers is https://prnt.sc/Nm93Ow1luGXo for google console
        Headers = {
            'access-control-allow-origin': '*',
            'accept-ranges': '*',
            'content-type': 'application/json',
            'charset': 'utf8',
        }
        
        # question mark
        data = {
            "cdn.robinhood.com": {
                "generated_assets": "generated_assets/brand/_next/static"
                }
            }
        
        # json dump the request
        json_val = [json.dumps(data).expandtabs(0),json.dumps(Headers).expandtabs(1)]
        
        #GET Requester Value
        get_val = requests.request("GET", url=url, headers=Headers, params=data)
        
        #POST Requester Value
        post_val = requests.request("POST", url=url, headers=Headers, params=data)
        
        # Contents of the request
        Content_val = get_val.content.decode("utf-8")
        #return all content values in csv format

        #checks if the post was successfully processed
        if post_val.status_code == 403:
            systemConsole("curl -i %{http_code} %{time_connect} %{url}" )
        if post_val.status_code == 202:
            post_val.json = json.dumps(post_val.content.decode("utf-8").translate("utf-8"))
            return print(post_val.iter_content)
        if post_val.status_code == 200:
            post_val.json = json.dumps(post_val.content.decode("utf-8").translate("utf-8"))
        
        #Return the responses into a dict containing information, easily accessible to print out the output of Request.req
        return_val = [json_val,'\nGet : %s' % get_val,'\nPost : %s' % post_val, '\nContent : %s' % Content_val]

        return print('\n',return_val[0][0],'\n',return_val[0][1],'\n',return_val[0],'\n',return_val[1],return_val[2],return_val[3])

def systemConsole(cmd):
    """System Console Command"""
    #really just like opening a terminal you can't see visibly with the eye
    sleep(0.5)
    a = os.system(cmd)
    return a 

def main(i):
    #System Console to make exec look nicer to eyes of Artificial Intelligence(AI)
    website = input("What Website do you want to connect to?: ")
    systemConsole("cls")
    # for loop to read out data duhhh #
    # if you want to change things be my guest :) :)
    for x in range(0, i):
        Request.req(website)
        # Checks netstats 
        systemConsole("netstat -f")
    return website

if __name__ == "__main__":
    # The number is the amount of times you want to run it
    website = main(571135420)
    print(f"main(HTTPS Requester) called on %s" % website)
    
    # opaaaah 

    # custom output for debugging
    #   [.-.] ,-<Why am I not like everyone else>      [._.] ,-<You are not like everyone else explorer>
    #    /||\                                          /||\ ,-<Do you see your face?>
    #    _||_                                          _||_
    # an eternity later explorer crafts mirror from atoms *spongebob voice over*
    #         _____________
    # [.-.]  |{  [.-.]   } | ,<Are you F*)K*N& serious?>
    # /||\   | {  /||\   } | 
    # _||_   | {  _||_   } |
    # ------      ------
    #       Explorer has not been seen since this crafting of the mirror
    #           there is nothing tracing back to his whereabouts 
    #             ultimately the story is everyone is different
    #             ones looks deceives the world of their intent    
    #    <_<                      >_>  ,<Sir, I see movement coming from a experimental subject... Do we run?>
    # //| | |\\                //| | |\\
    #   |_|_|                    | | |  
    # -----                  -----
    # Sir disappeared from thin air
    #    [>_<] ,<But I thought life was real>
    #  //| | |\\         
    #    |_|_|
    # *************************
    # ********************************
    # a monkey comes from the pod, and so this is how the hoomans eventually became a thing. locking monkeys in ZOOS and harming poor monkeys for experiments
    # RIP the monkeys that had neural link, try a hooman that at least has no will to live to let them see a world this current world isn't ready for 
    # Also what if Harambe had neural link would we be able to see intention with the child he had with the hands of a gorilla that could crunch a skull?
    # what if Harambe had neural link and the child would be the cause that changes everyones live including his...
    # what if him dying he knows that the world doesn't understand his death will cause a timeline split... meaning to his life... and so HARAMBE BECAME A MEME living truly forever
    # sorry I probably should stop typing so much in comments... I normal upload NOTHING with comments 
    # P.S I know comments give others help at how things functions and I will try my best to do so.