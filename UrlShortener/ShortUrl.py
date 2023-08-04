import os
from dotenv import load_dotenv
import pyshorteners

load_dotenv()

url = input("Enter the URL : ")

bitlyShorten = pyshorteners.Shortener(api_key=os.getenv("BITLY_API_KEY"))
short_url = bitlyShorten.bitly.short(url)

print("The Shortened URL is : " + short_url)
