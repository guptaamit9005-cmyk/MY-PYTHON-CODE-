input("What is your name ?")  # Simple input function 
print("Hello" + " " + input("What is your name ?")) # function and string contatination
input("What is your name") # Simple input function.
print("Hey amit" + " " + "How are you ?")
# simple methos
print("Hey" + " " + input("What is your name? ") + " " + "How are you ?")

# 1. USING VARIABLE 
name = input("What is your name? ")
print("Hey " + name + " How are you?")

# 2. USING F-STRING 
name = input("What is your name? ")
print(f"Hey {name} How are you?")

# 3.USING FORMAT()
name = input("What is your name? ")
print("Hey {} How are you?".format(name))

# 4. Multiple Argumented 
name = input("What is your name? ")
print("Hey", name, "How are you?")


name = input("What is your name? ")
print("Hey %s How are you?" % name)


name = input("What is your name? ")
print(" ".join(["Hey", name, "How are you?"]))

name = input("What is your name? ")
greeting = "Hey " + name + " How are you?"
print(greeting)


name = input("What is your name? ")
print("Hey", name, "How are you?", sep=" ")


name = input("What is your name? ")
print("Hey {n} How are you?".format(n=name))

greet = lambda name: f"Hey {name} How are you?"
print(greet(input("What is your name? ")))


def greet(name):
    print(f"Hey {name} How are you?")

name = input("What is your name? ")
greet(name)























































































































