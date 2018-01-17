# URLChecker

A application can help you to judge a URL whether it is safe.

*Alias: MUS, Malicious URL Sniper*

## Dependecies

### Front-end 

Based on:
- [Bootstrap](https://github.com/twbs/bootstrap)
- [Springy](https://github.com/dhotson/springy/)
- [jquery-animateNumber](https://github.com/aishek/jquery-animateNumber)
- [bootstrap-waitingfor](https://github.com/ehpc/bootstrap-waitingfor)

### Back-end

Based on:
- [Pecan](https://github.com/pecan/pecan)
- [Grab](https://github.com/lorien/grab)

### Others

- [tldextract](https://github.com/john-kurkowski/tldextract)
- [Pbr](https://github.com/openstack-dev/pbr)

## Installation

    $ python setup.py install
    
p.s. You can change checker/cmd/model.py to add your own model.
    
## Run

    $ pecan serve config.py

