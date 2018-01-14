from pecan import conf
import sys
import logging


def getMod(config_name, callee_name):
    config = conf.to_dict().get(config_name)

    logging.info(config)
    cmd_dir = config.get('cmd_dir')
    if cmd_dir is None:
        return
    if not cmd_dir in sys.path:
        sys.path.append(cmd_dir)
    callee = config.get(callee_name)
    if not callee in sys.modules:
        callee_class = __import__(callee)
        return callee_class
    return None
