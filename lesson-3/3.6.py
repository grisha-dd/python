#nice авп ъghj jапро hjjпаро вапрghgh cool

# def int_func(user_text):
#     for item in user_text:
#         if ord(item) < 97 or ord(item) > 122:
#             return ""
#     return  user_text.capitalize()
#
#
# print(int_func(input("Введите слово из маленьких латинских букв: ")))

def ext_func(user_line):
    def int_func(user_text):
        for item in user_text:
            if ord(item) < 97 or ord(item) > 122:
                return ""
        return user_text.capitalize()

    user_list = user_line.split()
    result = []
    for word in user_list:
        cap_word = int_func(word)
        if cap_word != "":
            result.append(cap_word)
    return " ".join(result)


print(ext_func(input("Введите слово из маленьких латинских букв: ")))
