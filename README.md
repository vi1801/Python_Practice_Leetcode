# Python Concepts and Examples

## 1. Lists vs. Tuples
**Difference:**  
- **Lists** are mutable, meaning they can be changed (items can be added, removed, or modified).  
- **Tuples** are immutable, which means once they are created, they cannot be altered.

**When to Use:**  
- Use **lists** when you need a collection of items that may change over time (e.g., a shopping cart).
- Use **tuples** for fixed collections of items that shouldn't change (e.g., coordinates).

---

## 2. Dictionary Collisions
**Handling Collisions:**  
A dictionary in Python uses a hash table for storing key-value pairs. When two keys hash to the same index (collision), Python handles this using a technique called **open addressing**. It looks for the next available slot in the array to store the new key-value pair.

---

## 3. Using Sets
**Example Use Case:**  
Sets are useful for storing unique items and performing operations like unions and intersections. For instance, you can use a set to remove duplicate entries from a list:
```python
my_list = [1, 2, 2, 3, 4, 4]
unique_items = set(my_list)  # {1, 2, 3, 4}
```

---

## 4. Advantages of Dictionaries Over Lists
- **Fast Lookups:** Dictionaries provide O(1) average time complexity for lookups by key, while lists require O(n) for searching.
- **Key-Value Pairing:** Dictionaries allow you to store and retrieve data using meaningful keys, enhancing code readability.

---

## 5. Looping Through a List
**Example:**  
To iterate through a list and perform an operation on each element:
```python
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number * 2)  # Outputs: 2, 4, 6, 8, 10
```

---

## 6. Break and Continue Statements
- **`break`:** Exits the loop entirely.
- **`continue`:** Skips the current iteration and moves to the next one.

**Example:**
```python
for number in range(10):
    if number == 5:
        break  # Stops the loop when number is 5
    print(number)
```

---

## 7. Handling Multiple Conditions
You can handle multiple conditions in an if-else statement using `elif`:
```python
if condition1:
    # Code for condition1
elif condition2:
    # Code for condition2
else:
    # Code if neither condition is met
```

---

## 8. For Loop vs. While Loop
**For Loop:**  
Used when the number of iterations is known.  
**Example:**
```python
for i in range(5):  # Iterates 5 times
    print(i)
```

**While Loop:**  
Used when the number of iterations is not known.  
**Example:**
```python
count = 0
while count < 5:  # Continues until count is no longer less than 5
    print(count)
    count += 1
```

---

## 9. Defining Functions
**Definition Example:**
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Outputs: Hello, Alice!
```

---

## 10. Using *args and **kwargs
- **`*args`:** Allows you to pass a variable number of positional arguments to a function.
- **`**kwargs`:** Allows you to pass a variable number of keyword arguments.

**Example:**
```python
def example_function(*args, **kwargs):
    print(args)    # Tuple of positional arguments
    print(kwargs)  # Dictionary of keyword arguments

example_function(1, 2, 3, key1="value1", key2="value2")
```

---

## 11. Lambda Functions
**Use Case:**  
Lambda functions are useful for small, throwaway functions, especially when you need to pass a function as an argument.  
**Example:**
```python
double = lambda x: x * 2
print(double(5))  # Outputs: 10
```

---

## 12. Variable Scope
**Scope in Functions:**  
Variables defined inside a function have local scope, meaning they are not accessible outside the function.  
**Performance:**  
Minimizing the use of global variables can improve performance and reduce complexity in your code.

---

## 13. Four Pillars of OOP
- **Encapsulation:** Bundling data and methods within classes.
    ```python
    class Example:
        def __init__(self, value):
            self.__value = value  # Private variable

    obj = Example(10)
    ```

- **Inheritance:** Deriving new classes from existing ones.
    ```python
    class Parent:
        pass

    class Child(Parent):
        pass
    ```

- **Polymorphism:** Same method behaving differently across different classes.
    ```python
    class Dog:
        def sound(self):
            return "Woof!"

    class Cat:
        def sound(self):
            return "Meow!"

    for animal in (Dog(), Cat()):
        print(animal.sound())  # Outputs: Woof! Meow!
    ```

- **Abstraction:** Hiding complex implementation details.
    ```python
    from abc import ABC, abstractmethod

    class AbstractClass(ABC):
        @abstractmethod
        def abstract_method(self):
            pass
    ```

---

## 14. Errors vs. Exceptions
**Difference:**  
- **Error:** Generally indicates a serious problem (e.g., syntax error).
- **Exception:** Represents an expected issue that can be caught and handled (e.g., file not found).

---

## 15. Error Handling in File I/O
**Implementation Example:**
```python
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print(f"An error occurred: {e}")
```

---

## 16. Custom Exceptions
Custom exceptions are user-defined exceptions that extend the base Exception class.  
**Use Case:** When you need to raise errors specific to your application's domain.
```python
class CustomError(Exception):
    pass
```

---

## 17. Using Finally
The `finally` block is executed after the try-except block, regardless of whether an exception was raised or not.  
**Example:**
```python
try:
    # Code that may cause an exception
    pass
except Exception as e:
    print(e)
finally:
    print("This will always execute.")
```

---

Feel free to modify or expand any of the sections to better fit your project or personal style!
