import tkinter as tk

calculation = ""#calculation string empty string at first
def add_to_calculation(symbol):#symbol as a parameter we are going to add
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert("1.0",calculation)
def evaluate_calculation():  # which call eval function
    global calculation
    try:
        calculation="str(eval(calculation))"
        text_result.delete(1.0,"end")
        text_result.insert("1.0",calculation)

    except:
    pass
def clear_field():
    pass

root = tk.Tk()
root.geometry("300x280")
root.title("Calculator")

text_result =tk.Text(root,height=3,width=16,font=("Arial",20))#for displaying result
text_result.grid(columnspan=5)#grid 5 columns
root.mainloop()