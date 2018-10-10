#! /usr/bin/env python3 -0
#pw.py - Unsafe password manager

PASSWORDS = {'email': 'F7min1BDDuvKDLc934mdDFg76dD',
             'blog': 'Vmlfllas8589pamflDGsmwvkd960',
             'luggage': '12345'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Użycie: python pw.py [konto] - skopiowanie hasła wskazanego konta')
    sys.exit()

account = sys.argv[1]  #pierwszym argumentem wiersza poleceń jest nazwa konta.

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Hasło do konta ' + account + ' zostało skopiowane do schowka.')
else:
    print('Nie istnieje konto o nazwie ' + account + '.')
