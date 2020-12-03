import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
from PIL import ImageTk, Image

# --- Colors
lightblue = "#30B7F2"
myorange = "#FA8B07"

# --- Window variables
root = tk.Tk()
root.title("Practice")
root.geometry("500x500")
root.resizable(False, False)  # locked from resizing
root.attributes("-alpha", 0.97)  # makes window 0,03% transparent
root.iconbitmap('icon.ico')

# --- Images

logo = ImageTk.PhotoImage(Image.open("mm01r.jpg"))
climb1 = ImageTk.PhotoImage(Image.open("mm02r.jpg"))
climb2 = ImageTk.PhotoImage(Image.open("mm03r.jpg"))
climb3 = ImageTk.PhotoImage(Image.open("mm04r.jpg"))
climb4 = ImageTk.PhotoImage(Image.open("mm05r.jpg"))
climb5 = ImageTk.PhotoImage(Image.open("mm06r.jpg"))
climb6 = ImageTk.PhotoImage(Image.open("mm07r.jpg"))

addscreen = ImageTk.PhotoImage(Image.open("add.png"))  # 740x539
subscreen = ImageTk.PhotoImage(Image.open("sub.png"))  # 746x528
mulscreen = ImageTk.PhotoImage(Image.open("mul.png"))  # 744x529

# --- Variables
global add_res, add_col, add_correct, add_error, add_ch, sub_ch, mul_ch

# --- addition counters
add_correct = 0
add_error = 0
add_res = tk.StringVar()
add_col = tk.StringVar()
add_col.set("black")

# --- subtraction
sub_correct = 0
sub_error = 0
sub_res = tk.StringVar()
sub_col = tk.StringVar()
sub_col.set("black")

# --- multiplication
mul_correct = 0
mul_error = 0
mul_res = tk.StringVar()
mul_col = tk.StringVar()
mul_col.set("black")

# ---for binding purposes
add_ch = False
sub_ch = False
mul_ch = False


