import json
import math
import prob_flips as pf

def read_cards(filename="cards.json"):
    with open(filename, "r") as file:
        return json.load(file)

def create_deck(numbers, colors, jokers):
    deck = []
    for number in numbers:
        for color in colors:
            card = f"{number}{color}"
            deck.append(card)
    deck.extend(jokers)
    return deck

def draw_starting_hand(deck):
    print("---What is the size of you hand?---")
    number_handcards= int(input())
    hand_cards = []
    print("Please write the cards you drew \nExample of the writing: 1rams, 3crows, 5masks, 13tomes,0BJ, 14RJ\n confirm the card by pressing enter")
    for i in range(0, number_handcards):
        card = input()
        hand_cards.append(card)
    new_deck = deck.copy()
    for element in hand_cards:
        new_deck.remove(element)
    return new_deck
    
def draw():
    cards = []
    print("---Please write down the number of cards you want to get rid from the deck---")
    n = int(input())
    print("---Please write down the cards---")
    for i in range(0, n):
        card = input()
        cards.append(card)
    return cards

def combination_factorial(n,k,bj_A,weak_A,mod_A,sev_A, rj_A):
    omega = math.comb(n,k)
    P_bj = bj_A / omega
    P_weak = weak_A / omega
    P_mod = mod_A / omega
    P_sev = sev_A / omega
    P_rj = rj_A / omega
    return P_bj, P_weak, P_mod, P_sev, P_rj

def probability(deck):
    deck_prob = deck.copy()
    weak = []
    moderate = []
    severe = []

    for element in deck_prob:
        element = int(''.join(filter(str.isdigit, element)))
        if element <6:
            weak.append(element)
        elif element >10:
            severe.append(element)
        else: moderate.append(element)

    while True:
        print("\n---Chances of what kind of flip do you want to check? \n-triple neg -double neg - single neg -straight -single pos -double pos -triple pos -menu---")
        answer = input()
        if answer == "triple neg":
            bj_A, weak_A, moderate_A, severe_A, rj_A = pf.triple_neg(weak, moderate, severe,deck_prob)
            p_bj, p_weak, p_mod, p_sev, p_rj = combination_factorial(len(deck_prob),4 , bj_A, weak_A, moderate_A, severe_A, rj_A)

            print("Black Joker: " + str(round(p_bj,4)))
            print("Weak: " + str(round(p_weak,4)))
            print("Moderate: " + str(round(p_mod,4)))
            print("Severe: " + str(round(p_sev,4)))
            print("Red Joker: " + str(round(p_rj,4)))

        elif answer=="double neg":
            bj_A, weak_A, moderate_A, severe_A, rj_A = pf.double_neg(weak, moderate, severe,deck_prob)
            p_bj, p_weak, p_mod, p_sev, p_rj = combination_factorial(len(deck_prob),3 , bj_A, weak_A, moderate_A, severe_A, rj_A)

            print("Black Joker: " + str(round(p_bj,4)))
            print("Weak: " + str(round(p_weak,4)))
            print("Moderate: " + str(round(p_mod,4)))
            print("Severe: " + str(round(p_sev,4)))
            print("Red Joker: " + str(round(p_rj,4)))

        elif answer=="single neg":
            bj_A, weak_A, moderate_A, severe_A, rj_A = pf.single_neg(weak, moderate, severe,deck_prob)
            p_bj, p_weak, p_mod, p_sev, p_rj = combination_factorial(len(deck_prob),2 , bj_A, weak_A, moderate_A, severe_A, rj_A)

            print("Black Joker: " + str(round(p_bj,4)))
            print("Weak: " + str(round(p_weak,4)))
            print("Moderate: " + str(round(p_mod,4)))
            print("Severe: " + str(round(p_sev,4)))
            print("Red Joker: " + str(round(p_rj,4)))

        elif answer=="straight":
            if 0 in weak:
                print("Black Joker: " + str(round(1/len(deck_prob),4)))
                print("Weak: " + str((round((len(weak)-1)/len(deck_prob),4))))
            else:
                print("Black Joker: 0" )
                print("Weak: " + str((round((len(weak))/len(deck_prob),4))))
            print("Moderate: " + str(round(len(moderate)/len(deck_prob),4)))
            if 14 in severe:
                print("Severe: " + str((round((len(severe)-1)/len(deck_prob),4))))
                print("Red Joker: " + str(round(1/len(deck_prob),4)))
            else:
                print("Severe: " + str((round((len(severe))/len(deck_prob),4))))
                print("Red Joker: 0" )
                
        elif answer=="single pos":
            bj_A, weak_A, moderate_A, severe_A, rj_A = pf.single_pos(weak, moderate, severe,deck_prob)
            p_bj, p_weak, p_mod, p_sev, p_rj = combination_factorial(len(deck_prob),2 , bj_A, weak_A, moderate_A, severe_A, rj_A)

            print("Black Joker: " + str(round(p_bj,4)))
            print("Weak: " + str(round(p_weak,4)))
            print("Moderate: " + str(round(p_mod,4)))
            print("Severe: " + str(round(p_sev,4)))
            print("Red Joker: " + str(round(p_rj,4)))

        elif answer=="double pos":
            bj_A, weak_A, moderate_A, severe_A, rj_A = pf.double_pos(weak, moderate, severe,deck_prob)
            p_bj, p_weak, p_mod, p_sev, p_rj = combination_factorial(len(deck_prob),3 , bj_A, weak_A, moderate_A, severe_A, rj_A)

            print("Black Joker: " + str(round(p_bj,4)))
            print("Weak: " + str(round(p_weak,4)))
            print("Moderate: " + str(round(p_mod,4)))
            print("Severe: " + str(round(p_sev,4)))
            print("Red Joker: " + str(round(p_rj,4)))

        elif answer=="triple pos":
            bj_A, weak_A, moderate_A, severe_A, rj_A = pf.triple_pos(weak, moderate, severe,deck_prob)
            p_bj, p_weak, p_mod, p_sev, p_rj = combination_factorial(len(deck_prob),4 , bj_A, weak_A, moderate_A, severe_A, rj_A)

            print("Black Joker: " + str(round(p_bj,4)))
            print("Weak: " + str(round(p_weak,4)))
            print("Moderate: " + str(round(p_mod,4)))
            print("Severe: " + str(round(p_sev,4)))
            print("Red Joker: " + str(round(p_rj,4)))
    
        elif answer=="menu":
            break