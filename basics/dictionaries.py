# phonebook = {}
# phonebook["John"] = 938477566
# phonebook["Jack"] = 938377264
# phonebook["Jill"] = 947662781
# print(phonebook)


phonebook = {"John": 938477566, "Jack": 938377264, "Jill": 947662781}
print(phonebook.items())
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))
