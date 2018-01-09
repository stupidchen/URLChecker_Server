from checker.crawler.controller import SimpleGrabSpider

spider = SimpleGrabSpider()

def simple_grab(url):
    return spider.grab(url, 1)


def multi_grab(url, layer):
    return spider.grab(url, layer)
