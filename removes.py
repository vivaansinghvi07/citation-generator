import re

# removes everything between html tags labeled "target"
def remove(data, target):
    # gets all occurences of "<target..." in the data
    starts = [m.start() for m in re.finditer('<' + target, data)][::-1]

    # gets all occurences of "</target" in the data
    stops = [m.start() for m in re.finditer('</' + target, data)][::-1]

    # both are reversed in order to delete properly

    # converts length to variable to decrease runtime
    length = len(target)

    # performs removals; 3 added to account for the </ and > in the end tag
    for start, stop in zip(starts, stops): 
        data = data[:start] + data[(stop + length + 3):]

    # returns the data
    return data

def removeHTMLTags(data):
    # creates start and stop arrays
    starts, stops = [], []
    
    # gets starts and stops of html tags
    for i in range(len(data)):
        if data[i] == "<":
            starts.append(i)
        elif data[i] == ">":
            stops.append(i)

    # performs the deletions
    for start, stop in zip(starts, stops):
        data = data[:start] + data[(stop + 1):]
    
    # returns the data
    return data
