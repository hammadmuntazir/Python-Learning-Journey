import tkinter as tk

root=tk.Tk()#intializing our main  window ab agr sirf isy hi dekhy to humy kuch nazar nai aye ga mgr asal mn kuch hoga windown jaldi sy open aur close hogi hum dekh nai sky gye
root.title("Hammad App")#for adding title

lbl =tk.Label(root)
btn =tk.Button(root, text="Button 1")#we are passing root because it is going to be the parent window where our widget willl be added and we donot have any  other right now so let's go ahead and pass in root and we will
btn.grid()
root.mainloop() #if we run this we will get blank window with no error