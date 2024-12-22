File Hash Comparator:
This Python application allows users to compare the hash values of two files using different hashing algorithms (SHA-256 and SHA-512). It provides a simple graphical user interface (GUI) built with Tkinter for easy interaction. The program calculates and displays the hash values of the selected files and compares them to determine if the files match. Additionally, the comparison results can be exported to a .txt file.

Features:
File Selection: Allows users to browse and select two files for comparison.
Hash Calculation: Computes the hash values of the selected files using SHA-256 and SHA-512 hashing algorithms.
Comparison: Displays whether the hash values of the two files match or not for each algorithm.
Export Results: Provides an option to export the comparison results to a text file.

Requirements:
Python 3.x
Tkinter (for GUI)
hashlib (for hash calculations)

How to Use:
Launch the Program: Run the Python script to open the GUI window.
Select Files: Click on the "Browse" button to select the two files you wish to compare.
Compare Files: After selecting the files, click on "Compare Files" to calculate their hash values.
Export Results: If you'd like to save the results, click on "Export Results". The comparison results will be saved as a text file named comparison_results.txt in the current working directory.

Example Output:
SHA-256 Hash of File 1: <hash_value>
SHA-256 Hash of File 2: <hash_value>
SHA-256 - The files match! ✅
SHA-512 Hash of File 1: <hash_value>
SHA-512 Hash of File 2: <hash_value>
SHA-512 - The files do not match. ❌

Installation:
To use this program, simply clone the repository and run the Python script:

git clone https://github.com/LaelafaceBubbaboo/hash-compare.git
cd Simple_Hash_Two Files
python Simple_Hash_Two Files.py
