from typing import Dict


class HistoryDict:
    def __init__(self, hist_dict: Dict = None):
        """
        Initialize a HistoryDict object.

        Args:
            hist_dict (Dict, optional): Initial dictionary to initialize the HistoryDict with. Defaults to None.
        """
        if hist_dict is None:
            self.hist_dict = {}  # If no initial dictionary is provided, create an empty dictionary.
        else:
            self.hist_dict = hist_dict  # Otherwise, initialize with the provided dictionary.

        self.changed_keys = []  # Initialize a list to keep track of changed keys.

    def set_value(self, key: (str, int), item: (str, int)):
        """
        Set a key-value pair in the history dictionary and track the changed keys.

        Args:
            key (Tuple[str, int]): Key to set in the history dictionary.
            item (Tuple[str, int]): Value to associate with the key.

        Returns:
            None
        """
        self.hist_dict[key] = item  # Set the key-value pair in the history dictionary.

        if key in self.changed_keys:
            self.changed_keys.remove(key)  # Remove the key from changed_keys if it was already present.

        self.changed_keys.append(key)  # Add the key to the list of changed keys.

        if len(self.changed_keys) > 5:
            del self.changed_keys[0]  # If the list exceeds 5 elements, remove the oldest key.

    def get_history(self):
        """
        Get the list of changed keys.

        Returns:
            List: List of changed keys.
        """
        return self.changed_keys  # Return the list of changed keys.
