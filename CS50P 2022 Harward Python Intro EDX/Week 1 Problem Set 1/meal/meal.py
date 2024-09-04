def main():
    time = input ("Enter the time (format eg 24 hrs in #:## or ##:##) to check meal schedule: \n").strip()
    if 7.0 <= convert(time) <= 8.0 :
       print ("breakfast time")
    elif 12.0 <= convert(time) <= 13.0 :
       print ("lunch time")
    elif 18.0 <= convert(time) <= 19.0 :
       print ("dinner time")
    else:
       pass #or just type return

def convert(time):
      hours, minutes = time.split(":")
      time = float(int (hours) + int (minutes) /60)
      return (time)

if __name__ == "__main__":
      main()