def addition():
    """ This function is run when Addition button is pressed.
    First it destroys buttons from menu then starts to load queries.
    When Check button is clicked add_check function is started to compare if provided result is correct.
    In case if its correct then add_correct variable is growing up by one and when it reaches next level
    then difficulty is increased. Otherwise when its incorrect then add_error variable is growing up and difficulty
    can be lowered.
    """
    # Displays the problem randomNum1 + randomNum2 on the screen
    # 4 options but 1 correct answer which is the sum of randomNum1 + randomNum2
    # If user answered questions wrong 3x, open up new window to show example on how to add
    # If user answered correctly, move on to next question without any comments

    global parent, a, b, c, r, result_lbl, add_correct, add_error, add_ch, sub_ch, mul_ch

    # set binding script
    add_ch = True
    sub_ch = False
    mul_ch = False

    # Clear menu screen and creates new widgets
    try:
        parent.destroy()
    except:
        pass
    items = [addButton, subButton, multiButton]
    for i in items:
        i.destroy()
    parent = tk.Frame(root, bg="white")
    parent.pack(expand=True, fill="both")

    # to reset entrybox value = None
    r = tk.StringVar()

    if 7 <= add_correct - add_error < 15:
        logo_lbl.configure(image=climb2)
        a = random.randint(1, 20)
        b = random.randint(1, 10)
        c = 0

        question_lbl = tk.Label(parent, text=str(a) + " + " + str(b) + " = ", font=("Comic Sans MS", 22), bg="white", )
        question_lbl.pack()

        ans_ent = tk.Entry(parent, textvariable=r).pack()

        result_lbl = tk.Label(parent, text=add_res.get(), bg="white", font=("Comic Sans MS", 20), fg=add_col.get())
        result_lbl.pack(fill="x")

    elif 15 <= add_correct - add_error < 25:
        logo_lbl.configure(image=climb2)
        a = random.randint(5, 20)
        b = random.randint(1, 25)
        c = 0

        question_lbl = tk.Label(parent, text=str(a) + " + " + str(b) + " = ", font=("Comic Sans MS", 22), bg="white")
        question_lbl.pack()

        ans_ent = tk.Entry(parent, textvariable=r).pack()

        result_lbl = tk.Label(parent, text=add_res.get(), bg="white", font=("Comic Sans MS", 20), fg=add_col.get())
        result_lbl.pack(fill="x")

    elif 25 <= add_correct - add_error < 45:
        logo_lbl.configure(image=climb3)
        a = random.randint(10, 30)
        b = random.randint(15, 35)
        c = 0

        question_lbl = tk.Label(parent, text=str(a) + " + " + str(b) + " = ", font=("Comic Sans MS", 22), bg="white")
        question_lbl.pack()

        ans_ent = tk.Entry(parent, textvariable=r).pack()

        result_lbl = tk.Label(parent, text=add_res.get(), bg="white", font=("Comic Sans MS", 20), fg=add_col.get())
        result_lbl.pack(fill="x")

    elif 45 <= add_correct - add_error < 75:
        logo_lbl.configure(image=climb4)
        a = random.randint(10, 30)
        b = random.randint(15, 35)
        c = random.randint(1, 30)

        question_lbl = tk.Label(parent, text=str(a) + " + " + str(b) + " + " + str(c) + " = ",
                                font=("Comic Sans MS", 22), bg="white")
        question_lbl.pack()

        ans_ent = tk.Entry(parent, textvariable=r).pack()

        result_lbl = tk.Label(parent, text=add_res.get(), bg="white", font=("Comic Sans MS", 20), fg=add_col.get())
        result_lbl.pack(fill="x")

    elif 75 <= add_correct - add_error <= 99:
        logo_lbl.configure(image=climb5)

        a = random.randint(10, 100)
        b = random.randint(15, 100)
        c = random.randint(1, 100)

        question_lbl = tk.Label(parent, text=str(a) + " + " + str(b) + " + " + str(c) + " = ",
                                font=("Comic Sans MS", 22), bg="white")
        question_lbl.pack()

        ans_ent = tk.Entry(parent, textvariable=r).pack()

        result_lbl = tk.Label(parent, text=add_res.get(), bg="white", font=("Comic Sans MS", 20), fg=add_col.get())
        result_lbl.pack(fill="x")

    elif add_correct - add_error == 100:
        logo_lbl.configure(image=climb6)
        tk.messagebox.showinfo(title="Great Success!", message="You're truly master of addition!\nCongratulations!")
        reset_btn = tk.Button(parent, text="Reset", bg="red", fg="white", command=add_reset).pack()


    else:
        logo_lbl.configure(image=climb1)
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        c = 0

        question_lbl = tk.Label(parent, text=str(a) + " + " + str(b) + " = ", font=("Comic Sans MS", 22), bg="white")
        question_lbl.pack()

        ans_ent = tk.Entry(parent, textvariable=r).pack()

        result_lbl = tk.Label(parent, text=add_res.get(), bg="white", font=("Comic Sans MS", 20), fg=add_col.get())
        result_lbl.pack(fill="x")

    check_btn = tk.Button(parent, text="  Check   ", bg=myorange, fg="white", font=("Comic Sans MS", 18),
                          command=add_check).pack()

    button2 = Button(parent, text="Go back", bg=lightblue, fg="white", font=("Comic Sans MS", 20), command=restore)
    button2.pack(side=BOTTOM, fill="x")


