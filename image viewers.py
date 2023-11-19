from tkinter import * 
root = Tk();
from PIL import ImageTk, Image
from tkinter import filedialog

root.title("Image Viewer and Rotater")
root.geometry("700x650")
root.configure(background="#acaefa")

label_image = Label(root,bg="#acaefa",highlightthickness=5)
label_image.place(relx=0.5,rely=0.5,anchor=CENTER)

img_path = ""

def open_image() :
    global img_path
    
    img_path = filedialog.askopenfilename(title = "Open Image File", filetypes = [("Image Files", "*.jpg;*.gif;*.png;*.jpeg;*txt")])
    print(img_path)
    
    img =  ImageTk.PhotoImage(Image.open(img_path))
    
    
    label_image['image'] = img 
    img.close()
    
button_open = Button(root,text="Open Image",font=("Ink Free",16,"bold"),bg="#6e6f99",fg="#ffffff",relief=SOLID,padx=1,pady=1,command=open_image)
button_open.place(relx=0.5,rely=0.1,anchor=CENTER)
root.mainloop();

