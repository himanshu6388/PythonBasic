print("Welcome ! Book Your ticket Now.")
print("Check Ticket Price.")
day = str(input("Enter Day: "))
age = int(input("Enter your age: "))


price = 12 if age >= 18 else 8

if day == "Wednesday" or "wednesday":
    price = price -2

print("Ticket price for you is $:",price)