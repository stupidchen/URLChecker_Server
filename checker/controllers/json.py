from pecan import expose
from checker.driver.crawler import CrawlerDriver
from checker.driver.model import ModelDriver
import logging
import traceback


class JSONController(object):
    @expose('json')
    def safety(self, **kwargs):
        url = kwargs.get('url')
        ret = ModelDriver().query(url)

        return {
            "safety": ret,
            "error": 0
        }

    @expose('json')
    def related(self, **kwargs):
        logging.info(kwargs)
        url = kwargs.get('url')
        layer = int(kwargs.get('layer'))
        ret_dict = None
        error = 0
        errorMsg = None

        try:
            ret = CrawlerDriver().query_related_domain(url, layer)
            ret_dict = map(lambda x: x.__dict__, ret)
        except Exception as e:
            logging.error(e)
            traceback.print_exc(logging._srcfile)
            error = 1
            errorMsg = e.message

        return {
            "data": ret_dict,
            "error": error,
            "errorMsg": errorMsg
        }

    @expose('json')
    def query(self, **kwargs):
        logging.info(kwargs)
        url = kwargs.get('url')
        layer = int(kwargs.get('layer'))
        error = 0
        errorMsg = None
        ret_dict = None

        try:
            ret = CrawlerDriver().query_related_domain(url, layer)
            for node in ret:
                node.s = ModelDriver().query(node.u)
            ret_dict = map(lambda x: x.__dict__, ret)
        except Exception as e:
            logging.error(e)
            traceback.print_exc(logging._srcfile)
            error = 1
            errorMsg = e.message

        return {
            "data": ret_dict,
            "root": {
                "url": url,
                "safety": ModelDriver().query(url)
            },
            "error": error,
            "errorMsg": errorMsg
        }
