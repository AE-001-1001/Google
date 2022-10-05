import random
import time

dict = []
class Matrix(object):
    def __init__(self, x,y,z,s,t,d,x1,y1,z1,s1,t1,d1):
        self.x = x
        self.y = y
        self.z = z
        self.s = s
        self.t = t
        self.d = d
        self.d1 = d1
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
        self.s1 = s1
        self.t1 = t1
        self.d1 = d1
        return 
    def shape(x,y,z,s,t,d,x1,y1,z1,s1,t1,d1):
        for i in range(0, x):
            dict.append(i)
            if i >= 5:
                i -= 1
            if i <= 5:
                '\n'
            print('\t',dict[i])

        for j in range(1, y):
            dict.append(j)
            if j >= 8:
                j -= 1 
            if len(dict) >= 10:
                '\n'
            print('\t\t',dict[j],)

        for k in range(2, z):
            dict.append(k)
            if k >= 12:
                k -= 1 
            if k <= 18:
                '\n'
            print('\t\t\t', dict[k],'\t\t',dict[k+j])

        for n in range(3, s):
            dict.append(n)
            if n >= 16:
                n *= k
            if n <= 24:
                '\n'
            print('\t\t\t\t',dict[n],'\t\t\t',dict[n + k])

        for l in range(5, t):
            dict.append(l+n)
            if l >= 20:
                l -= 1
            if l >= 25:
                '\n'
            print('\t\t\t\t\t',dict[l],'\t\t\t\t',dict[l+n])

        for h in range(6, d):
            dict.append(h+l)
            if h >= 30:
                h -= 100
            if h >= 30:
                '\n'
            print('\t\t\t\t\t\t',dict[h-1],'\t\t\t\t\t',dict[h+l])
                
        for p in range(7, x1):
            dict.append(p)
            if p >= 35:
                p -= 100
            if len(dict) >= 35:
                '\n'
            print('\t\t\t\t\t\t\t',dict[p],'\t\t\t',dict[p+h])
        for a1 in range(8, y1):
            dict.append(a1+p)
            if a1 >= 40:
                a1 -= 100
            if (len(dict)) >= 40:
                '\n'
            print('\t\t\t\t\t\t',dict[a1],'\t\t',dict[a1+p])
        for b1 in range(9,z1):
            dict.append(b1+a1)
            if b1 >= 45:
                b1 -= 100
            if (len(dict)) >= 45:
                '\n'
            print('\t\t\t\t\t',dict[b1],'\t',dict[b1+a1])
            return b1
        for h1 in range(10,s1):
            dict.append(h1+b1)
            if h1 >= 50:
                h1 -= 100
            if (len(dict)) >= 50:
                '\n'
            print('\t\t\t\t\t',dict[h1],'\n',dict[h1+b1])
            
        for k1 in range(11,t1):
            dict.append(k1+h1)
            if k1 >= 55:
                k1 -= 100
            if (len(dict)) >= 55:
                '\n'
            print('\t\t\t',dict[k1],'\n',dict[k1+b1])
        
        for zH in range(12,d1):
            dict.append(zH+k1)
            if zH >= 100:
                zH -= 100
            if (len(dict)) >= 55:
                '\n'
            print('\t\t',dict[zH])
        
        time.sleep(0.005)

        return 0
    def shape2(x,y,z,s,t,d,x1,y1,z1,s1,t1,d1):
        for i in range(0, x):
            dict.append(i)
            if i >= 5:
                i -= 1
            if i <= 5:
                '\n'
            print('\t',dict[i])

        for j in range(1, y):
            dict.append(j)
            if j >= 8:
                j -= 1 
            if len(dict) >= 10:
                '\n'
                print('\t\t',dict[j],'\t\t',dict[j+i])

        for k in range(2, z):
            dict.append(k)
            if k >= 12:
                k -= 1 
            if k <= 18:
                '\n'
            print('\t\t\t', dict[k],'\t\t\t',dict[k+j])

        for n in range(3, s):
            dict.append(n)
            if n >= 16:
                n *= k
            if n <= 24:
                '\n'
            print('\t\t\t\t\t',dict[n],'\t\t\t\t',dict[n + k])

        for l in range(5, t):
            dict.append(l+n)
            if l >= 20:
                l -= 1
            if l >= 25:
                '\n'
            print('\t\t\t\t\t\t',dict[l],'\t\t\t\t\t',dict[l+n])

        for h in range(6, d):
            dict.append(h+l)
            if h >= 30:
                h -= 100
            if h >= 30:
                '\n'
            print('\t\t\t\t\t\t\t',dict[h-1],'\t\t\t\t\t\t',dict[h+l])
                
        for p in range(7, x1):
            dict.append(p)
            if p >= 35:
                p -= 100
            if len(dict) >= 35:
                '\n'
            print('\t\t\t\t\t\t\t\t',dict[p],'\t\t\t\t\t',dict[p+h])
        for a1 in range(8, y1):
            dict.append(a1+p)
            if a1 >= 40:
                a1 -= 100
            if (len(dict)) >= 40:
                '\n'
            print('\t\t\t\t\t\t',dict[a1],'\t\t\t\t',dict[a1+p])
        for b1 in range(9,z1):
            dict.append(b1+a1)
            if b1 >= 45:
                b1 -= 100
            if (len(dict)) >= 45:
                '\n'
            print('\t\t\t\t\t',dict[b1],'\t\t\t',dict[b1+a1])
            return b1
        for h1 in range(10,s1):
            dict.append(h1+b1)
            if h1 >= 50:
                h1 -= 100
            if (len(dict)) >= 50:
                '\n'
            print('\t\t\t\t\t',dict[h1],'\t\t',dict[h1+b1])
            
        for k1 in range(11,t1):
            dict.append(k1+h1)
            if k1 >= 55:
                k1 -= 100
            if (len(dict)) >= 55:
                '\n'
            print('\t\t\t',dict[k1],'\t',dict[k1+b1])
        
        for zH in range(12,d1):
            dict.append(zH+k1)
            if zH >= 100:
                zH -= 100
            if (len(dict)) >= 55:
                '\n'
            print('\t\t',dict[zH],'\t',dict[zH+k1])
        
        time.sleep(0.075)

        return 0



def main(x,y,z,s,t,d,x1,y1,z1,s1,t1,d1):
    Matrix.shape(x,y,z,s,t,d,x1,y1,z1,s1,t1,d1)
    Matrix.shape2(x-1,y*1,z**1,s+1,t+1,d+1,x1+1,y1+1,z1+1,s1**1,t1*1,d1-1)
    return 0

a = random.randint(1,3)
b = random.randint(2,12)
c = random.randint(3,16)
d = random.randint(4,20)
e = random.randint(5,24)
f = random.randint(6,28)
g = random.randint(7,32)+f
h = random.randint(8,36)+g
i1 = random.randint(9,40)+h
j = random.randint(10,44)+i1
k = random.randint(11,46)+j
l = random.randint(12,50)+k
dict = [a,b,c,d,e,f,g,h,i1,j,k,l]

if __name__ == "__main__":
    for i in range(0,555005500):
        main(dict[0],dict[1],dict[2],dict[3],dict[4],dict[5],dict[6],dict[7],dict[8],dict[9],dict[10],dict[11])