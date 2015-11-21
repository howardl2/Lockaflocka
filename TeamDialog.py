import tkinter
import TeamPlayerDecs
DEFAULT_FONT = ('Helvetica', 14)

class TeamDialog:
    def __init__(self, list_of_teams):
        self._dialog_window = tkinter.Toplevel()
        self._listOfTeams = list_of_teams
        
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
        self._listOfTeams.append(TeamPlayerDecs.Team(self._team, "", [], "", 0, 0))
        self._dialog_window.destroy()
        
        
    def _on_cancel_button(self) -> None:
        self._dialog_window.destroy()

    




