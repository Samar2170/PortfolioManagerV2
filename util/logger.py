import datetime
import logging
import logging.handlers
import socket
import uuid
from time import strftime
from django.utils.deprecation import MiddlewareMixin
from pf_manager.constants import LOGGING_FILES_DIR

class Logger:
    __root_file_handler=None
    __metric_file_handler=None
    __audit_file_handler=None

    __root_logger=None
    __metric_logger=None
    __audit_logger=None

    __root_logger_file_name = '{}/{}-{}-app.log'.format(LOGGING_FILES_DIR,
                                                        socket.gethostname(), strftime('%Y-%m-%d'))
    __metric_logger_file_name = '{}/{}-{}-metric.log'.format(LOGGING_FILES_DIR,
                                                             socket.gethostname(), strftime('%Y-%m-%d'))
    __audit_logger_file_name = '{}/{}-{}-audit.log'.format(LOGGING_FILES_DIR,
                                                           socket.gethostname(), strftime('%Y-%m-%d'))

    def __init__(self):
        self.__stream_handler = logging.StreamHandler()
        print('Logger initialized')
        self.__root_logger = logging.getLogger()
        self.__root_logger.setLevel(logging.INFO)

        self.__metric_logger = logging.getLogger('metricLogger')
        self.__metric_logger.setLevel(logging.INFO)
        self.__metric_logger.propagate = True

        self.__audit_logger = logging.getLogger('auditLogger')
        self.__audit_logger.setLevel(logging.INFO)
        self.__audit_logger.propagate = True

        formatter = logging.Formatter('[%(asctime)s][PID:%(process)d][TID:%(thread)d][%(levelname)s][%(name)s]--%(message)s')
        self.init_root_logger(formatter)
        self.init_metric_logger(formatter)
        self.init_audit_logger(formatter)

    def init_root_logger(self, formatter):
        self.__root_file_handler = logging.handlers.RotatingFileHandler(self.__root_logger_file_name,maxBytes=100*1024*1024,backupCount=5)
        self.__root_file_handler.setFormatter(formatter)
        self.__root_file_handler.setLevel(logging.INFO)
        self.__root_logger.addHandler(self.__root_file_handler)
        
        self.__stream_handler.setLevel(logging.INFO)
        self.__stream_handler.setFormatter(formatter)

        self.__root_logger.addHandler(self.__stream_handler)
        self.__root_logger.info('Root Logger initialized')
    
    def init_metric_logger(self, formatter):
        self.__metric_file_handler = logging.handlers.RotatingFileHandler(self.__metric_logger_file_name,maxBytes=100*1024*1024,backupCount=5)
        self.__metric_file_handler.setFormatter(formatter)
        self.__metric_file_handler.setLevel(logging.INFO)
        self.__metric_logger.addHandler(self.__metric_file_handler)
        self.__metric_logger.info('Metric Logger initialized')

    def init_audit_logger(self,formatter):
        self.__audit_file_handler = logging.handlers.RotatingFileHandler(self.__audit_logger_file_name,maxBytes=100*1024*1024,backupCount=5)
        self.__audit_file_handler.setFormatter(formatter)
        self.__audit_file_handler.setLevel(logging.INFO)
        self.__audit_logger.addHandler(self.__audit_file_handler)
        self.__audit_logger.info('Audit Logger initialized')

class DjangoRequestLogger(MiddlewareMixin):
    metric_logger = logging.getLogger('metricLogger')
    audit_logger = logging.getLogger('auditLogger')

    def process_request(self,request):
        curr_time=datetime.datetime.utcnow()
        request.request_start_time=curr_time
        request._request_id=str(uuid.uuid4())
        self.audit_logger.info('Got Request for the API %s at time %s.Generated request id is %s. Request data is %s.',
                               request.path, curr_time, request._request_id, self.get_request_information(request))

    def process_response(self,request,response):
        curr_time=datetime.datetime.utcnow()
        diff = curr_time - request.request_start_time
        self.metric_logger.info('%s sec elapsed in processing API %s request with id %s.', diff.total_seconds(),request.path,request._request_id)
        return response
    
    def get_request_information(self,request):
        request_information=dict()
        request_information['path']=request.path
        request_information['headers']=request.headers
        request_information['cookies'] = request.COOKIES
        request_information['data'] = request.GET or request.POST
        return request_information