from tkinter import *

root =Tk()
root.title("Hammad") #i can write title name here
root.iconbitmap(r'hammad.ico') #for location we use r ' '
#size of GUi
root.geometry("500x500") #for size of GUI app
window_width = 500
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# Calculate the position to center the window
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
# Set the geometry with the calculated position
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

root.mainloop()
