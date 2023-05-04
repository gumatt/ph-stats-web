from src.xutilities.logging import logger as default_logger



def logging_test_uc1(info, logger=default_logger):
    # logger parameter included so that context logger can be passed in with 
    #   tracer id (and other extras) already bound to it
    my_logger = logger.bind(info=info)
    my_logger.info('in logging_test_uc1, info:{}', info)
    return logging_test_uc2(logger)


def logging_test_uc2(logger=default_logger):
    logger.patch(lambda record: record['extra'].update(uc2_payload={'a': 1234, 'bar': 'foo'})).info('in uc2')
    logger.info('in logging_test_uc2')
    return True
