from random import choice
import webbrowser


s = "2-6, 19, 21, 23-38, 45-99, 101, 103-107, 118-123, 126-169, 172-173, 175-194, 200-201, 205-228, 230-250, 252-273, 275-286, 289-291"
lst = map(lambda x: map(lambda d: int(d), x.split("-")), s.split(", "))

eps = []
for l in lst:
    for el in l:
        eps.append(el)

i = choice(eps)
url = "https://watch-dbz52.funonline.co.in/dragon-ball-z-episode-%d/" % i

#print(eps)
print(url)


# get chrome path
# MacOS
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
# Windows
# chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
# Linux
# chrome_path = '/usr/bin/google-chrome %s'

webbrowser.get(chrome_path).open(url)

