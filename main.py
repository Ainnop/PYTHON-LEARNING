# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import function_calls
import nested_function
import flow_control


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.
    year = "Py 3.7"
    print("The year value is: {}".format(year))

    a = "atwau"
    b = "innocent"

    list_example = [1, 2, 3, "a", "b", "c"]
    print("An example of a list is: {}".format(list_example))

    tuple_example = (1, 2, 3, "a", "b", "c")
    print("An example of a tuple is: {}".format(tuple_example))

    set_example = set([1, 2, 3, 4, 5])
    print("An example of a set is: {}".format(set_example))

    frozenset_example = frozenset([1, 2, 3, 4, 5])
    print("An example of a frozenset is: {}".format(frozenset_example))

    #    string length using len() method
    string_0 = "Python is becoming the worlds most popular programming language today"
    print(len(string_0))

    # string concatenation using + sign
    string_1 = "Python is becoming the worlds most " + "popular programming language today "
    print(string_1)
    #    string concatenation using join() method
    string_2 = "".join(("Python is becoming the worlds most ", "popular programming language today"))
    print(string_2)
    #    substrings (or splices) using [start, start + length]
    #    get 'Python' word from the start
    string_3 = string_0[0:6]
    print(string_3)
    #    remove 'Python' word from the start
    string_4 = string_0[7:]
    print(string_4)
    #    remove 'today' word from the end
    string_5 = string_0[:-6]
    print(string_5)
    #    select 'programming' word only
    string_6 = string_0[43:54]
    print(string_6)
    #    count how many times letter 'a' is in string
    string_7 = string_0.count("a")
    print(string_7)
    #    find what position 'language' word starts
    string_8 = string_0.find("language")
    print(string_8)
    #    remove any whitespace from the start to end
    string_9 = string_0.strip()
    print(string_9)
    #    convert to lower case
    string_10 = string_0.lower()
    print(string_10)
    #    convert to upper case
    string_11 = string_0.upper()
    print(string_11)
    #    replace 'Python' word with 'Java'
    string_12 = string_0.replace("Python", "Java")
    print(string_12)
    #    split string into substring in 'most' word
    string_13 = string_0.split("most")
    print(string_13)
    #    check if 'popular' word is in string
    string_14 = "popular" in string_0
    print(string_14)


def learn_functions():
    # We have Build-in functions, User-defined functions and Anonymous functions
    my_message = "I like Python programming language"
    print(my_message)


def addition_two_number(number_1, number_2):
    """
   calculate the addition of two numbers
   :param number_1: first number
   :param number_2: second number
   :return: sum of first number plus
   """
    number_addition = number_1 + number_2
    print (number_addition)
    return


def payment_day(amount_of_working_hours, payment_hour=None):
    """
   calculate payment by day
    :type amount_of_working_hours: object
   :param amount_of_working_hours: amount of working hours
   :param payment_hour: payment by hour
   :return: payment by day
   """

    if payment_hour is not None:
        amount_of_total_payment = amount_of_working_hours * payment_hour
    else:
        amount_of_total_payment = 0
    return amount_of_total_payment


# def sum_number(*args):
#     total_sum = sum(args)
#     return total_sum


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    learn_functions()
    addition_two_number(4, 9)
    working_hours = 8
    # calling payment day function
    total_payment = payment_day(working_hours)
    print("The total payment is: {}".format(total_payment))

    # Call summation of numbers
    result_1 = function_calls.sum_number(1, 2, 3, 4, 5)
    print("result_1: {}".format(result_1))

    result_2 = function_calls.sum_number(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print("result_2: {}".format(result_2))

    function_calls.print_dictionary(value1=1, value2="Python", value3=False, value4=3.14)

    value = 10
    value_double = function_calls.calculate_double(value)
    print("The value double in main() is: {}".format(function_calls.x_global))

    value = 10
    value_double = nested_function.outer_function(value)

    # Lambda Functions
    function_double = lambda x: x * 2
    x = 10
    print("The x value is: {}".format(function_double(x)))

    # FLOW CONTROL
    flow_control.flows()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
