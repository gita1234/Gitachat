#use this "lewis" and "1234" in user-name and password
loginun="Geetashri"                      #variable taken
loginps="12345"
def details():
    while 1 == 1:
        print "Enter your username:"  # created username
        logi = raw_input()
        if logi==loginun:
            print "Enter your password:"  # created password
            login = raw_input()
            if login==loginps:
                print "login sucessful:!!!"
                break;

            else:
                print"Password incorrect"

        else:
            print "login failed!!!\t re-enter"

    print "wel come back\n\t Mr Lewis\n\tage-20\n\trating-4(good)\n\tyou are online * now"