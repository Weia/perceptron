# coding:utf-8
class Perceptron(object):
    """

    """
    def __init__(self,input_num,activator):

        self.activator=activator
        #权重初始化为0
        self.weights=[0.0 for i in range(input_num)]
        #偏置项初始化为0
        self.bias=0.0
        #self.bias=[0.0 for i in range(input_num)]
    def __str__(self):
        """打印学习到的权重和偏置项"""
        return 'weights: %s \n bias :%f \n' %(self.weights ,self.bias)
    def caculate(self,input_x):
        """输入向量，输出计算结果"""
        return self.activator(
            reduce(lambda a,b:a+b,
                   map(lambda (x,w) :x*w ,zip(input_x,self.weights)),self.bias)
        )
    def train(self,input_all,labels,iteration,rate):
        for i in range(iteration):
            self._one_iteration(input_all,labels,rate)

    def _one_iteration(self, input_all, labels, rate):
        samples=zip(input_all,labels)
        for input_x,label in samples:

            output=self.caculate(input_x)
            if output!=label:
                self._update_weights(input_x,output,label,rate)

    def _update_weights(self,input_x,output,label,rate):
        d=label-output
        self.weights=map(lambda (x,w):w+x*rate*d,zip(input_x,self.weights))
        self.bias+=d*rate
def f(x):
    """
    激活函数
    :param x:
    :return:
    """
    return 1 if x>0 else 0
def get_dataset():
    input_all=[[1,1],[1,0],[0,1],[0,0]]
    labels=[1,0,0,0]
    return input_all,labels
def train_and_perceptron():
    p=Perceptron(2,f)
    input_all,labels=get_dataset()
    p.train(input_all,labels,10,0.1)
    return p

if __name__ == '__main__':
    and_perceptron=train_and_perceptron()
    print and_perceptron
    print and_perceptron.caculate([1,1])
    print and_perceptron.caculate([1,0])
    print and_perceptron.caculate([0,1])
    print and_perceptron.caculate([0,0])






