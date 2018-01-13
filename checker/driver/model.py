from checker.driver.base import HasMod


class ModelDriver(HasMod):
    def __init__(self):
        self.mod = None
        self.getMod('checker', 'model')

    def query(self, url):
        ret = getattr(self.mod, 'query')(url)
        return ret
