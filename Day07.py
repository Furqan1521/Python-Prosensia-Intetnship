def manual_sort(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[i]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers

def analyze_list(numbers):
    total = 0
    minimum = numbers[0]
    maximum = numbers[0]
    
    for num in numbers:
        total += num
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num

    average = total / len(numbers)
    return {
        "Sorted List": manual_sort(numbers.copy()),
        "Sum": total,
        "Average": round(average, 2),
        "Minimum": minimum,
        "Maximum": maximum
    }

def print_summary(stats):
    for i, (key, value) in enumerate(stats.items(), 1):
        print(f"{i}. {key}: {value}")

# Input with validation
raw_input = input("Enter numbers separated by spaces: ")
try:
    number_list = [float(x) for x in raw_input.strip().split()]
    if not number_list:
        print("No numbers entered.")
    else:
        stats = analyze_list(number_list)
        print_summary(stats)
except ValueError:
    print("Invalid input. Please enter only numeric values.")
