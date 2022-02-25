import random 
import time
J = 11
D = 12
K = 13
A = 14
karty = [2,3,4,5,6,7,8,9,10,J,D,K,A]
punkty = []
def Losowanie():
    pytanieMain = str(input("Start?"))
    while pytanieMain == "Tak" or pytanieMain == "tak":
            for x in range(2):
                losowanie = random.choice(karty)
                print(losowanie) 
                punkty.append(losowanie)
                sumapkt = sum(punkty)
            time.sleep(1)
            if sumapkt >= 21:
                print("Przegrales!")
                break
         
            pytanie1 = str(input("Dalej?"))
            if pytanie1 == "Tak" or pytanie1 == "tak":
                continue
            else:
                print(f"Twoja ilosc kart: {sumapkt}")
                break



    
    















Losowanie()