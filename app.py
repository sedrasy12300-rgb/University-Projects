import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



st.title("Polynomial Root Finder")
st.subheader("Bisection Method")

st.write("Find an approximate root of a polynomial using the Bisection Method.")

with st.expander("Details & Explanation") :
      st.write("""حول التطبيق\n
      يتيح هذا التطبيق إيجاد جذر تقريبي لكثير الحدود باستخدام طريقة التنصيف (Bisection Method).\n
      كيفية إدخال كثير الحدود\n
      أدخلي عدد الحدود، ثم حددي معامل كل حد وأُسّه. وأخيرًا، أدخلي الحد الثابت.\n
      اختيار الفترة\n
      أدخلي الحد الأدنى والحد الأعلى للفترة التي تريدين إيجاد الجذر ضمنها. يجب أن تكون قيم الدالة عند طرفَي الفترة مختلفتَي الإشارة.\n
      كيف تعمل الطريقة؟\n
      تقسم الطريقة الفترة إلى نصفين بشكل متكرر، ثم تختار النصف الذي يحتوي على تغيّر في إشارة الدالة، وتستمر بهذه العملية حتى الوصول إلى الدقة المطلوبة.\n
      فهم النتائج\n
      الجذر التقريبي: يعرض القيمة التقريبية للجذر الذي تم إيجاده.\n
      عدد التكرارات: يعرض عدد الخطوات التي نُفّذت للوصول إلى النتيجة.\n
      الرسم البياني: يعرض منحنى كثير الحدود.\n
      جدول التكرارات: يعرض خطوات الحساب التي أُجريت خلال تطبيق الطريقة.\n
      ملاحظة مهمة\n
      النتيجة تقريبية، وتتطلب طريقة التنصيف أن تكون الدالة متصلة وأن تكون الفترة المختارة مناسبة لتطبيق الطريقة.""")
      st.subheader("Example")
      st.write("""
      Suppose you want to find a root of the polynomial f(x) = x² - 4.\n
      Enter the following values:\n
      Number of terms: 1\n
      Coefficient: 1\n
      Exponent: 2\n
      Constant term: -4\n
      Lower bound: 1\n
      Upper bound: 3\n
      Click Show to calculate the approximate root and view the graph and iteration table.\n
      The approximate root is 2.""")

num_terms= st.number_input("Enter the number of terms (1-20): ",min_value=1,max_value= 20,value=3)

coefficients =[]
exponentents =[]

for i in range(1,num_terms+1):
    col1 ,col2 =st.columns(2)
    with col1: 
          coef =st.number_input(f"Enter coefficient for term  {i} : ",value=0)
    coefficients.append(coef)
    with col2:
          exp =st.number_input(f"Enter exponent for term  {i} (0-20) : ",min_value=0,max_value=20)
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
st.subheader("Your Polynomial Equation")
st.write("The equation defined by your inputs is:Your Polynomial EquationThe equation defined by your inputs is:")

chng =""
for n in range(len(coefficients)):
      
      if coefficients[n] > 0 and n >0:
            chng+="+"
      
      ch_text =f"""{str(coefficients[n])}x^{{{str(exponentents[n])}}}"""
      chng+=ch_text
constStr =const
if constStr >=0:
      constStr="+"+ str(constStr)
chng =chng + str(constStr)

      
st.latex(chng)

if (a>b):
        st.warning("Invalid interval : a must be less than b. ")
elif  a==b:
            st.warning(" Invalid interval: a and b must be different.")
elif f(a)*f(b) >0:
        st.warning("Invalid interval: f(a) and f(b) must have opposite signs, unless an endpoint is a root.")

elif f(a)* f(b) == 0:
        if(f(a)==0):
            st.success(f" A root was found at the lower bound: {a} ")
        else:
            st.success(f" A root was found at the upper bound: {b}")

else:
       if st.button("Show"):
            
            x=np.linspace(a,b,1000)

            epsilon=10**(-4)
            count =0
            found=False
            iteration_data =[]
               
            while (b-a)/2 > epsilon:
                  
                  m0 =(a+b)/2
                  iteration_data.append({
                        "Iteration":count+1,
                        "a":a,
                        "b":b,
                        "Midpoint m":m0,
                        "f(m)":f(m0),
                        "Half-interval":(b-a)/2
                  })
                  if f(m0) ==0:
                    found =True
                    root =m0
                    count+=1
                    break 
                  elif f(m0)*f(a)>0:  
                    a =m0
                                            
                  elif f(m0) *f(a) <0:
                        b=m0
                  
                  count+=1
                  
                 
            if not found:
                  root =(a+b)/2
                  

                             
            iteration_df =pd.DataFrame(iteration_data)
            
            st.write("Approximate root : ",root)
            st.write("Number of iterations : ",count)
            st.success("The stopping criterion has been satisfied.")
            
            

            tab1 ,tab2 =st.tabs(["Graph","Iteration Table"])
            with tab1:
                  st.subheader("You are viewing the results as a line graph.")
                  plt.title("Polynomial Root Finding - Bisection Method ")
                  plt.xlabel("x")
                  plt.ylabel("f(x)")
                  plt.plot(x,f(x),color="blue")
                  plt.scatter(root,f(root),color="red")
                  plt.grid(True)
                  plt.axhline(y=0,color="green")
                  st.pyplot(plt.gcf())
            with tab2:
                  st.subheader("You are viewing the iteration results in tabular form.")
                  st.dataframe(iteration_df,use_container_width=True)
