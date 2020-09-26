user_name = ["rikin","turyam","swami","brata","jeast"]
admin = ["rikin"]
members = ["turyam","swami","brata","jeast"]                  #if admin print message "" & if members print diff. message.
who = input("name? ")
if who in admin:
    print("hey admin!, would you like to see a status report. ")
elif who in user_name:
    print(who + ",glad you are here!")
else:                                                           #if not admin or member ...tell them to sign up.
    print("please sign up! ")
print("thanks for visiting us!")
haters = []                                                     #what if list is empty?....print message.
if haters:
    print("This are our hater.")
else:
    #print(f"we don't have haters.we need to find some r haters..... :\  ")
    print(f"we don't have haters.we need to find some haters...... :\ ")
print("\n hey!, nice to see you. let's sign up!! ;) ")
new_user = ["rikin","turyam","swami"]
current_user =["rikin","turyam","swami","brata","jeast","arjun","dooryodhan","shiv","krishna"]
try_limit=3                                                                          #while loop is added by me.
try_count=0                                                                          #program is from ch5 last exercise(ceash_course py.) 
while try_count<try_limit:                                                           #lots of modification are done by me!...see original que. from ch5_last ex..  
    try_count += 1
    sign_up = input("\ncreate user name for yourself as your identity. ")
    if sign_up.title() in current_user:
        print("user_name already in use....try with another user_name.")
    elif sign_up.upper() in current_user:
        print("user_name already in use....try with another user_name.")
    elif sign_up.lower() in current_user:
        print("user_name already in use....try with another user_name.")
    else:
        print("yes!, user_name avaliable")
        print("\n type ok to create your account with this user_name.")
        confirmation = input(" ok? ")
        if confirmation=="ok":
            print("woohoo!! user_name confirmed,Account created")
            current_user.append(sign_up)
            print("wanna see current_user list? if you, type 'yes'.")
            show_list = input("yes?!")
            if show_list == "yes":
                print(current_user)
        else:
            print("user_name not registered.")
        break
else:
    print("too many try!!...try after some time!")
print(sign_up +",Thanks for visiting us!")

