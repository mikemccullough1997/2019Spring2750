#5
n = 0
while n <= 50:
    n = n + 5 
    print(n)

#6 
def strFunc(numSix):
    n = 0 
    spaces = 0
    while n < len(numSix):
        if numSix[n] == " ":
            spaces = spaces + 1
        spaces = spaces + 1
    return spaces

#7
# Big thanks to Dylan for assisting on this one a little bit
# I think I'm close but still slightly off...
def avgScores():
    examScores = True
    scores = 0 
    sumScores = 0

    while examScores:
        action = None

        try:
            action = input("Enter Score:")
            if examScores == "stop"
                else:
                    scores = scores + 1
                    sumScores = sumScores + action
    return sumScores / scores

#8
def paliQuestion(numEight):
    palidrome = True
    n = 0

    while n < len(numEight) / 2 + 1:
        if numEight[n].lower() != numEight[-n - 1].lower():
            palindrome = False
            n = n + 1
    return palindrome

    