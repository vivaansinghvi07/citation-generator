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
