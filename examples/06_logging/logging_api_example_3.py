import logging

logger = logging.getLogger('My Script')
logger.setLevel(logging.DEBUG)

logfile = logging.FileHandler('logfile.log', 'w')
logfile.setLevel(logging.WARNING)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logfile.setFormatter(formatter)

logger.addHandler(logfile)

## messages
logger.debug('Сообщение уровня debug')
logger.info('Сообщение уровня info')
logger.warning('Сообщение уровня warning')

