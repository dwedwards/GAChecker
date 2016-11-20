import re
from urllib2 import urlopen

#siteName = raw_input('Enter the URL you want to check>>')

file= raw_input('Enter the text filename with sites to check >>')

def getSite (site):

        print "%s\n" % site

        siteOpen = urlopen(site)
        siteContent = siteOpen.read()

        #Find the location of "UA-" in a variable based on a regex
        #the 'r' states it is regex

        if re.search(r"\bUA-\d{4,10}-\d{1,4}\b", siteContent):

            print "\t**Google Analytics is installed**\n"

        else:

            print "\t**No Google Analytics found**\n"

with open(file) as f:

    for line in f:

        getSite(line)
