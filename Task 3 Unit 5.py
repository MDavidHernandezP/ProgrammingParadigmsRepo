# Import necessary libraries/modules
import tkinter as tk

def button_click_handler():
    print("Button Clicked!")

# Create the main window
window = tk.Tk()
window.title("Event-Oriented Programming")

# Create a button and associate the event handler
button = tk.Button(window, text="Click Me!", command=button_click_handler)
button.pack(padx=20, pady=20)

# I started playing with the buttons XD
button2 = tk.Button(window, text="Don't Click Me!", command=button_click_handler)
button2.pack(padx=20, pady=20)

# Start the main event loop
window.mainloop()