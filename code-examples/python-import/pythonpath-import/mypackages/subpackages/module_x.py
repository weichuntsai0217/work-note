from module_y import fy1

def fx1(args = None):
    if args:
        print('In fx1, args = ', args)
        fy1(args)
    else:
        print('fx1')
