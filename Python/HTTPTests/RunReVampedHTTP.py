from ReVampedHTTP import main #Template for HTTP requests
import time as t

## G = Runs HTTP_v1.py 
def g(i):
    for i in range(0,i):
        if i >= 1:
            main(i,"https://google.com/search?q=google","https://robinhood.com","https://youtube.com","https://www.tcusd3.org","https://microsoft.com/","https://www.kraken.com/en-us",12)
            main(i-1,"https://instagram.com","https://www.tiktok.com","https://twitter.com","https://www.facebook.com","https://www.github.com","https://snapchat.com",13)
    return t.sleep(1),print(0+i-3,' ',0+i)

if __name__ == '__main__':
    g(2)
    