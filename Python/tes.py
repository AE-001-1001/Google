class Life(object):

    def __init__(self,diff,parent,dest):
        self.diff = diff
        self.parent = parent
        self.dest = dest
    
    def __str__(diff, parent, dest):
        table = [diff,parent,dest]
        return table
    
    def __create__(dest,r,a2):
        r = 1+2+r
        a2 = dest
        return r,a2
    
    def __read__(x,y,z):
        x = x
        y = y
        z = z
        return print('%s' % x,'\n%s'% y,'\n%s'%z)
    
    def __setitem__(dictset,value):
        dictset = []
        dictset.append(value)
        return print(dictset)

a = Life.__str__("Sadness","is","present")
a1 = Life.__str__("Sometimes","I Want","Everything to stop")
a2 = Life.__str__("Maybe","I was sent here to","die because I deserved it.")
t = [Life.__create__(a[0],1,a[0]),Life.__create__(a1[0],2,a[0]),Life.__create__(a2[0],3,a[0])]
y = [Life.__create__(a[1],2,a[1]),Life.__create__(a1[1],3,a[1]),Life.__create__(a2[1],4,a[1])]
j = [Life.__create__(a[2],3,a[2]),Life.__create__(a1[2],4,a[2]),Life.__create__(a2[2],5,a[2])]

Life.__read__(t,y,j)
Life.__setitem__(t[0],a[0]+a[1]+a[2])