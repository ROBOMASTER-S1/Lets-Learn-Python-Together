class Pets:
    def __init__(self,dog,cat,bird,fish):
        self.dog=dog;self.cat=cat
        self.bird=bird;self.fish=fish

    def get_attributes(self): # (self) calls itself to get the attribute values we want.
        print('I got the',self.dog,'attribute from the function \
get_attributes, through the base class Pets.')

a=Pets('Dog','Cat','Bird','Fish') # attribute values from the Pets class

print('I got the',a.dog,'attribute right from the base class Pets.')

Pets.get_attributes(a) # call the function get_attributes, via the Pets class.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This Pets class Python program example is exactly the
# same as the Pets class Python program example above.
# However, without a __init__ constructor method, the program
# looks rather bulky and cluttered.

class Pets:
    def get_attributes(self):  # (self) calls itself to get the attribute values we want.
        print('I got the',self.dog,'attribute from the function \
get_attributes, through the base class Pets.')

a=Pets()
a.dog='Dog'
a.cat='Cat'
a.bird='Bird'
a.fish='Fish'  # attribute values from the Pets class

print('I got the',a.dog,'attribute right from the base class Pets.')

Pets.get_attributes(a) # call the function get_attributes, via the Pets class.
