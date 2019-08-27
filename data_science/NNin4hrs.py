import numpy as np

def sigmoid(x):
  return 1/(1+np.exp(-x))

def sigmoid_derivative(x):
  return x*(1-x)

#input data
x = np.array([[0,0,1],
            [0,1,1],
            [1,0,1],
            [1,1,1]])
X = x.T

#output data
y = np.array([[0],
            [1],
            [1],
            [0]])
Y = y.T
m = Y.shape[1]

#layer_dims = np.array([3,4,1])  

#parameters initialization
W1 = (2*np.random.random((4,3))-1)*0.1 
W2 = (2*np.random.random((1,4))-1)*0.1
b1 = np.zeros((4,1))
b2 = np.zeros((1,1))

#training step
for i in range(60000):
    
    #forward propagation
    A0 = X
    Z1 = np.dot(W1, A0) + b1   
    A1 = sigmoid(Z1)
    Z2 = np.dot(W2, A1) + b2
    A2 = sigmoid(Z2)
    
    CostJ = -np.sum((np.multiply(Y,np.log(A2))+
                     np.multiply((1-Y),np.log(1-A2))))/m
    
    if i%10000 == 0:
      print ("Error: " + str(np.mean(np.abs(CostJ))))
    
    #backward propagation
    dZ2 = A2 - Y
    dW2 = np.dot(dZ2, A1.T)/m
    db2 = np.sum(dZ2, axis=1, keepdims=True)/m
    
    dZ1 = np.dot(W2.T, dZ2)*sigmoid_derivative(A1)
    dW1 = np.dot(dZ1,A0.T)/m
    db1 = np.sum(dZ1, axis=1, keepdims=True)/m
    
    #update parameters
    W1 = W1 - dW1
    b1 = b1 - db1
    W2 = W2 - dW2
    b2 = b2 - db2
    
print ("Output after training")
print (A2)
