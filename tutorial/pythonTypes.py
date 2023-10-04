def add(firstName: str,lastName: str):
    
    return firstName.capitalize() + " " + lastName


fname="yash"
lname= "Arora"

name = add(fname,lname)
print(name)

class Person:
 def __init__(self, name: str):
        self.name = name

def get_person_name(one_person: Person):
    return one_person.name

person = Person("John Doe");
person_name = get_person_name(person)
print(person_name)

