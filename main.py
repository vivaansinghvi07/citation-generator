import requests
import removes

# get the web url from the user
url = input("Enter the URL here: ")

# gets the request
r = requests.get(url)

# tries to get the data from the webpage
try:
    data = r.text
except:
    print("Data could not be retrived from this page!")

ignore = False

data = removes.removeScripts(data)
data = removes.removeStyles(data)

print(data)


