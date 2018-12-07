jon = str(input())
doctor = str(input())

jonA = list(jon)
doctorA = list(doctor)

checkJon = 0
checkDoctor = 0
for character in jonA:
    if character == "a":
        checkJon += 1
    elif character == "h":
        pass
    else:
        checkJon = 0
for character in doctorA:
    if character == "a":
        checkDoctor += 1
    elif character == "h":
        pass
    else:
        checkDoctor = 0

if checkJon > checkDoctor:
    print("go")
else:
    print("no")
