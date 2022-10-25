
"""

Implement a superclass Appointment and subclasses Onetime, Daily, and Monthly. An 
appointment has description (for example, "see the dentist") and a date. Write a method
occursOn(year, month, day) that check whether the appointment occurs on that date. For
example, for a monthly appointment, you must check whether the day of the month matches.
Then fill a list of Appointment objects with a mixture of appointments. Have the user 
enter a date and print out all appointments that occurs on that date.

"""

##
#  This module defines the Appointments superclass
#

class Appointment():
    ## Constructs an appointment
    # @param description description of appointment
    # @param year year of appointment
    # @param month month of appointment
    # @param day day of appointment
    #
    def __init__(self, description, year, month, day):
        self._description = description
        self._year = year
        self._month = month
        self._day = day
    
    ## Checks whether appointment occurs on given date. Defined in subclasses
    #
    def occursOn(self):
        raise NotImplementedError

##
#  This module defines the onetime appointment subclass.
#

class Onetime(Appointment):
    ## Constructs a onetime appointment for a specific date
    # @param description description of appointment
    # @param year year of appointment
    # @param month month of appointment
    # @param day day of appointment
    #
    def __init__(self, description, year, month, day):
        super().__init__(description, year, month, day)
    
    ## Checks whether appointment occurs on given year/month/day
    #  @param's year/month/day are crosschecked with appointments year/month/day
    #  @return description and date for appointment if equal to appointments year/month/day
    #
    def occursOn(self, year, month, day):
        if (self._year == year) and (self._month == month) and (self._day == day):
            print(f"Onetime appointment: {self._description} on {self._day}/{self._month}/{self._year}")


##
#  This module defines the daily appointment subclass.
#

class Daily(Appointment):
    ## Constructs an appointment with which repeats daily
    # @param description description of appointment    
    #
    def __init__(self, description):
        super().__init__(description, "0000", "00", "00")
    
    ## Daily appointment will occur with daily frequency
    #  @param's year/month/day are crosschecked with appointments year/month/day    
    #  @return returns the description of the daily appointment
    #
    def occursOn(self, year, month, day):
        print(f"Daily appointment: {self._description}")
 
##
#  This module defines the Monthly appointment subclass.
#

class Monthly(Appointment):
    ## Constructs a monthly appointment at a specific day of month
    # @param description description of appointment
    # @param day day of appointment
    #
    def __init__(self, description, day):
        super().__init__(description,"0000","00", day)
    
    ## Monthly appointment will occur with monthly frequency on specific day of month
    #  @param's year/month/day are crosschecked with appointments year/month/day    
    #  @return description of appointment if day matches appointment day
    #
    def occursOn(self, year, month, day):
        if (self._day == day):
            print(f"Monthly appointment: {self._description} on the {self._day} each month")




# Create appointment list
appointments = []

# Add appointments relating to each subclass
onetime = Onetime("See the dentist", "2022", "11", "11")
appointments.append(onetime)

daily = Daily("Go to bed at 22:00")
appointments.append(daily)

monthly = Monthly("Pay electricity bill", "15")
appointments.append(monthly)


# User can input date and retrieve appointments
year = str(input("Input year: "))
month = str(input("Input month: "))
day = str(input("Input day: "))

for i in appointments:
    if (i.occursOn(year, month, day)) == True:
        print(i.occursOn(year, month, day))


