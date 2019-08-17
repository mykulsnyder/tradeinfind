#!/usr/local/bin/python3

# User inputs to determine the make/carrier/name of the device.
device = str.lower(input('Insert Device')).split()
carrier = str.lower(input('Insert Carrier (t-mobile requires the hyphen)'))
make = str.lower(input('Insert Make (Samsung/Apple/etc)'))

# Initially defines the hyphens/pluses needed for the urls.
deviceHy = ''
deviceP = ''

# Uses a for loop to cycle the name to create the necessary strings for the urls.
for j in device:
    deviceHy = ('%s-%s' %(deviceHy, j)).lstrip('-')
    deviceP = ('%s+%s' %(deviceP, j)).lstrip('+')

# Creates links for Apple devices due to sites using a unique url.
if make == 'apple':
    print('\n')
    print('Usell Link')
    print('https://usell.com/sell/%s/%s/%s' %(device[0],deviceHy,carrier.lstrip()),'\n')

    print('Gazelle Link')
    print('https://gazelle.com/%s/%s/%s' %(device[0],deviceHy,carrier.lstrip()),'\n')

    print('Gamestop Link')
    print('https://gamestop.com/trade/?q=%s+%s&lang=default' %(deviceP,carrier.lstrip()),'\n')

    print('Swappa Link')
    print('https://swappa.com/mobile/buy/%s-%s/%s' %(make.lstrip(),deviceHy,carrier.lstrip()),'\n')

# Android makes use the same urls.
elif make is not 'apple':
     print('\n')
     print('Usell Link')
     print('https://usell.com/sell/cell-phone/%s/%s' %(make.lstrip(),carrier.lstrip()),'\n')

     print('Gazelle Link')
     print('https://gazelle.com/sell/cell-phone/%s/%s' %(make.lstrip(),carrier.lstrip()),'\n')

     print('Gamestop Link')
     print('https://gamestop.com/trade/?q=%s+%s+%s&lang=default' %(make.lstrip(),deviceP,carrier.lstrip()),'\n')

     print('Swappa Link')
     print('https://swappa.com/mobile/buy/%s-%s/%s' %(make.lstrip(),deviceHy,carrier.lstrip()),'\n')
