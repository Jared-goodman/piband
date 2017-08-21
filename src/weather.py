import urllib, urllib2, json
from speech import say

def conditions():
			baseurl = "https://query.yahooapis.com/v1/public/yql?"
			yql_query = "select item.condition from weather.forecast where woeid in (select woeid from geo.places(1) where text=\"seattle\")"
			yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&format=json"
			result = urllib2.urlopen(yql_url).read()
                        data = json.loads(result)
                        raw =  str(data['query']['results']).lower()
                        #print raw
                        tempvar = raw[raw.index("u\'temp\'")+11:]
                        #print tempvar
                        tempvar = tempvar[0:tempvar.index("\'")]
                        toPrint =  "In your current location, it is " + tempvar + " degrees "
                        #print toPrint
                        tempvar = raw[raw.index("u\'text\'")+11:]
                        tempvar = tempvar[0:tempvar.index("\'")]
                        #print tempvar
                        toPrint = toPrint + "and it is " + tempvar + " outside."
                        print toPrint
                        say (toPrint)

