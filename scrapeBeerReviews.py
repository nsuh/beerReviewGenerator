import urllib2
from lxml.html import fromstring
import sys
import time
  
urlprefix = "http://www.beerpal.com/Westvleteren-Abt-12-Beer/"


for page in xrange(1, 1000):
    try:
        response = urllib2.urlopen(urlprefix + str(page))
        html = response.read()
        dom = fromstring(html)
        sels = dom.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "rdat", " " ))]')
        for review in sels:
            if review.text:
                print review.text.rstrip()
        sys.stdout.flush()
        time.sleep(2)
    except:
        continue

