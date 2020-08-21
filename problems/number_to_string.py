
numbers_dict = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero",
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen",
    "20": "twenty",
    "30": "thirty",
    "40": "forty",
    "50": "fifty",
    "60": "sixty",
    "70": "seventy",
    "80": "eighty",
    "90": "ninety",
    "100": "hundred",
}

_names_dict = {
    "0": "",
    "1": "thousand",
    "2": "million",
    "3": "trillion"
}


def get_description(digit, position, prev_digit=""):
    import math
    if digit == '0':
        return ""
    place = numbers_dict[str(int(math.pow(10, position)))]
    if place == "ten" or position == 1:
        if digit == '1':
            return numbers_dict[digit + prev_digit]
        return numbers_dict[str(int(digit) * 10)]
    else:
        if place == "one":
            return numbers_dict[digit]
        return numbers_dict[digit] + " " + place


def get_string(number):
    three_digit_value = ""
    prev_digit = ""
    for index, j in enumerate(number[::-1]):
        if index == 1 and j == "1":
            three_digit_value = ""
        three_digit_value = get_description(j, index, prev_digit) + " " + three_digit_value
        prev_digit = j
    return three_digit_value


def represent_number_in_words(number):
    iterations = int(len(number) / 3) + (1 if int(len(number) % 3) else 0)
    step = 3 if len(number) > 2 else len(number)
    end = len(number)
    start = end - step
    final_string = ""

    for i in range(iterations):
        curr_num = number[start:end]
        end = start
        start = (end - step) if end > step else 0
        if curr_num in numbers_dict.keys():
            final_string = numbers_dict.get(curr_num) + " " + _names_dict[str(i)] + " " + final_string
        else:
            final_string = get_string(curr_num) + " " + _names_dict[str(i)] + " " + final_string
    return final_string


input_number = "999999999999"
print(represent_number_in_words(str(int(input_number.replace(",", "")))))


# Complete the isBalanced function below.
def isBalanced(s):
    open_parenthesis_dict = {')': '(', ']': '[', '}': '{'}
    stack = []
    for x in s:
        if stack and open_parenthesis_dict.get(x) == stack[-1]:
            stack.pop()
        else:
            stack.append(x)
    if stack:
        print('invalid-T')
        del stack
        return 'NO'
    else:
        print('valid')
        del stack
        return 'YES'


isBalanced("({({})})")
