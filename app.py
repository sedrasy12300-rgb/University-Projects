import streamlit as st
from scipy.optimize import bisect as bt
import matplotlib.pyplot as plt
import numpy as np

st.title("Polynomial Root Finder")
st.subheader("Bisection Method")

st.write("Find an approximate root of a polynomial using the Bisection Method.")

num_terms= st.number_input("Enter the number of terms : ",min_value=1,max_value= 20,value=3)

coefficients =[]
exponentents =[]
for i in range(1,num_terms+1):
    col1 ,col2 =st.columns(2)
    with col1: 
          coef =st.number_input(f"Enter coefficient for term  {i} : ",value=0)
    coefficients.append(coef)
    with col2:
          exp =st.number_input(f"Enter exponent for term  {i} : ",min_value=0,max_value=20)
    exponentents.append(exp)

const=st.number_input("Enter the constant term : ")

def f(x):    
    c=0
    for j in range(len(coefficients)):
        d =coefficients[j]*x**exponentents[j]
            
        c+=d   
    return c +const
col3,col4 = st.columns(2)   

with col3 :
      a=st.number_input("Enter lower bound (a) : ")
with col4:
      b =st.number_input(" Enter upper bound (b) : ")

if (a>b):
        st.warning("Invalid interval : a must be less than b. ")
elif  a==b:
            st.warning(" Invalid interval: a and b must be different.")
elif f(a)*f(b) >0:
        st.warning("Invalid interval: f(a) and f(b) must have opposite signs, unless an endpoint is a root.")

elif f(a)* f(b) == 0:
        if(f(a)==0):
            st.warning(f" A root was found at the lower bound: {a} ")
        else:
            st.warning(f" A root was found at the upper bound: {b}")
else:
        if st.button("Show"):
            root ,result = bt(f,a,b,xtol=0.0001,full_output=True)
            st.write("Approximate root : ",root)
            st.write("Number of iterations : ",result.iterations)
            st.write("converged successfully : ",result.converged)
            x=np.linspace(a,b,1000)
            plt.title("Polynomial Root Finding - Bisection Method ")
            plt.xlabel("x")
            plt.ylabel("f(x)")
            plt.plot(x,f(x),color="blue")
            plt.scatter(root,f(root),color="red")
            plt.grid(True)
            plt.axhline(y=0,color="green")
            st.pyplot(plt.gcf())
            plt.show()