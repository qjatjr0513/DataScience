import urllib.request

response = urllib.request.urlopen("http://theteamlab.io")
print(response.read())