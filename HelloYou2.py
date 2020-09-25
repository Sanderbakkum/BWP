import datetime

x = datetime.datetime.now()

# Introductie
print("Hello You!, Ik ben Sander")
print("Wie ben jij?")
naam = input()
print("Hello" " " + naam)

# Datum
print("Datum en Tijd is:")
print(x)

# Klaar of Resetten
print(naam + " wil jij dit progamma nog een keer doen? Type dan Y/N")
print("Y is het herstarten van het progamma")
print("N is het eindigen van het progamma")
Message=input()
if Message=="N":
	print("Dankjewel voor het invullen" " " + naam + "!")
if Message=="Y":
	print("TYPE: \033[1;32;40m Python3 HelloYou2.py \n")
