import functions as func

def main():
    params = func.read_cards()
    numbers = params["numbers"]
    colors = params["colors"]
    jokers = params["jokers"]
    new_deck = func.create_deck(numbers, colors, jokers)
    deck = func.draw_starting_hand(new_deck)
    print("---Cards left in the deck---")
    print(deck)

    while True:
        print("---What do you want to do?---\n-draw\n-prob\n-newdeck\n-quit---")
        answer = input()
        if answer == "draw":
            cards = func.draw()
            for x in cards:
                deck.remove(x)
            print("---Cards left in the deck:---")
            print(deck)
        elif answer == "prob":
            func.probability(deck)
        elif answer == "quit":
            break
        elif answer == "newdeck":
            deck = func.draw_starting_hand(new_deck)
            print("---Cards left in the deck---")
            print(deck)    

if __name__ == "__main__":
    main()