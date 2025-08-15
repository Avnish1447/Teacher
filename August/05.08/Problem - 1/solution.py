def toChatOrNot():
    userName = input("")
    userNameSet = set(userName)
    userNameLength = len(userNameSet)

    if userNameLength % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")

toChatOrNot()
