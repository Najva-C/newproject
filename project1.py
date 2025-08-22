# LIST OPERATIONS

# list=["apple","orange","kiwi","mango","banana"]
# print(list)
# print(list[0])
# print(list[1:3])
# list.append("lemon")        
# print(list)
# if "berry" in list:
#     print("berry is present")
# else:
#     print("not present")
# print(list.remove("kiwi"),list)
# list.remove("banana")
# print(list)

# while True:
#     print("MENU:-")
#     print("1.Add")
#     print("2.View")
#     print("3.Exit")
#     choice = input("Enter Your Choice(1-3):")
#     if choice == '1':
#         list1=input("enter the item to be appended:")
#         list.append(list1)
#         print("item appendend!")
#     elif choice == '2':
#         print(list)
#     else:
#         print("EXITED!")
#         break
# for i in list:
#     print(i)
# for i,it in enumerate(list,start=1):
#     print(i,it)

# dict=[{"Name":"Apple","Price":30,"Quantity":1},
#        {"Name":"Orange","Price":30,"Quantity":1},
#        {"Name":"Kiwi","Price":30,"Quantity":1},
#        {"Name":"Mango","Price":30,"Quantity":1},
#        {"Name":"Banana","Price":30,"Quantity":1}]
# print(dict)
# for i in dict:
#     print(i)

fruits = []

while True:
    print("\nFRUITS MENU")
    print("1. Add")
    print("2. View")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter fruit name: ").lower()
        price = float(input("Enter fruit price: "))
        fruits.append({"name": name, "price": price})
        print(f"Fruit added: {name} (${price})")

    elif choice == "2":
        if not fruits:
            print("No fruits in the list.")
        else:
            print("Fruit List:")
            for fruit in fruits:
                print(f"- {fruit['name']} (${fruit['price']})")

    elif choice == "3":
        name = input("Enter the fruit name to update: ").lower()
        found = False
        for fruit in fruits:
            if fruit["name"] == name:
                new_name = input("Enter new fruit name: ").lower()
                new_price = float(input("Enter new price: "))
                fruit["name"] = new_name
                fruit["price"] = new_price
                print(f"Fruit updated: {new_name} (${new_price})")
                found = True
                break
        if not found:
            print("Fruit not found.")

    elif choice == "4":
        name = input("Enter the fruit name to delete: ").lower()
        found = False
        for fruit in fruits:
            if fruit["name"] == name:
                fruits.remove(fruit)
                print(f"{name} removed successfully.")
                found = True
                break
        if not found:
            print(f"{name} not found in the list.")

    elif choice == "5":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please select a valid option.")



        
        #     print("EXITED!")
        #     break
            
            # names=input("Enter new fruit:")
            # price=float(input("enter fruit price to be updated:"))
            # prices=float(input("Enter new price:"))
            # dict.update({"name":name,"price":price})
            # print(f"Fruit updated: {names} (${prices})")

        
            

