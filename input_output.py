def input_output():
    zip_code = input("Enter your zip code: ")
    print("The entered zip code is: {}".format(zip_code))


def file_writing():
    file_test = open("test.txt", "w")
    file_test.write("Python is great language.\nSure!\n")
    file_test.close()


def file_append():
    file_test = open("test.txt", "a")
    file_test.write("Add this new line to the end of the file test.txt")
    file_test.close()


def file_read():
    file_test = open("test.txt", "r")
    print(file_test.read())
