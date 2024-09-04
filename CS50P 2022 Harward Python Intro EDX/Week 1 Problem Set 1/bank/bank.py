
g = input("Greetings of the day:").casefold().strip()

if g.startswith ("hello"):
   print ("$0")
elif g.startswith ("h"):
    print ("$20")
else:
    print ("$100")


