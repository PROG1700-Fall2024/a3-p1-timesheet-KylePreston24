#Program 1 – Timesheet
#Description:   Design and write a program that accepts the number of hours worked on 
#               each of five work days from the user, then displays different 
#               information calculated about those entries as output. 
#Student #:   W0443556  
#Student Name: Kyle Preston

    
def hours_Worked(workhours):                                                                    #loop statement
    for workday in range(1,6):
        workhours_input = int(input(f"Enter hours worked on Day #{workday}: "))
        workhours.append(workhours_input)


def printBusiestDay(workhours):
    most_hours = max(workhours)
    longest_day = workhours.index(most_hours) + 1
    print("The most hours worked was on: \nDay #{0} when you worked {1} hours.".format(longest_day,most_hours))


def total_h(workhours):
    totalhours = sum(workhours)
    averagehours = sum(workhours) / len(workhours)
    print("The total number of hours worked was: {0}\nThe average number of hours worked each day was: {1}".format(totalhours,averagehours))


def underseven(workhours):


    print("Days you slacked off (i.e. worked less than 7 hours):")
    for workday in workhours:
        if workday < 7:
            shortdays = workhours.index(workday) + 1
            print('Day #{0}: {1} hours'.format(shortdays, workday))


def main():
    
    workhours=[]
    hours_Worked(workhours)
    print("--------------------------------------------------------------------------------------------------")
    printBusiestDay(workhours)
    print("--------------------------------------------------------------------------------------------------")
    total_h(workhours)
    print("--------------------------------------------------------------------------------------------------")
    underseven(workhours)
  
  
  
  # YOUR CODE ENDS HERE

main()