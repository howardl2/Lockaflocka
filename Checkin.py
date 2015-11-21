import tkinter
import team_class
from collections import namedtuple
from tkinter.test.support import destroy_default_root

DEFAULT_FONT = ('Helvetica', 14)

class TeamDialog:
    def __init__(self):
        self._dialog_window = tkinter.Toplevel()
         
        name_label = tkinter.Label(
            master = self._dialog_window, text = 'Enter Team Name:',
            font = DEFAULT_FONT)
         
        name_label.grid(
            row = 0, column = 0, columnspan = 1, padx = 10, pady = 10,
            sticky = tkinter.W)
 
        self._team_entry = tkinter.Entry(
            master = self._dialog_window, width = 20, font = DEFAULT_FONT)
 
        self._team_entry.grid(
            row = 0, column = 1, padx = 10, pady = 1,
            sticky = tkinter.E)
         
        button_frame = tkinter.Frame(master = self._dialog_window)
 
        button_frame.grid(
            row = 1, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)
 
        ok_button = tkinter.Button(
            master = button_frame, text = 'OK', font = DEFAULT_FONT,
            command = self._on_ok_button)
 
        ok_button.grid(row = 1, column = 0, padx = 10, pady = 10)
 
        cancel_button = tkinter.Button(
            master = button_frame, text = 'Cancel', font = DEFAULT_FONT,
            command = self._on_cancel_button)
 
        cancel_button.grid(row = 1, column = 1, padx = 10, pady = 10)
         
        self._dialog_window.rowconfigure(5, weight = 1)
        self._dialog_window.columnconfigure(1, weight = 1)
         
        self._team = ''
         
    def show(self) -> None:
       
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()
         
    def get_team(self) -> str:
        return self._team
     
    def _on_ok_button(self) -> None:
        self._ok_clicked = True
        self._team = self._team_entry.get()
        listOfTeams.append(team_class.Team(self._team, "", [], "", 0, 0))
        self._dialog_window.destroy()
         
         
    def _on_cancel_button(self) -> None:
        self._dialog_window.destroy()
 
