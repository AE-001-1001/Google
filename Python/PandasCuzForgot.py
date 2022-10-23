import pandas as pd
import requests as r

#Create function to ping website

def ping(url):
    try:
        response = r.get(url)
        return response.status_code
    except Exception as e:
        print(e)
        return -1

#Read return on successful

def read_return(url):
    try:
        response = r.get(url)
        return response.text
    except Exception as e:
        print(e)
        return -1

#Try Posting to website with param to backend

def post(url, data):
    try:
        response = r.post(url, json=data)
        return response.status_code
    except Exception as e:
        print(e)
        return -1




def main():
    website = input("What Website: ")
    print(ping(website))
    print(read_return(website))
    #For post it needs to be Application/Json format
    print(post(website,"Application/Json"))
    return 

if __name__ == "__main__":
    main()