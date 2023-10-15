# Employee Management System

This Python script demonstrates a simple employee management system using object-oriented programming. It defines three classes: `emp`, `tcs`, and `tcs_sales`, each representing an employee type with different properties and behaviors.

## Usage

1. Create employee instances by providing their ID, name, and initial salary:

```python
e1 = tcs(23, "sandeep", 34000)
e2 = tcs_sales(55, "kuldeep", 67000)
```

2. Use the methods and attributes of these employee objects to demonstrate their behaviors and properties.

## Features

### `emp` Class

- `__init__(self, ID, Name, Salary)`: Initializes an employee with an ID, name, and salary.

- `show()`: Displays the ID, name, and salary of the employee.

- `update(new_name)`: Updates the employee's name.

### `tcs` Class

- Inherits from the `emp` class.

- Overrides the `show()` method to provide a specialized implementation.

- `salary_hike()`: Increases the salary of a TCS employee by 5%.

### `tcs_sales` Class

- Inherits from the `tcs` class.

- Overrides the `show()` method to provide a specialized implementation.

- `salary_inc()`: Increases the salary of a TCS sales employee by an additional 10% after the 5% hike provided by the `tcs` class.

## Example

Here's an example of how to use this script:

1. Create instances of `tcs` and `tcs_sales` employees.

2. Display the initial employee details using the `show()` method.

3. Apply a salary hike using the appropriate method.

4. Display the updated employee details.

## Note

This is a basic implementation for educational purposes. In real-world applications, you may want to consider more comprehensive employee management features, such as employee records, a database, and additional functionality like promotions and role changes.
