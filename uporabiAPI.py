#Najdi državo z največ prebivalci
import requests


url = "https://restcountries.com/v3.1/all?fields=name, population"

klic = requests.get(url)

print(klic)