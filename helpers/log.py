import logging


class Log():
    # Log's format
    __log_formatter = (
        '[%(levelname)-7s|%(asctime)s] %(module)-10s:%(lineno)-3s| '
        '%(funcName)-18s | %(message)s'
    )

    def __init__(self, path=None):
        self.__logger = logging.getLogger(__name__)
        self.__formatter = logging.Formatter(self.__log_formatter)
        self.__logger.setLevel(logging.INFO)
        self.__logger_console()
        if path is not None:
            self.__logger_file(path)

    def __logger_console(self):
        """
        Method to create a console handler
        """
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(self.__formatter)
        console_handler.setLevel(logging.INFO)
        self.__logger.addHandler(console_handler)

    def __logger_file(self, path):
        """ Method to create a file handler and create this file in the path

        Arguments:
            path {String} -- Path to create the log file
        """
        handler_info = logging.FileHandler(path)
        handler_info.setFormatter(self.__formatter)
        handler_info.setLevel(logging.INFO)
        self.__logger.addHandler(handler_info)

    def get_logger(self):
        """Method to obtain the logger

        Returns:
            [logger] -- the logger where write the log menssage
        """
        return self.__logger


class DriverLog():
    def create_log(self):
        """
        Method to create the log. If the evidence path isn't None, create the
        log file in the evidence path.
        """
        from settings import evidence_path
        test_case = self.__class__.__name__
        log_extension = '.log'
        if evidence_path is not None:
            log_path = '{}/{}{}'.format(
                evidence_path, test_case, log_extension
            )
        else:
            log_path = None
        self.log = Log(log_path)
        self.log = self.log.get_logger()
        return self.log
