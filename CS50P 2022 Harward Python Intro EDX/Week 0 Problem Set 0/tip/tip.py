#import re

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print (f"Leave ${tip:.2f}")

def dollars_to_float (d):
    meal_money = float(d.replace ("$",""))
    return meal_money
# another way was d=d.replace("$","")) return float (d)


def percent_to_float (p):
    # roughwork: if p.endswith('%'):
    # rough work:      #  p= p[:-1]
     tip_percentage = float(p.replace("%",""))
     return float(tip_percentage)/100
#if _name_ == "_main_"':
main ()


#Rough
#match = re.search(r'\$([0-9]*\.?[0-9]+)',d)
    #if match:
        #    return float (match.group())
    #else :
         #   raise ValueError ("No dollar value found")
