from grab import Grab
import re
import tldextract


class Node():
    def __init__(self, url, parent, depth):
        self.u = url
        self.f = parent
        self.d = depth


class SimpleGrabSpider():
    def __init__(self, *args):
        self.href_regx = '(?<=href=\").*?(?=\")|(?<=href=\').*?(?=\')'
        self.timeout = 2
        pass

    def get_related_url(self, url):
        g = Grab(timeout=self.timeout)
        try:
            resp = g.go(url).body
            urls = re.findall(self.href_regx, resp)
        except:
            urls = []

        return urls

    def get_related_domain(self, url):
        urls = self.get_related_url(url)

        domains = []
        t = tldextract.extract(url)
        domain = t.registered_domain
        if len(domain) != 0:
            domains.append(domain)

        for u in urls:
            t = tldextract.extract(u)
            if len(t.registered_domain) > 0:
                domains.append(t.registered_domain)

        return list(set(domains))

    def grab(self, url, layer):
        t = tldextract.extract(url)
        domain = t.registered_domain
        if len(domain) == 0:
            return []

        q = [Node(domain, None, 0)]
        founded = [domain]
        h = 0
        t = 1
        while h < t:
            if q[h].d >= layer:
                break

            c = self.get_related_domain(q[h].u)
            for u in c:
                if u not in founded:
                    founded.append(u)
                    t += 1
                    q.append(Node(u, h, q[h].d + 1))

            h += 1

        return q, founded


if __name__ == '__main__':
    g = SimpleGrabSpider()
    res, founded = g.grab('http://docs.grablib.org/en/latest/grab/response_search.html', 2)
    print(founded)
