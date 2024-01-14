from tkinter import Text, StringVar, Entry, Tk, Button, Frame, ttk, PanedWindow, END
from ModCalcular import calculate
import functools

#-----Color variables-----
color0="#26233a" #_BackGround
color1="#26233a" #_BackGround_Botones
color2="#1f1d2e" #_BackGround_TextBox
color3="#eb6f92" #_Botones_Letras
color4="#eb6f92" #_TextBox_Letras
color5="#191724" #_Bordes_TextBox

#-----Frame-----
class Window(Frame):
    def buttonPrint(self, text=""):
        self.In.insert(len(self.In.get()), text)

    def buttonClean(self):
        self.In.delete(len(self.In.get())-1, END)

    def buttonCleanC(self):
        self.In.delete(0, END)

    def buttonCleanAC(self):
        self.In.delete(0, END)
        self.Out.delete("1.0", END)

    def buttonResult(self):
        self.Out.delete("1.0", END)
        self.Out.insert(END, str(calculate(str(self.In.get())))+"\n\n")
        
    def __init__(self, master):
        super().__init__(master)
        
        self.btnx = 50
        self.btny = 40
        self.enty = 60 
        self.txtx = 350
        self.btnpy = self.enty
    
        master.geometry(str(self.btnx*6 + self.txtx)+"x"+str(self.btnpy + self.btny*7))
        master.configure(bg = color0)
        master.resizable(width=False, height=False)
        master.title("Calculator")
        
        #--Texto de Salida--
        #strCalc1 = StringVar() 
        #self.Out = Entry(master)
        #self.Out.place(x = 0, 
                        #               y = 0, 
                        #width = self.btnx*6, 
                        #height = self.enty)
        #self.Out.configure(font = ("Cambria", "17"), 
                            #                   bg = color2, 
                            #fg = color4, 
                            # textvariable = strCalc1, 
                            #insertbackground = "white", 
                            #highlightthickness = 1, 
                            #highlightcolor = "white", 
                            #relief = "flat")

        #--Texto de Salida--
        self.Out = Text(master)
        self.Out.place(x = self.btnx*6, 
                      y = 0, 
                      width = self.txtx, 
                      height = self.btnpy + self.btny*7)
        self.Out.configure(font = ("Cambria", "16"), 
                           bg = color2, 
                           fg = color4, 
                           insertborderwidth = 1, 
                           insertbackground = "white", 
                           bd = 0, 
                           highlightthickness = 1, 
                           highlightcolor = color5)


        #--Texto de Entrada--
        strCalc2 = StringVar() 
        self.In = Entry(master)
        self.In.place(x = 0, 
                      y = 0, 
                      width = self.btnx*6, 
                      height = self.enty)
        self.In.configure(font = ("Cambria", "17"), 
                           bg = color2, 
                           fg = color4, 
                           textvariable = strCalc2, 
                           insertbackground = "white", 
                           highlightthickness = 1, 
                           highlightcolor = "white", 
                           relief = "flat")
        self.In.focus()

        self.frame_objects(master)

    def frame_objects(self, master):
        #--Botones--
        info_btn = [
                    {"text":"π", "x":0, "y":self.btnpy, "width":self.btnx, "print":"π"}, 
                    {"text":"e", "x":self.btnx, "y":self.btnpy, "width":self.btnx, "print":"e"},
                       #
                       #
                       #

                    {"text":"and", "x":0, "y":self.btnpy + self.btny, "width":self.btnx, "print":"&"},
                    {"text":"not", "x":self.btnx, "y":self.btnpy + self.btny, "width":self.btnx, "print":"~"},
                    {"text":"(", "x":self.btnx*2, "y":self.btnpy + self.btny, "width":self.btnx, "print":"("},
                    {"text":")", "x":self.btnx*3, "y":self.btnpy + self.btny, "width":self.btnx, "print":")"},
                       #

                    {"text":"!x", "x":0, "y":self.btnpy + 2*self.btny, "width":self.btnx, "print":"!"},
                    {"text":"√", "x":self.btnx, "y":self.btnpy + 2*self.btny, "width":self.btnx, "print":"√("},
                    {"text":"^", "x":self.btnx*2, "y":self.btnpy + 2*self.btny, "width":self.btnx, "print":"^"},      
                    {"text":".", "x":self.btnx*3, "y":self.btnpy + 2*self.btny, "width":self.btnx, "print":"."},
                    {"text":"x", "x":self.btnx*4, "y":self.btnpy + 2*self.btny, "width":self.btnx*2, "print":"x"},
                    
                    {"text":"sin¯¹", "x":0, "y":self.btnpy + 3*self.btny, "width":self.btnx, "print":"sin¯¹("},
                    {"text":"sin", "x":self.btnx, "y":self.btnpy + 3*self.btny, "width":self.btnx, "print":"sin("},
                    {"text":"+", "x":self.btnx*2, "y":self.btnpy + 3*self.btny, "width":self.btnx, "print":"+"},
                    {"text":"7", "x":self.btnx*3, "y":self.btnpy + 3*self.btny, "width":self.btnx, "print":"7"},
                    {"text":"8", "x":self.btnx*4, "y":self.btnpy + 3*self.btny, "width":self.btnx, "print":"8"}, 
                    {"text":"9", "x":self.btnx*5, "y":self.btnpy + 3*self.btny, "width":self.btnx, "print":"9"},
                    
                    {"text":"cos", "x":0, "y":self.btnpy + 4*self.btny, "width":self.btnx, "print":"cos("},
                    {"text":"cos¯¹", "x":self.btnx, "y":self.btnpy + 4*self.btny, "width":self.btnx, "print":"cos¯¹("},
                    {"text":"-", "x":self.btnx*2, "y":self.btnpy + 4*self.btny, "width":self.btnx, "print":"-"},
                    {"text":"4", "x":self.btnx*3, "y":self.btnpy + 4*self.btny, "width":self.btnx, "print":"4"},
                    {"text":"5", "x":self.btnx*4, "y":self.btnpy + 4*self.btny, "width":self.btnx, "print":"5"}, 
                    {"text":"6", "x":self.btnx*5, "y":self.btnpy + 4*self.btny, "width":self.btnx, "print":"6"}, 
                    
                    {"text":"tan", "x":0, "y":self.btnpy + 5*self.btny, "width":self.btnx, "print":"tan("},
                    {"text":"tan¯¹", "x":self.btnx, "y":self.btnpy + 5*self.btny, "width":self.btnx, "print":"tan¯¹("},
                    {"text":"*", "x":self.btnx*2, "y":self.btnpy + 5*self.btny, "width":self.btnx, "print":"*"},
                    {"text":"1", "x":self.btnx*3, "y":self.btnpy + 5*self.btny, "width":self.btnx, "print":"1"},
                    {"text":"2", "x":self.btnx*4, "y":self.btnpy + 5*self.btny, "width":self.btnx, "print":"2"},
                    {"text":"3", "x":self.btnx*5, "y":self.btnpy + 5*self.btny, "width":self.btnx, "print":"3"},
                    
                    {"text":"/", "x":0, "y":self.btnpy + 6*self.btny, "width":self.btnx, "print":"/"},
                    {"text":"log", "x":self.btnx, "y":self.btnpy + 6*self.btny, "width":self.btnx, "print":"log("},
                    {"text":"ln", "x":self.btnx*2, "y":self.btnpy + 6*self.btny, "width":self.btnx, "print":"ln("},
                    {"text":"0", "x":self.btnx*3, "y":self.btnpy + 6*self.btny, "width":self.btnx*3, "print":"0"}
                    ]

        for info in info_btn:     
            btn = Button(master, 
                         text = info["text"], 
                         command = functools.partial(self.buttonPrint, 
                                                     text = info["print"]))
            btn.place(x = info["x"], 
                      y = info["y"], 
                      width = info["width"], 
                      height = self.btny)
            btn.configure(font = ("Cambria", "15"), 
                          background = color1, 
                          highlightcolor = color5, 
                          fg = color3, 
                          bd = 0)

        info_btn = [
            {"text" : "←","function" : self.buttonClean, "x": self.btnx*4, "y": self.btnpy + self.btny,"width": self.btnx*2},
            {"text" : "C", "function" : self.buttonCleanC, "x": self.btnx*3, "y": self.btnpy, "width": self.btnx},
            {"text" : "AC", "function" : self.buttonCleanAC, "x": self.btnx*2, "y": self.btnpy, "width": self.btnx},
            {"text" : "=", "function" : self.buttonResult, "x": self.btnx*4, "y": self.btnpy, "width": self.btnx*2}]

        for info in info_btn:    
            btn = Button(master, 
                         text = info["text"], 
                         command = info["function"])
            btn.place(x = info["x"], 
                      y = info["y"], 
                      width = info["width"], 
                      height = self.btny)
            btn.configure(font = ("Caviar_Dreams", "15"), 
                          background = color1, 
                          highlightcolor = color5, 
                          fg = color3, 
                          bd = 0)

if __name__ == "__main__":
    app = Window(Tk())
    app.mainloop()

