# def print_numbers(int):
#     x = 1
#     while x <= int:
#         print x
#         x += 1
#
# print_numbers(10)
#-----------------------

def remove(somestring, sub):
    """Return somestring with sub removed."""
    location = somestring.find(sub)
    if location >= 0:
        #print "here is location:",location
        length = len(sub)
        part_before = somestring[:location]
        part_after = somestring[location + length:]
        return part_before + part_after
    return somestring

#
# Don't change these test cases!
print remove('audacity', 'a')
print remove('pythonic', 'ic')
print remove('substring institution', 'string in')
print remove('ding', 'do')  # "do" isn't in "ding"; should print "ding"
print remove('doomy', 'dooming')  # and this should print "doomy"
print remove('doomy', 'doomy')
print remove('fart', 'f')
