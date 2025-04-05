'''Encapsulation
Restricting direct access to some components
Access modifiers (naming conventions in Python):
Public: Regular names (accessible from anywhere)
Protected: Names with single underscore prefix _var (convention only)
Private: Names with double underscore prefix __var (name mangling)
Getter and setter methods: Control access to attributes
Python transforms __private_var to _MyClass__private_var behind the scenes. This is the name mangling process.

obj = MyClass()
print(obj._MyClass__private_var)  # Works: "I'm mangled"
print(obj._MyClass__private_method())  # Works: "Private method"
1.Prevent accidental name collisions in inheritance hierarchies
2.Provide a weak form of encapsulation (not true privacy)

Important Distinctions
Single underscore (_var): Convention indicating "private" but no mangling occurs
Double underscore (__var): Name mangling occurs
Double underscore on both ends (__var__): Special methods, no mangling



'''
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
        
my_account = BankAccount("Debajyoti", 5545554)
#print(my_account.__id) # This would cause an error
print(my_account.get_id()) # Private members can be accessed by getter methods
print(my_account._BankAccount__id) # Direct access to mangled name