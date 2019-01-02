class A(object):
    def __init__(self, name):
        print('enter A')
        self.name = name + 'A'
        self._name = '_' +  name + 'A'
        self.__name = name + 'A'
        print('leave A')

class B(A):
    def __init__(self, name):
        print('enter B')
        self.name = name + 'B'
        self._name = '_' +  name + 'B'
        self.__name = name + 'B'
        super(B, self).__init__(name)
        print('leave B')

class C(A):
    def __init__(self, name):
        print('enter C')
        self.name = name + 'C'
        self._name = '_' +  name + 'C'
        self.__name = name + 'C'
        super(C, self).__init__(name)
        print('leave C')

class D(B, C):
    def __init__(self, name):
        print('enter D')
        self.name = name + 'D'
        self._name = '_' +  name + 'D'
        self.__name = name + 'D'
        super(D, self).__init__(name)
        print('leave D')

if __name__ == '__main__':
    d = D('John')
    print(d._D__name)
    print(d.__dict__)
    
