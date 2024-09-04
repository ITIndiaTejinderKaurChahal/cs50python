def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
     pl = len(s)
     if 6 >= pl >= 2 and s[0:2].isalpha() and s.isalnum():
      #isalnum to check no special character. Just aplha and numbers
      #s[0:2] will check index 0 and 1
         for char in s:
             if char.isdigit():
                 index = s.index(char)
                 if s[index:].isdigit() and int(char) != 0:
                     #int(char) to change s str to int type before comparsion to zero
                     return True
                 else:
                     return False
         return True



main()

''' if not (plate[0].isalpha()) and (plate[1].isalpha()) and (plate[2].isalpha()) and (plate[3].isalpha()) and (plate[4].isalpha()) and (plate[5].isalpha()):
          return False
     if not (plate[-2] != 0):
          return False
     for char in plate [2:]:
             if not (char.isalpha() or char.isdigit() or char != '0'):
                 return False
             else:
                  return True '''


