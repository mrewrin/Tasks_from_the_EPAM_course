class Bird:
    def __init__(self, name: str):
        """
        Initialize a Bird object with a name.

        Args:
            name (str): The name of the bird.
        """
        self.name = name

    def fly(self):
        """
        Define the fly behavior of the bird.

        Returns:
            str: A string indicating that the bird can fly.
        """
        return f'{self.name} bird can fly'

    def walk(self):
        """
        Define the walk behavior of the bird.

        Returns:
            str: A string indicating that the bird can walk.
        """
        return f'{self.name} bird can walk'


class FlyingBird(Bird):
    ration = "grains"  # Class attribute defining the ration for flying birds.

    def __init__(self, name: str):
        """
        Initialize a FlyingBird object.

        Args:
            name (str): The name of the flying bird.
        """
        super().__init__(name)

    def __str__(self):
        """
        Define the string representation of a FlyingBird object.

        Returns:
            str: A string indicating that the bird can walk and fly.
        """
        return f"{self.name} bird can walk and fly"

    def eat(self):
        """
        Define the eating behavior of the bird.

        Returns:
            str: A string indicating the eating habit of the bird.
        """
        return f'It eats mostly {self.ration}'


class NonFlyingBird(Bird):

    def __init__(self, name: str, ration: str = 'fish'):
        """
        Initialize a NonFlyingBird object.

        Args:
            name (str): The name of the non-flying bird.
            ration (str, optional): The ration of the non-flying bird. Defaults to 'fish'.
        """
        super().__init__(name)
        self.ration = ration

    def __str__(self):
        """
        Define the string representation of a NonFlyingBird object.

        Returns:
            str: A string indicating that the bird can walk and swim.
        """
        return f"{self.name} bird can walk and swim"

    def fly(self):
        """
        Define the fly behavior of the bird (overrides the fly method in Bird).

        Raises:
            AttributeError: Non-flying bird cannot fly.

        Returns:
            str: A string indicating that the bird cannot fly.
        """
        raise AttributeError(f"{self.name} object has no attribute 'fly'")

    def swim(self):
        """
        Define the swim behavior of the bird.

        Returns:
            str: A string indicating that the bird can swim.
        """
        return f'{self.name} bird can swim'

    def eat(self):
        """
        Define the eating behavior of the bird.

        Returns:
            str: A string indicating the eating habit of the bird.
        """
        return f'It eats mostly {self.ration}'


class SuperBird(NonFlyingBird, FlyingBird):
    def __init__(self, name: str):
        """
        Initialize a SuperBird object.

        Args:
            name (str): The name of the super bird.
        """
        super().__init__(name, ration='fish')

    def __str__(self):
        """
        Define the string representation of a SuperBird object.

        Returns:
            str: A string indicating that the bird can walk, swim, and fly.
        """
        return f"{self.name} bird can walk, swim and fly"

    def fly(self):
        """
        Define the fly behavior of the bird (overrides the fly method in NonFlyingBird).

        Returns:
            str: A string indicating that the bird can fly.
        """
        return FlyingBird.fly(self)

    def eat(self):
        """
        Define the eating behavior of the bird.

        Returns:
            str: A string indicating the eating habit of the bird.
        """
        return f'It eats mostly {self.ration}'
