import urllib.request 


urllib.request.urlretrieve('https://dark-prince05.github.io/odin-recipes','webpage.html')
print(open('webpage.html'))
for line in open('webpage.html'):
    print(line)