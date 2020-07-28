import tkinter as tk
import random
import tkinter.messagebox

i = 1
conum = True

# Function for getting random number and for second game clear entry and label
def rand():
    global i        # It is used for guessing number and as process bar
    global conum    # It is used for clearing and starting again after right guess
    global g        # It is used for comparing guess correct or not
    global r
    entry.delete(0, len(entry.get()))

    label = tk.Label(lower_frame, text="")
    label.place(relwidth=1, relheight=1)

    if rvar.get() == 1:
        r = random.randint(1, 100)
    else:
        r = random.randint(100, 1000)

    g = r

    conum = True
    i = 1


# If radio buttons clicked after game started, it can be changed number range
def rbutton():
    if (conum == True) and (i > 1):
        tk.messagebox.showinfo("Warning", "You can not change range number after game started !"
                                          "\n\nWhen you want to start again, please click Start button !")
        if r < 100:
            rvar.set(1)
        else:
            rvar.set(2)
    else:
        rvar.get()



# Event for Enter Keystroke
def onReturn(event):
    if conum == True:
        control()
    else:
        rand()


# Control function for guessed number
def control():
    try:
        global i
        global conum

        if conum == False:  # It is used to return start, when clicking "Control" button after right guess
            rand()
        else:
            num = entry.get()
            if int(num) < g:
                label = tk.Label(lower_frame, text='\u258B'*i+"\n["+str(i)+"]"+"\n\nLarger than "+str(num))
                label.place(relwidth=1, relheight=1)
                label.config(font=("Comic Sans MS", 11))
            elif int(num) > g:
                label = tk.Label(lower_frame, text='\u258B'*i+"\n["+str(i)+"]"+"\n\nSmaller than "+str(num))
                label.place(relwidth=1, relheight=1)
                label.config(font=("Comic Sans MS", 11))
            else:
                label = tk.Label(lower_frame, text='\u258B'*i+"\n["+str(i)+"]"+"\n\n\u263A SUPER! \u263A"+"\n\n"+str(g)+"\n\nCongratulations. You guessed correctly.")
                label.place(relwidth=1, relheight=1)
                label.config(font=("Comic Sans MS", 11))
                conum = False

        i += 1
        entry.selection_range(0,len(entry.get()))

    except NameError:
        label = tk.Label(lower_frame, text="Please click first START button!")
        label.place(relwidth=1, relheight=1)
        label.config(font=("Comic Sans MS", 11))

    except ValueError:
        label = tk.Label(lower_frame, text="Please enter a number!")
        label.place(relwidth=1, relheight=1)
        label.config(font=("Comic Sans MS", 11))


# Window parameters to the end
root = tk.Tk()
root.title("Guess Game")
root.geometry("600x400")

frame = tk.Frame(root, bg='#DDB6C6', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=("Comic Sans MS", 14, 'bold'),justify="center",fg="#9A0A58")
entry.bind("<Return>", onReturn)
entry.place(relx =0.25, relwidth=0.5, relheight=1)

buttonS = tk.Button(frame, text='Start', bd=2.5, fg='#484C7F', command=lambda: rand())
buttonS.place(relx=0, relheight=1, relwidth=0.2)

buttonC = tk.Button(frame, text='Control', bd=2.5, fg='#484C7F', command=lambda: control())
buttonC.place(relx=0.8, relheight=1, relwidth=0.2)

labelR = tk.Label(root, text="Number range       :")
labelR.place(relx=0.125, rely=0.2)

rvar = tk.IntVar()
rvar.set(1)

radioButton1 = tk.Radiobutton(root, text="1-100", variable=rvar, value=1, command=lambda: rbutton())
radioButton1.place(relx=0.35, rely=0.2)

radioButton2 = tk.Radiobutton(root, text="100-1000", variable=rvar, value=2, command=lambda: rbutton())
radioButton2.place(relx=0.52, rely=0.2)

lower_frame = tk.Frame(root, bg='#DDB6C6', bd=7.5)
lower_frame.place(relx=0.5, rely=0.26, relwidth=0.75, relheight=0.6, anchor='n')

desc = "GUESS GAME\n\nPlease click Start button\n\n" \
       "Enter a number and check if it is correct with the Control button\n" \
       "Try to find the right number by following the clues in the game\n\n\n" \
       "GOOD LUCK"

label = tk.Label(lower_frame, text=desc)
label.place(relwidth=1, relheight=1)


root.mainloop()