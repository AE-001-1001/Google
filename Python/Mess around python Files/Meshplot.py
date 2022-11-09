import matplotlib.pylab as plt
import random
import tes

class buildArr(object):
    """Builds a Array of objects"""
    def __init__(self, X,Y,Z):
        """Constructor for Array"""
        self.X = X
        self.Y = Y
        self.Z = Z
        return 0
    def __init__(X,Y,Z):
        """Init for Array"""
        if Y == Y:
            Y += 1
            Z -= 1
        print(X,Y,Z)
        return X,Y,Z

class RunBuild(object):
    """Build for Build Arr"""
    def __init__(self,posX,posY,posZ):
        """Location of BUILD"""
        self.posX = posX
        self.posY = posY
        self.posZ = posZ
        return 0
    def __run__(self):
        """Run Build Arr"""
        print()
        return 

def test(x,y,z):
    """Test Build Arr"""
    a = buildArr.__init__(x,y,z)
    pass
    plt.plot(RunBuild.__run__(a[0]))
    plt.plot(RunBuild.__run__(a[2]))
    plt.show()
    return x,y,z
a = random.randint(0,25)
if __name__ == "__main__":     
    a = test(a+1,a+2,a+3).index
    b = test(a+2,a+3,a+4).index
    c = test(a+3,a+4,a+5).index
    tes.Run_Main([[a,b,c]])
