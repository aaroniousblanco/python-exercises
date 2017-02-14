import pickle

print """Electronic Phone Book
=====================
1. Look up an entry
2. Add/update an entry
3. Delete an entry
4. List all entries
5. Quit
"""

def phone_book():
    try:
        my_file = open('phone_book.pickle', 'r')
        phonebook_dict = pickle.load(my_file)
        my_file.close()
        print "Phonebook data restored."
    except IOError:
        print "No phone book data restored."
    while True:
        user_selection = raw_input("What do you want to do (1-7)? ")
        if user_selection == "1":
            user_input_name = raw_input("Who are you looking for? ").lower()
            phone_number = phonebook_dict.get((user_input_name),
            "")
            if phone_number == "":
                print "Entry not found. Please try again."
            else:
                print "Name: %s" % user_input_name
                print "Phone Number: %s" % phone_number
        elif user_selection == "2":
            new_user_input_name = raw_input("Who are you adding/updating? ").lower()
            new_phone_number = raw_input("Please enter the phone number. ")
            phonebook_dict[new_user_input_name] = new_phone_number
            print "Entry added/updated."
        elif user_selection == "3":
            entry_to_be_deleted = raw_input("Who are you deleting? ")
            del phonebook_dict[entry_to_be_deleted]
            print "Your entry has been deleted."
        elif user_selection == "4":
            for entry in phonebook_dict.items():
                print "%s's number is %s" % entry
        elif user_selection == "5":
            my_file = open('phone_book.pickle', 'w')
            pickle.dump(phonebook_dict, my_file)
            my_file.close()
            print "Your entries have been saved."
            print "Goodbye!"
            break
phone_book()
