import pyshorteners as sh

link = 'www.facebook.com'

s = sh.Shortener()
x = (s.tinyurl.short(link))

print(x)