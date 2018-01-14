from checker.driver.base import getMod


class CrawlerDriver():
    mod = getMod('checker', 'crawler')

    def __init__(self):
        pass

    def query_related_domain(self, url, layer):
        ret = getattr(self.mod, 'multi_grab')(url, layer)
        return ret
