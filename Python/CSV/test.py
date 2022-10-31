import tes
import numpy as np
# Runs tes.py in separate directory
if __name__ == '__main__':
    array = np.array([[.1,.2,.3],[.4,.5,.6],[.7,.8,.9],[.10,.11,.12],[.13,.14,.15],[.17,.18,.19]])
    tes.Run_Main(array)
    tes.timer()