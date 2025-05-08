import tkinter as tk
import random

root = tk.Tk()
root.title("Tic-Tac-Toe")
background_color = "darkgrey"
root.configure(bg=background_color)



label = tk.Label(root, text="Winner is ...", font=("Arial", 24),bg=background_color, fg="white")  
label.grid(row=3, column=0, columnspan=3)


a = tk.Button(root, text="_", width=10, height=4, font=("Arial", 18))  
a.grid(row=0, column=0)
b = tk.Button(root, text="_", width=10, height=4, font=("Arial", 18))
b.grid(row=0, column=1)
c = tk.Button(root, text="_", width=10, height=4, font=("Arial", 18))
c.grid(row=0, column=2)
d = tk.Button(root, text="_", width=10, height=4, font=("Arial", 18))
d.grid(row=1, column=0)
e = tk.Button(root, text="_", width=10, height=4, font=("Arial", 18))
e.grid(row=1, column=1)
f = tk.Button(root, text="_", width=10, height=4, font=("Arial", 18))
f.grid(row=1, column=2)
j = tk.Button(root, text="_", width=10, height=4, font=("Arial", 18))
j.grid(row=2, column=0)
h = tk.Button(root, text="_", width=10, height=4, font=("Arial", 18))
h.grid(row=2, column=1)
i = tk.Button(root, text="_", width=10, height=4, font=("Arial", 18))
i.grid(row=2, column=2)

retry = tk.Button(root, text="Retry", width=10, height=2, font=("Arial", 18),bg=background_color,fg='white', command=lambda: [btn.config(text="_") for btn in buttons] + [label.config(text="Winner is ...")]+ [btn.config(state=tk.NORMAL) for btn in buttons])
retry.grid(row=4, column=0, columnspan=3)

buttons = [a, b, c, d, e, f, j, h, i]

winning_combinations = [
        (a, b, c),
        (d, e, f),
        (j, h, i),
        (a, d, j),
        (b, e, h),
        (c, f, i),
        (a, e, i),
        (c, e, j)
    ]

def win_check():
    # Check for a winner
    for combo in winning_combinations:
        if combo[0]["text"] == combo[1]["text"] == combo[2]["text"] != "_":
            winner = combo[0]["text"]
            label.config(text=f"Winner is {winner}")
            for btn in buttons:
                btn.config(state=tk.DISABLED)
            return True

    # Check for a tie
    if all(btn["text"] != "_" for btn in buttons):
        label.config(text="It's a Tie!")
        return True

    return False

def ai_move():
    # Check if AI can win in the next move
    for combo in winning_combinations:
        values = [btn["text"] for btn in combo]
        if values.count("O") == 2 and values.count("_") == 1:
            combo[values.index("_")].config(text="O")
            win_check()
            return

    # Check if the player is about to win and block them
    for combo in winning_combinations:
        values = [btn["text"] for btn in combo]
        if values.count("X") == 2 and values.count("_") == 1:
            combo[values.index("_")].config(text="O")
            win_check()
            return

    # Take the center if available
    if e["text"] == "_":
        e.config(text="O")
        win_check()
        return

    # Take a corner if available
    corners = [a, c, j, i]
    available_corners = [btn for btn in corners if btn["text"] == "_"]
    if available_corners:
        random.choice(available_corners).config(text="O")
        win_check()
        return

    # Otherwise, pick a random move
    available_buttons = [btn for btn in buttons if btn["text"] == "_"]
    if available_buttons:
        random.choice(available_buttons).config(text="O")
        win_check()

def player_move(button):
    if button["text"] == "_":
        button.config(text="X")
        if not win_check():
            ai_move()


for btn in buttons:
    btn.config(command=lambda b=btn: player_move(b))

root.mainloop()