while True:
    try:
     user_input = input(f"Fraction: ")
     x, y = user_input.split("/")
     x , y = int(x) , int(y)
     tank_fuel = (x / y) * 100
     if round(tank_fuel) <= 1:
      print("E")
      break
     elif 100 >= round(tank_fuel) >= 99:
       print("F")
       break
     elif round(tank_fuel) >=100: #x > y cases
       pass
     else:
       print(round(tank_fuel), "%", sep="")
       break
    except (ValueError, ZeroDivisionError, TypeError):
      pass

# tried without break and found this was continuing &
# was not coming out even after trying all the choices
