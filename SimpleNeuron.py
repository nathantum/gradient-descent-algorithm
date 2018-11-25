

# need to update this files


weights = [2,4]

bias = 1

# Implement the following functions

# Activation (sigmoid) function
def sigmoid(x):
    return 1/(1+np.exp(-x))

# Output (prediction) formula
def output_formula(features, weights, bias):
    output = sigmoid(weights[0]*features[0] + weights[1]*features[1] + bias)

# Error (log-loss) formula
def error_formula(y, output):
    return -y*np.log(output)-(1-y)*np.log(1-output)

# Gradient descent step
def update_weights(x, y, weights, bias, learnrate):
#     𝑤𝑖⟶𝑤𝑖+𝛼(𝑦−𝑦̂ )𝑥𝑖
    
    output = output_formula(X,weights,bias)
    weights[0] = weights[0] + learnrate*(y - output)*x[0]
    weights[1] = weights[1] + learnrate*(y - output)*x[1]
    
#     𝑏⟶𝑏+𝛼(𝑦−𝑦̂ )
    bias = bias + learnrate*(y - output)

b = output_formula(X, weights, bias)
print( b)