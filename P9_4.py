"""
Implement a class Address. An address has a house number, a street, an optional
apartment number, a city, a state, and a postal code. Define the constructor such that
an object can be created in one of two ways: with an apartment number or without.

• Supply a print method that prints the address with the street on one line and the city,
  state, and postal code on the next line. 

• Supply a method def comesBefore(self, other)
  that tests whether this address comes before other when compared by postal code.
"""

##
#  This module defines the Address class.
#

class Address:

    ## A constructor with the initial inputs, with apartment number set to "None" as the object can be created without
    def __init__(self, houseNumber, street, city, state, postalCode, apartmentNumber = None):
        self._houseNumber = houseNumber
        self._street = street
        self._city = city
        self._state = state
        self._postalCode = postalCode
        self._apartmentNumber = apartmentNumber
    
    ## Method which prints the address with street on one line and city, state, and postal code on next line.
    def getAddress(self):
        return print(f"{self._street}\n{self._city}, {self._state}, {self._postalCode}")
    
    ## Tests whether this address comes before other when compared by postal code
    def postalCode(self):
        return self._postalCode
    
    def comesBefore(self, otherAddress):
        if int(self._postalCode) > int(otherAddress.postalCode()):
            print("This address comes after the other")
        else:
            print("This address comes before the other")
    

# Testing two addresses
Address1 = Address("12", "Selma E", "Oslo", "Viken", "0581", "7022")
Address2 = Address("30", "Knut A", "Oslo", "Viken", "0555")
Address1.getAddress()
Address2.getAddress()

# Testing if the first address comes after or before the second address        
Address1.comesBefore(Address2)

    
