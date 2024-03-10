from itertools import product
def calculate_expression(expression, values):
    # 소문자 알파벳을 숫자로 대체
    for letter, value in values.items():
        expression = expression.replace(letter, str(value))

    # 모든 연산은 같은 우선순위를 가지므로 왼쪽에서 오른쪽으로 계산
    elements = expression.split(' ')
    result = int(elements[0])
    for i in range(1, len(elements), 2):
        operator = elements[i]
        operand = int(elements[i + 1])
        if operator == '+':
            result += operand
        elif operator == '-':
            result -= operand
        elif operator == '*':
            result *= operand
    return result
def parse_expression(expression):
    # 각 연산자와 피연산자 사이에 공백 추가
    parsed_expression = ""
    for char in expression:
        if char in "+-*":
            parsed_expression += f' {char} '
        else:
            parsed_expression += char
    return parsed_expression

def max_expression_result(expression):
    # 식 파싱
    parsed_expression = parse_expression(expression)

    # 나머지 코드는 동일하게 유지
    letters = set(filter(str.isalpha, parsed_expression))
    max_result = float('-inf')
    for values in product(range(1, 5), repeat=len(letters)):
        letter_to_value = dict(zip(letters, values))
        result = calculate_expression(parsed_expression, letter_to_value)
        max_result = max(max_result, result)
    return max_result

# 사용자 입력 처리
test = input()
print(max_expression_result(test))