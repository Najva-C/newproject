# # cart=[] 

# # print("SHOPPING CART MENU")
# # print("1.ADD ITEM ")
# # print("2.REMOVE ITEM ")
# # print("3.UPDATE ITEM ")
# # print("4.VIEW ITEM")
# # print("5.SEARCH FOR ITEM ")
# # print("6.SLICE CART")
# # print("7.SORT CART")
# # print("8.EXIT")

# # # print=(input("Choose an option from 1-8:"))
# # item=input("Enter an item:")
# # cart.append(item)
# # print(f"{item} added to cart.")

# # # print=(input("Choose an option from 1-8:"))
# # item = input("Enter item to remove: ")
# # cart.remove(item)
# # print(f"'{item}' removed from cart.")



# # print(cart)




# shopping_cart = []

# while True:
#     print("\n===== Shopping Cart Menu =====")
#     print("1. Add item")
#     print("2. Remove item")
#     print("3. Update item")
#     print("4. View cart")
#     print("5. Search for item")
#     print("6. Slice cart")
#     print("7. Sort cart")
#     print("8. Exit")

#     choice = input("Choose an option (1-8): ")

#     if choice == '1':
#         item = input("Enter item to add: ")
#         shopping_cart.append(item)
#         print(f"'{item}' added to cart.")
#         print("cart:",shopping_cart)

#     elif choice == '2':
#         item = input("Enter item to remove: ")
#         if item in shopping_cart:
#             shopping_cart.remove(item)
#             print(f"'{item}' removed from cart.")
#             print("cart:",shopping_cart)

#         else:
#             print(f"'{item}' not found in cart.")


#     elif choice == '3':
#         old_item = input("Enter the item to update: ")
#         if old_item in shopping_cart:
#             new_item = input("Enter new item name: ")
#             index = shopping_cart.index(old_item)
#             shopping_cart[index] = new_item
#             print(f"'{old_item}' updated to '{new_item}'.")
#             print("cart:",shopping_cart)

#         else:
#             print(f"'{old_item}' not found in cart.")


#     elif choice == '4':
#         print("\nYour Shopping Cart:")
#         if shopping_cart:
#             for i in range(len(shopping_cart)):
#                 print(f"{i + 1}. {shopping_cart[i]}")
#                 print("cart:",shopping_cart)

#         else:
#             print("Cart is empty.")


#     elif choice == '5':
#         item = input("Enter item to search: ")
#         if item in shopping_cart:
#             print(f"'{item}' found at position {shopping_cart.index(item) + 1}")
#             print("cart:",shopping_cart)

#         else:
#             print(f"'{item}' not found in cart.")


#     elif choice == '6':
#         start = int(input("Enter start index: "))
#         end = int(input("Enter end index: "))
#         print("Cart slice:", shopping_cart[start:end])
#         print("cart:",shopping_cart)


#     elif choice == '7':
#         shopping_cart.sort()
#         print("Cart sorted alphabetically.")
#         print("cart:",shopping_cart)


#     elif choice == '8':
#         print("Exiting... Thank you!")
#         break

#     else:
#         print("Invalid choice. Please select a number from 1 to 8.")


