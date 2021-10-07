highway_number = int(input(''))
if highway_number % 100 == 0:
    print(highway_number, 'is not a valid interstate highway number.')

if highway_number >= 1 and highway_number <= 99:
    prim = 'is primary,'
    if (highway_number % 2) == 0:
        print('I-' + str(highway_number), prim, 'going east/west.')
    else:
        print('I-' + str(highway_number), prim, 'going north/south.')
elif highway_number >= 100 and highway_number <= 999 and highway_number % 100 != 0:
    aux = 'is auxiliary,'
    if (highway_number % 2) == 0:
        print('I-' + str(highway_number), aux, 'serving I-%d, going east/west.' % (highway_number%100))
    else:
        print('I-' + str(highway_number), aux, 'serving I-%d, going north/south.' % (highway_number%100))
