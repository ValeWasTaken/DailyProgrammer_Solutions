#Counts the amount of $7.99 "Three book bundles" listed on thriftbooks.com

import urllib
from bs4 import BeautifulSoup

def bundleCounter():
        totalBundles = 0
        url = 'http://www.thriftbooks.com/deals.aspx?featureid=402'
        soup = BeautifulSoup(urllib.urlopen(url).read())

        for bundle in soup.find_all("div", class_="bundle-item"):
                totalBundles += 1
        print("Total amount of bundles listed: {0}".format(str(totalBundles)))
bundleCounter()
