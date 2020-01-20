def find_nemo(variable):
    split_list = variable.split()
    result = False
    for i in range(0, len(split_list)):
        seek_word = split_list[i]
        if seek_word == "Nemo":
            postition = str(i + 1)
            result = True
    if result == True:
        print("I found Nemo at " + postition + "!")
    else:
        print("I can't find Nemo :(")
find_nemo(str(input("String: ")))