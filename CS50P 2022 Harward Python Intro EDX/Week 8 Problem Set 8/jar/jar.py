class Jar:
    def __init__(self, capacity=12):
        """
        Initialize a Jar with a specified capacity.

        :param capacity: Maximum number of cookies the jar can hold. Default is 12.
        """
        self.capacity = capacity  # Set the initial capacity
        self.size = 0  # Start with an empty jar

    def __str__(self):
        """
        Return a string representation of the Jar.
        This will display the jar with cookies represented by '🍪' characters.

        :return: A string of '🍪' characters based on the number of cookies in the jar.
        """
        return "🍪" * self.size

    def deposit(self, n):
        """
        Deposit a number of cookies into the jar.

        :param n: Number of cookies to deposit.
        :raises ValueError: If the number of cookies to deposit exceeds the jar's capacity.
        """
        if self.size + n > self.capacity:
            raise ValueError("Deposit error: Adding cookies exceeds jar capacity.")
        self.size += n

    def withdraw(self, n):
        """
        Withdraw a number of cookies from the jar.

        :param n: Number of cookies to withdraw.
        :raises ValueError: If attempting to withdraw more cookies than are present in the jar.
        """
        if n > self.size:
            raise ValueError("Withdraw error: Not enough cookies in the jar.")
        self.size -= n

    @property
    def capacity(self):
        """
        Get the current capacity of the jar.

        :return: The capacity of the jar.
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """
        Set a new capacity for the jar.

        :param capacity: New capacity of the jar.
        :raises ValueError: If the new capacity is less than 1.
        """
        if capacity < 1:
            raise ValueError("Capacity error: Capacity must be at least 1.")
        self._capacity = capacity

    @property
    def size(self):
        """
        Get the current size (number of cookies) in the jar.

        :return: The size of the jar.
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Set the number of cookies in the jar.

        :param size: New size of the jar.
        :raises ValueError: If the new size exceeds the jar's capacity.
        """
        if size > self.capacity:
            raise ValueError("Size error: Size cannot exceed jar capacity.")
        self._size = size


def main():
    """
    Main function to demonstrate the usage of the Jar class.
    """
    jar = Jar()  # Create a new Jar instance with default capacity
    print(jar)  # Print the current state of the jar (empty)

    jar.deposit(1)  # Deposit 1 cookie into the jar
    print(jar)  # Print the jar state

    jar.deposit(3)  # Deposit 3 more cookies
    print(jar)  # Print the jar state

    jar.withdraw(2)  # Withdraw 2 cookies
    print(jar)  # Print the jar state


if __name__ == "__main__":
    main()
