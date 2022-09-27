class regenerate(object):
    def __init__(self, name, version):
        self.name = name
        self.version = version
    def setName(self,name):
        if self == 0.102:
            print('Successfully generated_assets')
        if name == 'Andrew':
            print("Hello, "+name)
        a = [("Got ID: %s" % str(self)),("Got name: %s" % str(name))]
        assert a == [("Got ID: %s" % str(self)),("Got name: %s" % str(name))]
        print(a)
        return self,name
    def setVersion(version):
        version = version
        return version
    def getVersion(version):
        print(version)
        return 0
    def BrainExternalConsole(name,version):
        a = [('Connected to brain: %s' % name),("BrainExternalConsole: "+name,"Version: "+version)]
        return print(a[0],'\n',a[1],flush=True)

version = regenerate.setVersion('0.01')
name = regenerate.setName(1,'Andrew')
regenerate.BrainExternalConsole(name[1],version)