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

    def Displaystatus(url):
        for i in range(0,20040905745):
            print("Status: ",requests.get(url).status_code)
        return
# use Requests to make requests to given URL
def create_connection(w,y,h):
    h = h+1
    t1 = requests.post(y,headers={'Content-Type': 'image/png', 'Accept' : 'image/avif,image/webp,/image/apng,/image/svg+xml,image/*,*/*;q=0.8'}).headers
    t2 = requests.post(w,headers={'Content-Type': 'text/javascript'}).headers
    time = t.strftime("%Y-%m-%d %H:%M:%S")
    data = [("Creating SSL connection %s" % time), ("SSL connection established:\n %s" % t1), ("SSL connection established: %s" % t2)]
    status_data = requests.get(y)
    print('Ran HTTP REQUESTER!\n%s' % data.index,"\nPost Data: %s" % status_data)
    return h

def RunConnection(t,w,w1,w2,website,website2,website3,h):
    web1 = Website(website)
    web2 = Website(website2)
    web3 = Website(w)
    web4 = Website(w1)
    web5 = Website(w2)
    web6 = Website(website3)
    a = create_connection("https://twitch.tv/sadlybreathingowo","https://tcusd3.org/",h)
    b = create_connection(web1.url,web2.url,h+1)
    c = create_connection(web3.url,web4.url,h+2)
    d = create_connection(web5.url,web6.url,h+3)
    for i in range(0, t):
        if t >= 2000:
            t = t / -t % 2
        print("Connection @ ", web1, a+i/ran.random())
        print("Connection @ ", web2, b+i-1/ran.random())
        print("Connection @ ", web3, c+i+2/ran.random())
        print("Connection @ ", web4, d+i-3/ran.random())
        print("Connection @ ", web5, d+i-4/ran.random())
        print("Connection @ ", web6, a+i+5/ran.random())
    return h+1,os.system('cls')
#Main function that handles running the create_connection, as well as setting another website to be requested and how many loops the user wants.
def main(time,y,z,w,w1,w2,w3,h):
    RunConnection(time,y,z,w,w1,w3,w2,h)
    for NULL in range(0, time):
        Website.Displaystatus(w1)
        Website.Displaystatus(w2)
        Website.Displaystatus(y)
        Website.Displaystatus(z)
        Website.Displaystatus(w)
        Website.Displaystatus(w3)
        return print(h)

if __name__ == '__main__':
    main(1000,"https://www.robinhood.com/","https://bing.com/","https://www.google.com/","https://www.yahoo.com/","https://www.tcusd3.org","https://www.google.com",12)
