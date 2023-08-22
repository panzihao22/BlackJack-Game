import random
import os

class BlackJack():
    def __init__(self, name=None, age=None, money=None, deck=None):
        if name is None or age is None or money is None or deck is None:
            self.collect_user_info()
            
        else:
            self.name = name
            self.age = age
            self.money = money
            self.deck = deck
        self.text = "\n\n\nHere is your current status:"+"\nName: "+str(self.name)+"\nAge: "+str(self.age)+ "\nCapital: "+str(self.money)+"\nMode: "+str(self.deck)+" deck"+ "\n\n\nMake yourself confortable, the game will start right away."+"\nGood Luck!"+"\nLoading..."
        self.dealer_beggin = "\n\nWelcome "+str(self.name)+ "! in this table we have 9 \"Normal box\" and in case of the Ace, also a \"Insurance box\""+"\nNow we'll start with "+ str(self.deck) + " deck..."+"\n mixing sound..."+"\n  mixing sound..."+"\n   mixing sound..."
        self.move_text = "[\nHit/Stand/Double/Split/Surrender\n]"
    def collect_user_info(self):
        print("Welcome to my simple and humble game of $£ BlackJack £$"+"\nTo start, please compile our questionnaire")
        self.name= input("What's your name:")
        while True:
            try:
                self.age= int(input("How old are you?"))
                if self.age <18:
                    print("Only for Adults, Go back... or tell me your age again ;)")
                else:
                    break
            except ValueError:
                print("Try again! Your age needs to be a integer number")

        while True:
            try:
                self.money= int(input("How much do you wanna play?: $"))
                break
            except ValueError:
                print("Please insert a integer number")

        while True:
            try:
                self.deck= int(input("With how many deck do you wanna play:" ))
                if self.deck not in [1, 2, 4, 6, 8]:
                    print("You can only choose between 1, 2, 4 , 6, and 8")
                else:
                    break
            except ValueError:
                print("Insert a intenger number")
                
    
        
        
        self.text = "\n\n\nHere is your current status:"+"\nName: "+str(self.name)+"\nAge: "+str(self.age)+ "\nCapital: "+str(self.money)+"\nMode: "+str(self.deck)+" deck"+ "\n\n\nMake yourself confortable, the game will start right away."+"\nGood Luck!"+"\nLoading..."
        self.dealer_beggin = "\n\nWelcome "+str(self.name)+ "! in this table we have 9 \"Normal box\" and in case of the Ace, also a \"Insurance box\""+"\nNow we'll start with "+ str(self.deck) + " deck..."+"\n mixing sound..."+"\n  mixing sound..."+"\n   mixing sound..."
        self.move_text = "[\nHit/Stand/Double/Split/Surrender\n]"

    def __repr__(self):
        return self.text
    
    def choose_box(self):
        print(self.dealer_beggin)
        player_bet = {}
        card_list = {}
        dealer_card = {}
        generaldeck= [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]*4*self.deck
        self.bet_total = 0
        self.side_bet= 0 
        Final_list = {}
        self.moneyss=self.money


        while True:
            try:
                self.box = int(input("Box: "))
                if self.box not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    print("Please choose between one of the 9 box")
                else:
                    break
            except ValueError:
                print("Please insert a integer number")
        while True:
            try:
                self.bet = int(input("Bet: $"))
                if self.bet > self.money:
                    print("You only have "+"$"+str(self.money)+" to play")
                else:
                    self.bet_total += self.bet
                    player_bet[str(self.box)]= self.bet
                    break
            except ValueError:
                print("Please insert a integer number")
        while len(player_bet) < 9 and self.money >0:
            self.question = str(input("Wanna bet another box (Yes/No): ")).lower()
            if self.question == "yes":
                while True: 
                    try:
                        self.box = int(input("Box: "))
                        i = self.box
                        if self.box not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                            print("Please choose between one of the 9 boxes")
                        elif i in player_bet:
                            print("You can't bet on the same box")
                        else:
                            break
                    except ValueError:
                        print("Please insert a integer number")
                while True:
                    try:
                        self.bet = int(input("Bet: $"))
                        if self.bet > self.money:
                            print("You only have "+"$"+str(self.money)+" to play")
                        elif len(player_bet) == 9:
                            print("You bet enough")
                            break
                        else:
                            self.bet_total += self.bet
                            player_bet[self.box]= self.bet
                            break
                    except ValueError:
                        print("Please insert a integer number")
            elif self.question == "no":
                break
            else:
                print("Answer yes or no")
                
            
        for box, value in player_bet.items():
            card_list[box] = list((random.choice(generaldeck), random.choice(generaldeck)))


        print("\nDealing Cards...")

        dealer_card["First_card"] = list((random.choice(generaldeck), random.choice(generaldeck)))
        print("Dealer's First Card: " + str(dealer_card["First_card"][0]))

        print(str(self.name)+"'s Cards:")
        for key, card in card_list.items():
            print("Box n."+str(key) + ": " + str(card))

        if dealer_card["First_card"] == "A":
            while True:
                try:
                    self.moves= str(input("Insurance(Yes/No)")).lower()
                    if self.moves =="yes":
                        side_move= int(input("Bet: "))
                        if side_move > self.bet_total/2:
                            print("You can only gamble up the half of your total bet")
                        elif side_move < 0:
                            print("What the f... Sorry.. Please use a positive number")
                        elif self.bet_total+side_move> self.money:
                            print("You don't have enough money")
                        else:
                            self.side_bet += side_move
                            break
                    elif self.moves== "no":
                        break
                    else:
                        print("Type 'yes' or 'no'")
                except ValueError:
                    print("Type a string")
