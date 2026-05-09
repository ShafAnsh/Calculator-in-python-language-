import tkinter as tk
from tkinter import ttk, messagebox
import math
import numpy as np
import statistics

# Calculation functions

def safe_float(s):
    try:
        return float(s)
    except:
        raise ValueError("Invalid numeric input")

def basic_math(op, a, b):
    if op == "Addition": return a + b
    if op == "Subtraction": return a - b
    if op == "Multiplication": return a * b
    if op == "Division":
        if b == 0: raise ZeroDivisionError("Division by zero")
        return a / b

def algebra_quadratic(a, b, c):
    if a == 0: raise ValueError("Coefficient a cannot be 0 for quadratic")
    d = b**2 - 4*a*c
    if d < 0: return "No real roots"
    r1 = (-b + math.sqrt(d)) / (2*a)
    r2 = (-b - math.sqrt(d)) / (2*a)
    return f"{r1}, {r2}"

def algebra_linear(a, b):
    if a == 0: raise ValueError("Coefficient a cannot be 0 for linear equation")
    return -b / a

def matrix_from_entries(entries):
    try:
        vals = [float(e.get()) for e in entries]
        return np.array([[vals[0], vals[1]], [vals[2], vals[3]]])
    except Exception:
        raise ValueError("Matrix entries must be numeric")

def matrix_add(m1, m2): return m1 + m2
def matrix_mul(m1, m2): return np.dot(m1, m2)
def matrix_det(m): return float(np.linalg.det(m))

def geometry_area_circle(r):
    if r < 0: raise ValueError("Radius cannot be negative")
    return math.pi * r * r

def geometry_area_rectangle(l, w):
    if l < 0 or w < 0: raise ValueError("Length/width cannot be negative")
    return l * w

def geometry_area_triangle(b, h):
    if b < 0 or h < 0: raise ValueError("Base/height cannot be negative")
    return 0.5 * b * h

def unit_convert(op, v):
    if op == "cm to m": return v / 100.0
    if op == "m to cm": return v * 100.0
    if op == "Celsius to Fahrenheit": return (v * 9/5) + 32
    if op == "Fahrenheit to Celsius": return (v - 32) * 5/9

def number_system_convert(op, n):
    if n < 0: raise ValueError("Only non-negative integers supported")
    if op == "Decimal to Binary": return bin(n)[2:]
    if op == "Decimal to Octal": return oct(n)[2:]
    if op == "Decimal to Hexadecimal": return hex(n)[2:].upper()

def stats_calc(op, nums):
    if len(nums) == 0: raise ValueError("No numbers provided")
    if op == "Mean": return statistics.mean(nums)
    if op == "Median": return statistics.median(nums)
    if op == "Mode": return statistics.mode(nums)

def trig_calc(op, angle_deg):
    rad = math.radians(angle_deg)
    if op == "Sine": return math.sin(rad)
    if op == "Cosine": return math.cos(rad)
    if op == "Tangent":
        cosv = math.cos(rad)
        if abs(cosv) < 1e-12: raise ValueError("Tangent undefined for this angle")
        return math.tan(rad)

# Helper UI functions

def show_result(value):
    messagebox.showinfo("Result", f"{value}")

def show_error(e):
    messagebox.showerror("Error", f"{e}")

# GUI Setup and Styling

root = tk.Tk()
root.title("Advanced Styled Calculator")
root.geometry("900x700")
root.resizable(False, False)

style = ttk.Style()

# Use a built-in theme and then customize

style.theme_use("clam")

# Colors and fonts
        
BG = "#2B2F3A"
TAB_BG = "#3B4252"
ACCENT = "#88C0D0"
BTN_BG = "#5E81AC"
FG = "#ECEFF4"
ENTRY_BG = "#ECEFF4"

root.configure(bg=BG)
style.configure("TNotebook", background=BG, borderwidth=0)
style.configure("TNotebook.Tab", background=TAB_BG, foreground=FG, padding=(12, 8), font=("Segoe UI", 10, "bold"))
style.map("TNotebook.Tab", background=[("selected", ACCENT)], foreground=[("selected", "#1B1F24")])

style.configure("TFrame", background=BG)
style.configure("TLabel", background=BG, foreground=FG, font=("Segoe UI", 11))
style.configure("TButton", background=BTN_BG, foreground=FG, font=("Segoe UI", 10, "bold"), padding=8)
style.map("TButton", background=[("active", ACCENT)])

