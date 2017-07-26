# coding:utf-8
class Perceptron(object):
    """

    """

    def __init__(self, input_dim, activator):
        self.input_dim = input_dim
        self.activator = activator
        self.weights = [0.0 for i in range(input_dim)]
        self.bias = 0.0

    def _forward(self, input_x):
        output = self.activator(reduce(lambda a, b: a + b,
                                       map(lambda (x, w): x * w, zip(input_x, self.weights)), self.bias))
        return output

    def _update_weights(self,input_x,output,label,rate):
        """"""
        d=(label-output)*rate
        self.weights=map(lambda (x,w): w+d*x,zip(input_x,self.weights))
        self.bias+=d
    def train(self,input_values,labels,rate,iterations):
        """"""
        for i in range(iterations):
            samples=zip(input_values,labels)
            for input_x,label in samples:
                output=self._forward(input_x)
                if output!=label:
                    self._update_weights(input_x,output,label,rate)
    def print_weights(self):
        print self.weights
        print self.bias


def activator(x):
    return 1 if x > 0 else 0

def get_dataset():
    input_all=[[1,1],[1,0],[0,1],[0,0]]
    labels=[1,0,0,0]
    return input_all,labels

