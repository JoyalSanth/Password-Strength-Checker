import re
import tkinter as tk
from tkinter import messagebox, ttk

def check_password_strength(password):
    criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "digits": bool(re.search(r"\d", password)),
        "special_chars": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    }
    
    strength_score = sum(criteria.values())
    
    feedback = []
    if not criteria["length"]:
        feedback.append("Password should be at least 8 characters long.")
    if not criteria["uppercase"]:
        feedback.append("Include at least one uppercase letter.")
    if not criteria["lowercase"]:
        feedback.append("Include at least one lowercase letter.")
    if not criteria["digits"]:
        feedback.append("Include at least one number.")
    if not criteria["special_chars"]:
        feedback.append("Include at least one special character (!@#$%^&* etc.).")
    
    strength_levels = {1: ("Very Weak", "#FF0000"), 2: ("Weak", "#FF4500"), 3: ("Moderate", "#FFD700"), 4: ("Strong", "#32CD32"), 5: ("Very Strong", "#006400")}
    
    return {
        "strength": strength_levels.get(strength_score, ("Very Weak", "#FF0000")),
        "feedback": feedback if feedback else ["Your password is strong!"]
    }

def toggle_password():
    if entry_password.cget('show') == "*":
        entry_password.config(show="")
        show_button.config(text="Hide")
    else:
        entry_password.config(show="*")
        show_button.config(text="Show")

def on_check_password():
    password = entry_password.get()
    result = check_password_strength(password)
    label_strength.config(text=f"Strength: {result['strength'][0]}", fg=result['strength'][1])
    feedback_text.set("\n".join(result['feedback']))

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("500x450")
root.configure(bg="#1E1E1E")
root.resizable(False, False)

style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=5)
style.configure("TLabel", font=("Arial", 12), background="#1E1E1E", foreground="white")

frame_main = tk.Frame(root, bg="#2C3E50", padx=20, pady=20, relief=tk.GROOVE, bd=8)
frame_main.pack(pady=20, padx=20)

title_label = tk.Label(frame_main, text="🔐 Password Strength Checker", font=("Arial", 16, "bold"), bg="#2C3E50", fg="white")
title_label.pack(pady=10)

tk.Label(frame_main, text="Enter Password:", font=("Arial", 12, "bold"), bg="#2C3E50", fg="white").pack(pady=5)
frame = tk.Frame(frame_main, bg="#2C3E50")
frame.pack(pady=5)

entry_password = tk.Entry(frame, show="*", width=30, font=("Arial", 12), bg="#ECF0F1", fg="#2C3E50", relief=tk.FLAT)
entry_password.pack(side=tk.LEFT, padx=5)
entry_password.bind("<KeyRelease>", lambda event: on_check_password())

show_button = ttk.Button(frame, text="Show", command=toggle_password)
show_button.pack(side=tk.LEFT, padx=5)

label_strength = tk.Label(frame_main, text="Strength: ", font=("Arial", 12, "bold"), bg="#2C3E50")
label_strength.pack(pady=5)

feedback_text = tk.StringVar()
label_feedback = tk.Label(frame_main, textvariable=feedback_text, fg="#E74C3C", wraplength=400, justify="left", font=("Arial", 12), bg="#2C3E50")
label_feedback.pack(pady=5)

def close_app():
    root.destroy()

exit_button = ttk.Button(root, text="Exit", command=close_app, style="TButton")
exit_button.pack(pady=10)

root.mainloop()
