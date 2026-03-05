import random

# Main function, generates a random valid national ID. 
# Takes birth date as day month year as parameters. Leave blank for random birth date.
def generateFNr(day,month,year):
    #Generate random birth date if left blank
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
    
    # Generate random "individual number". Does not take birth year into account (yet).
    #TODO take birth year into account.
    indNumber = str(random.randrange(000,999)).rjust(3,"0")

    #Concatenate everything but control numbers
    cSource = day + month + year + indNumber

    #Create control number 1
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

    #Create control number 2
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

    #Concatenate everything to create national ID
    fNr =  cSource + str(control1) + str(control2)
    return fNr