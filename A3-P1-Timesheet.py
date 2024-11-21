#Program 1 – Timesheet
#Description:   Design and write a program that accepts the number of hours worked on 
#               each of five work days from the user, then displays different 
#               information calculated about those entries as output. 
#Student #:   W0443556  
#Student Name: Kyle Preston

    
def hours_Worked(workhours):                                                                    #loop statement  works with a for loop ranging my numbers between 1 to 5 for the data needed for days
    for workday in range(1,6):                                                                   #workday uses the loop values to repeat itself with the input asking for the hours, append command holds my values entered through input for each day
        workhours_input = int(input(f"Enter hours worked on Day #{workday}: "))
        workhours.append(workhours_input)


def printBusiestDay(workhours):                                                           # function is to find and determine which day was worked the longest and how many hours were worked on that day      
    most_hours = max(workhours)
    longest_day = workhours.index(most_hours) + 1
    print("The most hours worked was on: \nDay #{0} when you worked {1} hours.".format(longest_day,most_hours))


def total_h(workhours):                                                                 #this function is to find the average hours on the five day rotation and having be displayed through a print statement
    totalhours = sum(workhours)
    averagehours = sum(workhours) / len(workhours)
    print("The total number of hours worked was: {0}\nThe average number of hours worked each day was: {1}".format(totalhours,averagehours))


def underseven(workhours):


    print("Days you slacked off (i.e. worked less than 7 hours):")                             # this function worked to discover which days you "slacked off " by which is working under 7 hours, it displays all days relevant with hours worked on those days
    for workday in workhours:
        if workday < 7:
            shortdays = workhours.index(workday) + 1
            print('Day #{0}: {1} hours'.format(shortdays, workday))


def main():                                                                                                     #My main function to basically call all of my other functions and to clean up the print statement with bordered instructed to be like the output given from assignment doc.
    
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