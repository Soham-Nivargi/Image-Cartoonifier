import numpy as np
import matplotlib.pyplot as plt

def compute_cost(w, b, years, sal):
    squared_error = 0
    for i in range(0, len(years)):
        squared_error += (w*years[i] + b - sal[i])**2
    cost = squared_error/(2*len(years))
    return cost

def compute_gradient(w, b, years, sal):
    deriv = []
    error = []
    deriv_w = 0
    deriv_b = 0
    for i in range(0, len(years)):
        error.append(w*years[i]+b-sal[i])
        deriv_w += error[i]*years[i]
        deriv_b += error[i]
    deriv.append(deriv_w/3)
    deriv.append(deriv_b/3)
    return deriv

def compute_gradient_descent(years, sal, w_init, b_init, alpha, num_iters):
    w = w_init
    b = b_init
    
    for i in range(0, num_iters):
        temp = compute_gradient(w, b, years, sal)
        w = w - alpha*temp[0]
        b = b - alpha*temp[1]
    
    param = [w,b]
    return param
        
        

years = [1,3,5]
sal = [300, 480, 570]

plt.scatter(years, sal)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot')
#plt.show()
#print(compute_cost(200,100,years,sal))

#print(compute_gradient(200, 100, years, sal))

listt = compute_gradient_descent(years, sal, 0, 0, 0.01, 10000)
print(listt)

print(compute_cost(listt[0], listt[1], years, sal))