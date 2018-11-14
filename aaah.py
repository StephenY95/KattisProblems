jon = str(input())
doctor = str(input())

jonA = list(jon)
jonA = jonA[:-1]

doctorA = list(doctor)
doctorA = doctorA[:-1]

if len(jon) > len(doctor):
    print("go")
else:
    print("no")
