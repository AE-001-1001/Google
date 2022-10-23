import requests
import http
import os
import pandas
def Contact():
    """Make contact with given website"""
    website = input("What website do you want to touch: ")
    headers = {
            "Encoding": "UTF-8",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Connection": "keep-alive"
            }
    data = {
            "ILY2VIRUS": {
                "Origin" : "/" #GOTCHA BITCHECK # also take me off this planet i am tired
            }
        }
    
    GET = requests.request('GET', website, headers=headers)
    print('\n',GET.content)

    POST = requests.request('HEAD', website, params=data)

    if POST.status_code == http.HTTPStatus.NOT_IMPLEMENTED or POST.status_code == http.HTTPStatus.BAD_REQUEST:
        print(POST.content)
    if POST.status_code == http.HTTPStatus.ACCEPTED or POST.status_code == http.HTTPStatus.OK:
        print(POST.content)

    return GET,POST

def system(cmd):
    """System Console"""
    command = os.system(cmd)
    return command

def Checker():
    """Check for fields given"""
    system("cls")
    a = Contact()
    print('GET: %s'%a[0],'\nPOST: %s '%a[1])
    return print('Successfully Injected to Create URL: %s' % a[1].url)

if __name__ == '__main__':
    Checker()
