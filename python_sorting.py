def sort_list(input_list):
    """
    Sorts a list in ascending order.

    Args:
        input_list (list): List of elements to sort.

    Returns:
        list: Sorted list.
    """
    return sorted(input_list)

if __name__ == "__main__":
    sample_list = [5, 2, 9, 1, 5, 6]
    print("Original list:", sample_list)
    sorted_list = sort_list(sample_list)
    print("Sorted list:", sorted_list)