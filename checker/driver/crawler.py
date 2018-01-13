from checker.driver.base import HasMod


class CrawlerDriver(HasMod):

    def __init__(self):
        self.mod = None
        self.getMod( 'checker', 'crawler')

    def query_related_domain(self, url, layer):
        ret = getattr(self.mod, 'multi_grab')(url, layer)
        return ret
