from converter import convert_length, convert_weight, convert_temperature, convert_currency

while True:
    print("Choose the unit conversion type:")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")
    print("4. Currency")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        value = float(input("Enter the value: "))
        from_unit = input("Enter the source unit (m, km, cm, mm): ")
        to_unit = input("Enter the target unit: ")
        result = convert_length(value, from_unit, to_unit)
        print(f"Result: {value} {from_unit} = {result} {to_unit}")

    elif choice == '2':
        value = float(input("Enter the value: "))
        from_unit = input("Enter the source unit (g, kg, ton): ")
        to_unit = input("Enter the target unit: ")
        result = convert_weight(value, from_unit, to_unit)
        print(f"Result: {value} {from_unit} = {result} {to_unit}")

    elif choice == '3':
        value = float(input("Enter the value: "))
        from_unit = input("Enter the source unit (C, F, K): ")
        to_unit = input("Enter the target unit: ")
        result = convert_temperature(value, from_unit, to_unit)
        print(f"Result: {value} {from_unit} = {result} {to_unit}")

    elif choice == '4':
        value = float(input("Enter the value: "))
        from_unit = input("Enter the source unit (USD): ")
        to_unit = input("Enter the target unit (VND): ")
        result = convert_currency(value, from_unit, to_unit)
        print(f"Result: {value} {from_unit} = {result} {to_unit}")

    elif choice == '0':
        print("Exiting the program...")
        break
    else:
        print("Invalid choice, please try again.")
