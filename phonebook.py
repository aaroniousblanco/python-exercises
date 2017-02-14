import pickle

print """Electronic Phone Book
=====================
1. Look up an entry
2. Add/update an entry
3. Delete an entry
4. List all entries
5. Save entries
6. Load saved data
7. Quit """

def phone_book():
    my_file = open('phone_book.pickle', 'r')
    phonebook_dict = pickle.load(my_file)
    while True:
        global user_selection
        user_selection = raw_input("What do you want to do (1-7)? ")
        if user_selection == "1":
            user_input_name = raw_input("Who are you looking for? ")
            phone_number = phonebook_dict.get((user_input_name),
            "")
            if phone_number == "":
                print "Entry not found. Please try again."
                phone_book()
            else:
                print "Name: %s" % user_input_name
                print "Phone Number: %s" % phone_number
        elif user_selection == "2":
            new_user_input_name = raw_input("Who are you adding/updating? ")
            new_phone_number = raw_input("Please enter the phone number. ")
            phonebook_dict[new_user_input_name] = new_phone_number
            print "Entry added/updated."
        elif user_selection == "3":
            entry_to_be_deleted = raw_input("Who are you deleting? ")
            del phonebook_dict[entry_to_be_deleted]
            print "Your entry has been deleted."
        elif user_selection == "4":
            entries = phonebook_dict.items()
            print entries
        elif user_selection == "5":
            my_file = open('phone_book.pickle', 'w')
            pickle.dump(phonebook_dict, my_file)
            my_file.close()
            print "Your entries have been saved."
        elif user_selection == "6":
            my_file = open('phone_book.pickle', 'r')
            phonebook_dict = pickle.load(my_file)
            print "Here's the updated phonebook: %r" % phonebook_dict
        else:
            break
phone_book()
