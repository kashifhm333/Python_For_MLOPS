class football:
    def __init__(self):
        self.team = "Real Madrid"
        self.coach = "Carlo Ancelotti"
        self.players = ["Cristiano Ronaldo", "Neymar", "Suarez"]
    
    def display(self):
        print("Team:", self.team)
        print("Coach:", self.coach)
        print("Players:", ", ".join(self.players))

player = football()
player.display()