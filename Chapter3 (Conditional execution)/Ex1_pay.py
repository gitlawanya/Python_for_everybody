hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

if hours > 40:
    overtime = (hours - 40)
    pay = (40*rate) + (1.5*overtime*rate)
else:
    pay = hours*rate

print(f"Pay: {pay}")
