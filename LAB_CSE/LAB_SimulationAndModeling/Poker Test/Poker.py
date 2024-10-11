import csv

def readValues():
    with open("numbers.csv", 'r') as csvfile:
        file = csv.reader(csvfile)
        returned = []

        for number_line in file:
            for number in number_line:
                if (len(number)<5): #Used to weed out "non-poker hands"
                    #print(number)
                    continue
                returned.append(list(number))
    return returned

def evaluateHand(values):
    returned=[]
    for numbers in values:
        dictionary = {}
        for number in numbers:
            if (number in dictionary):
                dictionary[number]= int(dictionary[number]) +1
            else:
                dictionary.update({number:0})

        returned.append(something(dictionary))
    return returned

def something(dictionary):
    if (len(dictionary)== 5):
        return "Five different."
    elif (len(dictionary)== 4):
        return "Exactly one pair."
    elif (len(dictionary)== 3):
        if (3 in dictionary.values()):
            return "Exactly three of a kind."
        else:
            return "Exactly two pairs."
    elif (len(dictionary)==2):
        if (4 in dictionary.values()):
            return "Four of a kind."
        else:
            return "Three of a kind plus one pair."
    else:
        #The dictionary only contains one mapping
        return "Five of a kind."

def print_stats(stats_for_hands):
    five_different = list(filter(lambda x: x == "Five different.", stats_for_hands))
    one_pair = list(filter(lambda x: x == "Exactly one pair.", stats_for_hands))
    three_of_a_kind = list(filter(lambda x: x == "Exactly three of a kind.", stats_for_hands))
    two_pair = list(filter(lambda x: x == "Exactly two pairs.", stats_for_hands))
    four_of_a_kind = list(filter(lambda x: x == "Four of a kind.", stats_for_hands))
    three_of_a_kind_and_pair = list(filter(lambda x: x == "Three of a kind plus one pair.", stats_for_hands))
    five_of_a_kind = list(filter(lambda x: x == "Five of a kind.", stats_for_hands))

    print("We have "+str(len(five_different))+" numbers where you have five different values.")
    print("We have "+str(len(one_pair)) + " numbers where you have exactly one pair.")
    print("We have " + str(len(two_pair)) + " numbers where you have exactly two pair.")
    print("We have " + str(len(three_of_a_kind)) + " numbers where you have exactly three of a kind.")
    print("We have " + str(len(three_of_a_kind_and_pair)) + " numbers where you have exactly three of a kind and a pair.")
    print("We have " + str(len(four_of_a_kind)) + " numbers where you have exactly four of a kind.")
    print("We have " + str(len(five_of_a_kind)) + " numbers where you have exactly five of a kind.")





if __name__ == "__main__":
    values=readValues()
    stats_for_hands=evaluateHand(values)
    print_stats(stats_for_hands)