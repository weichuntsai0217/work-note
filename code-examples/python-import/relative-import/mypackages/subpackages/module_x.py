from ..module_y import fy1

def fx1(args = None):
    if args:
        print('In fx1, args = ', args)
        fy1(args)
    else:
        print('fx1')

if __name__ == '__main__':
    print('Unit test for module_x.py')
    fx1()
    fx1('run module_x.py unit test')
