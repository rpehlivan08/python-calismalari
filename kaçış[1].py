Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # \, \n, \t
>>> print('Python\'ın Gücü')
Python'ın Gücü
>>> # \n
>>> print(Merhaba \n Dünya)
SyntaxError: unexpected character after line continuation character
>>> print("Merhaba \n Dünya")
Merhaba 
 Dünya
>>> print("Merhaba \nDünya")
Merhaba 
Dünya
>>> #\t
>>> print("Merhaba \t Dünya")
Merhaba 	 Dünya
>>> print("Merhaba \tDünya")
Merhaba 	Dünya
>>> print("\n alt satıra geçmek için kullanılır.")

 alt satıra geçmek için kullanılır.
>>> print("\\n alt satıra geçmek için kullanılır.")
\n alt satıra geçmek için kullanılır.
>>> 
