
import random as ran
import time as t
import requests
import os

class Website:
    count = 0
    
    def __init__(self, url):
        self.url = url
        Website.count += 1

    def Displaystatus(url,a,b,a1,c):
        for i in range(0,10):
            a1 = requests.get(url)._content
            a = requests.post(url).headers.get('Content-Type', 'text/plain') or requests.post(url).headers.update('Accepted-Encoding', 'gzip,br,deflate')
            b = requests.get(url).status_code
            c = requests.get(url).apparent_encoding
            print("Status: ",a, '\n')
            print("Status Code: ",b,"\n",c,'\n',a1)
        return 
# use Requests to make requests to given URL
def create_connection(w,y,h):
    t1 = requests.post(y,headers={'Content-Type': 'image/png', 'Accept' : '*'}).elapsed
    t2 = requests.post(w,headers={'Content-Type': 'text/javascript'}).headers
    time = t.strftime("%Y-%m-%d %H:%M:%S")
    data = [("\nCreating SSL connection %s" % time), ("\nSSL connection established: %s" % t1), ("\nSSL connection established: %s" % t2)]
    status_data = requests.get(w)
    print('Ran HTTP REQUESTER!\n%s' % data.index,"\nPost Data: %s" % status_data)
    return h + 2

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
        print("Connection @ ", web2, b+i-1/ran.random()*2.14)
        print("Connection @ ", web3, c+i+2/ran.random()*3.41)
        print("Connection @ ", web4, d+i-3/ran.random()*3.14)
        print("Connection @ ", web5, d+i-4/ran.random()*5.13)
        print("Connection @ ", web6, a+i+5/ran.random()*1.53)
    return w,w1,w2,website,website2,website3
#Main function that handles running the create_connection, as well as setting another website to be requested and how many loops the user wants.
def main(time,y,z,w,w1,w2,w3,h):
    for NULL in range(0, time):
        RunConnection(time,y,z,w,w1,w3,w2,h)
        Website.Displaystatus(w1, w3 ,y, w2,z)
        Website.Displaystatus(w2, w  ,y, w3,w1)
        Website.Displaystatus(y,  z  ,w1, w,w3)
        Website.Displaystatus(z,  y  ,w3, w2,w)
        Website.Displaystatus(w,  w2 ,z, y,w3)
        Website.Displaystatus(w3, w1 ,w, z,w2)
    return print(Website.count+1,Website.count-1,Website.count+2,Website.count-2)