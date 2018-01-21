from grab import Grab
import re
import tldextract


class Node():
    def __init__(self, url, parent, depth):
        self.u = url
        self.f = parent
        self.d = depth
        self.t = 0


class SimpleGrabSpider():
    def __init__(self, *args):
        self.href_regx = '(?<=href=\").*?(?=\")|(?<=href=\').*?(?=\')'
        self.timeout = 1
        pass

    def get_related_url(self, url):
        try:
            g = Grab(timeout=self.timeout)
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
        domain = tldextract.extract(url).registered_domain
        if len(domain) == 0:
            return []

        q = [Node(domain, None, 0)]
        founded = [domain]
        times = [1]
        h = 0
        t = 1
        while h < t:
            if q[h].d >= layer:
                break

            c = self.get_related_domain(q[h].u)
            for u in c:
                if u not in founded:
                    founded.append(u)
                    times.append(1)
                    t += 1
                    q.append(Node(u, h, q[h].d + 1))
                else:
                    times[founded.index(u)] += 1

            h += 1

        for node in q:
            node.t = times[founded.index(node.u)]
        return q


if __name__ == '__main__':
    g = SimpleGrabSpider()
    res = g.grab('http://www.baidu.com', 1)
    print(res)
