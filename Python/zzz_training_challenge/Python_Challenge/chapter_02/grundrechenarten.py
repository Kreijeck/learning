def calc(m, n):
    mul = m * n
    div = mul // 2

    return div % 7


def calc_sum_and_count_all_numbers_div_by_2_or_7(max_exclusive):
    div_2 = []
    div_7 = []
    count = 0
    sum = 0

    for i in range(1, max_exclusive):
        if i % 2 == 0 or i % 7 == 0:
            sum += i
            count += 1
            if i % 2 == 0:
                div_2.append(i)
            if i % 7 == 0:
                div_7.append(i)

    return div_2, div_7, count, sum


def number_as_text(n):
    num2str_dict = {0: "ZERO",
                    1: "ONE",
                    2: "TWO",
                    3: "THREE",
                    4: "FOUR",
                    5: "FIVE",
                    6: "SIX",
                    7: "SEVEN",
                    8: "EIGHT",
                    9: "NINE"
                    }
    value_list = []
    while n != 0:
        remainder = n % 10
        n = n // 10
        value_list.insert(0, num2str_dict[remainder])

    return " ".join(value_list)


number_as_text(4123)

def check_divisor_sum(n):
    div = []
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            div.append(i)
            sum += i

    return div, sum

def calc_perfect_numbers(max_exclusive):
    perfect_number = []
    for i in range(1, max_exclusive):
        _,  sum = check_divisor_sum(i)
        if i == sum:
            perfect_number.append(i)

    return perfect_number
