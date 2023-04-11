import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        # Initialize the frame
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=2, column=0, padx=(10,10) , pady=(10,10)) 

        # Create text entry widget for user input
        self.user_input = Entry(self.master, width=50)
        self.user_input.grid(row=0, column=0, padx=10, pady=10)

        # Create button to initiate HTML page generation process
        self.generate_btn = Button(self.master, text="Generate Web Page", width=30, height=2, command=self.generateHTML)
        self.generate_btn.grid(row=1, column=0, padx=10, pady=10)

        #self.btn = Button(self.master, text="Default HTML Page", width=30, height=2)
        #self.btn.grid(padx=(10,10) , pady=(10,10)) 

    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    def generateHTML(self):
        htmlText = self.user_input.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
