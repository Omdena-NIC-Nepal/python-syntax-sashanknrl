def format_string(name, age):
    return f"My name is {name} and I am {age} years old"


def conditional_check(number):
    if number > 10:
        return "Greater"
    elif number < 10:
        return "Lesser"
    else:
        return "Equal"


def loop_sum(n):
    sum = 0
    for number in range(1, n+1):
        sum += number
    return sum


def list_operations(numbers):
    sum = 0
    max = numbers[0]
    min = numbers[0]

    for num in numbers:
        sum += num

        if num > max:
            max = num
        elif num < min:
            min = num
    
    return (sum, max, min)


def dict_operations(students_dict):
    stud_list = []
    for x, y in students_dict.items():
        if y > 80:
            stud_list.append(x)
    
    return stud_list


def set_operations(list1, list2):
    commmon_elements = set(list1).intersection(set(list2))
    return commmon_elements


def arithmetic_ops(a, b):
    try:
        return {
            "sum": a + b,
            "difference": a - b,
            "product": a * b,
            "quotient": a / b
        }
    except ZeroDivisionError:
        print("Cannot divide by Zero")
        return {
            "sum": a + b,
            "difference": a - b,
            "product": a * b,
        }


def logical_ops(x, y):
    return {
        "and": x and y,
        "or": x or y,
        "not_x": not x
    }


def bitwise_ops(a, b):
    return {
        "and": a & b,
        "or": a | b,
        "xor": a ^ b
    }