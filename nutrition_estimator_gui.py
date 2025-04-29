import tkinter as tk
from tkinter import messagebox

# 🧠 Smart logic: Indian dishes with estimated nutrition
nutrition_map = {
    "poha": {"calories": 180, "protein": 4.0, "fiber": 1.5},
    "dal chawal": {"calories": 320, "protein": 10.0, "fiber": 3.5},
    "chapati sabzi": {"calories": 300, "protein": 7.5, "fiber": 4.0},
    "idli sambar": {"calories": 270, "protein": 6.0, "fiber": 2.5},
    "upma": {"calories": 200, "protein": 5.0, "fiber": 1.8},
    "paneer tikka": {"calories": 250, "protein": 14.0, "fiber": 0.5},
    "rajma chawal": {"calories": 350, "protein": 11.0, "fiber": 5.0},
    "tea": {"calories": 90, "protein": 1.0, "fiber": 0.0},
    "milk": {"calories": 150, "protein": 6.0, "fiber": 0.0},
    "aloo paratha": {"calories": 330, "protein": 7.5, "fiber": 3.0},
    "maggie": {"calories": 310, "protein": 6.0, "fiber": 2.0}
}

# 🔍 Lookup function
def search_dish():
    dish = entry.get().strip().lower()
    result_text.delete("1.0", tk.END)

    if not dish:
        messagebox.showwarning("Missing Input", "Please enter a dish name.")
        return

    nutrition = nutrition_map.get(dish)

    if nutrition:
        result = (
            f"🍽️ Dish: {dish.title()}\n"
            f"🔸 Calories: {nutrition['calories']} kcal\n"
            f"🔸 Protein: {nutrition['protein']} g\n"
            f"🔸 Fiber: {nutrition['fiber']} g\n"
        )
    else:
        result = f"❌ Sorry! No data found for '{dish}'. Try a different Indian dish."

    result_text.insert(tk.END, result)

# 🎨 GUI Layout
root = tk.Tk()
root.title("🍲 Nutrition Estimator (Indian Dishes)")
root.geometry("450x360")
root.configure(bg="#f5f5f5")
root.resizable(False, False)

title = tk.Label(root, text="Nutrition Estimator", font=("Helvetica", 18, "bold"), bg="#f5f5f5", fg="#333")
title.pack(pady=(20, 10))

entry = tk.Entry(root, font=("Arial", 14), width=30)
entry.pack(pady=5)

search_btn = tk.Button(root, text="Search", font=("Arial", 12, "bold"), bg="#2e8b57", fg="white", command=search_dish)
search_btn.pack(pady=10)

result_text = tk.Text(root, height=8, width=45, font=("Courier New", 11), bd=2, relief="solid", fg="#222")
result_text.pack(pady=(5, 15))

footer = tk.Label(root, text="~ Estimates for common Indian dishes ~", font=("Arial", 9), bg="#f5f5f5", fg="#666")
footer.pack(side=tk.BOTTOM, pady=5)

root.mainloop()
