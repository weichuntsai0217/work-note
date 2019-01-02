import logging

def set_log(flag='both'):
    msg_fmt = '[%(asctime)s]%(message)s'
    if flag == 'console':
        logging.basicConfig(format=msg_fmt, level=logging.INFO)
    elif flag == 'file':
        logging.basicConfig(format=msg_fmt, level=logging.INFO, filename='myapp.log')
    else: # 'both'
        logging.basicConfig(format=msg_fmt, level=logging.INFO, filename='myapp.log')
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter(msg_fmt))
        logging.getLogger().addHandler(console_handler)

