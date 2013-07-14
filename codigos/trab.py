import urllib.request

url = "http://heeeeeeeey.com"
resposta = urllib.request.urlopen(url)
print (resposta.read())