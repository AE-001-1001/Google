import time as t
import requests
class regenerate(object):
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def setName(self,name):
        """Set name and ID"""
        if self == '0.404':
            print('','Successfully generated_assets')
        if self != '0.404':
            print('You have sent your data to the FBI')
        if name == 'Andrew':
            print('',"Hello, "+name)
        a = [("Got ID: %s" % str(self)),("Got name: %s" % str(name))]
        # Making sure layout is correct
        assert a == [("Got ID: %s" % str(self)),("Got name: %s" % str(name))]
        print('',a)
        return self,name

    def getName(name):
        """Gets Name"""
        return name

    def setVersion(version):
        """Sets the version"""
        version = version
        return version
    
    def getVersion():
        """Returns the version"""
        version = version
        print(version)
        return 0
    
    def BrainExternalConsole(name,version):
        """External Console interface"""
        h = t.strftime("%Y-%m-%d %H:%M:%S")
        if name == 'Andrew':
            print('','Getting Neural Network data: %s' % name)
        if name != 'Andrew':
            print('','You arent getting anything from this')
            return False
        a = [('Connected to brain: %s' % name),("Brain Console: "+name),("Version: "+version)]
        return print('',a[0],'\n',a[1],'\n',a[2],'\n',h,flush=True)
    
def verify(boolean,Name,key):
    """Verify that the given field is correct"""
    if boolean == False:
            name_set = regenerate.setName(key,Name)
            name = regenerate.getName(name_set[1])
            # Checks if function return False
            regenerate.BrainExternalConsole(name,version='None')
            return None
    # if Checks return True passes
    if boolean == True:
        version = regenerate.setVersion(key)
    # If the name is None then return custom error message
    if Name == None:
        print('You must provide a name fuck head')
    # Checks the name if the name is Owner
    if Name == 'Andrew':
        name = regenerate.setName(key,Name)
    if Name != 'Andrew':
        print('Incorrect User: %s' % name)
        return None
    if key == '0.404':
        regenerate.BrainExternalConsole(name[1],version='0.0.1c')
    if key != '0.404':
        print('Incorrect Key: %s' % key)
        return None
    return boolean,Name,key

def website_grabber(boolean,website):
    """Gets the website """
    if boolean == False:
        print('','Not Correct User')
        return None
    if boolean == True:
            data = requests.get(website)
            return print(data)
    return boolean,website

def main(Name,Key,website):
    if Name == 'Andrew':
        verify(True,Name,Key)
        website_grabber(True,website)
    if Name != 'Andrew':
        verify(False,Name,Key)
        website_grabber(False,website)
    return Name,Key

username = input("What's your username: ")
password = input("What's your password: ")
website = input("What Website to grab: ")
if __name__ == '__main__':
    main(username, password, website)
