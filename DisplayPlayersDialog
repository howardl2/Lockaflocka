import tkinter

DEFAULT_FONT = ('Helvetica', 14)

class DisplayPlayersDialog:
    def __init__(self, team_name, list_of_teams):
        self._dialog_window = tkinter.Toplevel()
        self._team_name = team_name
        self._list_of_teams = list_of_teams
        
        who_label = tkinter.Label(
            master = self._dialog_window, text = self._team_name+' Players',
            font = DEFAULT_FONT)

        who_label.grid(
            row = 0, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)
        
        listbox = tkinter.Listbox(master = self._dialog_window)
        listbox.grid(row = 1, column = 1, padx = 10, pady = 10)
        
        team_object = self._list_of_teams[0]
        for team in self._list_of_teams:
            if (team.team_to_str() == team_name):
                team_object = team
        for item in team_object.players:
            listbox.insert(tkinter.END, item.name)
            
    def show(self) -> None:
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()
        
        