def subtraction():
    """ This function is run when Subtraction button is pressed.
    First it destroys buttons form menu page then to load queries."""
    # Displays the problem randomNum1 + randomNum2 on the screen
    # 4 options but 1 correct answer which is the sum of randomNum1 + randomNum2
    # If user answered questions wrong 3x, open up new window to show example on how to add
    # If user answered correctly, move on to next question without any comments

    global parent, a, b, c, r, result_lbl, sub_correct, sub_error, add_ch, sub_ch, mul_ch

    # set binding scirpt
    add_ch = False
    sub_ch = True
    mul_ch = False

    # Clear menu screen and creates new widgets
    try:
        parent.destroy()
    except:
        pass
    items = [addButton, subButton, multiButton]
    for i in items:
        i.destroy()
    parent = tk.Frame(root, bg="white")
    parent.pack(expand=True, fill="both")

    # to reset entry box value = None
    r = tk.StringVar()

    if 7 <= sub_correct - sub_error < 15:
        logo_lbl.configure(image=climb2)

        a = random.randint(1, 15)
        b = random.randint(1, a)
        c = 0

        question_lbl = tk.Label(parent, text=str(a) + " - " + str(b) + " = ", font=("Comic Sans MS", 22), bg="white", )
        question_lbl.pack()

        ans_ent = tk.Entry(parent, textvariable=r).pack()

        result_lbl = tk.Label(parent, text=sub_res.get(), bg="white", font=("Comic Sans MS", 20), fg=sub_col.get())
        result_lbl.pack(fill="x")

    elif 15 <= sub_correct - sub_error < 25:
        logo_lbl.configure(image=climb2)

        a = random.randint(1, 30)
        b = random.randint(1, a)
        c = 0

        question_lbl = tk.Label(parent, text=str(a) + " - " + str(b) + " = ", font=("Comic Sans MS", 22), bg="white", )
        question_lbl.pack()

        ans_ent = tk.Entry(parent, textvariable=r).pack()

        result_lbl = tk.Label(parent, text=sub_res.get(), bg="white", font=("Comic Sans MS", 20), fg=sub_col.get())
        result_lbl.pack(fill="x")

    elif 25 <= sub_correct - sub_error < 45:
        logo_lbl.configure(image=climb3)

        a = random.randint(1, 50)
        b = random.randint(1, a)
        c = 0
        question_lbl = tk.Label(parent, text=str(a) + " - " + str(b) + " = ", font=("Comic Sans MS", 22), bg="white", )
        question_lbl.pack()

        ans_ent = tk.Entry(parent, textvariable=r).pack()

        result_lbl = tk.Label(parent, text=sub_res.get(), bg="white", font=("Comic Sans MS", 20), fg=sub_col.get())
        result_lbl.pack(fill="x")

    elif 45 <= sub_correct - sub_error < 75:
        logo_lbl.configure(image=climb4)

        a = random.randint(1, 100)
        b = random.randint(1, a)
        c = random.randint(1, a - b)

        question_lbl = tk.Label(parent, text=str(a) + " - " + str(b) + " - " + str(c) + " = ",
                                font=("Comic Sans MS", 22), bg="white", )
        question_lbl.pack()

        ans_ent = tk.Entry(parent, textvariable=r).pack()

        result_lbl = tk.Label(parent, text=sub_res.get(), bg="white", font=("Comic Sans MS", 20), fg=sub_col.get())
        result_lbl.pack(fill="x")

    elif 75 <= sub_correct - sub_error <= 99:
        logo_lbl.configure(image=climb5)

        a = random.randint(1, 500)
        b = random.randint(1, a)
        c = random.randint(1, a - b)

        question_lbl = tk.Label(parent, text=str(a) + " - " + str(b) + " - " + str(c) + " = ",
                                font=("Comic Sans MS", 22), bg="white", )
        question_lbl.pack()

        ans_ent = tk.Entry(parent, textvariable=r).pack()

        result_lbl = tk.Label(parent, text=sub_res.get(), bg="white", font=("Comic Sans MS", 20), fg=sub_col.get())
        result_lbl.pack(fill="x")

    elif sub_correct - sub_error == 100:
        logo_lbl.configure(image=climb6)
        tk.messagebox.showinfo(title="Great Success!", message="You're truly master of subtraction!\nCongratulations!")
        reset_btn = tk.Button(parent, text="Reset", bg="red", fg="white", command=sub_reset).pack()

    else:
        logo_lbl.configure(image=climb1)
        a = random.randint(1, 10)
        b = random.randint(1, a)
        c = 0

        question_lbl = tk.Label(parent, text=str(a) + " - " + str(b) + " = ", font=("Comic Sans MS", 22), bg="white", )
        question_lbl.pack()

        ans_ent = tk.Entry(parent, textvariable=r).pack()

        result_lbl = tk.Label(parent, text=sub_res.get(), bg="white", font=("Comic Sans MS", 20), fg=sub_col.get())
        result_lbl.pack(fill="x")

    check_btn = tk.Button(parent, text="  Check   ", bg=myorange, fg="white", font=("Comic Sans MS", 18),
                          command=sub_check).pack()
    button2 = Button(parent, text="Go back", bg=lightblue, fg="white", font=("Comic Sans MS", 20), command=restore)
    button2.pack(side=BOTTOM, fill="x")


