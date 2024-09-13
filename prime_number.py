import math

def is_prime_number(x):
    if x <= 1:
        return "오류: 입력값은 1보다 커야 합니다."

    if x == 2:
        return True  # 2는 유일한 짝수 소수입니다.

    if x % 2 == 0:
        return False  # 2를 제외한 모든 짝수는 소수가 아닙니다.

    # 3부터 x의 제곱근까지 홀수만 체크합니다.
    for num in range(3, int(math.sqrt(x)) + 1, 2):
        if x % num == 0:
            return False  # 약수를 찾았으므로 x는 소수가 아닙니다.

    return True  # 약수를 찾지 못했으므로 x는 소수입니다.
