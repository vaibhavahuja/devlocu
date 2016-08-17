import urllib.request
import json

api_key = '62ed5ca809b4039f48356800ed840d79920169c7'
pin = str(input('enter the pin where you need to find restaurants  '))
if len(pin) != 6:
    print('enter again')
    pin = str(input('enter the pin where you need to find restaurants  '))

web = 'https://api.locu.com/v1_0/venue/search/?country=INDIA&postal_code='+pin+'&api_key=62ed5ca809b4039f48356800ed840d79920169c7'

my_web = urllib.request.urlopen(web).read().decode('utf8')

data = json.loads(my_web)

for i in data['objects']:
    print(i['name'], end='  ')
    print(i['phone'])



