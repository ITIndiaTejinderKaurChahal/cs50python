ans = input ("What is the answer to the the great question of Life, the Universe and Everything?\n").casefold().strip()
#case folde is better than lower() method as it can mange special charcters and accented characters
#  aggresively than lower
match ans:
    case "42" | "forty-two" | "forty two" | "Forty Two" | "Forty-Two" | " 42" | "42 " | " 42 ":
         print ("Yes")
    case _:
          print ("No")