#Move
        for box, card in card_list.items():
            print("\n"+"It's the Box n."+str(box))
            while True:
                try:
                    self.movess= str(input("Make your move:")).lower()
                    if self.movess not in ["hit", "split", "double", "stand", "surrender"]:
                        print("Please choose between [Hit/Split/Double/Stand/Surrender]")
                    elif self.movess == "hit":
                        card_list[box].append(random.choice(generaldeck))
                        Final_list[box] = card_list[box]
                        break
                    elif self.movess == "stand":
                        Final_list[box] = card_list[box]
                        break
                    elif self.movess == "double":
                        card_list[box].append(random.choice(generaldeck))
                        Final_list[box] = card_list[box]
                        player_bet[box]*= 2
                        print("You are betting $"+str(player_bet[box])+ " now.")
                        break
                    elif self.movess == "split":
                        if card_list[box][0]== card_list[box][1]:
                            bet= int(input("Bet: $"))
                            if bet+ self.bet_total > self.money:
                                print("You have $"+str(self.money)+ " to play")
                            elif bet <= 0:
                                        print("Play a positive number")
                            else: 
                                Final_list["box1"]= card_list[box][0], random.choice(generaldeck)
                                Final_list["box2"]= card_list[box][1], random.choice(generaldeck)
                                player_bet[box].append(bet)
                                break   
                        else:
                            print("You can't play split")
                            break        
                    elif self.movess == "surrender":
                        self.money -=player_bet[box]/2
                        print("You lost $"+str(player_bet[box]/2))

                    else:
                        print("Please choose a valid move")
                except ValueError:
                    print("Type a string")
        

        Player_ace= {}
        dealer_ace= {} 

        valoreJQK= 10
        temporary_value= 0
        print(str(Final_list))
#player
        
        for key, value in Final_list.items():
            updated_value = [valoreJQK if item in ["J","K","Q"] else (11 if item == "A" else item) for item in value]
            Player_ace[key]= sum(updated_value)
            if Player_ace[key]>21 and "A" in value:
                Player_ace[key] -=10


