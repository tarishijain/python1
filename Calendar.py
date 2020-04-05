import calendar
y = int(input("Enter the year : "))

print("\n***** CALENDAR *****")
Cal = calendar.TextCalendar(calendar.SUNDAY)
''' An instance of TextCalendar class is created and calendar.
Sunday meeans ypu want to start displaying the calendar from Sunday.'''

i=1
while i<=12 :
    Cal.prmonth(y,i)
    print('\r')
    i+=1
# prmonth() is a function of the class that prints the calendar for given month and year.