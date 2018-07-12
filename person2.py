#July 12th 2018
#Return a dictionary

def build_person(first_name, last_name, age=""):
    """Return a dictionary of information about a person"""
    person = {"first" : first_name, "last" : last_name}
    if age:
        person["age"] = age
    return person

musician = build_person("Jimi", "Hendrix", age=27)
print(musician)
