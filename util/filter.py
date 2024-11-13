def filter_list(input_list, condition):
    """
    Filters elements in a list based on a given condition.

    Parameters:
        input_list (list): The list to filter.
        condition (function): A function that takes an element as input and returns True if it meets the condition.

    Returns:
        list: A new list containing elements that satisfy the condition.
    """
    return [item for item in input_list if condition(item)]
