#this module file holds the main functions for the outfit program

import random #random module for randomizing clothing selections
import os #module for automatically clearing the terminal
import time #for adding a pause before loading certain output to terminal
import pickle #for reading and writing worn outfits and favorites
from outfitdictionary import spring #dictionaries from the outfitdictionary file
from outfitdictionary import summer
from outfitdictionary import winter
from outfitdictionary import fall

#line 14 creates an empty list for the pickle file to save outfit combos to.
#This list is then looped through later to avoid duplication
# outfitdata = []
#line 15 creates and empty list for the pickle to save worn outfit combos to
pastoutfitsdata = []
currentoutfitdata = []
favoutfitdata = []#empty list for saving favorited outfits

# clothing_selection function takes in as arguments, the season and occasion
# selection from the user with raw_input calls in the main loop
# (randomized_outfit). It also takes in the appropriate occasion
# selections for shoes, tops, and bottoms, based on the occasion selected by
# the user in the main loop below.
def clothing_selection(season, occasion, shoeitem, topitem, bottomitem):
#ifs below convert the argument from season selection prompt (1-4) to an alias
#(season2).
    if season == "1":
        s2 = winter
    elif season == "2":
        s2 = spring
    elif season == "3":
        s2 = summer
    elif season == "4":
        s2 = fall
#The season2 alias from above is used below to point to the appropriate seasonal
#dictionary (winter, spring, summer, or fall), and then index that dict. to
#return a combo of randomly selected shoes, top, and bottom.
    shoe_selection = s2[shoeitem][random.randint(0, len(s2[shoeitem]) - 1)] #gets random shoe selection
    top_selection = s2[topitem][random.randint(0, len(s2[topitem]) - 1)] #gets random top selection
    bottom_selection = s2[bottomitem][random.randint(0, len(s2[bottomitem]) - 1)] #gets random bottom selection
    global currentoutfitdata
    currentoutfitdata = shoe_selection, top_selection, bottom_selection
#line below appends outfit combos from this session only to the outfitdata list
#above. This list is used to avoid duplication.
    # outfitdata.append([shoe_selection, top_selection, bottom_selection])
#ifs below determine the header for the terminal printout for each clothing item
    if shoeitem == 'casual shoes' or shoeitem == 'professional shoes' or shoeitem == 'nightout shoes':
        shoe_header = "SHOE SELECTION"
    if topitem == 'casual tops' or topitem == 'professional tops' or topitem == 'nightout tops':
        top_header = "TOP SELECTION"
    if bottomitem == 'casual bottoms' or bottomitem == 'professional bottoms' or bottomitem == 'nightout bottoms':
        bottom_header = "BOTTOM SELECTION"
#the code below formats the rest of the terminal printout for the clothing combos.
    print "Alright, how about this? "
    print ""
    header = shoe_header + "    |    " + top_header + "    |   " + bottom_header
    print header
    print "+" * len(header)
    print "Color: %s" % shoe_selection['color'] + \
    (" " * (11 - len(shoe_selection['color']))) + \
    "| " + "Color: %s" % top_selection['color'] + \
    (" " * (13 - len(top_selection['color']))) + "| " + \
     "Color: %s" % bottom_selection['color']
    print "Brand: %s" % shoe_selection['brand'] + \
    (" " * (11 - len(shoe_selection['brand']))) + \
    "| " + "Brand: %s" % top_selection['brand'] + \
    (" " * (13 - len(top_selection['brand']))) + "| " + \
     "Brand: %s" % bottom_selection['brand']
    print "Style: %s" % shoe_selection['style'] + \
    (" " * (11 - len(shoe_selection['style']))) + \
    "| " + "Style: %s" % top_selection['style'] + \
    (" " * (13 - len(top_selection['style']))) + "| " + \
     "Style: %s" % bottom_selection['style']
    print ("-" * len(header))
    print "Notes:%s" % shoe_selection['notes'] + \
    (" " * (12 - len(shoe_selection['notes']))) + \
    "| " + "Notes:%s" % top_selection['notes'] + \
    (" " * (14 - len(top_selection['notes']))) + "| " + \
     "Notes:%s" % bottom_selection['notes']
    print "+" * len(header);
    print "\n"

#NEED HELP WITH DUPE CHECK BELOW. HOW TO LOOP THROUGH A LIST OF DICTIONARIES
#TO CHECK FOR DUPES WITH MULTIPLE KEY VALUE PAIRS AND MULTIPLE combinations
#OF THOSE PAIRS
# def dupecheck(shoe_selection, top_selection, bottom_selection):
#     for i in outfitdata:
#         if shoe_selection['color'] == shoe_selection['color']:


