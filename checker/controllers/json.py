from pecan import expose
from checker.driver.crawler import CrawlerDriver
from checker.driver.model import ModelDriver
import logging
import traceback


class JSONController(object):
    @expose('json')
    def safety(self, *args, **kwargs):
        url = args[0]
        ret = ModelDriver().query(url)

        return {
            "url": url,
            "safety": ret
        }

    @expose('json')
    def related(self, *args, **kwargs):
        logging.info(kwargs)
        url = kwargs.get('url')
        layer = int(kwargs.get('layer'))

        try:
            ret = CrawlerDriver().query_related_domain(url, layer)
        except Exception as e:
            logging.error(e)
            traceback.print_exc(logging._srcfile)

        return {
            "data": ret,
            "error": 0
        }
