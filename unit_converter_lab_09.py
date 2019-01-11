#unit_converter_lab_09.py
while True:
    #Line 4 is a dictionary of of other common units of measurement. Each is how many meters go into each unit.
    convert_to_meters = {"feet in meter": 3.2804, "ft": .3048, "mi": 1609.34, "m": 1, "km": 1000, "yd": .9144, "in": .0254, "cm": .01, "mm": .001}
    while True:
        try:
            input_number = float(int(input("Let's do some unit of measurement conversions. Please enter the number of units you wish to convert. > ")))
            break
        except ValueError:
            print("Please enter a number.")
    input_unit = input("What unit of measurement do you wish to convert? > ")
    output_unit = input("What unit of measurement do you wish to convert to? > ")
    #Line 9 is taking the users number of units and multiplying it by the users' inputted (chosen) unit of measurement. This gives the unit equivalent in meters. Note that convert_to_meters[input_unit] is calling the desired unit from the dictionary in line 4.
    meters = (float(input_number * convert_to_meters[input_unit]))
    #Line 11 then divides meters by the users' inputted (chosen) output unit of measurement. This gives the equivalent in chosen output units.
    output_number = (float(meters / convert_to_meters[output_unit]))
    print(f"Your {input_number} {input_unit} is equal to {output_number} {output_unit}.")
    exit = input("Would you like to do more conversions? > ")
    if exit != 'yes':
        break
