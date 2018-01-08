from pecan import expose

class JSONController(object):
    @expose('json')
    def safety(self, *args):
        return {"url": args[0], "safety": 50}

    @expose('json')
    def related(self, *args):
        return {"url": args[0], "layer": args[1], "url_num":2, "related_urls": ["url1", "url2"]}
