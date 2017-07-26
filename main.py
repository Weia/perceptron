import my_perceptron
if __name__ == '__main__':
    p = my_perceptron.Perceptron(2,my_perceptron.activator)
    input_all,labels=my_perceptron.get_dataset()
    p.train(input_all,labels,0.1,10)
    p.print_weights()
    print p._forward([1,1])
    print p._forward([1,0])
    print p._forward([0,1])
    print p._forward([0,0])
