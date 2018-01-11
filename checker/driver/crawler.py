from checker.driver.base import BaseDriver


class CrawlerDriver(BaseDriver):
    def __init__(self):
        BaseDriver.__init__(self, 'crawler')

    def query_related_domain(self, url, layer):
        ret = getattr(self.mod, 'multi_grab')(url, layer)
        return ret
