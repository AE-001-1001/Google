import random as ran
import time as t
import requests
import os

class Website:
    count = 0

    def __init__(self, url):
        self.url = url
        Website.count += 1

    def Displayerstatus(url):
        print("Status: ",Website.count)

# use Requests to make requests to given URL
def create_connection(w,y,h):
    h = h+1
    t1 = requests.post(y,headers={'Content-Type': 'image/png', 'Accept' : 'image/avif,image/webp,/image/apng,/image/svg+xml,image/*,*/*;q=0.8'}).headers
    t2 = requests.post(w,headers={'Content-Type': 'text/javascript'}).headers
    time = t.strftime("%Y-%m-%d %H:%M:%S")
    data = [("Creating SSL connection %s" % time), ("SSL connection established:\n %s" % t1), ("SSL connection established: %s" % t2)]
    status_data = requests.get(y)
    os.system('cls')
    print('Ran HTTP REQUESTER!\n%s' % data.index,"\nPost Data: %s" % status_data)
    return h

def RunConnection(t,w,w1,w2,website,website2,h):
    web1 = Website(website)
    web2 = Website(website2)
    a = create_connection("https://twitch.tv/sadlybreathingowo","https://tcusd3.org/",h)
    b = create_connection(web1.url,web2.url,h+1)
    for t in range(0, t):
        os.system('ping -a '+w)
        pass
        os.system('ping -a '+w1)
        pass 
        os.system('ping -a '+w2)
    print("Connection @ ", web1, a, b)
    return h+1
#Main function that handles running the create_connection, as well as setting another website to be requested and how many loops the user wants.
def main(time,y,z,w,w1,w2,h):
    RunConnection(time,y,z,w,w1,w2,h)
    return print(Website.count,h)

if __name__ == '__main__':
    main(2,"www.robinhood.com","www.google.com","www.tcusd3.org","https://www.tcusd3.org","https://www.google.com",12)