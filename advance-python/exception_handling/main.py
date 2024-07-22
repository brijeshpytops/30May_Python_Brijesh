"""
Exception handling in Python is a robust way to manage errors gracefully and maintain the normal flow of a program. Python uses the try, except, else, and finally blocks to handle exceptions.

Basic Structure
try block: Wraps the code that might raise an exception.
except block: Catches and handles the exception.
else block: Executes if the try block doesn't raise an exception.
finally block: Always executes, regardless of whether an exception was raised or not.

Benefits of Exception Handling in Python
Improved Program Stability

Graceful Error Handling: Exception handling allows your program to catch errors and handle them without crashing. This keeps your program running and can provide meaningful feedback to the user.
Continuity: Code outside the try block can continue to execute even if an error occurs, maintaining the flow of the application.
Enhanced Readability and Maintenance

Clear Separation of Error-Prone Code: Using try and except blocks separates the main logic from error-handling logic, making the code more readable and maintainable.
Simplifies Complex Error Handling: By isolating error-prone sections, developers can focus on core logic without worrying about handling exceptions in multiple places.
Specific Error Handling

Catch Specific Errors: Python allows catching specific exceptions, enabling precise control over different types of errors and how each should be handled.
Detailed Error Messages: Provides detailed error information, which can be used to give more informative messages to users or logs, helping in troubleshooting.
Resource Management

Automated Resource Cleanup: Using finally blocks or context managers (like the with statement) ensures that resources such as file handles or network connections are properly released, even if an error occurs.
Improves Debugging

Traceback Information: Python provides traceback information when an exception is raised, which helps in pinpointing the exact location and cause of the error during debugging.
Logging: Integrating exception handling with logging helps in capturing and recording the state of the program at the time of the exception, aiding in post-mortem analysis.
Flexibility in Handling Multiple Exceptions

Multiple Exception Types: You can handle multiple exceptions differently within the same try block, providing more granular control over various error scenarios.
Custom Exceptions: Python allows you to define custom exceptions, which can be tailored to the specific needs of your application for more nuanced error handling.
Prevents Unnecessary Program Termination

Avoids Crashes: By catching and handling exceptions, you can avoid abrupt termination of the program and provide a chance to correct the error or take alternative actions.
Fallback Mechanisms: Allows implementation of fallback mechanisms or default behaviors when an error occurs, improving the robustness of the application.
Supports Clean-Up Operations

finally Block: The finally block ensures that cleanup code is always executed, regardless of whether an exception was raised or not, making sure that resources are properly managed.
Simplifies Code

Eliminates Nested Conditionals: Without exception handling, error checks often require deeply nested conditionals. Exception handling flattens this structure, making the code simpler and easier to follow.
Enhances User Experience

User-Friendly Error Messages: Proper handling of exceptions allows you to provide users with clear, actionable error messages instead of generic program crashes.
Graceful Degradation: Ensures that the application can degrade gracefully in case of unexpected issues, improving user trust and satisfaction.
"""

# print("start")
# a = int(input("Enter a num a: "))
# b = int(input("Enter a num b: "))
# a = a/b # ZeroDivisionError: division by zero
# print(a) # NameError: name 'a' is not defined
# print("end")

# print("start")
# try:
#     a = int(input("Enter a num a: "))
#     b = int(input("Enter a num b: "))
#     c = 10
#     a = a/b + c # ZeroDivisionError: division by zero
# except NameError:
#     print("Oops! something is not define.")
# except ZeroDivisionError:
#     print("You can not assign 0 for b")
# except ValueError:
#     print("You can not assign string for b or a")
# except Exception as error:
#     print("Error Occured: ", error)

# else:
#     print(a)
# finally:
#     print("I will be execute anyway.")
# print("end")

# bal = 1000
# w = 2000
# assert (w <= bal), "balance insufficent"

# bal = 1000
# w = 2000

# if w > bal:
#     raise ValueError("balance insufficent")