import requests
import removes

# get the web url from the user
url = input("Enter the URL here: ")

# gets the request
try:
    r = requests.get(url)
except:
    print("Invalid URL!")
    quit()

# tries to get the data from the webpage
try:
    data = r.text
except:
    print("Data could not be retrived from this page!")

# removes the scripts and styles from the html source
data = removes.remove(data, "script")
data = removes.remove(data, "style")

# prints the data
print(data)


