"""
수학 계산 라이브러리
다양한 수학 연산 및 통계 함수를 제공합니다.
"""

import math
from typing import List, Tuple, Optional
from functools import reduce


def calculate_factorial(n: int) -> int:
    """
    팩토리얼을 계산합니다.
    
    Args:
        n: 팩토리얼을 계산할 정수
        
    Returns:
        n!
    """
    if n < 0:
        raise ValueError("음수는 팩토리얼을 계산할 수 없습니다")
    if n == 0 or n == 1:
        return 1
    return reduce(lambda x, y: x * y, range(1, n + 1))


def is_prime(n: int) -> bool:
    """
    소수 여부를 판별합니다.
    
    Args:
        n: 판별할 정수
        
    Returns:
        소수 여부
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def generate_primes(limit: int) -> List[int]:
    """
    에라토스테네스의 체를 사용하여 소수를 생성합니다.
    
    Args:
        limit: 상한값
        
    Returns:
        소수 리스트
    """
    if limit < 2:
        return []
    
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    
    return [i for i in range(limit + 1) if sieve[i]]


def calculate_gcd(a: int, b: int) -> int:
    """
    최대공약수를 계산합니다.
    
    Args:
        a: 첫 번째 정수
        b: 두 번째 정수
        
    Returns:
        최대공약수
    """
    while b:
        a, b = b, a % b
    return abs(a)


def calculate_lcm(a: int, b: int) -> int:
    """
    최소공배수를 계산합니다.
    
    Args:
        a: 첫 번째 정수
        b: 두 번째 정수
        
    Returns:
        최소공배수
    """
    return abs(a * b) // calculate_gcd(a, b)


def fibonacci_sequence(n: int) -> List[int]:
    """
    피보나치 수열을 생성합니다.
    
    Args:
        n: 생성할 항의 개수
        
    Returns:
        피보나치 수열 리스트
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence


def calculate_distance(point1: Tuple[float, float], 
                       point2: Tuple[float, float]) -> float:
    """
    두 점 사이의 유클리드 거리를 계산합니다.
    
    Args:
        point1: 첫 번째 점 (x, y)
        point2: 두 번째 점 (x, y)
        
    Returns:
        거리
    """
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def solve_quadratic(a: float, b: float, c: float) -> Optional[Tuple[float, float]]:
    """
    이차방정식의 해를 구합니다 (ax² + bx + c = 0).
    
    Args:
        a: x²의 계수
        b: x의 계수
        c: 상수항
        
    Returns:
        해의 튜플 또는 None (실근이 없는 경우)
    """
    if a == 0:
        return None
    
    discriminant = b**2 - 4*a*c
    
    if discriminant < 0:
        return None
    
    sqrt_discriminant = math.sqrt(discriminant)
    x1 = (-b + sqrt_discriminant) / (2*a)
    x2 = (-b - sqrt_discriminant) / (2*a)
    
    return (x1, x2)


def calculate_compound_interest(principal: float, rate: float, 
                                 time: float, n: int = 1) -> float:
    """
    복리 이자를 계산합니다.
    
    Args:
        principal: 원금
        rate: 연이율 (소수로 표현, 예: 5% = 0.05)
        time: 기간 (년)
        n: 연간 복리 계산 횟수
        
    Returns:
        최종 금액
    """
    return principal * (1 + rate / n) ** (n * time)


def calculate_standard_deviation(numbers: List[float]) -> float:
    """
    표준편차를 계산합니다.
    
    Args:
        numbers: 숫자 리스트
        
    Returns:
        표준편차
    """
    if not numbers:
        return 0.0
    
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return math.sqrt(variance)