style.configure("TEntry", fieldbackground=ENTRY_BG, foreground="#1B1F24", font=("Segoe UI", 11))

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both", padx=12, pady=12)

# Utility to create labeled entry

def labeled_entry(parent, label_text):
    frame = ttk.Frame(parent)
    lbl = ttk.Label(frame, text=label_text)
    ent = ttk.Entry(frame, width=30)
    lbl.pack(anchor="w", pady=(0,4))
    ent.pack(fill="x")
    return frame, ent

# Basic Mathematics Tab

tab_math = ttk.Frame(notebook, padding=16)
notebook.add(tab_math, text="Basic Mathematics")

f1, ent_a = labeled_entry(tab_math, "First number")
f1.pack(fill="x", pady=6)
f2, ent_b = labeled_entry(tab_math, "Second number")
f2.pack(fill="x", pady=6)

btn_frame = ttk.Frame(tab_math)
btn_frame.pack(pady=12)

def math_action(op):
    try:
        a = safe_float(ent_a.get())
        b = safe_float(ent_b.get())
        res = basic_math(op, a, b)
        show_result(res)
    except Exception as e:
        show_error(e)

for i, op in enumerate(["Addition", "Subtraction", "Multiplication", "Division"]):
    ttk.Button(btn_frame, text=op, width=18, command=lambda o=op: math_action(o)).grid(row=0, column=i, padx=6, pady=6)

# Algebra Tab

tab_alg = ttk.Frame(notebook, padding=16)
notebook.add(tab_alg, text="Algebra")

fa, ent_aa = labeled_entry(tab_alg, "Coefficient a")
fa.pack(fill="x", pady=6)
fb, ent_bb = labeled_entry(tab_alg, "Coefficient b")
fb.pack(fill="x", pady=6)
fc, ent_cc = labeled_entry(tab_alg, "Coefficient c (for quadratic)")
fc.pack(fill="x", pady=6)

alg_frame = ttk.Frame(tab_alg)
alg_frame.pack(pady=12)

def alg_quadratic_action():
    try:
        a = safe_float(ent_aa.get()); b = safe_float(ent_bb.get()); c = safe_float(ent_cc.get())
        res = algebra_quadratic(a, b, c)
        show_result(res)
    except Exception as e:
        show_error(e)

def alg_linear_action():
    try:
        a = safe_float(ent_aa.get()); b = safe_float(ent_bb.get())
        res = algebra_linear(a, b)
        show_result(res)
    except Exception as e:
        show_error(e)

ttk.Button(alg_frame, text="Quadratic Roots", width=20, command=alg_quadratic_action).grid(row=0, column=0, padx=8, pady=6)
ttk.Button(alg_frame, text="Solve Linear ax+b=0", width=20, command=alg_linear_action).grid(row=0, column=1, padx=8, pady=6)

# Matrix Operations Tab

tab_mat = ttk.Frame(notebook, padding=16)
notebook.add(tab_mat, text="Matrix Operations")

ttk.Label(tab_mat, text="Matrix entries are entered row-wise for 2x2 matrices").pack(anchor="w", pady=(0,8))

mat_frame = ttk.Frame(tab_mat)
mat_frame.pack(fill="x", pady=6)

# Matrix 1 entries