def multiplication():
    """     Displays the problem a * b * c on the screen
     If user answered questions wrong 3x, open up new window to show example on how to multiply"""

    global parent, a, b, c, r, result_lbl, mul_correct, mul_error, add_ch, sub_ch, mul_ch

    # set binding script
    add_ch = False
    sub_ch = False
    mul_ch = True

    # Clear menu screen and creates new widgets
    try:
        parent.destroy()
    except:
        pass
    items = [addButton, subButton, multiButton]
    for i in items:
        i.destroy()
    parent = tk.Frame(root, bg="white")
    parent.pack(expand=True, fill="both")

    # to reset entry box value = None
    r = tk.StringVar()

    if 7 <= mul_correct - mul_error < 15:
        logo_lbl.configure(image=climb2)
        a = random.randint(0, 10)
        b = random.randint(0, 10)
        c = 1

        question_lbl = tk.Label(parent, text=str(a) + " x " + str(b) + " = ", font=("Comic Sans MS", 22), bg="white")
        question_lbl.pack()

        ans_ent = tk.Entry(parent, textvariable=r).pack()

        result_lbl = tk.Label(parent, text=mul_res.get(), bg="white", font=("Comic Sans MS", 20), fg=mul_col.get())
        result_lbl.pack(fill="x")

    elif 15 <= mul_correct - mul_error < 25:
        logo_lbl.configure(image=climb2)
        a = random.randint(1, 25)
        b = random.randint(1, 25)
        c = 1

        question_lbl = tk.Label(parent, text=str(a) + " x " + str(b) + " = ", font=("Comic Sans MS", 22), bg="white")
        question_lbl.pack()

        ans_ent = tk.Entry(parent, textvariable=r).pack()

        result_lbl = tk.Label(parent, text=mul_res.get(), bg="white", font=("Comic Sans MS", 20), fg=mul_col.get())
        result_lbl.pack(fill="x")

    elif 25 <= mul_correct - mul_error < 45:
        logo_lbl.configure(image=climb3)
        a = random.randint(1, 50)
        b = random.randint(1, 50)
        c = 1

        question_lbl = tk.Label(parent, text=str(a) + " x " + str(b) + " = ", font=("Comic Sans MS", 22), bg="white")
        question_lbl.pack()

        ans_ent = tk.Entry(parent, textvariable=r).pack()

        result_lbl = tk.Label(parent, text=mul_res.get(), bg="white", font=("Comic Sans MS", 20), fg=mul_col.get())
        result_lbl.pack(fill="x")

    elif 45 <= mul_correct - mul_error < 75:
        logo_lbl.configure(image=climb4)
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        c = 1

        question_lbl = tk.Label(parent, text=str(a) + " x " + str(b) + " = ", font=("Comic Sans MS", 22), bg="white")
        question_lbl.pack()

        ans_ent = tk.Entry(parent, textvariable=r).pack()

        result_lbl = tk.Label(parent, text=mul_res.get(), bg="white", font=("Comic Sans MS", 20), fg=mul_col.get())
        result_lbl.pack(fill="x")

    elif 75 <= mul_correct - mul_error <= 99:
        logo_lbl.configure(image=climb5)
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        c = random.randint(1, 10)

        question_lbl = tk.Label(parent, text=str(a) + " x " + str(b) + " x " + str(c) + " = ",
                                font=("Comic Sans MS", 22), bg="white")
        question_lbl.pack()

        ans_ent = tk.Entry(parent, textvariable=r).pack()

        result_lbl = tk.Label(parent, text=mul_res.get(), bg="white", font=("Comic Sans MS", 20), fg=mul_col.get())
        result_lbl.pack(fill="x")

    elif mul_correct - mul_error == 100:
        logo_lbl.configure(image=climb6)
        tk.messagebox.showinfo(title="Great Success!",
                               message="You're truly master of multiplication!\nCongratulations!")
        reset_btn = tk.Button(parent, text="Reset", bg="red", fg="white", command=mul_reset).pack()

    else:
        logo_lbl.configure(image=climb1)
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        c = 1

        question_lbl = tk.Label(parent, text=str(a) + " x " + str(b) + " = ", font=("Comic Sans MS", 22), bg="white")
        question_lbl.pack()

        ans_ent = tk.Entry(parent, textvariable=r).pack()

        result_lbl = tk.Label(parent, text=mul_res.get(), bg="white", font=("Comic Sans MS", 20), fg=mul_col.get())
        result_lbl.pack(fill="x")

    check_btn = tk.Button(parent, text="  Check   ", bg=myorange, fg="white", font=("Comic Sans MS", 18),
                          command=mul_check).pack()

    button2 = Button(parent, text="Go back", bg=lightblue, fg="white", font=("Comic Sans MS", 20), command=restore)
    button2.pack(side=BOTTOM, fill="x")


