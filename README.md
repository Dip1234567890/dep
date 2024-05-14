This code creates a functional scientific calculator with a GUI, supporting basic arithmetic, advanced mathematical functions, and constants.


1. Importing Libraries:

The code imports the tkinter library for creating the graphical user interface.
The math library is imported to use mathematical functions and constants.
Click Event Handler:

2. The click function handles button click events on the calculator.
It retrieves the text of the clicked button and the current value in the entry widget.
Depending on the button text, it performs various operations:
Evaluates the expression for the equals (=) button.
Clears the screen for the clear (C) button.
Deletes the last character for the backspace (BS) button.
Performs mathematical operations like square root, trigonometric functions, natural logarithm, exponentiation, and cube root.
Appends mathematical constants and results of functions to the current expression.
Uses a try-except block to catch and handle any exceptions during evaluation.
Creating the Main Application Window:

3. The root object is created as the main application window using Tk().
The window size is set to 520x685 pixels and its minimum and maximum sizes are defined to prevent resizing.
Entry Widget for Display:

4. A StringVar object scvalue is created to hold the current value of the calculator's display.
An entry widget screen is created to display scvalue, styled with a large font, and packed to fill the horizontal space.
Button Configuration:

5. A list buttons defines the symbols for all calculator buttons.
The pack_buttons function creates and packs buttons into frames. It binds the click event of each button to the click function.
The buttons are divided into rows of six symbols each.
Creating Button Rows:

6. The rows list comprehension divides the buttons list into sublists, each containing six buttons.
For each row in rows, a new frame is created, and the buttons are packed into the frame.
Starting the Main Event Loop:

7. The root.mainloop() call starts the Tkinter main event loop, making the application window responsive to user interactions.
