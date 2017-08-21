import urllib2, re
from speech import say

def find(x):     #simple dictionary code copy-pasted from stack overflow
    srch=str(x)
    x=urllib2.urlopen("http://dictionary.reference.com/browse/"+srch+"?s=t")
    x=x.read()
    items=re.findall('<meta name="description" content="'+".*$",x,re.MULTILINE)
    for x in items:
        y=x.replace('<meta name="description" content="','')
        z=y.replace(' See more."/>','')
        m=re.findall('at Dictionary.com, a free online dictionary with pronunciation,              synonyms and translation. Look it up now! "/>',z)
        if m==[]:
            if z.startswith("Get your reference question answered by Ask.com"):
                print "Word not found! :("
            else:
		z = z[z.index(',')+2:z.index("See more")]
               # print z
		say(z)
