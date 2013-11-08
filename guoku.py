# -*- coding: utf-8 -*-
# import re
# import urllib2
# for i in xrange(1, 100):
#     p = urllib2.urlopen(url + str(i))
#     content = p.read()
#     print content
#     exit()

from pyquery import PyQuery as pq

url = 'http://guoku.com/selected/?p='

fp = open('/Users/Julytwilight/Documents/Development/Python/exercise/guoku.txt', 'w')

num = 0
for page in xrange(1, 1000):
    html = pq(url + str(page))
    divs = html('.entity-attrs')
    for i in xrange(0, len(divs)):
        div = divs.eq(i)
        title = div('h3 a').text().encode('utf-8').strip()
        div.make_links_absolute()
        href = div('h3 a').attr('href')
        fp.write(title + '\n')
        fp.write(href + '\n\n\n')

    num += 1
    print num

fp.close()