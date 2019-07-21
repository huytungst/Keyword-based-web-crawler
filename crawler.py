from googlesearch import search
import urllib.request
import urllib.error
from urllib.request import Request, urlopen
from inscriptis import get_text
import ssl

keyword = input('What are you searching for? ')
num = int(input ('Number of search results? '))

allresults = ''

with open("TEXT.txt", "w") as f:
  for url in search(keyword, stop=num):
    try:
      ssl._create_default_https_context = ssl._create_unverified_context
      req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'})
      html = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')
      text = get_text(html)
      result = url+'\n'+text+'\n************************************\n'
      f.write(allresults.join(result))
      print (url +'\n Done.')
    except urllib.request.HTTPError:
      print (url+'\n HTTP Error. Can not open this link.')
    except urllib.error.HTTPError:
      print (url+'\n HTTP Error. Can not open this link.')
    except UnicodeEncodeError:
      print (url+'\n ENCODE Error. Can not open this link.')
    except ValueError:
      print (url + '\n VALUE Error. Can not open this link.')
      
print ('\nEND OF SCRAPING. DOWNLOAD THE TEXT FILE FOR THE RESULTS.')
