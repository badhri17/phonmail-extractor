from phonmail import extractor # import the main class (extractor)

text = """ random data with phones and emails 
 rcn14@optonline.net  Resources, Rolland Miranda blablalbla 814-825-6659 nsdsjnoee lorem  ipsm bedroo_17@yahoo.com
 example@gmail.com apple orange bananaannanananaa 9660501023226 0567886300 kkemjnjn jrgjrgn erfef 
 rmiranda90@verizon.net  Manager, Ned Davenport, 868-537-8850, ndavenport8@gmail.com  Medic
 al, Alden Kirby, 574-528-9602, akirby82@comcast.net  Comput er, Antione Harvey, 732-995-8604, aharvey7@aol.com  Operating, Bret
Bruce, 513-704-8737, bbruce99@me.com  Lead, Nathanael Marsh, hihihihih 689-6810, nmarsh@aol.com  Artificial, Odis Nunez, 201-626-6879dfddsfs, onunez@sbcglobal.net  Film, Manual Brennan, 510-505-3719sdsdsdsds, mbrennan@live.c
 """

ex = extractor(text) # extractor opject , pass the data (text) inside it

print("---------------------------------------emails------------------------------------")
print(ex.emails()) # this method for emails

print("---------------------------------------phones------------------------------------")
print(ex.phones())

# print("---------------------------------------specific emails------------------------------------")
# print(ex.emails(provider="gmail")) # if you want specific provider like Gmail

# print("---------------------------------------specific phones------------------------------------")
# print(ex.phones(country_code="966")) # if you want specific country

print(ex.phone_counter(country_code="966"))
