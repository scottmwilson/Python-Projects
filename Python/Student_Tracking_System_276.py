import tkinter as tk
import sqlite3

# Create a database connection
connection = sqlite3.connect('students.db')
cursor = connection.cursor()

# Create a table to store student data if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        phone_number TEXT,
        email TEXT,
        current_course TEXT
    )
''')

# Create the main window
root = tk.Tk()
root.title("Student Tracking")

# Create the form labels and input fields
tk.Label(root, text="First Name").grid(row=0, column=0)
first_name_entry = tk.Entry(root)
first_name_entry.grid(row=0, column=1)

tk.Label(root, text="Last Name").grid(row=1, column=0)
last_name_entry = tk.Entry(root)
last_name_entry.grid(row=1, column=1)

tk.Label(root, text="Phone Number").grid(row=2, column=0)
phone_number_entry = tk.Entry(root)
phone_number_entry.grid(row=2, column=1)

tk.Label(root, text="Email").grid(row=3, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=3, column=1)

tk.Label(root, text="Current Course").grid(row=4, column=0)
current_course_entry = tk.Entry(root)
current_course_entry.grid(row=4, column=1)

# Define a function to submit the form data to the database
def submit_form():
    # Get the form data
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    phone_number = phone_number_entry.get()
    email = email_entry.get()
    current_course = current_course_entry.get()
    
    # Insert the data into the database
    cursor.execute('''
        INSERT INTO students (first_name, last_name, phone_number, email, current_course)
        VALUES (?, ?, ?, ?, ?)
    ''', (first_name, last_name, phone_number, email, current_course))
    
    # Clear the form fields
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    phone_number_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    current_course_entry.delete(0, tk.END)
    
    # Commit the changes to the database
    connection.commit()
    
# Add a submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=5, column=0, columnspan=2)

# Define a function to delete a selected student from the database
def delete_student():
    # Get the selected student ID from the listbox
    selected_student = student_listbox.curselection()
    if selected_student:
        student_id = student_listbox.get(selected_student[0])[0]
        
        # Delete the student from the database
        cursor.execute('DELETE FROM students WHERE id=?', (student_id,))
        
        # Commit the changes to the database
        connection.commit()
        
        # Refresh the listbox
        display_students()
    
# Add a delete button
delete_button = tk.Button(root, text="Delete Selected", command=delete_student)
delete_button.grid(row=6, column=0, columnspan=2)

# Create the listbox to display student data
student_listbox = tk.Listbox(root, width=60)
student_listbox.grid(row=7, column=0, columnspan=2)

# Define a function to display
