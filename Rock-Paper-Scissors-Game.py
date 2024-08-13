import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import time

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x600")

# Load images
rock_img = ImageTk.PhotoImage(Image.open("img/rock.png"))
paper_img = ImageTk.PhotoImage(Image.open("img/paper.png"))
scissors_img = ImageTk.PhotoImage(Image.open("img/scissors.png"))

# Store references to images to prevent garbage collection
images = {
    "Rock": rock_img,
    "Paper": paper_img,
    "Scissors": scissors_img
}

def animate_winning(choice):
    win_canvas = tk.Canvas(root, width=400, height=400)
    win_canvas.pack()
    
    img = images[choice]  # Get the appropriate image
    
    for i in range(10):  # animate 10 frames
        win_canvas.delete("all")
        win_canvas.create_image(200, 200, image=img)
        root.update()
        time.sleep(0.20)  # pause for a short duration to create the animation effect
    
    win_canvas.destroy()

def play(choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    result = ""
    if choice == computer_choice:
        result = "It's a tie!"
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Paper" and computer_choice == "Rock") or \
         (choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
        animate_winning(choice)  # Call the animation function
    else:
        result = "You lose!"
    messagebox.showinfo("Result", f"Your choice: {choice}\nComputer's choice: {computer_choice}\n{result}")

# Create UI elements
tk.Label(root, text="Choose Rock, Paper or Scissors", font=("Helvetica", 16)).pack(pady=20)
tk.Button(root, text="Rock", command=lambda: play("Rock"), height=2, width=15).pack(pady=10)
tk.Button(root, text="Paper", command=lambda: play("Paper"), height=2, width=15).pack(pady=10)
tk.Button(root, text="Scissors", command=lambda: play("Scissors"), height=2, width=15).pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
