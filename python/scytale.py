#str1 becomes scyatle cipher with key
def scytale(str1, key):
    new_str = ""    #sctaled string
    strlist = []
    key_count = 0
    # the number of list is key
    for k in range(key):
        strlist.append("")
    # distribute str to strlist implement
    for s in str1:
        strlist[key_count] += s
        key_count = (key_count + 1) % key
    # united string of strlist
    for strs in strlist:
        new_str += strs
    return new_str

#programming now...
#def disscytale(str1, key):
#    return new_str

str1 = "ItsHotToday"
key = 3
str1_scytale = scytale(str1,key)
print(str1_scytale)
#str1_disscytale = disceaser(str1_scytale,key)
#print(str1_disscyatle)