#!../bin/python3
# lucky.py - Opens several Google search results.

import requests, sys, webbrowser, bs4

print('Googling...')        # display text while downloading the Google page
res = requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
print(res)
# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, features="html.parser")

# Open a browser tab for each result.
#linkElems = soup.select('.MjjYud a')
linkElems = ['facebook.com', 'yahoo.com', 'linkedin.com']
numOpen = min(5, len(linkElems))
if linkElems == []:
    print("NO LINKS AVAILABLE")
else:
    for i in range(numOpen):
        webbrowser.open(linkElems[i])
