'''
Victor Lara
PC01 Basic Bot
'''
userName = input ("Hi, and welcome to the world. What is your name?")
userName = userName.title()
print(f"Hello {userName}, you are now online.")
print(f"Being online is a big responsibility,{userName}.")
status = input("How are you doing today?")
if status in ('good', 'alright', 'pretty well', 'pretty good'):
    print("Feeling", status, "is awesome.")
if status in ('bad', 'terrible', 'not good', 'okay'):
    print("Hey, feeling", status, "is also a part of life." "\nThough, I am sorry to hear that.")
location = input("In order for us to move forward, we need to know where you are. Can you share your current location?")
print("Great.", location.title(), "is a fun place to be. I heard there is great coffee around there.""\nHope you enjoy it out there!")
