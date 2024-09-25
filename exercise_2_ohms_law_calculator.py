calculate = str(input("What do you want to calculate: Voltage, Current, or Resistance? ")).lower()

if calculate == "voltage":
    current = float(input("Enter the value of Current (in amperes): "))
    resistance = float(input("Enter the value of Resistance (in ohms): "))
    total_voltage = current * resistance
    print(f"The Voltage is {total_voltage} volts")

elif calculate == "current":
    voltage = float(input("Enter the value of Volatage (in volts): "))
    resistance = float(input("Enter the value of Resistance (in ohms): "))

