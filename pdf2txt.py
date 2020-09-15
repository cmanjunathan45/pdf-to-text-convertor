from tkinter import *
import tkinter as tk
from tkinter import filedialog,messagebox 
import PyPDF2
import tkinter as ttk
from tkinter.scrolledtext import ScrolledText
import webbrowser

root=tk.Tk()
root.title("PDF Extractor | Manjunathan C")
root.geometry("500x200")
root.config(bg="skyblue")
root.iconphoto(False,tk.PhotoImage(file="icon.png"))

def file():
	try:
		try:
			file=filedialog.askopenfile(filetypes=[("PDF","*pdf")])
			pdf_file=open(file.name,"rb")
			read_pdf =PyPDF2.PdfFileReader(pdf_file)
			number_of_pages=read_pdf.getNumPages()
			page=read_pdf.getPage(number_of_pages-1)
			page_content=page.extractText()
			print(page_content)
		except:
			messagebox.showerror("Error","Unknown file type\nor\nPlease choose valid file")
		def new():
			root1=tk.Tk()
			root1.config(bg="skyblue")
			root1.title("TEXT WINDOW | Manjunathan C")
			root1.geometry("1400x700")
			root.iconphoto(True,tk.PhotoImage(file="icon.png"))
			tex=ScrolledText(root1,font=("fontawesome",10,"bold italic"),bg="skyblue",fg="darkblue",height=40,width=160,borderwidth=5)
			tex.pack()
			tex.insert(tk.END,page_content)
			def save():
				root1.filename = filedialog.asksaveasfile(mode="w",defaultextension='.txt')
				if root1.filename is None:
						return
				file_save =  str(tex.get(1.0,END))
				root1.filename.write(file_save)
				root1.filename.close()
			buttons=Button(root1,text="SAVE",font=("fontawesome",10,"bold italic"),bg="darkblue",fg="skyblue",command=save)
			buttons.place(x=540,y=600)
			buttoncl=Button(root1,text="CLEAR",font=("fontawesome",10,"bold italic"),bg="darkblue",fg="skyblue",command=lambda: tex.delete("1.0",END))
			buttoncl.place(x=640,y=600)
				
			buttonex=Button(root1,text="EXIT",font=("fontawesome",10,"bold italic"),bg="darkblue",fg="skyblue",command=root1.quit)
			buttonex.place(x=740,y=600)

			buttonco=Button(root1,text="CONTACT",font=("fontawesome",10,"bold italic"),bg="darkblue",fg="skyblue",command=lambda :webbrowser.open("https://github.com/cmanjunathan45/"))
			buttonco.place(x=628,y=650)


		new()
		pdf_file.close()
	except:
		messagebox.showerror("Error","Unknown Error Occured")
	

def exit():
        message = messagebox.askquestion('PDF Extractor',"Do you want to close?")
        if message == "yes":
                root.quit()

label1=Label(root,text="PDF TO TEXT CONVERTOR",font=("font awesome",15,"bold italic"),bg="skyblue",fg="darkblue")
label1.place(x=100,y=10)

label1=Label(root,text="Choose the File",font=("font awesome",15,"bold italic"),bg="skyblue",fg="darkblue")
label1.place(x=150,y=45)

button1=Button(root,text="Choose",font=("font awesome",15,"bold italic"),bg="darkblue",fg="skyblue",command=file)
button1.place(x=180,y=85)

button2=ttk.Button(root,text="Exit",font=("font awesome",15,"bold italic"),bg="darkblue",fg="skyblue",command=exit)
button2.place(x=200,y=125)

root.mainloop()