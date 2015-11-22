from tkinter import *
from tkinter.ttk import *
from tkinter.colorchooser import *
import tkinter.font
import TeamPlayer


class main_canvas:
    def __init__(self):
        self.root_window = Tk()
        self.canvas = Canvas(self.root_window, bg = "blue")

        def getColor():
            color = askcolor()
            print(color)

        Button(text = "Select Color", command = getColor).grid(row = 5)
        
        bold_font = tkinter.font.Font(family = "Helvetica", size = "14", weight = "bold")

        dropdown_font = tkinter.font.Font(family = "Helvetica", size = "10")
        
        
        style = Style()
        style.configure("Label", foreground = "#00006c")
       
    ###Create text boxes###
        ##Tournament type##
        saved_tourney = StringVar(self.root_window)
        saved_tourney.set("Single Elimination")
        tourney_label = Label(self.root_window, text = "Tournament style: ", style = "Label", font = bold_font)
        tourney_label.grid(row = 0, column = 0)
        tourney_entry = OptionMenu(self.root_window, saved_tourney, "Single Elimination", \
                                   "Single Elimination", "Double Elimination", "Round Robin")
        tourney_entry.config(width = 20)
        tourney_entry["menu"].config(fg="#169ea9", font = dropdown_font)
        tourney_entry.grid(row = 0, column = 1)

        ##Game type##
        saved_game = StringVar(self.root_window)
        saved_game.set("League of Legends")
        game_label = Label(self.root_window, text = "Game Type: ", style = "Label", font = bold_font)
        game_label.grid(row = 1, column = 0)
        game_entry = OptionMenu(self.root_window, saved_game, "League of Legends", "League of Legends", "DOTA", "Heroes of the Storm",\
                                "Starcraft 2", "Call of Duty", "Super Smash Bros Melee",\
                                "Halo 5", "Super Smash Bros 4")
        game_entry.config(width = 20)
        game_entry["menu"].config(fg="#169ea9", font = dropdown_font)

        game_entry.grid(row = 1, column = 1)
        ##Series type##
        saved_series = StringVar(self.root_window)
        saved_series.set("Best of 1")
        series_label = Label(self.root_window, text = "Series Type: ", style = "Label", font = bold_font)
        series_label.grid(row = 2, column = 0)
        series_entry = OptionMenu(self.root_window, saved_series, "Best of 1", "Best of 1", "Best of 3", \
                                  "Best of 5", "Best of 7", "Best of 9", "Best of 11")
        series_entry.config(width = 20)
        series_entry["menu"].config(fg="#169ea9", font = dropdown_font)
        series_entry.grid(row = 2, column = 1)
        ##Final series type##
        saved_final = StringVar(self.root_window)
        saved_final.set("Best of 1")
        final_label = Label(self.root_window, text = "Finals Series Type: ", style = "Label", font = bold_font)
        final_label.grid(row = 3, column = 0)
        final_entry = OptionMenu(self.root_window, saved_final, "Best of 1", "Best of 1", "Best of 3", \
                                  "Best of 5", "Best of 7", "Best of 9", "Best of 11")
        final_entry.config(width = 20)
        final_entry["menu"].config(fg="#169ea9", font = dropdown_font)
        

        final_entry.grid(row = 3, column = 1)
        
        def get_entries():
            print("Tournament type:", saved_tourney.get())
            print("Game type:", saved_game.get())
            print("Series type:", saved_series.get())
            print("Finals series type:", saved_final.get())
#             self.root_window.quit()
            self.root_window.destroy()
        test = Button(self.root_window, text = "TEST", command = get_entries)
        test.grid(row = 5, ipadx = 20, column = 1, sticky = 'w')
        '''
        def check_errors():
            if not num_teams_entry.get().isdigit():
                messagebox.showerror("Error", "Please enter a valid number of teams")
            
        
        button = Button(self.root_window, text = "Done", command = check_errors)
        button.pack(fill=X)
        '''
        def closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.root_window.destroy()
        self.root_window.protocol("WM_DELETE_WINDOW", closing)
        
        def done():
            if messagebox.askokcancel("Done", "Are you sure you are done?"):
                self.root_window.destroy()
        Button(self.root_window, text = "Done", command = done).grid(row = 4,ipadx = 20, column = 1, sticky = 'w')
        self.root_window.mainloop()
     


    def start(self):
        self.canvas
    
        

    def get_tourney_type(self):
        return saved_tourney.get()

    def get_game_type(self):
        return saved_game.get()

    def get_series_type(self):
        return saved_series.get()

    def get_finals_series_type(self):
        return saved_final.get()
        
            
        







if __name__ == '__main__':
    main_canvas().start()
    listOfTeams = []
    rosterList = []
    
    TeamPlayer.TeamPlayerApplication(listOfTeams, rosterList).start()
 
    numTeams = len(listOfTeams)
    print("number of teams: " + str(numTeams))
    
