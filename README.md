# Lockaflocka
HackUCI 2015

Develop a tournament organization application that allows organizers to keep track of and update team information and create brackets to set up tournament style play. Designed with an emphasis on esports.

What is the criteria?
Create an esports event/tournament management and bracket application.
Application needs
All standard tournament formats
Customizable
Check in interface
Score/result updates

RUN THROUGH "tourney_info_window.py"


After throwing away a previous project from aiming a bit too high and being a totally new team of hackers, we used what experience and time we had left to create an esports tournament bracket creator.

What we accomplished:
-tourney display window that takes in tournament style, game type, series type, and finals series type (drop down menus)
-check in window that adds teams to the program, adds in player data to teams, and displays that teams players (must 
first select a team after creating one; drop down menu)
-the logic to simulate an entire single elimination tournament (creates bracket based on number of teams, accounts for first round byes, eliminates teams upon selecting winners, putting byes on correct sides of the tournament)
-the gui for the single elimination tournament upon starting the tournament (displays the teams in the first 2 rounds correctly)

Unfinished:
-connecting the files so that the logic could update with manual input, not test statements
-updating the gui as the tournament progresses

Supplemental end goals:
-fancier gui
-selection of bracket types
-accounting for different game types
-direct gui interaction
-gui displays team/game info

Contributors:
Howard Liu - tourney display window
Vivian Thach and Henry Tran - check in window (create teams, add players (must select a team), display players (must select a team))
Ryan Chan and Aaron Ching - single elimination logic, bracket gui (displays the teams in the first 2 rounds correctly)


