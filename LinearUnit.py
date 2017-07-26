from perceptron import  Perceptron

class LinearUnit(Perceptron):
    """"""
    def __init__(self,input_dim,f):
        """"""
        Perceptron.__init__(self,input_dim,f)
def activator(x):
    return  x
def get_dataset():
    input_all=[[1,2,3],[2,3,0.4],[3,4,3.5]]
    labels=[3000,4000,5000]
    return input_all,labels
def train_LinearUnit():
    input_all,labels=get_dataset()
    lu=LinearUnit(3,activator)
    lu.train(input_all,labels,10,0.01)
    return lu

if __name__ == '__main__':
    lu=train_LinearUnit()
    print  lu
    print lu.caculate([1, 2, 3])
    print lu.caculate([2,3,0.4])
    print lu.caculate([3,4,3.5])
