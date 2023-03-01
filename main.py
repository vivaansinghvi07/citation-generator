import requests
import removes
import re

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
data = removes.removeByTag(data, "script")
data = removes.removeByTag(data, "style")

# removes all HTML tags
data = removes.removeHTMLTags(data)

# removes whitespace
data = re.sub("[\n \t]+", " ", data)

# splits the data by spaces
words = data.split(" ")

# gets the lengths
character_count = len(data)
word_count = len(words)

# prints the length of the data
print(f"Characters: {character_count}")
print(f"Words: {word_count}")

# shows what was read if asked
show_data = input("Would you like to see what was read? (y/n): ")
if show_data in ['y', 'Y']:
    print(data)