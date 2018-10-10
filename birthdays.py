birthdays = {'Alice': '1st of April', 'Bob': '12th of December', 'Carl': '4th of March'}

while True:
    print('Type a desired name: (or leave empty to finish a program)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the day of ' + name + 's' + ' birthday' + '.')
    else:
        print('Could not find information about ' + name + 's ' + 'birthday' + '.')
        print('When is his/her birthday?')
        bday = input()
        birthdays[name] = bday
        print('The database has been updated' + '.')
