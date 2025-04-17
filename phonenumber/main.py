import phonenumbers
from phn import number
from phonenumbers import geocoder
pepnumber = phonenumbers.parse(number)
location = geocoder.discription_for_number(pepnumber,"en")
print(location)
