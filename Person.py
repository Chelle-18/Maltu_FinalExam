class Person:
    def __init__(self, name, age, address):
        """Constructor to initialize name, age, and address."""
        self.__name = name
        self.__age = age
        self.__address = address

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Getter for age
    def get_age(self):
        return self.__age

    # Setter for age
    def set_age(self, age):
        if age >= 0:  # Validate that age is non-negative
            self.__age = age
        else:
            raise ValueError("Age must be a non-negative number.")

    # Getter for address
    def get_address(self):
        return self.__address

    # Setter for address
    def set_address(self, address):
        self.__address = address


# Example usage
person = Person("Jochelle",19, "42 Aurora Hill")
print("Name:", person.get_name())  # Output: Name: John Doe
print("Age:", person.get_age())    # Output: Age: 28
print("Address:", person.get_address())  # Output: Address: 123 Main St

# Update attributes using setter methods
person.set_name("Jaja")
person.set_age(19)
person.set_address("456 Asin")
print("Updated Name:", person.get_name())  # Output: Updated Name: Jane Doe
print("Updated Age:", person.get_age())    # Output: Updated Age: 30
print("Updated Address:", person.get_address())  # Output: Updated Address: 456 Oak St
