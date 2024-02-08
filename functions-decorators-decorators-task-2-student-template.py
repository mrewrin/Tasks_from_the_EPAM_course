import time

def log(func):
    """
    A decorator function to log information about the execution of another function.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The wrapped function.
    """
    def wrapper(*args, **kwargs):
        """
        Wrapper function that adds logging functionality around the decorated function.

        Args:
            *args: Positional arguments passed to the decorated function.
            **kwargs: Keyword arguments passed to the decorated function.

        Returns:
            Any: Result of the decorated function.
        """
        start_time = time.time()  # Record the start time of the function execution.
        result = func(*args, **kwargs)  # Call the decorated function.
        end_time = time.time()  # Record the end time of the function execution.

        # Construct a log message with information about the function call and execution time.
        log_message = (
            f"{func.__name__}; args: {', '.join([f'{arg[0]}={arg[1]}' for arg in zip(func.__code__.co_varnames, args)])}; "
            f"kwargs: {', '.join([f'{key}={value}' for key, value in kwargs.items()])}; "
            f"execution time: {end_time - start_time:.2f} sec."
        )

        # Write the log message to a file named "log.txt".
        with open("log.txt", "a") as log_file:
            log_file.write(log_message + "\n")

        return result  # Return the result of the decorated function.

    return wrapper  # Return the wrapper function.