#dealer
        for key, value in dealer_card.items():
            updated_value = [valoreJQK if item in ["J","K","Q"] else (11 if item == "A" else item) for item in value]
            dealer_ace[key]= sum(updated_value)
            if dealer_ace[key]>21 and "A"in value:
                dealer_ace[key] -=10



        print("\nDealing Cards...")

        
        while dealer_ace['First_card'] <17:
            ram= random.choice(generaldeck)
            dealer_card['First_card'].append(ram) 
            if ram in ["J", "K", "Q"]:
                dealer_ace['First_card'] += valoreJQK
            elif ram == "A":
                if dealer_ace['First_card'] + 11 <= 21:
                     dealer_ace['First_card'] += 11
                else:
                    dealer_ace['First_card'] += 1
            else:
                dealer_ace['First_card'] += ram


        print("Dealer's Cards: " + str(dealer_card["First_card"]))
        print(str(self.name)+"'s Cards:")
        for key, card in Final_list.items():
            print("Box n."+str(key) + ": " + str(card))

        print("-------------------------")
        
#Result
        
        for key, value in Player_ace.items():
            if value > 21 and dealer_ace['First_card']<21:
                self.moneyss-=player_bet[key]
                print("Box n."+str(key)+": Bust to the player! "+"You lost $"+str(player_bet[key]))
            elif dealer_ace['First_card']>21 and value>21:
                self.moneyss+=player_bet[key]
                print("Box n."+str(key)+": Bust to the dealer! "+"You win $"+str(player_bet[key]))
            elif value >21 and dealer_ace['First_card']:
                self.moneyss-=player_bet[key]
                print("Box n."+str(key)+": Bust to the player! "+"You lost $"+str(player_bet[key]))

            elif value < 21 and dealer_ace['First_card'] < 21:
                if value > dealer_ace['First_card']:
                    self.moneyss += player_bet[key]
                    print("Box n."+str(key) + ": You win $" + str(player_bet[key]))
                elif value < dealer_ace['First_card']:
                    self.moneyss -= player_bet[key]
                    print("Box n."+str(key) + ": You lost $" + str(player_bet[key]))
                else:
                    print("Box n."+str(key) + ": It's a push! Your bet is returned.")
            elif value==21:
                self.moneyss += player_bet[key]
                print("Box n."+str(key) +": BlackJack!!!" +" You win $"+str(player_bet[key]))
            elif dealer_ace['First_card']==21:
                self.moneyss -= player_bet[key]
                print("Box n."+str(key) +": BlackJack for the dealer! You lost $"+str(player_bet[key]))
            else:
                print("Box n."+str(key) +": It's a push! Your bet is returned.")
            

        if self.moneyss >self.money:
            asd=self.moneyss-self.money
            print("Name: "+str(self.name)+"\nAge: "+str(self.age)+"\nFinal Capital: $"+str(self.moneyss)+"\nYOU GAIN $"+str(asd))
        elif self.moneyss <self.money:
            asd=self.money-self.moneyss
            print("Name: "+str(self.name)+"\nAge: "+str(self.age)+"\nFinal Capital: $"+str(self.moneyss)+"\nYOU LOST $"+str(asd))
        else:
            print("Name: "+str(self.name)+"\nAge: "+str(self.age)+"\nFinal Capital: $"+str(self.moneyss)+"\n$SAME$ = $SAME$")

        print("-------------------------")
        
        self.money = self.moneyss

        with open('player_data.txt', 'w') as file:
            file.write(f"{self.name}\n{self.age}\n{self.money}")

        while True: 
            try:
                Answer = input("Do you wanna continue (Yes/No): ").lower()
                if Answer == "yes":
                    Player1 = BlackJack(self.name, self.age, self.money, self.deck)
                    print(Player1)
                    Player1.choose_box()
                elif Answer == "no":
                    break
                else:
                    print("Please type \"yes\" or \"no\"")
            except ValueError:
                print("Please type \"yes\" or \"no\"")   



#--------------------
Player1 = BlackJack()
print(Player1)
Player1.choose_box()