import tkinter
import TeamPlayerDecs
DEFAULT_FONT = ('Helvetica', 14)

class PlayerDialog:
    def __init__(self, team_name, list_of_teams, roster_list):
        # A Toplevel object is  a
        # separate, additional window.
        self._dialog_window = tkinter.Toplevel()
        self._team_name = team_name
        self._list_of_teams = list_of_teams
        self._roster_list = roster_list


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

        p = TeamPlayerDecs.Player(self._team_name, self._first_name, self._age, self._position)
        self._roster_list.append(p)
        for thing in self._list_of_teams:
            if (thing.team_to_str() == p.team):
                thing.players.append(p)
                print("list of players" + str(thing.players))
                
        
        f = open("Roster.txt", "a")
        f.write(str(p)+'\n')
        f.close()
        
        

        self._dialog_window.destroy()


    def _on_cancel_button(self) -> None:
        self._dialog_window.destroy()
        
        
        
