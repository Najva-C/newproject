# emoji={"happy":'😁',"sad":'😒'}
# message=(input("Enter your emotion:"))
# if emoji is message:
#     happy=emoji["happy"]
#     print(message,emoji["happy"])
# else:
#     print(message,emoji["sad"])
    

def emojireplace(message):
    emoji_dict = {"happy": '😁', "sad": '😒'}
    for key, value in emoji_dict.items():
        message = message.replace(key, value)
    return message

user_input = input("Enter your emotion: ")
print(emojireplace(user_input.lower()))



# emoji={'happy':'😁','sad':'😢','angry':'😡','pizza':'🍕'}
# n=input("Enter message:")
# for key,value in emoji.items():
#       n=n.replace(key,value)
# print(n)

# OR

# emoji={'happy':'😁','sad':'😢','angry':'😡','pizza':'🍕'}
# n=input("Enter message:")
# for a in emoji:
#     if a in n:
#         n=n.replace(a,emoji[a])
# print(n)
