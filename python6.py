#25
total = 0
print "how many numbers do you want to add together?"
userInput = int(raw_input())

for x in range(userInput):
    print "Enter a number"
    userInput = int(raw_input())
    total = total + userInput
print total 

#50

totalCost = []
print "How many numbers do you want to add together?"
userInput2 = int(raw_input())

for x in range(userInput):
    print "enter a number"
    userInput2 = int(raw_input())
    totalCost.append(userInput2)
print sum(totalCost)

#75
print "what number do you want to take the factorial of?"
userInput3 = int(raw_input())
#def factorial(userInput3)
for x in range(userInput3):
    print "enter a number"
    user