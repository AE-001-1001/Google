from ssl import OPENSSL_VERSION
import requests 
# Use OPENSSL functions to create connections
def create_connection(w,y):
    VERSION = OPENSSL_VERSION
    test = requests.post(w, y,headers={'Content-Type': 'application/json'})
    data = [("Creating SSL connection: %s" % VERSION), ("SSL connection established: %s" % test)]
    return print(data, sep='\n',end='\n')

create_connection("https://www.robinhood.com","https://www.google.com")
