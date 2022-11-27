import math
import numpy as np
from plot import printApprox, printError
from RK import adaptiveRK34


tol = 10**(-6)
t0 = 0
tf = 1000
#y0=1 part 1
#N = 10 # number of samples
#A = 3
#h = abs(t0-tf)/N

# part 1
#def f(t, y):
#    return A*y #np.exp(1, t)

#Y = list(range(N)) # our approximation
#t = [n*h for n in range(N)]
#real = [np.exp(n*h) for n in range(N)]
#error = [np.log(abs(real[n] - Y[n])) for n in range(N)]

a, b, c, d = 3, 9, 15, 15 # for part 2
def lotka(t, u : list): # part 2
    unew1 = a*u[0]-b*u[0]*u[1]
    unew2 = c*u[0]*u[1]-d*u[1]

    k = np.array([unew1, unew2])
    
    return k


def find_H(x, y):
    return c*x + b*y - d*np.log(x) -a*np.log(y)



y0 = np.array([1,1])

if __name__=="__main__":
    T, Y = adaptiveRK34(f=lotka, t0=t0, tf=tf, y0=y0, tol=tol)
    print(T)
    #print(Y)
    Y1 = [y[0] for y in Y]
    Y2 = [y[1] for y in Y]
    H = [find_H(Y1[i] , Y2[i]) for i in range(len(Y1))]
    #print(H)
    H_to_print = [abs(H[i]/(H[0]-1)) for i in range(len(H))]

    printApprox(approx=H_to_print, real=H_to_print, t=T)
    #printApprox(approx=Y1, real=Y1, t=Y2) # for part 2. the period is about 1.

    # FOR part 1
    #real = [y0*math.exp(3*t) for t in T]
    #for i in range(1,100):
    #    if i<len(real):
    #        print(real[len(real)-i]-Y[len(real)-i])

    #printError(error=error, t=[np.log(i) for i in range(N)])
