def all_loops():
    ebooks = ["python", "perl", "ruby"]
    for item in ebooks:
        print("The eBook is: {}".format(item))


def using_range():
    for x in range(6, 11):
        print(x)


def using_while():
    ebooks = ["python", "perl", "ruby"]
    i = 0
    while ebooks[i] != "ruby":
        print(ebooks[i])
        i += 1


def using_while_continue():
    ebooks = ["python", "perl", "ruby"]
    i = 0
    while ebooks[i] != "ruby":
        i += 1
        if ebooks[i] == "python":
            continue
        print(ebooks[i])


def using_break():
    ebooks = ["python", "perl", "ruby"]
    for item in ebooks:
        print(item)
        if item == "perl":
            break
