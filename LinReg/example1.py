
# linear & polynomial regression model in Python
# url: https://www.youtube.com/watch?v=ro5ftxuD6is
# This brief tutorial demonstrates how to use Numpy and SciPy functions in Python 
# to regress linear or polynomial functions that minimize the least squares difference 
# between measured and predicted values.

import numpy as np

x=np.array([0,1,2,3,4,5])
y=np.array([0,0.8,0.9,0.1,-0.8,-0.1])
print(x)
print(y)


from scipy.interpolate import *
p1=np.polyfit(x,y,1)
p2=np.polyfit(x,y,2)
p3=np.polyfit(x,y,3)
print('p1=',p1)
print('p2=',p2)
print('p3=',p3)


from matplotlib.pyplot import *
plot(x,y,'o')
xp=np.linspace(-2,6,100)
plot(xp,np.polyval(p1,xp),'r-')
plot(xp,np.polyval(p2,xp),'g--')
plot(xp,np.polyval(p3,xp),'m:')
#%matplotlib inline

show()

# compute the residual square error
yfit=p1[0]*x+p1[1]
print(yfit)
print(y)
yresid=y-yfit
SSresid=sum(pow(yresid,2))
SStotal=len(y)*np.var(y)
rsq=1-SSresid/SStotal
print(rsq)

# compute the same value using scipy 
from scipy.stats import *
slope, intercept, r_value, p_value, std_err = linregress(x,y)
print(pow(r_value,2))
