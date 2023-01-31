#Handle Coordinate Information task-1
f = open('average-latitude-longitude-countries.csv', 'r')
f.readline()  # caution !

code_to_name = []
code_to_loc = []

# read in data and make maps
for line in f:
    L = line.split(',')
    code = L[0].strip('"')

    name = ','.join(L[1:-2])
    name = name.strip('"')

    latitude = float(L[-2])
    longitude = float(L[-1])

    code_to_name.append((code, name))
    code_to_loc.append((code, (latitude, longitude)))

print(code_to_name)
print(code_to_loc)



#Handle Coordinate Information task-2
f = open('average-latitude-longitude-countries.csv')
f.readline()  # caution !

for line in f:
    L = line.split(',')
    name = ','.join(L[1:-2])
    name = name.strip('"')

    latitude = float(L[-2])

    if latitude < 0:
        print(name)



#Coordinate Information task-3
f = open('average-latitude-longitude-countries.csv')
f.readline()  # caution !

dict_code2name = {}
for line in f:
    L = line.split(',')
    code = L[0].strip('"')

    name = ','.join(L[1:-2])
    name = name.strip('"')

    dict_code2name[code] = name

user_input = input('Enter a country code : ')
print (dict_code2name[user_input])