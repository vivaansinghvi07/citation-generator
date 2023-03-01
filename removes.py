import re

# removes anything between script tags in the data
def removeScripts(data):
    # gets all occurences of "<script..." in the data
    starts = [m.start() for m in re.finditer('<script', data)][::-1]

    # gets all occurences of "</script" in the data
    stops = [m.start() for m in re.finditer('</script', data)][::-1]

    # both are reversed in order to delete properly

    # performs removals
    for start, stop in zip(starts, stops): 
        data = data[:start] + data[(stop + 9):]

    # returns the data
    return data

# removes anything between style tags in the data
def removeStyles(data):
    # gets all occurences of "<style..." in the data
    starts = [m.start() for m in re.finditer('<style', data)][::-1]

    # gets all occurences of "</style..." in the data
    stops = [m.start() for m in re.finditer('</style', data)][::-1]

    # reversed for same reason

    # goes through every and removes all styles
    for start, stop in zip(starts, stops):
        data = data[:start] + data[(stop + 8):]

    # returns data
    return data