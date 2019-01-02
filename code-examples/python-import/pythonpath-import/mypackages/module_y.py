import module_z as mz

def fy1(args = None):
    if args:
        print('In fy1, args = ', args)
        mz.fz1(args)
    else:
        print('fy1')
