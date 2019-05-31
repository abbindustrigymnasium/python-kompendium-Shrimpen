#importerar funktioner
import requests
import json
from random import randint
import random

#Api för lätta frågor
urlLätt = 'https://opentdb.com/api.php?amount=50&difficulty=easy&type=boolean'
rLätt = requests.get ( urlLätt )
response_dictionaryLätt = rLätt.json() #gör om det till ett json object 

#Api för medel frågor
urlMedel = 'https://opentdb.com/api.php?amount=50&difficulty=medium&type=boolean'
rMedel = requests.get (urlMedel)
response_dictionaryMedel = rMedel.json() #gör om det till ett json object

#Api för svåra frågor
urlSvår = 'https://opentdb.com/api.php?amount=50&difficulty=hard&type=boolean'
rSvår = requests.get (urlSvår)
response_dictionarySvår = rSvår.json() #gör om det till ett json object

poäng= 0 #poäng varibeln
spelade_gånger = 0 #antal spelade gånger varibeln

#Intro till spelet
print("Välkommen till spelet sant eller falsk!\n\nSpelets regler är väldigt lätta och \ndet ända du behöver göra är att välja \nsvårighetsgrad och sen svara sant eller faskt!\n")

nivå = input("Vilken av nivåerna lätt,medel och svår vill du välja?\n") #input för vilken nivå
nivå = nivå.lower()#gör om alla bokstäver i nivå till små

#print (json.dumps(response_dictionaryLätt,indent=4)) Underlättar att se vad som finns i dictunari
print(nivå)

if nivå == "lätt": #om man valde nivå lätt
    print("\n\n\n\nDu valde nivå lätt:") #skriver nivån du valde
    while spelade_gånger < 10: #antal gånger du får spela
        slumpad = randint(0,49) #tar ett random nummer för att välja fråga
        topicLätt = response_dictionaryLätt["results"][slumpad]["category"] #tar categorin som randit valde
        frågaLätt = response_dictionaryLätt["results"][slumpad]["question"] #tar questionen som randit valde

        frågaLätt = frågaLätt.replace('&#039','') #ersätter vissa tecken i frågorna
        frågaLätt = frågaLätt.replace('&quot;','')
        frågaLätt = frågaLätt.replace(': ',' ')
        frågaLätt = frågaLätt.replace(':',' ')
        frågaLätt = frågaLätt.replace('&eacute;','e')
        frågaLätt = frågaLätt.replace(';','"')


        print(topicLätt) #skriver ut topic variablen
        print(frågaLätt) #skriver ut frågan 
        svar = input("Is it true or false? \nDitt svar:") #ber om svar
        svar = svar.title() #gör om svaret till title

        if svar == response_dictionaryLätt["results"][slumpad]["correct_answer"]: #om svaret är samma som i dictionaryt 
            print("Du svarade rätt") #skriver rätt
            poäng += 1 #ger poäng
            spelade_gånger +=1 #plusar antalet gånger spelade
            print("Du har nu ",poäng," poäng\n----------------------------------------------") #skriver nuvarande poäng
        else:
            print("Du svarade fel") #om fel svar 
            spelade_gånger +=1 #plusar antalet gånger spelade
            print("Du har nu ",poäng," poäng\n----------------------------------------------") #skriver nuvarande poäng
  
if nivå == "medel":  #om nivån är medel
    print("\n\n\n\nDu valde nivå medel:")
    while spelade_gånger < 10: #hur många gånger man får spela
        slumpad = randint(0,49) #slumpar
        topicMedel = response_dictionaryMedel["results"][slumpad]["category"]#tar categorin som randit valde
        frågaMedel = response_dictionaryMedel["results"][slumpad]["question"]#tar questionen som randit valde

        frågaMedel = frågaMedel.replace('&#039','') #ersätter vissa saker i frågorna
        frågaMedel = frågaMedel.replace('&quot;','')
        frågaMedel = frågaMedel.replace(': ',' ')
        frågaMedel = frågaMedel.replace(':',' ')
        frågaMedel = frågaMedel.replace('&eacute;','e')
        frågaMedel = frågaMedel.replace(';','"')


        print(topicMedel) #skriver topicen 
        print(frågaMedel) #skriver frågan
        svar = input("Is it true or false? \nDitt svar:") #ber om svar
        svar = svar.title() #gör om svaret till title

        if svar == response_dictionaryMedel["results"][slumpad]["correct_answer"]: #om svar = dictionary händer denna satsen
            print("Du svarade rätt") #skriver rätt svar
            poäng += 1 #ger poäng
            spelade_gånger +=1 #lägger till 1 på spelade gånger
            print("Du har nu ",poäng," poäng\n----------------------------------------------") #visar poäng
        else:
            print("Du svarade fel") #skriver att du hade fel
            spelade_gånger +=1 #lägger till 1 på spelade gånger 
            print("Du har nu ",poäng," poäng\n----------------------------------------------") #visar poäng

if nivå == "svår": #om du valde svår
    print("\n\n\n\nDu valde nivå svår:") #skriver nivån
    while spelade_gånger < 10: #antal gånger du får spela
        slumpad = randint(0,49) #slumpar nummer
        topicSvår = response_dictionarySvår["results"][slumpad]["category"] #tar categorin som randit valde
        frågaSvår = response_dictionarySvår["results"][slumpad]["question"] #tar question som randit valde

        frågaSvår = frågaSvår.replace('&#039','') #ersätter ord
        frågaSvår = frågaSvår.replace('&quot;','')
        frågaSvår = frågaSvår.replace(': ',' ')
        frågaSvår = frågaSvår.replace(':',' ')
        frågaSvår = frågaSvår.replace('&eacute;','e')
        frågaSvår = frågaSvår.replace(';','"')


        print(topicSvår) #skriver topic
        print(frågaSvår) #skriver frågan
        svar = input("Is it true or false? \nDitt svar:") #ber om svar
        svar = svar.title() #gör om svaret till title

        if svar == response_dictionarySvår["results"][slumpad]["correct_answer"]: #kollar om svaret är rätt
            print("Du svarade rätt") #skriver rätt
            poäng += 1 #ger poäng
            spelade_gånger +=1 #lägger till 1 på spelade gånger
            print("Du har nu ",poäng," poäng\n----------------------------------------------") #skriver poäng
        else:
            print("Du svarade fel") #skriver du hade fel
            spelade_gånger +=1   #lägger till 1 på spelade gånger
            print("Du har nu ",poäng," poäng\n----------------------------------------------") #skriver poäng

#skriver avslutning och poäng
print("Din totala poäng var",poäng,"\n----------------------------------------------\nTack för att du spelade\n----------------------------------------------")
