"""
Context:
This project is a generator and assignment assistant for
Player Character (PC) starting statistics in the Warhammer
40k tabletop RPG system, Deathwatch. In this game, players
take the role of Space Marines in the Warhammer 40k setting.

Part of intial PC generation includes rolling and assigning
those values to various Characteristics. The Characteristics
represent a PC's raw ability in different areas (e.g. Ballistic
Skill indicating how good a marksman they are).

Higher values in a Characteristic are better; to succeed at
tests, players use the associated Characteristic. The
Characteristics are generally best thought of as percentiles
of success. I.e. a PC with a Ballistic Skill of 50 generally
has a 50% chance of hitting something they are shooting at,
a 30 indicating 30%, 70 == 70%, etc., which can be modified
further in-game after Character Generation.

While this generator is not a complete PC builder for this
game, it can be further escalated later for further functions
in later iterations.
"""

#program is to use random library to roll values
import random

#BASELINE constant indicates basic Characteristic value of
#all Deathwatch Player Characters, to which rolled values
#are added. *RANDOM constants are for dice rolls.
BASELINE = 30
MIN_RANDOM = 2
MAX_RANDOM = 20

def main():
    print('Welcome to Player Character generation for the Warhammer 40k RPG, Deathwatch.')
    print('This program will roll 2d20 nine times for you and present your rolls!')

    #asks user how many complete sets of 9x2d10 rolls to make (1-3), and assigns them to Lists or Dictionary
    #Set starting value for how many rolls to make, and includes the Dictionary constant counter that each List will go in
    user_rolls = 0

    print('First, we will roll a set of nine 2d10 for one set of Characteristic rolls.')
    print('How many complete sets of Characteristic rolls would you like? Input a whole number, 1-3.')
    user_rolls = int(input(""))

    #Demand new input for values not 1-3.
    while (user_rolls < 1) or (user_rolls > 3):
        print("Please enter a whole number, 1-3: ")
        user_rolls = int(input(""))

    #Roll sets of Characteristic values per user input, the associated sum, then store the values (w/o sum) to Dictonary
    if user_rolls == 1: #If-statement for just one roll set.
        list_rolls = []
        for i in range(9): #rolls nine values for nine Characteristics
            rollsum = 0
            roll = random.randint(MIN_RANDOM, MAX_RANDOM)
            list_rolls.append(roll)
            rollsum = sum(list_rolls)
        print('Total value for roll sequence (below): ' + str(int(rollsum)))
        print('We will use these for your roll set: ', list_rolls)

    if user_rolls > 1: #If-statement for more than one roll set.
        starterrolls = {}
        listnum = 0
        for i in range(user_rolls):
            listnum += 1
            list_rolls = []
            for i in range(9):
                rollsum = 0
                roll = random.randint(MIN_RANDOM, MAX_RANDOM)
                list_rolls.append(roll)
                rollsum = sum(list_rolls)
            print(list_rolls)
            print('Total value for roll sequence ' + str(listnum) + ': ' + str(int(rollsum)))
            starterrolls[listnum] = list_rolls

        #Select which List in the Dictionary of roll sets to use.
        print('Which set would you like to keep?')
        dictkey = int(input('Enter a whole number for the list you would like: '))
        list_rolls = starterrolls.pop(dictkey)
        print('We will use these for your roll set: ', list_rolls)

    #Tell user code for Characteristics
    print('')
    print('Each Characteristic has a specific abbreviation we will use to reference it here: ')
    print('Weapon Skill = WS, Ballistic Skill = BS, Strength = S, Toughness = T, Agility = AG')
    print('Intelligence = INT, Perception = PER, Willpower = WP, Fellowship = FP')
    print('Your rolls: ', list_rolls)
    print('')

    print('You can assign your values one by one. Baseline Space Marine stats are: ')
    #I admit I haven't thought out a way to prevent double-assignment of values to one Characteristic yet
        #as well as QoL changes for key:value assignement.
    characteristics = {'WS':30, 'BS':30, 'S':30, 'T':30, 'AG':30, 'INT':30, 'PER':30, 'WP':30, 'FEL':30}
    print(characteristics)

    for i in range(len(list_rolls)): #Assigns rolled values one by one to a Characteristic/key in a Dictionary
        print('Choose a Characteristic to assign to. Those with a value of 30 are still unassigned!')
        charakey = str(input('Remember to use the case-dependent Characteristic abbreviation without apostrophes (e.g, just WS): '))
        charavalue = int(input('Which value from your roll set would you like to assign it? '))
        characteristics[charakey] += charavalue
        list_rolls.remove(charavalue)
        print('')
        print('Current Characteristics: ', characteristics)
        print('Remaining values: ', list_rolls)

    #Closing report and remarks.
    print('')
    print('Your final stats for chargen are: ', characteristics)
    print('Thank you for using this PC generation assistant! Go forth for the Imperium, noble Astartes!')

if __name__ == '__main__':
    main()