def add_check():
    global parent, a, b, c, r, result_lbl, add_res, add_correct, add_error

    if r.get() == "":
        tk.messagebox.showinfo(title="Answer is missing", message="Please provide an answer.")

    else:
        if (a + b + c) == int(r.get()):
            print(a + b + c)

            add_res.set("Correct")
            add_col.set("green")
            add_correct += 1
            addition()


        else:
            add_res.set("Incorrect")
            add_col.set("red")
            add_error += 1
            addition()

    if abs(add_error) in [3, 6, 9, 12, 15, 18, 21, 25, 30, 33, 36, 39, 42, 45]:
        # print(add_error)
        add_top()

    else:
        pass
    print(add_correct - add_error)


def add_top():
    add_top = tk.Toplevel()
    add_top.geometry("740x538")
    add_top.configure(bg="white")
    add_top.title("Addition Info")
    addsc_lbl = tk.Label(add_top, image=addscreen)
    addsc_lbl.pack()


def add_reset():
    """ This function can be used to reset progress once game is finished for addition """
    global add_correct, add_error
    add_correct = 0
    add_error = 0
    add_res.set(" ")
    restore()


def sub_check():
    global parent, a, b, c, r, result_lbl, sub_res, sub_correct, sub_error

    if r.get() == "":
        tk.messagebox.showinfo(title="Answer is missing", message="Please provide an answer.")

    else:
        if (a - b - c) == int(r.get()):
            print(a - b - c)

            sub_res.set("Correct")
            sub_col.set("green")
            sub_correct += 1
            subtraction()


        else:
            sub_res.set("Incorrect")
            sub_col.set("red")
            sub_error += 1
            subtraction()

    if abs(sub_error) in [3, 6, 9, 12, 15, 18, 21, 25, 30, 33, 36, 39, 42, 45]:
        # print(sub_error)
        sub_top()

    else:
        pass
    print(sub_correct - sub_error)


