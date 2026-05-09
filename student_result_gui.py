import sys
import subprocess

# ---------- AUTO INSTALL REQUIRED PACKAGES ----------
def install(pkg):
    subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

packages = ["pandas", "openpyxl"]

for p in packages:
    try:
        __import__(p)
    except ImportError:
        install(p)

# ---------- IMPORTS ----------
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

PASS_MARK = 35
data = None
subjects = []

# ---------- FUNCTIONS ----------
def select_excel():
    global data, subjects

    file_path = filedialog.askopenfilename(
        title="Select Excel File",
        filetypes=[("Excel Files", "*.xlsx")]
    )

    if not file_path:
        return

    try:
        data = pd.read_excel(file_path)
        subjects = list(data.columns[2:])  # Dynamic subjects
        status_label.config(text="📄 File Loaded Successfully!", fg="green")
        show_classes()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def calculate_gpa(row):
    return row[subjects].mean()

def show_classes():
    for w in class_frame.winfo_children():
        w.destroy()

    if data is None:
        return

    classes = sorted(data["Class"].unique())
    for cls in classes:
        tk.Button(
            class_frame, text=cls, width=12, bg="#4CAF50", fg="white",
            command=lambda c=cls: show_results(c)
        ).pack(pady=4)

def show_results(selected_class):
    pass_list.delete(0, tk.END)
    fail_list.delete(0, tk.END)

    class_data = data[data["Class"] == selected_class]
    pass_students, fail_students = [], []

    for _, row in class_data.iterrows():
        failed = [s for s in subjects if row[s] < PASS_MARK]
        gpa = calculate_gpa(row)

        if failed:
            fail_students.append((row["Name"], gpa, len(failed), failed))
        else:
            pass_students.append((row["Name"], gpa))

    pass_students.sort(key=lambda x: x[1], reverse=True)
    fail_students.sort(key=lambda x: x[1], reverse=True)

    for p in pass_students:
        pass_list.insert(tk.END, f"{p[0]} | GPA: {p[1]:.2f}")

    for f in fail_students:
        fail_list.insert(
            tk.END,
            f"{f[0]} | GPA: {f[1]:.2f} | Failed: {f[2]} ({', '.join(f[3])})"
        )

    total = len(class_data)
    pass_count = len(pass_students)
    fail_count = len(fail_students)

    pass_label.config(
        text=f"Pass: {pass_count} students | {(pass_count/total)*100:.2f}%"
    )
    fail_label.config(
        text=f"Fail: {fail_count} students | {(fail_count/total)*100:.2f}%"
    )


# ---------- GUI ----------
root = tk.Tk()
root.title("📊 Student Result Management System")
root.geometry("1000x650")
root.config(bg="#f0f0f0")

# --- Sidebar Frame ---
sidebar = tk.Frame(root, width=200, bg="#1e3d59")
sidebar.pack(side=tk.LEFT, fill=tk.Y)

tk.Label(sidebar, text=" MENU", fg="white", bg="#1e3d59",
         font=("Helvetica", 16, "bold")).pack(pady=15, anchor="w")

tk.Button(sidebar, text="📁 Load Excel", bg="#f76c6c", fg="white",
          font=("Arial", 11, "bold"), command=select_excel).pack(fill=tk.X, padx=15, pady=8)

tk.Label(sidebar, text="Classes", fg="#fff", bg="#1e3d59",
         font=("Arial", 12, "underline")).pack(pady=(20, 8), anchor="w", padx=15)

class_frame = tk.Frame(sidebar, bg="#1e3d59")
class_frame.pack(fill=tk.X)

# --- Main Content ---
content = tk.Frame(root, bg="#f0f0f0")
content.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

status_label = tk.Label(content, text="Load a file to begin...", font=("Arial", 12),
                        fg="#555", bg="#f0f0f0")
status_label.pack(pady=5)

result_frame = tk.Frame(content, bg="#f0f0f0")
result_frame.pack(fill=tk.BOTH, expand=True, pady=15)

# Headings
tk.Label(result_frame, text="✅ Pass Students", bg="#6bbf59", fg="white",
         font=("Arial", 12, "bold")).grid(row=0, column=0, sticky="ew")

tk.Label(result_frame, text="❌ Fail Students", bg="#d9534f", fg="white",
         font=("Arial", 12, "bold")).grid(row=0, column=1, sticky="ew")

pass_list = tk.Listbox(result_frame, width=40, height=15, bg="#ffffff")
pass_list.grid(row=1, column=0, padx=8, pady=8)

fail_list = tk.Listbox(result_frame, width=70, height=15, bg="#ffffff")
fail_list.grid(row=1, column=1, padx=8, pady=8)

# Summary
summary_frame = tk.Frame(content, bg="#f0f0f0")
summary_frame.pack(pady=10)

pass_label = tk.Label(summary_frame, text="Pass: 0.00%", font=("Arial", 11), bg="#f0f0f0")
pass_label.pack(side=tk.LEFT, padx=15)

fail_label = tk.Label(summary_frame, text="Fail: 0.00%", font=("Arial", 11), bg="#f0f0f0")
fail_label.pack(side=tk.LEFT, padx=15)

root.mainloop()

