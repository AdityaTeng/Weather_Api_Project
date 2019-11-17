import logging

def learnLogging():

    username = "ABC User"
    errmsg = "INVALID PASSWORD"

    logging.basicConfig(level=logging.DEBUG, filename='xlsUploaderLog.log', filemode='a')
    logging.basicConfig(level=logging.DEBUG, filename='xlsUploaderLog.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')
    logging.basicConfig(level=logging.DEBUG, filename='xlsUploaderLog.log', filemode='a', format='%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s')
    logging.basicConfig(level=logging.DEBUG, filename='xlsUploaderLog.log', filemode='a', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

    logging.info('Admin logged in')
    logging.basicConfig(level=logging.DEBUG)
    logging.info('ABC User trying to log in')
    logging.warning('This will get logged to a file')
    logging.warning(f'{username} Could not login because of {errmsg}')
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')

if __name__ == '__main__':
    learnLogging()