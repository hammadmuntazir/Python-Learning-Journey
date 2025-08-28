import tkinter as  tk
from struct import calcsize

root = tk.Tk()#root=name of window

root.geometry("500x600")#ensue that there is no gap between l*w
root.title("Hammad")

label=tk.Label(root,text="Hello world!",font=("Arial",20))#label(name of window where to display,what to display)
label.pack(padx=20,pady=40)#ensure that it is displayed in window ,can add padding too

textbox=tk.Text(root,height =3,font=("Arial",15)) #for creating text box#3 mean 3 lines height will show
textbox.pack(padx=20,pady=40)

# Create a frame for buttons
buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)  # Make column 0 stretch
buttonframe.columnconfigure(1, weight=1)  # Make column 1 stretch
buttonframe.columnconfigure(2, weight=1)  # Make column 2 stretch

# Create buttons with proper grid row and column values
btn1 = tk.Button(buttonframe, text="1", font=("Arial", 18))#root ki jaga button frame lygyein bcz us mn add krna hai
btn1.grid(row=0, column=0, sticky=tk.W + tk.E)

btn2 = tk.Button(buttonframe, text="2", font=("Arial", 18))
btn2.grid(row=0, column=1, sticky=tk.W + tk.E)

btn3 = tk.Button(buttonframe, text="3", font=("Arial", 18))
btn3.grid(row=0, column=2, sticky=tk.W + tk.E)

btn4 = tk.Button(buttonframe, text="4", font=("Arial", 18))
btn4.grid(row=1, column=0, sticky=tk.W + tk.E)

btn5 = tk.Button(buttonframe, text="5", font=("Arial", 18))
btn5.grid(row=1, column=1, sticky=tk.W + tk.E)

btn6 = tk.Button(buttonframe, text="6", font=("Arial", 18))
btn6.grid(row=1, column=2, sticky=tk.W + tk.E)

# Pack the buttonframe into the root window
buttonframe.pack(fill="x")

# button=tk.Button(root,text="Click Me!",font=("Arial",18))#for adding button
# button.pack(padx=20,pady=40)

"""myentry=tk.Entry(root)#for text entry in window
myentry.pack()"""


root.mainloop()

