from pecan import conf
import sys


class BaseDriver(object):
    def __init__(self, config_name='base'):
        config = conf.to_dict().get(config_name)

        dir = config.dir
        if dir is None:
            return
        if not dir in sys.path:
            sys.path.append(dir)
        callee = config.callee
        if not callee in sys.modules:
            callee_class = __import__(callee)
        else:
            eval('import ' + callee)
            callee_class = eval('reload(%s)' % callee)
        self.driver_class = callee_class
        self.method = config.method
