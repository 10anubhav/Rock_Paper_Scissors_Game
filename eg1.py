import tkinter as tk
import random

def toggle_dark_mode():
    global dark_mode
    dark_mode = not dark_mode
    update_colors()

def update_colors():
    bg_color = "grey" if dark_mode else "white"
    fg_color = "white" if dark_mode else "black"
    button_bg = "light green" if dark_mode else "light blue"
    button_fg = "white" if dark_mode else "black"
    label_bg = "#222" if dark_mode else "white"
    
    root.config(bg=bg_color)
    choose_label.config(bg=label_bg, fg=fg_color)
    frame.config(bg=bg_color)
    player_label.config(bg=label_bg, fg=fg_color)
    vs_label.config(bg=label_bg, fg=fg_color)
    computer_label.config(bg=label_bg, fg=fg_color)
    result_value_label.config(bg=label_bg, fg=fg_color)
    result_value_label.config(bg=label_bg, fg=fg_color)
    dark_mode_button.config(bg=button_bg, fg=button_fg)
    reset_button.config(bg=button_bg, fg=button_fg)
    b1.config(bg=button_bg, fg=button_fg)
    b2.config(bg=button_bg, fg=button_fg)
    b3.config(bg=button_bg, fg=button_fg)

def reset_game():
    global match_result
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    player_label.config(text="Player")
    computer_label.config(text="Computer")
    result_value_label.config(text="")
    match_result = "none"

def play(player_choice):
    global match_result
    c_v = computer_dict[str(random.randint(0, 2))]
    
    if player_choice == c_v:
        match_result = "Tie!"
    elif (player_choice == "Rock" and c_v == "Scissors") or \
         (player_choice == "Paper" and c_v == "Rock") or \
         (player_choice == "Scissors" and c_v == "Paper"):
        match_result = "Player Wins"
    else:
        match_result = "Computer Wins"

    result_value_label.config(text=match_result)
    player_label.config(text=player_choice)
    computer_label.config(text=c_v)
    b1["state"] = "disable"
    b2["state"] = "disable"
    b3["state"] = "disable"

dark_mode = False

root = tk.Tk()
root.geometry("400x400")
root.title("Rock, Paper, Scissors")

computer_dict = {
    "0": "Rock",
    "1": "Paper",
    "2": "Scissors"
}

# Dark mode button
dark_mode_button = tk.Button(root, text="Toggle Dark Mode", command=toggle_dark_mode)
dark_mode_button.pack(pady=10)

# Choose label
choose_label = tk.Label(root, text="Choose any one: Rock, Paper, Scissors", font=("Helvetica", 12, "bold underline"))
choose_label.pack()

# Game frame
frame = tk.Frame(root)
frame.pack()

player_label = tk.Label(frame, text="Player", font=10)
vs_label = tk.Label(frame, text="VS", font="Consolas")
computer_label = tk.Label(frame, text="Computer", font=10)
player_label.pack(side="left")
vs_label.pack(side="left")
computer_label.pack(side="right")

result_value_label = tk.Label(root, text="", font="Consolas", bg="white", width=15, borderwidth=2, relief="solid")
result_value_label.pack(pady=30)

# Button frame
frame1 = tk.Frame(root)
frame1.pack()

b1 = tk.Button(frame1, text="Rock", font=8, width=7, bg="light blue", command=lambda: play("Rock"))
b2 = tk.Button(frame1, text="Paper", font=8, width=7, bg="light blue", command=lambda: play("Paper"))
b3 = tk.Button(frame1, text="Scissors", font=8, width=7, bg="light blue", command=lambda: play("Scissors"))

b1.pack(side='left', padx=10)
b2.pack(side='left', padx=10)
b3.pack(side='left', padx=10)

# Reset button
reset_button = tk.Button(root, text="RESET THE GAME", font=10, fg="red", bg="light grey", command=reset_game)
reset_button.pack(pady=20)

update_colors()  # Set initial colors based on dark mode state
root.mainloop()
