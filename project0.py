import numpy as np
import matplotlib.pyplot as plt
from math import log10, sqrt


#matplotlib inline

# Define parameters


ORIGINAL = np.array([1]) # matrix [ [-2, 0] , [2, 5] ] 
sizeA = int(sqrt(ORIGINAL.size))
print(sizeA)
t0 = 0
tf = 10
N = 100 # number of steps
h = abs((t0-tf))/N # Step size
f = lambda t, h: np.exp(3*t*h) # ODE
y0 = np.array([1]) # Initial Condition



IMPLICIT = np.linalg.inv(np.identity(sizeA)-h*ORIGINAL)
diagonalized = np.diag(ORIGINAL)



# Explicit Euler Method
approx = [None for i in range(N)]
real = [None for i in range(N)]


def eulerInt(A, y0, t0, tf, N):
    approx[0] = y0
    real[0] = y0

    for i in range(N-1):
        approx[i + 1] = np.matmul(A, approx[i])
        #approx[i+1] = np.matmul(A, approx[i])
        real[i+1] = f(i+1, h) 


eulerInt(IMPLICIT, y0,t0, tf, N)

error = [abs(approx[i]-real[i]) for i in range(N-1)]


def printApprox():
    print(approx)
    t = [i*h for i in range(N)]
    plt.style.use('seaborn-poster')
    plt.figure(figsize = (12, 8))
    plt.plot(t, approx, 'bo--', label='Approximate')
    #plt.plot(t, real, 'g', label='Exact')
    plt.title('Approximate and Exact Solution \
    for Simple ODE')
    plt.xlabel('t')
    plt.ylabel('f(t)')
    plt.grid()
    plt.legend(loc='lower right')
    plt.show()

printApprox()

def printError():
    t = [i*h for i in range(N)]
    error = []
    for i in range(N):
        #error.append(np.linalg.norm(real[i]-approx[i]))
        
        err = real[i]-approx[i]
        norm = np.linalg.norm(real[i])
        print(norm)
        error.append(err/norm)

    plt.style.use('seaborn-poster')
    plt.figure(figsize = (12, 8))
    plt.plot(t, error, 'g', label='error')
    plt.title('Error-plot')
    plt.xlabel('t')
    plt.ylabel('norm(approx-real)')
    plt.grid()
    plt.legend(loc='lower right')
    plt.show()

#printError()