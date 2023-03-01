import re

# removes anything between script tags in the data
def removeScripts(data):
    starts = [m.start() for m in re.finditer('<script', data)][::-1]
    stops = [m.start() for m in re.finditer('</script', data)][::-1]

    for start, stop in zip(starts, stops): 
        data = data[:start] + data[(stop + 9):]

    return data

# removes anything between style tags in the data
def removeStyles(data):
    starts = [m.start() for m in re.finditer('<style', data)][::-1]
    stops = [m.start() for m in re.finditer('</style', data)][::-1]

    for start, stop in zip(starts, stops):
        data = data[:start] + data[(stop + 8):]

    return data