items = ["Valorant", "Minecraft", "Apex Legends", "GTA V", "Witcher 3"]
options = ["Show all items","Add new item","Remove an item","Sort items (A–Z)","Reverse order","Find item index","Exit"]

print(f"The list : {items} , Select the number associated with the given option to perform operations")

for index , option in enumerate(options):
    print(f"* Enter {index + 1} to {option}")

while True :
    select = int(input("Enter the option number : ").strip())
    match select:
        case 1:
            print(items)
        case 2:
            new_item_input = input("Enter the new element")
            new_input_type = input("Enter the type (int , float , str , bool) :").lower()
            new_element = ""
            match new_input_type:
                case "int":
                    new_element = int(new_item_input)
                case "str":
                    new_element = new_item_input
                case "float":
                    new_element = float(new_item_input)
                case "bool":
                    new_element = bool(new_item_input)
                case _:
                    print("---- Invalid element type ----")
            items.append(new_element)
        case 3:
            remove_item = int(input("Enter the index of element you want to remove:").strip())
            items.pop(remove_item)
        case 4:
            items.sort()
        case 5:
            items.reverse()
        case 6:
            search_Item = input("Enter the item : ").strip()
            print(f"The index of {search_Item} is : {items.index(search_Item)}")
        case 7:
            print("Mutation window - terminated.")
            break # Exit option selected 
        case _:
            continue # No valid option selected





