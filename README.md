# phonmail-extractor
an emails/phones extractor python library with GUI( extract your emails and phones from any file)
you can use phonmail as a python library or a desktop app or an online website.

## phonmail-online 
you can use phonmail extractor as an online service here **www.phonmail.net** but unlike the desktop version it can't handle larger files

## phonmail-desktop
the desktop version is built over the phonmail.py library with tkinter

![Screenshot (8)](https://user-images.githubusercontent.com/60823745/132062604-1327ba51-2db8-4b72-9348-f43ec71e3980.png)

## phonmail-library
one single independent file you can import it into your project

#### Usage
check the demo.py and follow the steps below

###### importing 

```python
from phonmail import extractor # import the main class (extractor)
```

###### extraction 
there is two main methods in the extarctor opject "emails" and "phones"

```python
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
```
