from scipy.optimize import bisect as bt
import matplotlib.pyplot as plt
import numpy as np



num_terms =int(input("Enter the number of terms : "))

if (num_terms <=0 or  num_terms > 20):
    print("Invalid input. Please enter a number between 1 and 20")
else:
    coefficients =[]
    exponentents =[]
    for i in range(1,num_terms+1):
        coef =float(input("Enter coefficient for term : "))
        coefficients.append(coef)
        exp =int(input("Enter exponent for term"))
        
        while(exp <0):
            print("Negative numbers are not allowed.")
            exp =int(input("Enter exponent for term"))
        exponentents.append(exp)

    const=float(input("Enter the constant term : "))

    def f(x):    
        c=0
        for j in range(len(coefficients)):
            d =coefficients[j]*x**exponentents[j]
            
            c+=d   
        return c +const
        
        

    a= float(input("Enter lower bound (a) : "))
    b=float(input(" Enter upper bound (b) : "))
    if (a>b):
        print("Invalid interval : a must be less than b. ")
    elif  a==b:
            print(" Invalid interval: a and b must be different.")
    elif f(a)*f(b) >0:
        print("Invalid interval: f(a) and f(b) must have opposite signs, unless an endpoint is a root.")

    elif f(a)* f(b) == 0:
        if(f(a)==0):
            print(f" A root was found at the lower bound: {a} ")
        else:
            print(f" A root was found at the upper bound: {b}")
    else:
            root ,result = bt(f,a,b,xtol=0.0001,full_output=True)
            print("Approximate root : ",root)
            print("Number of iterations : ",result.iterations)
            print("converged successfully : ",result.converged)
            x=np.linspace(a,b,1000)
            plt.title("Polynomial Root Finding - Bisection Method ")
            plt.xlabel("x")
            plt.ylabel("f(x)")
            plt.plot(x,f(x))
            plt.scatter(root,f(root))
            plt.grid(True)
            plt.axhline(y=0)
            plt.show()