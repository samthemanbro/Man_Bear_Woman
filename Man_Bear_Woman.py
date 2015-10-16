#using a class with Tkinter

from random import choice
from Tkinter import *

class Application(Frame):
    """a GUI application with three buttons. """

    def __init__(self, master):
        """Initialize the Frame"""
        Frame.__init__(self,master)
        self.grid()
        self.button_clicks =0 #count the number of button clicks
        self.create_widgets()
        self.Bear_clicks =0  #count the number of clicks on bear
        self.Man_clicks =0 #count on the clicks on man
        self.Woman_clicks =0 #count on Woman
        

    def create_widgets(self):
        """create button which desplays number of clicks"""
        self.instruction = Label(self, text = "Enter your name: ")
        self.instruction.grid(row= 0, column = 0, columnspan = 2, sticky = W)
        self.name = Entry(self)
        self.name.grid(row =0, column = 1, sticky = W)

        self.submit_button = Button(self, text = "Sumbit", command = self.reveal)
        self.submit_button.grid(row = 2, column = 0, sticky = W)

        self.Bear = Button(self, text = "Choose Bear", command = self.game1)
        
        self.Bear["command"] = self.game1
        
        #update_Bear_count
        self.Bear.grid(row = 3, column = 0, sticky = W)
        self.Man = Button(self, text = "Choose Man")
        self.Man["command"] = self.game2
        self.Man.grid(row = 3, column = 1, sticky = W)

        self.Woman = Button(self, text = "Choose woman")
        self.Woman ["command"] = self.game3
        self.Woman.grid(row = 3, column = 2, sticky = W)

        self.text = Text(self, width = 35, height = 5,wrap = WORD)
        self.text.grid(row = 4, column = 0, columnspan = 2, sticky = W)

        self.button = Button(self)
        self.button["text"] = "Total Clicks: 0"
        self.button["command"] = self.update_count
        self.button.grid()

    def reveal(self):
        content = self.name.get()

        message = "lets play bear man woman!       Bear kills the woman, the woman tricks the man, and the man beats the bear                                       "
        self.text.insert(0.0, message)
        
    def game1(self):
        #self.text.insert(0.0,"test 1")
        bmw = ['Bear', 'Man', 'Woman']
        py = choice(bmw)
        self.text.insert(0.0,py)
        
        if "Bear" == py:
            start = " you chose " + self.user + "I chose " + py + "hence a tie! "
            self.text.insert(0.0, start)
                
        elif py == "Woman":
            win1= " you entered Bear. I had Woman. You Win!                                                                                                                                                                 "
            self.text.insert(0.0, win1)
            u+=1
        elif py == "Man":
            win2= " you entered Bear. I had Man. you lose!                                                                                                                                                                            "
            self.text.insert(0.0, win2)
            v+=1

            
    def game2(self):
        #self.text.insert(0.0,"test 1")
        bmw = ['Bear', 'Man', 'Woman']
        py = choice(bmw)
        self.text.insert(0.0,py)
        
        if "Man" == py:
            start = " you chose " + self.user + "I chose " + py + "hence a tie! "
            self.text.insert(0.0, start)
                
        elif py == "Woman":
            win1= " you entered  Man. I had Woman. You lose!                                                                                                                                                            "
            self.text.insert(0.0, win1)
            u+=1
        elif py == "Bear":
            win2= " you entered Man. I had Bear. you win!                                                                                                                                                   "
            self.text.insert(0.0, win2)
            v+=1

            
    def game3(self):
        #self.text.insert(0.0,"test 1")
        bmw = ['Bear', 'Man', 'Woman']
        py = choice(bmw)
        self.text.insert(0.0,py)
        
        if "Woman" == py:
            start = " you chose " + self.user + "I chose " + py + "hence a tie! "
            self.text.insert(0.0, start)
                
        elif py == "Man":
            win1= " you entered Woman. I had Man. You Win!                                                                                                                                                 "
            self.text.insert(0.0, win1)
            u+=1
        elif py == "Bear":
            win2= " you entered Woman. I had Bear. you lose!                                                                                                                                                   "
            self.text.insert(0.0, win2)
            v+=1
       


       



        
    def game(self):
        
        
        #Bear = self.Bear.get()
        
        #Man = self.Man.get()
        #Woman = self.Woman.get()
        bmw = ['Bear', 'Man', 'Woman']
        #Bear == 'Bear'
        #Man == 'Man'
        #Woman == 'Woman'
        u = 0
        v = 0

        test = "this is a test"
        self.text.insert(0.0, test)
        #while 1:
             
             #user = "choose among the three buttons!"
        self.text.insert(0.0, "test")
        py = choice(bmw)

        if self.user == py:
            start = " you chose " + user + "I chose " + py + "hence a tie! "
            self.text.insert(0.0, start)
                
        elif self.user == "Bear" and py == "Woman":
            win1= " you entered Bear. I had Woman. You Win!"
            self.text.insert(0.0, win1)
            u+=1
        elif self.user == "Bear" and py == "Man":
            win2= " you entered Bear. I had Man. you lose!"
            self.text.insert(0.0, win2)
            v+=1
        elif self.user == "Woman" and py == "Man":
            win3= " you entered Woman. I had Man. you Win!"
            self.text.insert(0.0, win3)
            u+=1
        elif self.user == "Woman" and py == "Bear":
            win4= " you entered Woman. I had Bear. you lose!"
            self.text.insert(0.0, win4)
            v+=1
        elif self.user == "Man" and py == "Woman":
            win5= " you entered Man. I had Woman. you lose!"
            self.text.insert(0.0, win5)
            v+=1
        elif self.user == "Man" and py == "Bear":
            win6= " you entered Man. I had Bear. you win!"
            self.text.insert(0.0, win6)
            u+=1

            
                
            
            
                
                
        
        

    def update_count(self):
        """increase click count and display new total"""
        self.button_clicks += 1
        self.button["text"] = "total Clicks: " + str (self.button_clicks)

    def update_Bear_count(self):
        self.button_clicks += 1
        self.button["text"] = "total Clicks: " + str (self.button_clicks)
        self.Bear_clicks += 1
        self.Bear["text"] = "Choose Bear " + str (self.Bear_clicks)
        self.user="Bear"
        self.game1
        
    def update_Man_count(self):
        self.button_clicks += 1
        self.button["text"] = "total Clicks: " + str (self.button_clicks)
        self.Man_clicks += 1
        self.Man["text"] = "Choose Man " + str (self.Man_clicks)
        self.user = "Man"
        self.game
    def update_Woman_count(self):
        self.button_clicks += 1
        self.button["text"] = "total Clicks: " + str (self.button_clicks)
        self.Woman_clicks += 1
        self.Woman["text"] = "Choose Woman " + str (self.Woman_clicks)
        self.user = "Woman"
        self.game
         
root = Tk()
root.title("Sam's Bear, Man, Woman game")
root.geometry("500x500")

app = Application(root)

root.mainloop()

"""python tutorial 38 using text and entry widgets"""

