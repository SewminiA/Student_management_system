import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import sys


con = sqlite3.connect("sms_db")
cur = con.cursor()


def sign_up():

    login.destroy()

    def insert_users():

        uname = name_entry.get()
        u_password = password_entry.get()
        uc_password = confirm_password_entry.get()

        if uname == "" or u_password == "" or uc_password == "":
            messagebox.showerror("Error", "Missing information..")

        elif uc_password != u_password:
            messagebox.showerror("Error", "Please enter valid password...")
        elif uc_password == uc_password:
            query = "insert into users(name, password, confirm_password) values('" + name_entry.get() + "', '" + password_entry.get() + "', '" + confirm_password_entry.get() + "')"
            cur.execute(query)
            con.commit()

            messagebox.showinfo("Register user", "You are now user in the system...")

            reset_details()

    global sign
    sign = tk.Tk()
    sign.title("Register for users")
    sign.geometry("480x360")
    sign.configure(bg="#006400")

    name = tk.Label(sign, text="Name : ", font=("Comic Sans MS", 14), bg="#006400", fg="white")
    name.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)

    name_entry = tk.Entry(sign, font=("Comic Sans MS", 14))
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    password = tk.Label(sign, text="Password : ", font=("Comic Sans MS", 14), bg="#006400", fg="white")
    password.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)

    password_entry = tk.Entry(sign, font=("Comic Sans MS", 14), show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    confirm_password = tk.Label(sign, text="Confirm Password : ", font=("Comic Sans MS", 14), bg="#006400", fg="white")
    confirm_password.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)

    confirm_password_entry = tk.Entry(sign, font=("Comic Sans MS", 14), show="*")
    confirm_password_entry.grid(row=2, column=1, padx=10, pady=10)

    def reset_details():
        name_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        confirm_password_entry.delete(0, tk.END)

    submit = tk.Button(sign, text="Submit", font=("Comic Sans MS", 12), command=insert_users)
    submit.grid(row=3, columnspan=2, pady=10)

    reset = tk.Button(sign, text="Reset", font=("Comic Sans MS", 12), command=reset_details)
    reset.grid(row=4, columnspan=2, pady=10)

    login_back = tk.Button(sign, text="Back to login", font=("Comic Sans MS", 12), command=lambda: (sign.destroy(), login_page()))
    login_back.grid(row=5, columnspan=2, pady=10)

    sign.mainloop()


def login_page():
    global login
    login = tk.Tk()
    login.title("Login")
    login.geometry("520x300")
    login.configure(bg="#8B3A62")

    def reset_login():
        name_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

    login_title = tk.Label(login, text="Login", font=("Comic Sans MS", 20, "bold"), bg="#8B3A62", fg="white")
    login_title.grid(row=0, column=0, columnspan=2, pady=(20, 10))

    # UserName
    name_label = tk.Label(login, text="User name:", font=("Comic Sans MS", 14), bg="#8B3A62", fg="white")
    name_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)

    global name_entry
    name_entry = tk.Entry(login, font=("Comic Sans MS", 12), width=25)
    name_entry.grid(row=1, column=1, pady=10, padx=10, sticky=tk.W)

    # Password
    password_label = tk.Label(login, text="Password:", font=("Comic Sans MS", 14), bg="#8B3A62", fg="white")
    password_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)

    global password_entry
    password_entry = tk.Entry(login, font=("Comic Sans MS", 12), show="*", width=25)
    password_entry.grid(row=2, column=1, pady=10, padx=10, sticky=tk.W)

    # Buttons Frame
    buttons_frame = tk.Frame(login, bg="#8B3A62")
    buttons_frame.grid(row=3, column=0, columnspan=2, pady=20)

    login_button = tk.Button(buttons_frame, text="Login", font=("Comic Sans MS", 12), width=10, command=login_success)
    login_button.pack(side=tk.LEFT, padx=10)

    reset_button = tk.Button(buttons_frame, text="Reset", font=("Comic Sans MS", 12), width=10, command=reset_login)
    reset_button.pack(side=tk.LEFT, padx=10)

    reg_button = tk.Button(buttons_frame, text="Sign up", font=("Comic Sans MS", 12), width=10, command=sign_up)
    reg_button.pack(side=tk.LEFT, padx=10)

    exit_button = tk.Button(buttons_frame, text="Exit", font=("Comic Sans MS", 12), width=10, command=sys.exit)
    exit_button.pack(side=tk.RIGHT, padx=10)

    login.mainloop()


