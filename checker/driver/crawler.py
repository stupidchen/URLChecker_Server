from checker.driver.base import BaseDriver


class CrawlerDriver(BaseDriver):
    def __init__(self):
        BaseDriver.__init__(self, 'crawler')

    def query_related_url(self, url, layer):
        ret = getattr(self.driver_class, self.method)(url, layer)
        return ret
