Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> metin = "{} ve {} iyi bir ikilidir"
metin.format("Python", "Django")
SyntaxError: multiple statements found while compiling a single statement
>>> metin.format("Python", "Django")
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    metin.format("Python", "Django")
NameError: name 'metin' is not defined
>>> metin = "{} ve {} iyi bir ikilidir"
>>> metin.format("Python", "Django")
'Python ve Django iyi bir ikilidir'
>>> tarih = input("tarih: ")
üniversite = input("üniversite adı: ")
fakülte = input("fakülte adı: ")
bölüm = input("bölüm adı: ")
öğrenci_no = input("öğrenci no. :")
öğretim_yılı = input("öğretim yılı: ")
yarıyıl = input("yarıyıl: ")
ad = input("öğrencinin adı: ")
soyad = input("öğrencinin soyadı: ")
tc_kimlik_no = input("TC Kimlik no. :")
adres = input("adres: ")
tel = input("telefon: ")
ekler = input("ekler: ")
print(dilekçe.format(tarih, üniversite, fakülte, bölüm,
öğrenci_no, öğretim_yılı, yarıyıl,
ad, soyad, tc_kimlik_no,
adres, tel, ekler))
SyntaxError: multiple statements found while compiling a single statement
>>> 30%4
2
>>> int(5/2)
2
>>> round(3,75)
3
>>> 25**2
625
>>> 625**0.5
25.0
>>> pow(25,3)
15625
>>> 
