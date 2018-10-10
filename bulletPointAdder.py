#! /usr/bin/env python 3
#bulletPointAdder.py - at the beginning of every verse
#of a text in a clipboard adds stars creating a bullet-point list.

import pyperclip
text = pyperclip.paste()

#Rozdzielenie poszczególnych wierszy i dodanie gwiazdek.
lines = text.split('\n')
for i in range(len(lines)):     #Iteracja przez wszystkie indeksy listy "lines".
    lines[i] = '* ' + lines[i]  #Dodanie gwiazdki do każdego ciągu tekstowego na liście "lines".
    text = '\n'.join(lines)
    
pyperclip.copy(text)
