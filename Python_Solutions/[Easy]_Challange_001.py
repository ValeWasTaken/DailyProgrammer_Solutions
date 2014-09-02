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