m1_frame = ttk.LabelFrame(mat_frame, text="Matrix 1", padding=10)
m1_frame.grid(row=0, column=0, padx=8, pady=6, sticky="n")
m1_entries = []
for i in range(4):
    e = ttk.Entry(m1_frame, width=8)
    e.grid(row=i//2, column=i%2, padx=6, pady=6)
    m1_entries.append(e)

# Matrix 2 entries

m2_frame = ttk.LabelFrame(mat_frame, text="Matrix 2", padding=10)
m2_frame.grid(row=0, column=1, padx=8, pady=6, sticky="n")
m2_entries = []
for i in range(4):
    e = ttk.Entry(m2_frame, width=8)
    e.grid(row=i//2, column=i%2, padx=6, pady=6)
    m2_entries.append(e)

def mat_action(op):
    try:
        m1 = matrix_from_entries(m1_entries)
        if op in ("Addition", "Multiplication"):
            m2 = matrix_from_entries(m2_entries)
        else:
            m2 = None
        if op == "Addition": res = matrix_add(m1, m2)
        elif op == "Multiplication": res = matrix_mul(m1, m2)
        elif op == "Determinant": res = matrix_det(m1)
        show_result(res)
    except Exception as e:
        show_error(e)

mat_btn_frame = ttk.Frame(tab_mat)
mat_btn_frame.pack(pady=12)
for i, op in enumerate(["Addition", "Multiplication", "Determinant"]):
    ttk.Button(mat_btn_frame, text=op, width=18, command=lambda o=op: mat_action(o)).grid(row=0, column=i, padx=8, pady=6)

# Geometry Tab

tab_geo = ttk.Frame(notebook, padding=16)
notebook.add(tab_geo, text="Geometry")

g1f, ent_g1 = labeled_entry(tab_geo, "Primary value (radius / length / base)")
g1f.pack(fill="x", pady=6)
g2f, ent_g2 = labeled_entry(tab_geo, "Secondary value (width / height) if needed")
g2f.pack(fill="x", pady=6)

def geo_action(op):
    try:
        if op == "Area of Circle":
            r = safe_float(ent_g1.get()); res = geometry_area_circle(r)
        elif op == "Area of Rectangle":
            l = safe_float(ent_g1.get()); w = safe_float(ent_g2.get()); res = geometry_area_rectangle(l, w)
        elif op == "Area of Triangle":
            b = safe_float(ent_g1.get()); h = safe_float(ent_g2.get()); res = geometry_area_triangle(b, h)
        show_result(res)
    except Exception as e:
        show_error(e)

for i, op in enumerate(["Area of Circle", "Area of Rectangle", "Area of Triangle"]):
    ttk.Button(tab_geo, text=op, width=22, command=lambda o=op: geo_action(o)).pack(pady=6)

# Unit Converter Tab

tab_unit = ttk.Frame(notebook, padding=16)
notebook.add(tab_unit, text="Unit Converter")

uf, ent_u = labeled_entry(tab_unit, "Enter value to convert")
uf.pack(fill="x", pady=6)

def unit_action(op):
    try:
        v = safe_float(ent_u.get())
        res = unit_convert(op, v)
        show_result(res)
    except Exception as e:
        show_error(e)

for op in ["cm to m", "m to cm", "Celsius to Fahrenheit", "Fahrenheit to Celsius"]:
    ttk.Button(tab_unit, text=op, width=26, command=lambda o=op: unit_action(o)).pack(pady=6)

# Number System Tab

tab_num = ttk.Frame(notebook, padding=16)
notebook.add(tab_num, text="Number System")

nf, ent_n = labeled_entry(tab_num, "Enter non-negative integer")
nf.pack(fill="x", pady=6)

def num_action(op):
    try:
        n = int(ent_n.get())
        if n < 0: raise ValueError("Enter a non-negative integer")
        res = number_system_convert(op, n)
        show_result(res)
    except Exception as e:
        show_error(e)

for op in ["Decimal to Binary", "Decimal to Octal", "Decimal to Hexadecimal"]:
    ttk.Button(tab_num, text=op, width=26, command=lambda o=op: num_action(o)).pack(pady=6)

# Statistics Tab

tab_stats = ttk.Frame(notebook, padding=16)
notebook.add(tab_stats, text="Statistics")

sf, ent_s = labeled_entry(tab_stats, "Enter numbers separated by commas")
sf.pack(fill="x", pady=6)

def stats_action(op):
    try:
        raw = ent_s.get().strip()
        if not raw: raise ValueError("Provide comma-separated numbers")
        nums = [safe_float(x) for x in raw.split(",")]
        res = stats_calc(op, nums)
        show_result(res)
    except Exception as e:
        show_error(e)

for op in ["Mean", "Median", "Mode"]:
    ttk.Button(tab_stats, text=op, width=20, command=lambda o=op: stats_action(o)).pack(pady=6)

# Trigonometry Tab

tab_trig = ttk.Frame(notebook, padding=16)
notebook.add(tab_trig, text="Trigonometry")

tf, ent_t = labeled_entry(tab_trig, "Enter angle in degrees")
tf.pack(fill="x", pady=6)

def trig_action(op):
    try:
        angle = safe_float(ent_t.get())
        res = trig_calc(op, angle)
        show_result(res)
    except Exception as e:
        show_error(e)

for op in ["Sine", "Cosine", "Tangent"]:
    ttk.Button(tab_trig, text=op, width=20, command=lambda o=op: trig_action(o)).pack(pady=6)

# Footer and run

footer = ttk.Label(root, text="Advanced Calculator • Basic algebra, matrices, geometry, conversions, stats, trig", anchor="center")
footer.pack(side="bottom", fill="x", pady=8)

root.mainloop()
