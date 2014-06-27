# Objective:
# Create a program that will ask the users name, age, and Reddit username. 
# Have it tell them the information back, in the format:
# "Your name is (blank), you are (blank) years old, and your username is (blank)"
# For extra credit, have the program log this information in a file to be accessed later.

def main():
        name = raw_input("Please enter your name: ")
        age = raw_input("Please enter your age: ")
        redditUsername = raw_input("Please enter your Reddit username: ")
        print("Your name is %s, you are %s years old, and your Reddit username is %s." % (name,age,redditUsername))

        # Store in a file
        out = open("easyChallange001_Storage.txt", 'a')
        storedInfo = "%s, %s, %s\n" % (name,age,redditUsername)
        out.write(storedInfo)
        out.close()
main()
