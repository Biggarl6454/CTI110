 # A brief description of the project
    # 9/30/2021
    # CTI-110 P2HW1 - Miles Per Gallon
    # Logan Biggar
    #

miles_driven = float(input('Enter miles driven: '))
gallons_used = float(input('Enter gallons used: '))
gallon_cost = float(input('Enter cost per gallon: '))
print()
miles_gallon = miles_driven / gallons_used
print('Miles per gallon:', format(miles_gallon, ",.2f"))
total_cost = gallons_used * gallon_cost
print('Total Gas Cost:', '$', format(total_cost, ",.2f"))
cost_mile = gallon_cost / miles_gallon
print('Cost Per Mile:', '$', format(cost_mile, ",.1f"))
