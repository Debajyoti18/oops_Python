'''Encapsulation
Restricting direct access to some components
Access modifiers (naming conventions in Python):
Public: Regular names (accessible from anywhere)
Protected: Names with single underscore prefix _var (convention only)
Private: Names with double underscore prefix __var (name mangling)
Getter and setter methods: Control access to attributes'''
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner      # Public attribute
        self._balance = balance  # Protected attribute (convention)
        self.__id = 12345       # Private attribute (name mangling)
    
    # Getter method
    def get_balance(self):
        return self._balance
    
    # Setter method
    def set_balance(self, amount):
        if amount > 0:
            self._balance = amount
    def get_id(self):
        return self.__id
         
my_account = BankAccount("Debajyoti",5545554)   
#print(my_account.__id) // error 
print(my_account.get_id()) #private members can be accessed by getter methods
