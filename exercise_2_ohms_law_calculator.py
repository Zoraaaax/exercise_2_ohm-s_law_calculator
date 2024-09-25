calculate = str(input("What do you want to calculate: Voltage, Current, or Resistance? ")).lower()

if calculate == "voltage":
    current = float(input("Enter the value of Current (in amperes): "))
    resistance = float(input("Enter the value of Resistance (in ohms): "))
    total_voltage = current * resistance
    print(f"The Voltage is {total_voltage} volts")

elif calculate == "current":
    voltage = float(input("Enter the value of Volatage (in volts): "))
    resistance = float(input("Enter the value of Resistance (in ohms): "))

    if resistance == 0:
        print(f"Invalid input! Resistance cannot be zero. Please try again")
    else:
        total_current = voltage / resistance
        print(f"The Current is {total_current} amperes")

elif calculate == "resistance":
    voltage = float(input("Enter the value of Voltage (in volts): "))
    current = float(input("Enter the value of Current (in amperes): "))

    if current == 0:
        print(f"Invalid input! Current cannot be zero. Please try again")
    else:
        total_resistance = voltage / current
        print(f"The Current is {total_resistance} ohms")

else:
    print("Invalid input! Please choose to calculate either Voltage, Current, or Resistance.")
    