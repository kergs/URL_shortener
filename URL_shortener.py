#pip install pyshorteners
import pyshorteners
print("Enter URL")
url  = input(":>> ")

type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(url)

print("Shortener Url is: "+ short_url)