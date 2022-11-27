
import matplotlib.pyplot as plt
def printApprox(approx, real, t):
    plt.style.use('seaborn-poster')
    plt.figure(figsize = (12, 8))
    plt.plot(t, approx, 'bo--', label='Approximate')
    plt.plot(t, real, 'g', label='Exact')
    plt.title('Approximate and Exact Solution \
    for Simple ODE')
    plt.xlabel('t')
    plt.ylabel('f(t)')
    plt.grid()
    plt.legend(loc='lower right')
    plt.show()



def printError(error, t):
    plt.style.use('seaborn-poster')
    plt.figure(figsize = (12, 8))
    plt.plot(t, error, 'g', label='error')
    plt.title('Error-plot')
    plt.xlabel('t')
    plt.ylabel('norm(error)')
    plt.grid()
    plt.legend(loc='lower right')
    plt.show()
