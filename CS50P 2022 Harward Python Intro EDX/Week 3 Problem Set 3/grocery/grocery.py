def main():

    grocery_list = {}                                       # Dictionary to hold item counts

    print("\n")

    while True:
        try:
            item = input().strip()
            if item:
                item_upper = item.upper()
                if item_upper in grocery_list:
                    grocery_list[item_upper] += 1
                else:
                    grocery_list[item_upper] = 1
        except EOFError:                                    # manage control plus D to stop further input and exit
            break


    sorted_items = sorted(grocery_list.keys())               # Sort the items alphabetically


    for item in sorted_items:                                # Print the items with their counts
        print(f"{grocery_list[item]} {item}")

if __name__ == "__main__":
    main()
