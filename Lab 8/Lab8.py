# 6
def wordPop(length):
    textOne = text.split ("")
    nList = 0

    for word in textOne:
        if len(word) = length:
            nList.append(word)
    print(nList)
#7 
ingWord = ". *ing"
firstWord = "manufacturing"
firstExample = re.findall(ingWord, firstWord)

print(firstExample)

#8
aWord = "a.*a$"
secWord = "gorilla"
secExample = re.findall(aWord, secWord)

print(secExample)


