from typing import List


def split_by_index(s: str, indexes: List[int]) -> List[str]:
    """
    Split a string `s` into substrings based on the specified list of indexes.

    Args:
        s (str): The input string to split.
        indexes (List[int]): A list of integers representing the indexes where the string should be split.

    Returns:
        List[str]: A list of substrings obtained by splitting the input string at the specified indexes.
    """
    split_list = []  # Initialize an empty list to store the split substrings.
    previous_index = 0  # Initialize the previous index as 0.

    # Iterate through each index in the list of indexes.
    for current_index in indexes:
        # If the current index is greater than the length of the string, break the loop.
        if current_index > len(s):
            break
        # Append the substring from the previous index to the current index to the split list.
        split_list.append(s[previous_index:current_index])
        # Update the previous index to the current index for the next iteration.
        previous_index = current_index

    # Append the remaining substring from the last index to the end of the string to the split list.
    split_list.append(s[previous_index:])

    return split_list  # Return the list of split substrings.
