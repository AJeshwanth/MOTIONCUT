from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
def login():
    # getting the text entered by the user in user_field and pass_field
    username = user_field.get()
    password = pass_field.get()
    # Removind the extra spaces 
    username=username.strip()
    password=password.strip()
    # opening the userdetails file in read mode
    with open("userdetails.txt", 'r') as f:
        # reading the content in file and splitting with delimeter \n and converting it to string using join method then splitting by space
        d=' '.join(f.read().split("\n")).split(" ")
        # destroying the login window
        root.destroy()
        count=0
        # checking whether the entered details already exists in the file or not
        for j in range(0, len(d)-1, 2):
            count+=1
            # if matches create_expenses window is invoked and passing username, password, prev and line number at which we found match
            if username==d[j] and password==d[j+1]:
                create_expenses_window(username, password, prev=True, line=count)
                break
        else:
            # if not found creating new user and passing username, password, prev=False and line as None
            messagebox.showinfo("Login", "New User Has Been Created")
            create_expenses_window(username,password)
def create_expenses_window(username,password,  prev=False, line=None):
    # creating a window named Expenses
    window = Tk()
    window.title("Expenses")
    window.geometry("400x300")
    # creating a label with username provided
    welcome_label = Label(window, text=f"Welcome {username}")
    welcome_label.pack(side=TOP, pady=10)
    # drawing a line under the label 
    canvas = Canvas(window, width=400, height=1, bg="black")  # Create a canvas for the line
    canvas.pack()
    # creating 4 labels exp, food, transport and Entertainment, 3 textfields f_exp, t_Exp, e_exp and placing these components in window
    exp=Label(window, text="Provide Your Daily Expenses")
    exp.pack(side=TOP, pady=5)
    food = Label(window, text="Food:")
    food.place(x=130, y=80)
    f_exp = Entry(window)
    f_exp.place(x=180, y=80)
    transport = Label(window, text="Transport:")
    transport.place(x=120, y=110)
    t_exp = Entry(window)
    t_exp.place(x=180, y=110)
    Entertainment = Label(window, text="Entertainment:")
    Entertainment.place(x=90, y=140)
    e_exp = Entry(window)
    e_exp.place(x=180, y=140)
    if not prev:
        # if prev is false we are creating a button named Expense analysis and invoking submit expenses with the paramenters 
        # provided in the text fieldsmethod when the button is clicked 
        submit_button = Button(window, text="Expense Analysis", command=lambda: submit_expenses(f_exp.get(), t_exp.get(), e_exp.get(),data=None, upd=not prev))
        submit_button.place(x=180, y=190)
        # opening userdetails file in append mode and appending username and password to it
        with open("userdetails.txt", 'a') as f:
            f.write(f"{username} {password}\n")
    else:
        # opeining Analysis file as read mode
        count=0
        with open("analysis.txt", 'r') as f:
            data=""
            # Iterating line by line and appending it data 
            for j in f:
                count+=1
                # if the line number and count value matches we taking values and storing in f, t and e and appending a to data for further modifying data
                if count == line:
                    values=j.split(" ")
                    f=values[0]
                    t=values[1]
                    e=values[2]
                    data+='a'
                    continue
                data+=j
        # creating two buttons submit button and prev button which invokes submit expenses method when they are clicked
        submit_button = Button(window, text="Expense Analysis", command=lambda: submit_expenses(f_exp.get(), t_exp.get(), e_exp.get(), data=data, upd=not prev))
        prev_button = Button(window, text="Previous Analysis", command=lambda: submit_expenses(f, t, e))
        prev_button.place(x=90, y=190)
        submit_button.place(x=210, y=190)

def submit_expenses(food, transportation, entertainment, data=None, upd=False):
    k=True
    try:
        # converting the values entered in the textfields to integers
        f_exp=int(food)
        t_exp=int(transportation)
        e_exp=int(entertainment)
        if upd:
            # opening Analysis file and writing values
            with open("analysis.txt", 'a') as f:
                f.write(f"{f_exp} {t_exp} {e_exp}\n")
        if data !=None:
            # opening Analysis file for modifying a line 
            with open("analysis.txt", 'w') as f:
                # a is replaced with the values and written into the file
                data=data.replace("a", f"{f_exp} {t_exp} {e_exp}\n")
                f.write(data)
    # If any exception is raised while converting values to integers it will be caught here
    except Exception as e:
        print(e)
        k=False
        # A dialog box is show to provide correct values
        messagebox.showinfo("Error", "Provide Correct Values")
    if k:
        # invoking mon_cat method by passing the values for displaying graph
        mon_cat(f_exp, t_exp, e_exp)

def mon_cat(food, transport, entertainment):
    # calculating the total expenses for month
    total_expense = food*30 + transport*30 + entertainment*30

    # These are the categories and values
    categories = ['Food', 'Transportation', 'Entertainment']
    values = [food*30, transport*30, entertainment*30]
    # setting size to the graph
    plt.figure(figsize=(6, 4))
    # creating bars with width 0.3, and the given values, categories
    bars = plt.bar(categories, values, color=['red', 'green', 'blue'], width=0.3)
    # displaying the categories expenditure for month above the graph
    for bar in bars:
        # getting the height of bar and storing in yval
        yval = bar.get_height()
        # placing the category expenditure per month above the graph and center
        plt.text(bar.get_x() + bar.get_width()/2, yval, f'₹{round(yval, 2)}', ha='center', va='bottom')
    # setting title to the graph
    plt.title(f'Monthly Expenditure-{total_expense}₹')
    # These are the xlabel and ylabel
    plt.xlabel('Categories')
    plt.ylabel('Expense (in ₹)')
    # displays the graph
    plt.show()
# Creating a window named Login
root = Tk()
root.title("Login")
#  Creating two labels user and passw and two textfields user_field and pass_field to take input from the user
user = Label(root, text="Username:")
user.grid(row=0, column=0, padx=10, pady=10)
user_field = Entry(root)
user_field.grid(row=0, column=1, padx=10, pady=10)
passw = Label(root, text="Password:")
passw.grid(row=1, column=0, padx=10, pady=10)
pass_field = Entry(root, show="*")
pass_field.grid(row=1, column=1, padx=10, pady=10)
# login button when it is clicked login method is invoked
log_in = Button(root, text="Login", command=login)
log_in.grid(row=2, column=0, columnspan=2, pady=10)
# Run the main loop
root.mainloop()


login_button = Button(root, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

# Run the main loop
root.mainloop()
