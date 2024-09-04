ques = input ("Enter an arithmetic question (format eg (2 / 2 or 2 + 2 or 2 - 2 or 2 * 2 etc) :\n")

x, y, z = ques.split(" ")
if y == "+":
    sum = round((float(x) + float (z)), 1)
    print (sum)
elif y == "-":
    sub = round((float(x) - float (z)), 1)
    print (sub)
elif y == "*":
    mult = round((float(x) * float (z)), 1)
    print (mult)
elif y == "/":
    div = round((float(x) / float (z)), 1)
    print (div)
elif y == "%":
    rem = round((float(x) % float (z)), 1)
    print (rem)
else:
    print ("This is not arithmetic quest. Try again! ")
