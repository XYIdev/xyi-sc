import os



setup =  open('setup.txt', 'r')
lines = [setup.readline(),setup.readline()]
setup.close()
if os.path.exists("setup.txt"):
  os.remove("setup.txt")
create = open("setup.txt", "w+")
create.close()
create = open("setup.txt", "a")
create.write("#Token:")
token = open("data/token.token", "w+")
token.write(lines[1])
token.close()
if os.path.exists("data/token.token"):
    print("Setup finished successfully.")
else:
    print("Setup failed.")
input("Press Return to exit.")
a = keyboard.read_key()
if (a):
    exit(0)


