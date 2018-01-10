from pecan import expose
from checker.driver.crawler import CrawlerDriver
from checker.driver.model import ModelDriver


class JSONController(object):
    @expose('json')
    def safety(self, *args):
        url = args[0]
        ret = ModelDriver().query(url)

        return {
            "url": url,
            "safety": ret
        }

    @expose('json')
    def related(self, *args):
        url = args[0]
        layer = args[1]

        ret = CrawlerDriver().query_related_url(url, layer)

        return {
            "graph": ret
        }
