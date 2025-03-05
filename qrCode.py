import qrcode
from tkinter import *
from tkinter import messagebox

wn = Tk()
wn.title('QR Code Generator')
wn.geometry('700x700')
wn.config(bg='SteelBlue3')

def generateCode():
    qr = qrcode.QRCode(version=int(size.get()), box_size=10, border=5)
    qr.add_data(text.get())
    qr.make(fit=True)
    img = qr.make_image()
    fileDirec = loc.get() + '\\' + name.get()
    img.save(f'{fileDirec}.png')
    messagebox.showinfo("QR Code Generator", "QR Code is saved successfully!")

headingFrame = Frame(wn, bg="azure", bd=5)
headingFrame.place(relx=0.15, rely=0.05, relwidth=0.7, relheight=0.1)
headingLabel = Label(headingFrame, text="Generate QR Code", bg='azure', font=('Times', 20, 'bold'))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

Frame1 = Frame(wn, bg="SteelBlue3")
Frame1.place(relx=0.1, rely=0.15, relwidth=0.7, relheight=0.3)
Label(Frame1, text="Enter text/URL:", bg="SteelBlue3", fg='azure', font=('Courier', 13, 'bold')).place(relx=0.05, rely=0.2, relheight=0.08)
text = Entry(Frame1, font=('Century 12'))
text.place(relx=0.05, rely=0.4, relwidth=1, relheight=0.2)

Frame2 = Frame(wn, bg="SteelBlue3")
Frame2.place(relx=0.1, rely=0.35, relwidth=0.7, relheight=0.3)
Label(Frame2, text="Enter save location:", bg="SteelBlue3", fg='azure', font=('Courier', 13, 'bold')).place(relx=0.05, rely=0.2, relheight=0.08)
loc = Entry(Frame2, font=('Century 12'))
loc.place(relx=0.05, rely=0.4, relwidth=1, relheight=0.2)

Frame3 = Frame(wn, bg="SteelBlue3")
Frame3.place(relx=0.1, rely=0.55, relwidth=0.7, relheight=0.3)
Label(Frame3, text="Enter QR Code name:", bg="SteelBlue3", fg='azure', font=('Courier', 13, 'bold')).place(relx=0.05, rely=0.2, relheight=0.08)
name = Entry(Frame3, font=('Century 12'))
name.place(relx=0.05, rely=0.4, relwidth=1, relheight=0.2)

Frame4 = Frame(wn, bg="SteelBlue3")
Frame4.place(relx=0.1, rely=0.75, relwidth=0.7, relheight=0.2)
Label(Frame4, text="Enter size (1-40):", bg="SteelBlue3", fg='azure', font=('Courier', 13, 'bold')).place(relx=0.05, rely=0.2, relheight=0.08)
size = Entry(Frame4, font=('Century 12'))
size.place(relx=0.05, rely=0.4, relwidth=0.5, relheight=0.2)

Button(wn, text='Generate Code', font=('Courier', 15), command=generateCode).place(relx=0.35, rely=0.9, relwidth=0.25, relheight=0.05)

wn.mainloop()
