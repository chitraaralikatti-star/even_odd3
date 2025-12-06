import pytest
def count_even_odd(numbers):
    even = 0
    odd = 0

    for n in numbers:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1

    result = (
        f"Even Count: {even}\n"
        f"Odd Count: {odd}"
    )
    return result


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 6, 7]
    print(count_even_odd(nums))
