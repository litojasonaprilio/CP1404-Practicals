NUMBER_OF_PEOPLE = 1
names = []
dobs = []
for i in range(NUMBER_OF_PEOPLE):
    name_input = input("Enter {} name: ".format(i + 1))
    names.append(name_input)
    dob_input = input("Enter {} date of birth (d/m/y): ".format(i + 1))
    parts = dob_input.split("/")
    one_dob = tuple([int(part) for part in parts])
    dobs.append(dob_input)

print("{} = {}".format(names, dobs))