def is_pesel(pesel):
    return len(pesel)==11 and pesel.isnumeric()

pesel = input("pesel: \n")
if is_pesel(pesel) :
    print("Pesel zgodny")
else:
    print("To nie jest prawidłowy pesel")