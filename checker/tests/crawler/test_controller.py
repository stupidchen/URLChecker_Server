from unittest import TestCase
from checker.crawler.controller import SimpleGrabSpider

class CrawlerControllerTestUnit(TestCase):

    def simple_test_unit01(self):
        g = SimpleGrabSpider()
        res = g.get_related_url('www.baidu.com')
        assert len(res) > 0

