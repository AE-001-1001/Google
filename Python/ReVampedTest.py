import math
import random as ran
import time as t
import requests
import os

class Website:
    count = 0
    
    def __init__(self, url):
        self.url = url
        Website.count += 1

    def Displaystatus(url,a,b):
        for i in range(0,10):
            a = (requests.get(url).headers.get('Content-Type'),requests.post(url).headers.get('server'))
            b = requests.get(url).status_code
            print("Status: ",a,'\n')
            print("Status Code: \n",b,"\n",a)
        return
# use Requests to make requests to given URL
def create_connection(w,y,h):
    h = h+1
    t1 = requests.post(y,headers={'Content-Type': 'image/png', 'Accept' : '*'}).elapsed
    t2 = requests.post(w,headers={'Content-Type': 'text/javascript'}).headers
    time = t.strftime("%Y-%m-%d %H:%M:%S")
    data = [("Creating SSL connection %s" % time), ("SSL connection established:\n %s" % t1), ("SSL connection established: %s" % t2)]
    status_data = requests.get(w)
    print('Ran HTTP REQUESTER!\n%s' % data.index,"\nPost Data: %s" % status_data)
    return h

def RunConnection(t,w,w1,w2,website,website2,website3,h):
    web1 = Website(w)
    web2 = Website(w1)
    web3 = Website(w2)
    web4 = Website(website)
    web5 = Website(website2)
    web6 = Website(website3)
    a = create_connection("https://twitch.tv/sadlybreathingowo","https://tcusd3.org",h)
    b = create_connection(web1.url,web2.url,h+1)
    c = create_connection(web3.url,web4.url,h+2)
    d = create_connection(web5.url,web6.url,h+3)
    for i in range(0, t):
        print("Connection @ ", web1, a+i/ran.random())
        print("Connection @ ", web2, b+i-1/ran.random())
        print("Connection @ ", web3, c+i+2/ran.random())
        print("Connection @ ", web4, d+i-3/ran.random())
        print("Connection @ ", web5, d+i-4/ran.random())
        print("Connection @ ", web6, a+i+5/ran.random())
    return h+1,os.system('cls')
#Main function that handles running the create_connection, as well as setting another website to be requested and how many loops the user wants.
def main(time,y,z,w,w1,w2,w3,h):
    for NULL in range(0, time):
        RunConnection(time,y,z,w,w1,w3,w2,h)
        Website.Displaystatus(w1,w3,y)
        Website.Displaystatus(w2,w,w2)
        Website.Displaystatus(y,z,w1)
        Website.Displaystatus(z,y,w3)
        Website.Displaystatus(w,w2,z)
        Website.Displaystatus(w3,w1,w)
    return print(Website.count)

if __name__ == '__main__':
    main(10,"https://www.twitch.tv/sadlybreathingowo","https://www.robinhood.com","https://www.tcusd3.org/","https://family.tcusd3.org/scripts/wsisa.dll/WService=wsEAplus/skyport","https://github.com/AE-001-1001/Google","https://www.youtube.com/channel/UCa5F6IQNvK6fMRS7MZCBt5A",12)
