from loguru import logger



def logging_test_uc1(info, logger=logger):
    my_logger = logger.bind(info=info)
    my_logger.info('in logging_test_uc1, info:{}', info)
    return logging_test_uc2(logger)


def logging_test_uc2(logger=logger):
    logger.patch(lambda record: record['extra'].update(uc2_payload={'a': 1234, 'bar': 'foo'})).info('in uc2')
    logger.info('in logging_test_uc2')
    return True
