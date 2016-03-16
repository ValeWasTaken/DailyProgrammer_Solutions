# Python 3.4
def store_info():
        name = input("Please enter your name: ")
        age = input("Please enter your age: ")
        username = input("Please enter your Reddit username: ")
        print("Info check: Name = {0}\n, Age = {1}\n, Username = {2}\n".format(name,age,username)

        # Store in a file
        out = open("easyChallange001_Storage.txt", 'a')
        storedInfo = "{0}, {1}, {2}\n".format(name,age,username)
        out.write(storedInfo)
        out.close()
store_info()
