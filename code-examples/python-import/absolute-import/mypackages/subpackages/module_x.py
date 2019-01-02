import os
abs_file_path = os.path.abspath(__file__)
abs_dir_path = os.path.dirname(abs_file_path)
abs_package_dir_path = os.path.join(abs_dir_path, '../')
print('module_x.py is in directory ' + '"' + abs_dir_path + '"')
print('mypackages directory abs path is ' + '"' + abs_package_dir_path + '"')

import sys
sys.path.insert(0, abs_package_dir_path)

from module_y import fy1

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