def main_loop():
    codebreaker = True
    while codebreaker == True:
        os.system("clear")
        print ""
        print "Here's what we picked out for you the \nlast time we worked together: "
        print ""
        lastoutfit = open('lastoutfit.pickle', 'rb')
        lastoutfitdata = pickle.load(lastoutfit)
        print "Shoes:"
        print 'Color: %s' % lastoutfitdata[0]["color"]
        print "Style: %s" % lastoutfitdata[0]['style']
        print "Brand: %s" % lastoutfitdata[0]['brand']
        print "Notes: %s" % lastoutfitdata[0]['notes']
        print ""
        print "Top: "
        print "Color: %s" % lastoutfitdata[1]['color']
        print "Style: %s" % lastoutfitdata[1]['style']
        print "Brand: %s" % lastoutfitdata[1]['brand']
        print "Notes: %s" % lastoutfitdata[1]['notes']
        print ""
        print "Bottom: "
        print "Color: %s" % lastoutfitdata[2]['color']
        print "Style: %s" % lastoutfitdata[2]['style']
        print "Brand: %s" % lastoutfitdata[2]['brand']
        print "Notes: %s" % lastoutfitdata[2]['notes']
        print ""
        lastoutfit.close()
        favorite = raw_input("Would you like to add this to your \nfavorites list? (y or n) ").lower()
        print ""
        if favorite == "y":
            favoutfitdata.append(lastoutfitdata)
            f = open('favoriteoutfits.pickle', 'ab')
            pickle.dump(favoutfitdata, f)
            f.close()
            print "Cool, we've added the outfit to your favorites."
            time.sleep(2)
            os.system("clear")
        else:
            os.system("clear")
            time.sleep(1)
        print "Ok, we need a little info before we put \ntogether today's outfit selection."
        time.sleep(2)
        print ""
        season = raw_input("""What's the weather like today? (1=winter 2=spring 3=summer 4=fall)
    **Enter 5 if you'd like to check out your favorites list.**""")
        print ""
        if season == "1":
            print "Ok, it's on the colder side. \nWe'll put together something warm for you."
        elif season == "2":
            print "Yay spring!"
        elif season == "3":
            print "Hot and muggy, eh? \nWe'll keep it on the light and airy side then."
        elif season == "4":
            print "We know it's hard to plan for fall weather, \nso if you're extra picky, we'll understand!"
        elif season == "5":
            "Feeling nostalgic, huh?"
            time.sleep(2)
            objects = []
            try:
                with (open("favoriteoutfits.pickle", "rb")) as openfile:
                    while True:
                        try:
                            objects.append(pickle.load(openfile))
                        except EOFError:
                            break
                    print "Here are your favorites: "
                    print objects #still need to format the favorite list
                    nostalgic = raw_input("Are you planning on going with a favorite? (y or n) ")
                    if nostalgic == 'y':
                        print "You're gonna look great!"
                        break
                    else:
                        pass
            except IOError:
                print "You have no favorites currently."
        season = raw_input("What's the weather like today? (1=winter 2=spring 3=summer 4=fall) ")
        print ""
        if season == "1":
            print "Ok, it's on the colder side. \nWe'll put together something warm for you."
        elif season == "2":
            print "Yay spring!"
        elif season == "3":
            print "Hot and muggy, eh? \nWe'll keep it on the light and airy side then."
        elif season == "4":
            print "We know it's hard to plan for fall weather, \nso if you're extra picky, we'll understand!"
        time.sleep(3)
        os.system("clear")
        occasion = raw_input("And, what's the occasion for your outfit? \n(1=Professional 2=A Night Out 3=Casual) ")
        print ""
        print "Alright, thanks for the info. Your selection is coming right up!"
        time.sleep(2)
        os.system("clear")
        print "\n"
        immediate_eval = False
        while immediate_eval == False:
            if occasion == "1":
                shoeitem = 'professional shoes'
                topitem = 'professional tops'
                bottomitem = 'professional bottoms'
            elif occasion == "2":
                shoeitem = 'nightout shoes'
                topitem = 'nightout tops'
                bottomitem = 'nightout bottoms'
            elif occasion == "3":
                shoeitem = 'casual shoes'
                topitem = 'casual tops'
                bottomitem = 'casual bottoms'
            clothing_selection(season, occasion, shoeitem, topitem, bottomitem)
            immediate = raw_input("Would you like another selection? (y or n) ").lower()
            if immediate == "n":
                os.system("clear")
                time.sleep(1)
                print "\n"
                print "                You're gonna look great!"
                print ""
                print "P.S Your selection was saved to your worn outfits list."
                pastoutfitsdata.append(currentoutfitdata)
                pastoutfits = open('pastoutfits.pickle', 'ab')
                pickle.dump(pastoutfitsdata, pastoutfits)
                pastoutfits.close() #This saves and closes the datafile
                lastoutfit = open('lastoutfit.pickle', 'wb')
                pickle.dump(currentoutfitdata, lastoutfit)
                lastoutfit.close() #This s
                codebreaker = False
                break
            elif immediate == "y":
                immediate_eval = False
                os.system("clear")
                print "We're putting together your next selection."
                time.sleep(2)
                print ""

main_loop()
