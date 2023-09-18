class Constants:
    def _setattr_(self, key, value):
        if hasattr(self, key):
            raise ValueError(f"Cannot modify constant: {key}")
        else:
            super().__setattr__(key, value)

# Create an instance of the Constants class
constants = Constants()

# Define constants
constants.MY_CONSTANT = 42

# Attempting to change the value will raise an error
try:
    constants.MY_CONSTANT = 99
except ValueError as e:
    print(e)

# Access the constant
print("Constant value:", constants.MY_CONSTANT)






Here's a simple example of defining a constant-like variable and changing its value:

# Define a constant-like variable
MY_CONSTANT = 20

# Attempt to change the value (not recommended)
MY_CONSTANT = 40  # This will generate a warning, but the value will change

# Print the updated value
print("Updated constant value:", MY_CONSTANT)



