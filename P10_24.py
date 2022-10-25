
"""
Improve the appointment book program of Exercises P10.22 and P10.23 by letting
the user save the appointment data to a file and reload the data from a file. The saving
part is straightforward: Make a method save. Save the type, description, and date to
a file. The loading part is not so easy. First determine the type of the appointment to
be loaded, create an object of that type, and then call a load method to load the data.

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
    
    ## Saving function. Will be different for each subclass such that we can classify type of appointment
    #
    def save(self):
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
    
    ## Saves appointment to a given text file. Will append multiple saved appointments to same text file
    #  @param filename name of text file, e.g., "appointments.txt"
    #
    def save(self, filename):
        file_object = open(filename, "a")
        string_rep  = "Onetime" + "/" + str(self._year) + "/" + str(self._month) + "/" + str(self._day) + "/" + self._description + "\n"
        file_object.write(string_rep)
        file_object.close()

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

    ## Saves appointment to a given text file. Will append multiple saved appointments to same text file
    #  @param filename name of text file, e.g., "appointments.txt"
    #    
    def save(self, filename):
        file_object = open(filename, "a")
        string_rep  = "Daily" + "/" + "0000" + "/" + "00" + "/" + "00" + "/" + self._description + "\n"
        file_object.write(string_rep)
        file_object.close()

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
    
    ## Saves appointment to a given text file. Will append multiple saved appointments to same text file
    #  @param filename name of text file, e.g., "appointments.txt"
    #
    def save(self, filename):
        file_object = open(filename, "a")
        string_rep  = "Monthly" + "/" + "0000" + "/" + "00" + "/" + str(self._day) + "/" + self._description + "\n"
        file_object.write(string_rep)
        file_object.close()


## Method for loading a textfile with an appointment list
def load(filename):
    
    # Opens text file from working directory
    textfile = open(filename, "r")

    # Creates empty list
    appointmentlist = []
    
    # Loop which checks for same format as when using the save method.
    for i in textfile:
        i = i.strip()
        split = i.split("/")
        
        # Retrieves the necessary values from string to run Onetime/Monthly/Daily method
        if split[0] == "Onetime":
            appointmentlist.append(Onetime(str(split[1]), str(split[2]), str(split[3]), split[4]))
        elif split[0] == "Monthly":
            appointmentlist.append(Monthly(str(split[1]), split[4]))
        elif split[0] == "Daily":
            appointmentlist.append(Daily(split[4]))
        i = i.strip()
    
    # Close the open file
    textfile.close()
    
    # Returns a list with the appointments in the loaded file
    return appointmentlist


################################## TESTER ##################################
## Four different appointments of each subclass
onetime_app = Onetime("See the dentist", "2022", "11", "11")
daily_app = Daily("Go to bed at 22:00")
monthly_app = Monthly("Pay electricity bill", "15")
onetime_app2 = Onetime("Christmas celebration", "2022", "12", "24")

## Save 3/4 methods
onetime_app.save("appointments.txt")
daily_app.save("appointments.txt")
monthly_app.save("appointments.txt")

## load the saved appointments
appointments = load("appointments.txt")
