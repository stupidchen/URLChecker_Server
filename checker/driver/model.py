
from checker.driver.base import getMod
import random


class ModelDriver():
    mod = getMod('checker', 'model')

    def __init__(self):
        pass

    def query(self, url):
        ret = getattr(self.mod, 'query')(url)
        return ret
