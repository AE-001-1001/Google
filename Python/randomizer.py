import math 
import time
import random
# ---------------------------------------------------------------- # 
def getTime(key):
    guid = key + key / random.randrange(1, 10);
    print("get Time called at: " + str(time.strftime("%Y-%m-%d %H:%M:%S")),"\nGUID:",guid);
    time.sleep(1);
    return print('\n',time.time());


def main(x):
    key = [getTime(x),2495.745,15704625.1572];
    data = key[key.index(x)];
    if key.index(2495.745) >= key[1]:
        print("key:",key);
    return print("Base Number:",data);
for i in range(1,2004):
    main(2495.745*3.14*2004)