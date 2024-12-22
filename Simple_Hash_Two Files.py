# created 12/22/2024
# ver 1

import tkinter as tk
from tkinter import filedialog, messagebox
import hashlib
import os

# Hashing Function
def calculate_hash(file_path, hash_algorithm):
    hash_func = hashlib.new(hash_algorithm)
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read file: {str(e)}")
        return None

# Compare Files
def compare_files():
    file1 = entry1.get()
    file2 = entry2.get()
    
    if not file1 or not file2:
        messagebox.showwarning("Warning", "Please select both files.")
        return

    hash_algorithms = ["sha256", "sha512"]

    result_text.delete(1.0, tk.END)

    for hash_type in hash_algorithms:
        hash1 = calculate_hash(file1, hash_type)
        hash2 = calculate_hash(file2, hash_type)

        if hash1 and hash2:
            result_text.insert(tk.END, f"{hash_type.upper()} Hash of File 1: {hash1}\n")
            result_text.insert(tk.END, f"{hash_type.upper()} Hash of File 2: {hash2}\n\n")

            if hash1 == hash2:
                result_text.insert(tk.END, f"{hash_type.upper()} - The files match! ✅\n\n")
            else:
                result_text.insert(tk.END, f"{hash_type.upper()} - The files do not match. ❌\n\n")

# Export Results
def export_results():
    results = result_text.get(1.0, tk.END).strip()
    if not results:
        messagebox.showwarning("Warning", "No results to export.")
        return

    file_path = os.path.join(os.getcwd(), "comparison_results.txt")
    with open(file_path, 'w', encoding='utf-8') as f:  # Ensure UTF-8 encoding
        f.write(results)
    messagebox.showinfo("Success", f"Results exported successfully to {file_path}")

# File Dialog
def browse_file(entry):
    file_path = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, file_path)

# GUI Setup
root = tk.Tk()
root.title("File Hash Comparator")
root.geometry("500x400")
root.resizable(True, True)

frame = tk.Frame(root)
frame.pack(pady=20)

# File 1 Selection
label1 = tk.Label(frame, text="Select First File:")
label1.grid(row=0, column=0, padx=10, pady=10)
entry1 = tk.Entry(frame, width=40)
entry1.grid(row=0, column=1)
btn1 = tk.Button(frame, text="Browse", command=lambda: browse_file(entry1))
btn1.grid(row=0, column=2)

# File 2 Selection
label2 = tk.Label(frame, text="Select Second File:")
label2.grid(row=1, column=0, padx=10, pady=10)
entry2 = tk.Entry(frame, width=40)
entry2.grid(row=1, column=1)
btn2 = tk.Button(frame, text="Browse", command=lambda: browse_file(entry2))
btn2.grid(row=1, column=2)

# Compare Button
compare_btn = tk.Button(root, text="Compare Files", command=compare_files)
compare_btn.pack(pady=10)

# Export Button
export_btn = tk.Button(root, text="Export Results", command=export_results)
export_btn.pack(pady=10)

# Result Display
result_frame = tk.Frame(root)
result_frame.pack(pady=10, fill=tk.BOTH, expand=True)
result_text = tk.Text(result_frame, height=12, width=58)
result_text.pack(pady=10, fill=tk.BOTH, expand=True)

root.mainloop()
