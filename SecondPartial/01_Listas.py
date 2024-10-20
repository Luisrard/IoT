#21310369

def capture_numbers():
    numbers = input("Enter numbers separated by spaces: ").split()
    return list(map(int, numbers))

def get_middle_sublist(numbers: list[int]):
    middle = len(numbers) // 2
    return numbers[middle - 1:middle + 1]

def get_first_last(numbers: list[int]):
    return numbers[0], numbers[-1]

def extend_list(numbers: list[int]):
    numbers.extend(numbers)
    return numbers

def sort_list_ascending(numbers: list[int]):
    return sorted(numbers)

def sort_list_descending(numbers: list[int]):
    return sorted(numbers, reverse=True)

def get_cubes(numbers: list[int]):
    return [x**3 for x in numbers]

def main():
    numbers = capture_numbers()

    middle_sublist = get_middle_sublist(numbers)
    print("Middle sublist:", middle_sublist)

    first, last = get_first_last(numbers)
    print("First and last element:", first, last)

    extended_list = extend_list(numbers)
    print("Extended list:", extended_list)

    sorted_asc = sort_list_ascending(numbers)
    print("List sorted ascending:", sorted_asc)

    sorted_desc = sort_list_descending(numbers)
    print("List sorted descending:", sorted_desc)

    cubes = get_cubes(numbers)
    print("Cubes of the list elements:", cubes)

if __name__ == "__main__":
    main()
