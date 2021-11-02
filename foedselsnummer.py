import random

def generateFNr(day,month,year):
    if day == None:
        day = str(random.randrange(1,31)).rjust(2,"0")
    else:
        day = str(day)
    if month == None:
        month = str(random.randrange(1,12)).rjust(2,"0")
    else:
        month = str(month)
    if year == None:
        year = str(random.randrange(00,99)).rjust(2,"0")
    else:
        year = str(year)

    indNumber = str(random.randrange(000,999)).rjust(3,"0")

    cSource = day + month + year + indNumber

    control1 = 11-((
        3*int(cSource[0]) +
        7*int(cSource[1]) +
        6*int(cSource[2]) +
        1*int(cSource[3]) +
        8*int(cSource[4]) +
        9*int(cSource[5]) +
        4*int(cSource[6]) +
        5*int(cSource[7]) +
        2*int(cSource[8]))%11)

    if control1 in [10,11]:
        control1 = 0

    control2 = 11-((
        5*int(cSource[0]) +
        4*int(cSource[1]) +
        3*int(cSource[2]) +
        2*int(cSource[3]) +
        7*int(cSource[4]) +
        6*int(cSource[5]) +
        5*int(cSource[6]) +
        4*int(cSource[7]) +
        3*int(cSource[8]) +
        2*int(control1))%11)

    if control2 in [10,11]:
        control2 = 0

    fNr =  cSource + str(control1) + str(control2)
    return fNr