# myapp.py
import logging
import libs.mylib as mylib
from libs.set_log import set_log

set_log('both')

if __name__ == '__main__':
    logging.debug('Started')
    mylib.do_something()
    logging.info('Finished')
