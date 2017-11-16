import urllib
import urllib2
url = "https://github.com/"
user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
volues = {'User-agent' : user_agent}
headers = {'User-Agent' :user_agent }
data = urllib.urlencode(volues) request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)
page = response.read()