class NameDialog:
    def __init__(self, team_name):
        self._dialog_window = tkinter.Toplevel()
        self._team_name = team_name


        who_label = tkinter.Label(
            master = self._dialog_window, text = 'Enter Player Information',
            font = DEFAULT_FONT)

        who_label.grid(
            row = 0, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)

        first_name_label = tkinter.Label(
            master = self._dialog_window, text = 'Name:',
            font = DEFAULT_FONT)

        first_name_label.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._first_name_entry = tkinter.Entry(
            master = self._dialog_window, width = 20, font = DEFAULT_FONT)

        self._first_name_entry.grid(
            row = 1, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        age_label = tkinter.Label(
            master = self._dialog_window, text = 'Age:',
            font = DEFAULT_FONT)

        age_label.grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._age_entry = tkinter.Entry(
            master = self._dialog_window, width = 20, font = DEFAULT_FONT)

        self._age_entry.grid(
            row = 2, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)
        
        position_label = tkinter.Label(
            master = self._dialog_window, text = 'Position:',
            font = DEFAULT_FONT)

        position_label.grid(
            row = 3, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._position_entry = tkinter.Entry(
            master = self._dialog_window, width = 20, font = DEFAULT_FONT)

        self._position_entry.grid(
            row = 3, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)
        

        button_frame = tkinter.Frame(master = self._dialog_window)

        button_frame.grid(
            row = 4, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)

        ok_button = tkinter.Button(
            master = button_frame, text = 'OK', font = DEFAULT_FONT,
            command = self._on_ok_button)

        ok_button.grid(row = 0, column = 0, padx = 10, pady = 10)

        cancel_button = tkinter.Button(
            master = button_frame, text = 'Cancel', font = DEFAULT_FONT,
            command = self._on_cancel_button)

        cancel_button.grid(row = 0, column = 1, padx = 10, pady = 10)

        self._dialog_window.rowconfigure(5, weight = 1)
        self._dialog_window.columnconfigure(1, weight = 1)


        self._ok_clicked = False
        self._first_name = ''
        self._age = ''
        self._position = ''


    def show(self) -> None:
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()


    def was_ok_clicked(self) -> bool:
        return self._ok_clicked


    def get_first_name(self) -> str:
        return self._first_name


    def get_age(self) -> str:
        return self._age
    
    def get_position(self) -> str:
        return self._position
    



    def _on_ok_button(self) -> None:
        self._ok_clicked = True
        self._first_name = self._first_name_entry.get()
        self._age = self._age_entry.get()
        self._position = self._position_entry.get()

        
       
#                
        p = Player(self._team_name, self._first_name, self._age, self._position)
        rosterList.append(p)
        for thing in listOfTeams:
            if (thing.team_to_str() == p.team):
                thing.players.append(p)
                print("list of players" + str(thing.players))
                
        
        f = open("Roster.txt", "a")
        f.write(str(p)+'\n')
        f.close()
        
        

        self._dialog_window.destroy()


    def _on_cancel_button(self) -> None:
        self._dialog_window.destroy()


class ViewRoster:
    def __init__(self, team_name):
        self._dialog_window = tkinter.Toplevel()
        self._team_name = team_name
        
        who_label = tkinter.Label(
            master = self._dialog_window, text = self._team_name+' Players',
            font = DEFAULT_FONT)

        who_label.grid(
            row = 0, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)
        
        listbox = tkinter.Listbox(master = self._dialog_window)
        listbox.grid(row = 1, column = 1, padx = 10, pady = 10)
        
        team_object = listOfTeams[0]
        for team in listOfTeams:
            if (team.team_to_str() == team_name):
                team_object = team
        for item in team_object.players:
            listbox.insert(tkinter.END, item.name)
            
    def show(self) -> None:
       
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()




class GreetingsApplication:
    def __init__(self):
        self._root_window = tkinter.Tk()
    
        greet_button = tkinter.Button(
            master = self._root_window, text = 'Add Player', font = DEFAULT_FONT,
            command = self._on_greet)

        greet_button.grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.S + tkinter.W)
        
        
        self._defaultVar = tkinter.StringVar(self._root_window)
        self._defaultVar.set("Select Team")
        self._team_entry= tkinter.OptionMenu(self._root_window, self._defaultVar, None)
        self._team_entry.grid(row = 0, column = 0, padx = 10, 
                        pady = 10, sticky = tkinter.N + tkinter.W)
        
        
        create_team_button = tkinter.Button(master = self._root_window, text = "Create Team", 
            font = DEFAULT_FONT, command = self._on_create_team)
        create_team_button.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N +tkinter.W)
        
       

        self._greeting_text = tkinter.StringVar()
        self._greeting_text.set('To be added: Team | Name | Age | Position')
      

        greeting_label = tkinter.Label(
            master = self._root_window, textvariable = self._greeting_text,
            font = DEFAULT_FONT)

        greeting_label.grid(
            row = 4, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.W )
        
        display_players_button = tkinter.Button(master = self._root_window, text = "Display Players",
                                                font = DEFAULT_FONT, command = self._on_display_players)
        
        display_players_button.grid(
            row = 3, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N +tkinter.W)

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.rowconfigure(4, weight = 1)
        self._root_window.columnconfigure(1, weight = 1)


    def start(self) -> None:
        self._root_window.mainloop()
        
        
    def _on_display_players(self):
        display_players = ViewRoster(self._defaultVar.get())
        display_players.show()



    def _on_greet(self) -> None:
        
        team_name = self._defaultVar.get()
        print(team_name)
        dialog = NameDialog(team_name)
        dialog.show()
        self._greeting_text.set('Successfully Added: {}|{}|{}|{}'.format(team_name, dialog.get_first_name(),
            dialog.get_age(), dialog.get_position()))
        self.update()

    
    
    def _on_create_team(self):
        create_team_dialog = TeamDialog()
        create_team_dialog.show()
        self.update()
        
        
        
    def update(self):
        self._team_entry.destroy()
        self._defaultVar = tkinter.StringVar(self._root_window)
        self._defaultVar.set("Select Team")
        teamNames = []
        for team in listOfTeams:
#             
            teamNames.append(team.team_to_str())
        self._team_entry = tkinter.OptionMenu(self._root_window, self._defaultVar, 
                                              *teamNames)
        self._team_entry.grid(row = 0, column = 0, padx = 10, 
                        pady = 10, sticky = tkinter.N + tkinter.W)
        
        
        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.rowconfigure(2, weight = 1)
        self._root_window.columnconfigure(1, weight = 1)
        
 
        

 
        
        
if __name__ == '__main__':
    listOfTeams = []
    rosterList = []
    
    Player = namedtuple('Player', 'team name age position')
    
    GreetingsApplication().start()
    for team in listOfTeams:
        print(team)
        
    for player in rosterList:
        print(player)
