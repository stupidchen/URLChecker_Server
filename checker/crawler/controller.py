from grab import Grab

class Node():
    def __init__(self, url, parent, depth):
        self.u = url
        self.f = parent
        self.d = depth

class SimpleGrabSpider():
    def __init__(self):
        self.g = Grab()

    def get_related_url(self, url):
        t = self.g.go(url).doc
        # TODO - Get related url in t and extract the domain name
        return ['test.com', 'aa.com']

    def grab(self, url, layer):
        q = []
        q.append(Node(url, None, 0))
        h = 0
        t = 1
        while h < t:
            if q[h].d >= layer:
                break

            c = self.get_related_url(q[h].u)
            for u in c:
                t += 1
                q.append(Node(u, h, q[h].d + 1))

            h += 1
        return q