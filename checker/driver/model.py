from checker.driver.base import BaseDriver


class ModelDriver(BaseDriver):
    def __init__(self):
        BaseDriver.__init__(self, 'model')

    def query(self, url):
        ret = getattr(self.driver_class, self.method)(url)
        return ret
