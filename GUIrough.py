from tkinter import *
from tkinter import ttk
from PIL import Image

team_array = ["BAL", "BOS", "CHA", "CLE", "COL", "DET", "KCA", "LAN", "MIL", "MIN", "NYY", "OAK", "SEA", "TBA", "TEX", "TOR", "ATL", "CHN", "CIN", "MIA", "HOU", "NYN", "PHI", "PIT", "SDN", "SFN", "SLN", "WAS", "ARI", "LAN"]
img_array = list(range(0,30))

k = 0
for i in team_array:
    img_array[k] = Image.open(i + ".png")
    k = k + 1

##Example predictions
##[team1, team2, score1, score2, pitcher1, pitcher2, inning, chance1, chance2]

examplePreds = [["BOS", "NYY", 4, 0, "pitcherA", "pitcherB",5, 77.8, 22.2], ["SFN", "LAD", 1, 0, "pitcherC", "pitcherD", 2, 55.5, 45.5], ["CHA", "CHN", 7, 1, "pitcherE", "pitcherF", 8, 91.5, 8.5], ["MIL", "DEN", 3, 2, "pitcherG", "pitcherH", 6, 63.7, 37.3]]

root = Tk()
root.title("Game Predictions")

mainframe = ttk.Frame(root, padding = "6 6 15 15")
mainframe.grid(column = 0, row = 0, sticky = (N,W,E,S))
root.columnconfigure(0,weight = 1)
root.rowconfigure(0, weight = 1)

k = 1

for i in examplePreds:
    ttk.Label(mainframe, text = "Game " + str(k)).grid(column = 1, row = 4 * k -3, sticky = (W,E))
    ttk.Label(mainframe, text = "Team").grid(column = 1, row = 4 * k - 2, sticky = (W,E))
    ttk.Label(mainframe, text = "Score").grid(column = 2, row = 4 * k - 2, sticky = (W,E))
    ttk.Label(mainframe, text = "Pitcher").grid(column = 3, row = 4 * k - 2, sticky = (W,E))
    ttk.Label(mainframe, text = "Inning").grid(column = 4, row = 4 * k - 2, sticky = (W,E))
    ttk.Label(mainframe, text = "Chance to Win").grid(column = 5, row = 4 * k - 2, sticky = (W,E))


    ttk.Label(mainframe, text = i[0]).grid(column = 1, row = 4 * k - 1, sticky = (W,E))
    ttk.Label(mainframe, text = i[1]).grid(column = 1, row = 4 * k, sticky = (W,E))
    ttk.Label(mainframe, text = i[2]).grid(column = 2, row = 4 * k - 1, sticky = (W,E))
    ttk.Label(mainframe, text = i[3]).grid(column = 2, row = 4 * k, sticky = (W,E))
    ttk.Label(mainframe, text = i[4]).grid(column = 3, row = 4 * k - 1, sticky = (W,E))
    ttk.Label(mainframe, text = i[5]).grid(column = 3, row = 4 * k, sticky = (W,E))
    ttk.Label(mainframe, text = i[6]).grid(column = 4, row = 4 * k - 1, sticky = (W,E))
    ttk.Label(mainframe, text = i[7]).grid(column = 5, row = 4 * k - 1, sticky = (W,E))
    ttk.Label(mainframe, text = i[8]).grid(column = 5, row = 4 * k, sticky = (W,E))

    k = k + 1


root.mainloop()

