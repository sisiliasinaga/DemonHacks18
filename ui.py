#twitter analysis
import os
import tweetHashtagAnalysis

class hashtag (object):
    def __init__(self,has):
        self.exists = True
        self.output = ''
        self.hash = has
    def ifexists (self):
        x = ['hiyou','hi','nonono','imme'] #this would be the list of tweet replies (urls)
        if (self.hash in x):
            return self.exists
        else:
            return False
    def name(self):
        return self.hash   
    def __str__(self):
        return self.output

from tkinter import Tk, Label, Frame, Entry, Button
from tkinter.messagebox import showinfo
class ui(Tk):
    def __init__(self,parent=None):
        Tk.__init__(self,parent)
        self.title('Personality Analysis')
        self.make_widgets()
    def calc_reponse(self):
        self.tweet = hashtag(self.hashT.get())
        hashAnalysis(self.tweet)
        """
        if (self.tweet.ifexists()):
            response = str(self.tweet)
            showinfo(message= str(self.hashT.get())+' exists.\n'+ response)
        else:
            showinfo(message= 'This hashtag doesn\'t exist.\nEnter another.')
            """
    def make_widgets(self):
        Label(self, text='Hashtag to search:',width=40).pack()
        self.hashT = Entry(self, width = 40)
        self.hashT.pack()
        Button(self,text='Submit', command=lambda:self.calc_reponse()).pack()
                
ui().mainloop()