def login_success():
    try:
        query = "SELECT * FROM users WHERE name = '" + name_entry.get() + "'"
        cur.execute(query)
        data = cur.fetchone()

        if data is not None:
            store_password = data[2]
            if password_entry.get() == store_password:
                messagebox.showinfo("Welcome", "Login Successful...")

                name_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)

                login.destroy()

                main_display()
            else:
                messagebox.showerror("Error", "Invalid password...")

                name_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Invalid details...")

            name_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
    except sqlite3.Error as e:
        print("Error:", e)
        messagebox.showerror("Database Error", "An error occurred while accessing the database.")


def main_display():
    def get_data():
        query = "SELECT * FROM details"
        cur.execute(query)
        rows = cur.fetchall()

        # Clear existing data in the TreeView
        for item in show_table.get_children():
            show_table.delete(item)

        # Insert new data into the TreeView
        for row in rows:
            show_table.insert('', tk.END, values=row)

    def add_data():
        if Id.get() == "" or name.get() == "" or gender.get() == "":
            messagebox.showerror("Error", "Missing information")
        else:
            query = "insert into details(id,name,gender,enrol_date,grade,test_no,marks) values('" + Id.get() + "', '" + name.get() + "', '" + gender.get() + "', '" + enroll_date.get() + "', '" + grade.get() + "', '" + test_no.get() + "', '" + marks.get() + "')"
            cur.execute(query)
            con.commit()

            messagebox.showinfo("Info", "Details are added.")
            get_data()
            clear_data()

    def clear_data():
        Id.set("")
        name.set("")
        gender.set("")
        enroll_date.set("")
        grade.set("")
        test_no.set("")
        marks.set("")

    def update_data():
        query = "update details set name = '" + name.get() + "',gender =  '" + gender.get() + "', enrol_date ='" + enroll_date.get() + "', test_no = '" + test_no.get() + "', marks =  '" + marks.get() + "' where id = '" + Id.get() + "' "
        cur.execute(query)
        con.commit()
        clear_data()
        get_data()

    def delete_data():
        query = "delete from details where id = '" + Id.get() + "'"
        cur.execute(query)
        con.commit()
        clear_data()
        get_data()

    def get_cursor_show(event):
        cursor_row = show_table.focus()
        content = show_table.item(cursor_row)
        row = content['values']
        Id.set(row[0])
        name.set(row[1])
        gender.set(row[2])
        enroll_date.set(row[3])
        grade.set(row[4])
        test_no.set(row[5])
        marks.set(row[6])

    def search_data():
        search_id = search.get()
        if search_id == "":
            messagebox.showerror("Error", "Please enter an ID to search.")
        else:
            show_table.delete(*show_table.get_children())
            query = "SELECT * FROM details WHERE id = '" + search_id + "'"
            cur.execute(query)
            row = cur.fetchone()
            if row is not None:
                show_table.insert("", tk.END, values=row)
            else:
                messagebox.showinfo("Info", "No student found with the entered ID.")

    def clear_search():
        search.set("")

    window = tk.Tk()
    window.title("Student Management System")
    window.geometry("1237x620")
    color_bg_form = "light green"
    button_bg = "yellow"
    window.configure(bg=color_bg_form)


    title_label = tk.Label(window, text='Student Management System', font=("Comic Sans MS", 30, "bold", "italic"),
                           border=2,
                           relief=tk.GROOVE, bg="green", fg="white")
    title_label.pack(side=tk.TOP, fill=tk.X)

    get_details_Frame = tk.LabelFrame(window, text="Fill Details", font=("Comic Sans MS", 15, "italic"),
                                      bg=color_bg_form,
                                      border=2, relief=tk.GROOVE)
    get_details_Frame.place(x=17, y=70, width=380, height=530)

    show_details_frame = tk.Frame(window, border=2, relief=tk.GROOVE, bg=color_bg_form)
    show_details_frame.place(x=420, y=83, width=800, height=518)

    Id = tk.StringVar()
    name = tk.StringVar()
    gender = tk.StringVar()
    enroll_date = tk.StringVar()
    grade = tk.StringVar()
    test_no = tk.StringVar()
    marks = tk.StringVar()
    search = tk.StringVar()

    id_label = tk.Label(get_details_Frame, text="ID", font=("Comic Sans MS", 12), bg=color_bg_form)
    id_label.grid(row=0, column=0, padx=10, pady=10)

    get_id = tk.Entry(get_details_Frame, bd=2, font=("Comic Sans MS", 12), textvariable=Id)
    get_id.grid(row=0, column=1, padx=10, pady=10)

    name_label = tk.Label(get_details_Frame, text="Name", font=("Comic Sans MS", 12), bg=color_bg_form)
    name_label.grid(row=1, column=0, padx=10, pady=10)

    get_name = tk.Entry(get_details_Frame, bd=2, font=("Comic Sans MS", 12), textvariable=name)
    get_name.grid(row=1, column=1, padx=10, pady=10)

    gender_label = tk.Label(get_details_Frame, text="Gender", font=("Comic Sans MS", 12), bg=color_bg_form)
    gender_label.grid(row=2, column=0, padx=10, pady=10)

    gender_combo = ttk.Combobox(get_details_Frame, values=["Male", "Female", "Other"], font=("Comic Sans MS", 11),
                                textvariable=gender)
    gender_combo.grid(row=2, column=1, pady=10, padx=10)

    date_label = tk.Label(get_details_Frame, text="Enroll Date\n(YYYY.MM.DD)", font=("Comic Sans MS", 12),
                          bg=color_bg_form)
    date_label.grid(row=3, column=0, padx=10, pady=10)

    get_date = tk.Entry(get_details_Frame, bd=2, font=("Comic Sans MS", 12), textvariable=enroll_date)
    get_date.grid(row=3, column=1, padx=10, pady=10)

    grade_label = tk.Label(get_details_Frame, text="Grade", font=("Comic Sans MS", 12), bg=color_bg_form)
    grade_label.grid(row=4, column=0, padx=10, pady=10)

    grade_combo = ttk.Combobox(get_details_Frame, values=["12", "13"], font=("Comic Sans MS", 11), textvariable=grade)
    grade_combo.grid(row=4, column=1, padx=10, pady=10)

    test_label = tk.Label(get_details_Frame, text="Test No.", font=("Comic Sans MS", 12), bg=color_bg_form)
    test_label.grid(row=5, column=0, padx=10, pady=10)

    test_combo = ttk.Combobox(get_details_Frame, values=["1st Term", "2nd Term", "3rd Term"],
                              font=("Comic Sans MS", 11),
                              textvariable=test_no)
    test_combo.grid(row=5, column=1, padx=10, pady=10)

    marks_label = tk.Label(get_details_Frame, text="Marks", font=("Comic Sans MS", 12), bg=color_bg_form)
    marks_label.grid(row=6, column=0, padx=10, pady=10)

    get_marks = tk.Entry(get_details_Frame, bd=2, font=("Comic Sans MS", 12), textvariable=marks)
    get_marks.grid(row=6, column=1, padx=10, pady=10)

    button_frame = tk.Frame(get_details_Frame, bg=color_bg_form)
    button_frame.grid(row=7, column=0, columnspan=2, pady=(20, 0))

    button_width = max(len("Add"), len("Update"), len("Delete"), len("Clear")) + 4

    add_button = tk.Button(button_frame, text="Add", font=("Comic Sans MS", 12), width=button_width, command=add_data,
                           bg=button_bg)
    add_button.grid(row=0, column=0, padx=10, pady=5)

    update_button = tk.Button(button_frame, text="Update", font=("Comic Sans MS", 12), width=button_width,
                              command=update_data,
                              bg=button_bg)
    update_button.grid(row=0, column=1, padx=10, pady=5)

    delete_button = tk.Button(button_frame, text="Delete", font=("Comic Sans MS", 12), width=button_width,
                              command=delete_data,
                              bg=button_bg)
    delete_button.grid(row=1, column=0, padx=10, pady=10)

    clear_button = tk.Button(button_frame, text="Clear", font=("Comic Sans MS", 12), width=button_width,
                             command=clear_data,
                             bg=button_bg)
    clear_button.grid(row=1, column=1, padx=10, pady=10)

    button_frame.grid_columnconfigure(0, weight=1)
    button_frame.grid_columnconfigure(1, weight=1)

    search_frame = tk.Frame(show_details_frame, bg=color_bg_form)
    search_frame.pack(side=tk.TOP, fill=tk.X)

    search_label = tk.Label(search_frame, text="Search student by ID", font=("Comic Sans MS", 12), bg=color_bg_form,
                            fg="#6A1B9A")
    search_label.grid(row=0, column=0, padx=10, pady=10)

    search_entry = tk.Entry(search_frame, font=("Comic Sans MS", 12), textvariable=search)
    search_entry.grid(row=0, column=1, padx=10, pady=10)

    find_btn = tk.Button(search_frame, text="Find", font=("Comic Sans MS", 12), command=search_data, bg="lightblue")
    find_btn.grid(row=0, column=2, pady=10, padx=10)

    show_btn = tk.Button(search_frame, text="Show All", font=("Comic Sans MS", 12),
                         command=lambda: (clear_search(), get_data()), bg="lightblue")
    show_btn.grid(row=0, column=3, padx=10, pady=10)

    exit_btn = tk.Button(search_frame, text="Exit", font=("Comic Sans MS", 12), bg="lightblue", command=sys.exit)
    exit_btn.grid(row=0, column=4, pady=10, padx=10)

    main_frame = tk.Frame(show_details_frame)
    main_frame.pack(fill=tk.BOTH, expand=True)

    horizontal_scroll = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL)
    vertical_scroll = tk.Scrollbar(main_frame, orient=tk.VERTICAL)

    show_table = ttk.Treeview(main_frame, columns=("ID", "Name", "Gender", "Enroll Date", "Grade", "Test No.", "Marks"),
                              yscrollcommand=vertical_scroll.set, xscrollcommand=horizontal_scroll.set)

    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview.Heading",
                    background="purple",
                    foreground="white",
                    font=("Comic Sans MS", 10, "bold"))

    horizontal_scroll.config(command=show_table.xview)
    vertical_scroll.config(command=show_table.yview)

    horizontal_scroll.pack(side=tk.BOTTOM, fill=tk.X)
    vertical_scroll.pack(side=tk.RIGHT, fill=tk.Y)

    show_table.heading("ID", text="ID")
    show_table.heading("Name", text="Name")
    show_table.heading("Gender", text="Gender")
    show_table.heading("Enroll Date", text="Enroll Date")
    show_table.heading("Grade", text="Grade")
    show_table.heading("Test No.", text="Test No.")
    show_table.heading("Marks", text="Marks")

    show_table['show'] = 'headings'

    show_table.column("ID", width=100)
    show_table.column("Name", width=100)
    show_table.column("Gender", width=100)
    show_table.column("Enroll Date", width=100)
    show_table.column("Grade", width=100)
    show_table.column("Test No.", width=100)
    show_table.column("Marks", width=100)

    show_table.pack(fill=tk.BOTH, expand=True)

    get_data()
    show_table.bind("<ButtonRelease-1>", get_cursor_show)

    window.mainloop()


login_page()


cur.close()
con.close()