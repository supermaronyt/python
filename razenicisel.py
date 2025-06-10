def simple_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                # Swap
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


numbers = list(map(int, input("Zadejte čísla oddělená mezerou: ").split()))
sorted_numbers = simple_sort(numbers)
print("Seřazený seznam:", sorted_numbers)
