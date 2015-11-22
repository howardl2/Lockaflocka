# TeamPlayer.py


# TeamPlayer.py


import tkinter
import TeamPlayerDecs
import TeamDialog
import PlayerDialog
import DisplayPlayersDialog
from collections import namedtuple
from tkinter.test.support import destroy_default_root

DEFAULT_FONT = ('Helvetica', 14)


# GreetingsApplication is the root window - main one
# Can Select team, create team, add player, display players
class TeamPlayerApplication:
    def __init__(self, list_of_teams, roster_list):
        self._root_window = tkinter.Tk()
        self._listOfTeams = list_of_teams
        self._roster_list = roster_list
        
        #add player button
        add_player_button = tkinter.Button(
            master = self._root_window, text = 'Add Player', font = DEFAULT_FONT,
            command = self._on_greet)

        add_player_button.grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.S + tkinter.W)
        
        #team select option menu
        self._teamOption = tkinter.StringVar(self._root_window)
        self._teamOption.set("Select Team")
        self._teamOptionMenu= tkinter.OptionMenu(self._root_window, self._teamOption, None)
        self._teamOptionMenu.grid(row = 0, column = 0, padx = 10, 
                        pady = 10, sticky = tkinter.N + tkinter.W)
        
        #create new team button
        create_team_button = tkinter.Button(master = self._root_window, text = "Create Team", 
            font = DEFAULT_FONT, command = self._on_create_team)
        create_team_button.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N +tkinter.W)
        
        #display players of selected team button
        display_players_button = tkinter.Button(master = self._root_window, text = "Display Players",
                                                font = DEFAULT_FONT, command = self._on_display_players)
        
        display_players_button.grid(
            row = 3, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N +tkinter.W)
        
        #display number of teams text
        self._num_teams_text = tkinter.StringVar()
        self._num_teams_text.set('Number of teams: '+ str(len(self._listOfTeams)))

        #display number of teams label
        self._num_teams_label = tkinter.Label(
            master = self._root_window, textvariable = self._num_teams_text,
            font = DEFAULT_FONT)

        self._num_teams_label.grid(
            row = 4, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.W )

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.rowconfigure(4, weight = 1)
        self._root_window.columnconfigure(1, weight = 1)


    def start(self) -> None:
        self._root_window.mainloop()
        
        
    def _on_display_players(self):
        display_players = DisplayPlayersDialog.DisplayPlayersDialog(self._teamOption.get(), self._listOfTeams)
        display_players.show()



    def _on_greet(self) -> None:
        team_name = self._teamOption.get()
        dialog = PlayerDialog.PlayerDialog(team_name,self._listOfTeams, self._roster_list)
        dialog.show()
#         self._num_teams_text.set('Successfully Added: {}|{}|{}|{}'.format(team_name, dialog.get_first_name(),
#             dialog.get_age(), dialog.get_position()))
        self.update()
        
    def _on_create_team(self):
        create_team_dialog = TeamDialog.TeamDialog(self._listOfTeams)
        create_team_dialog.show()
        self.update()
        
        
        
    def update(self):
        self._teamOptionMenu.destroy()
        self._teamOption = tkinter.StringVar(self._root_window)
        self._teamOption.set("Select Team")
        teamNames = []
        for team in self._listOfTeams:
            teamNames.append(team.team_to_str())
        self._teamOptionMenu = tkinter.OptionMenu(self._root_window, self._teamOption, 
                                              *teamNames)
        self._teamOptionMenu.grid(row = 0, column = 0, padx = 10, 
                        pady = 10, sticky = tkinter.N + tkinter.W)
        
        self._num_teams_label.destroy()
        self._num_teams_text = tkinter.StringVar()
        self._num_teams_text.set('Number of teams: ' + str(len(self._listOfTeams)))
        
        self._num_teams_label = tkinter.Label(
            master = self._root_window, textvariable = self._num_teams_text,
            font = DEFAULT_FONT)

        self._num_teams_label.grid(
            row = 4, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.W )

        
        
        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.rowconfigure(2, weight = 1)
        self._root_window.columnconfigure(1, weight = 1)
     

    
    