def sub_top():
    sub_top = tk.Toplevel()
    sub_top.geometry("746x539")
    sub_top.configure(bg="white")
    sub_top.title("Subtraction Info")
    subsc_lbl = tk.Label(sub_top, image=subscreen)
    subsc_lbl.pack()


def sub_reset():
    """ This function can be used to reset progress once game is finished for subtraction"""
    global sub_correct, sub_error
    sub_correct = 0
    sub_error = 0
    sub_res.set(" ")
    restore()


def mul_check():
    global parent, a, b, c, r, result_lbl, mul_res, mul_correct, mul_error

    if r.get() == "":
        tk.messagebox.showinfo(title="Answer is missing", message="Please provide an answer.")

    else:
        if (a * b * c) == int(r.get()):
            print(a * b * c)

            mul_res.set("Correct")
            mul_col.set("green")
            mul_correct += 1
            multiplication()


        else:
            mul_res.set("Incorrect")
            mul_col.set("red")
            mul_error += 1
            multiplication()

    if abs(mul_error) in [3, 6, 9, 12, 15, 18, 21, 25, 30, 33, 36, 39, 42, 45]:
        # print(mul_error)
        mul_top()

    else:
        pass

    print(mul_correct - mul_error)


def mul_top():
    mul_top = tk.Toplevel()
    mul_top.geometry("744x529")
    mul_top.configure(bg="white")
    mul_top.title("Multiplication Info")
    mulsc_lbl = tk.Label(mul_top, image=mulscreen)
    mulsc_lbl.pack()


def mul_reset():
    """ This function can be used to reset progress once game is finished for subtraction"""
    global mul_correct, mul_error
    mul_correct = 0
    mul_error = 0
    mul_res.set(" ")
    restore()


def check_bind(event):
    global add_ch, sub_ch, mul_ch
    """ This functions allows to sent results with clicking enter
    It will be different for each option we choose addition/subtraction/multiplication,
    when all are False then it will do nothing.
    With this binds user can answer with combination tab -> number -> enter, which allows to play without mouse"""

    if add_ch == True:
        add_check()
    elif sub_ch == True:
        sub_check()
    elif mul_ch == True:
        mul_check()
    else:
        pass


def restore():
    """ This function restore menu once button2 is clicked
        Recreates Menu """
    logo_lbl.configure(image=logo)

    global parent, add_ch, sub_ch, mul_ch

    # restore binds to False
    add_ch = False
    sub_ch = False
    mul_ch = False

    # Recreates widgets components
    parent.destroy()
    parent = tk.Frame(root)
    parent.pack(expand=True, fill="both")
    addButton = tk.Button(parent, text="Addition", font=("Comic Sans MS", 20), fg="white", bg=myorange,
                          command=addition)
    addButton.pack(expand="true", fill="both")
    subButton = tk.Button(parent, text="Subtraction", font=("Comic Sans MS", 20), fg="white", bg=myorange,
                          command=subtraction)
    subButton.pack(expand="true", fill="both")
    multiButton = tk.Button(parent, text="Multiplication", font=("Comic Sans MS", 20), fg="white", bg=myorange,
                            command=multiplication)
    multiButton.pack(expand="true", fill="both")


# Buttons for each functions that is displayed on the front page
# GUI added
logo_lbl = tk.Label(root, image=logo)
logo_lbl.pack()
addButton = tk.Button(root, text="Addition", font=("Comic Sans MS", 20), fg="white", bg=myorange, command=addition)
addButton.pack(expand="true", fill="both")
subButton = tk.Button(root, text="Subtraction", font=("Comic Sans MS", 20), fg="white", bg=myorange,
                      command=subtraction)
subButton.pack(expand="true", fill="both")
multiButton = tk.Button(root, text="Multiplication", font=("Comic Sans MS", 20), fg="white", bg=myorange,
                        command=multiplication)
multiButton.pack(expand="true", fill="both")

# This part allows to use enter instead of Check button.
try:
    root.bind("<Return>", check_bind)
except:
    pass

root.mainloop()
