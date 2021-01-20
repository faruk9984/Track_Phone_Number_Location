#Python Project | Track Phone Number Location Using Python

import phonenumbers
from project44test import number
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

ch_number=phonenumbers.parse(number,'CH')
c_name=geocoder.description_for_number(ch_number,'en')
print('Country Name: ',c_name)

t_zone=phonenumbers.parse(number)
time_zone=timezone.time_zones_for_number(t_zone)
print('Time Zone: ',time_zone)

service_number=phonenumbers.parse(number,'R0')
s_name = carrier.name_for_number(service_number,'en')
print('Service Name: ',s_name)




