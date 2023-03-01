import re

def removeScripts(data):
    starts = [m.start() for m in re.finditer('<script', data)][::-1]
    stops = [m.start() for m in re.finditer('</script', data)][::-1]

    for start, stop in zip(starts, stops): 
        data = data[:start] + data[(stop + 9):]

    return data
