#import tkinter as tk

#class gui:

#	def __init__(self):
#		self.window = tk.Tk(className="scraper.prototype")

#		self.window.geometry("900x500")
#		self.window.resizable(width=False, height=False)
#
#		self.urlLabel = tk.Label(text="Insert URL")
#		self.urlEntry = tk.Entry(width=55)
#
#		self.urlLabel.pack()
#		self.urlLabel.place(x=10, y=12)
#		self.urlEntry.pack()
#		self.urlEntry.place(x=90, y=12)
#
#		self.confirmButton = tk.Button(master=self.window, text="Confirm", width=15, height=1)
#		self.confirmButton.pack()
#		self.confirmButton.place(x=550, y=10)
#
#		self.clearButton = tk.Button(master=self.window, text="Clear", width=15, height=1, command=self.clearAll)
#		self.clearButton.pack()
#		self.clearButton.place(x=730, y=10)
#
#		self.allTextArea = tk.Text(width=60, height=29)
#		self.allTextArea.pack()
#		self.allTextArea.place(x=10, y=50)
#
#		self.topicArea = tk.Text(width=60, height=29)
#		self.topicArea.pack()
#		self.topicArea.place(x=460, y=50)
#
#		self.window.mainloop()
#
#	def setTextArea(valueToWrite):
#
#		self.allTextArea.insert(tk.END, valueToWrite)
#		self.allTextArea.config(state="disabled")
#
#	def setTopicText(valueToWrite):
#
#		self.topicArea.insert(ek.END, valueToWrite)
#		self.topicArea.config(state="disabled")
#
#	def clearAll(self):
#
#		self.allTextArea.config(state="normal")
#		self.topicArea.config(state="normal")
#		self.allTextArea.delete('1.0', END)
#		self.topicArea.delete('1.0', END)
#
#	def printHello():
#		print("Hello")