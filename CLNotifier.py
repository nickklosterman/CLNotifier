import sys
import urllib


Datafile=open('Data.txt')
for line in Datafile:
    if not line.strip():# (len(line)<5):#check for blank lines
        print "blank line"
    elif line[0]=='#':
        print "Comment:", line[1:].strip()
    else:
        String=line[:-1].split(',')
        print String
        [searchterms,citycode,pricemax,pricemin,searchcategory,titlematchorpostmatch,emailaddress,updateinterval,daysofresults]=line[:-1].split(',')
#        searchterms=String[0]
#        citycode=String[1]
        if searchcategory == '':
            searchcategory='sss'
        searchterms.replace(" ","+")
        searchterms.replace(' ','+')
        print searchterms
        url='http://%s.craigslist.org/search/' %citycode + \
            '%s?query' %searchcategory + \
            '=%s&catAbb=for&srchType=A' %searchterms + \
            '&minAsk=%s' %pricemin + \
            '&maxAsk=%s'  % pricemax
        print url
#data=urllib.urlopen(url).readlines()
