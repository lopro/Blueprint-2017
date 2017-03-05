###########
# Imports #
###########
from flask import Flask
from flask import render_template
from flask import request
from operator import itemgetter
import json

######################
# App initialization #
######################
app = Flask("Decide")

##############
# Collection #
##############
class Collection:
    def __init__(self):
        # names contains the names of the user
        # items contains the names of the options
        # cats contains the names of the catergories
        # data contains tuples of (catergory, weight)
        # ordered by score (maximum to minimum)
        self.names = []
        self.cats = []
        self.data = [][]
        # self.capacity = 10 # maximum leaderboard capacity

    def submit_names(self, names):
        self.cats.append(names)
        # self.cats = sorted(self.scores, key=itemgetter(1), reverse=True)
        # if len(self.scores) > self.capacity:
        #     # Remove lowest score if over capacity
        #     self.scores.pop(self.capacity)

    def submit_categories(self, criteria[], weights[]):
        var i = 0
        while i in range(len(criteria)):
            self.cats.append({criteria[i], weights[i]})

leaderboard = Leaderboard()

##########
# Routes #
##########

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cats", methods=["POST"])
def scores():
    # Extract data from request
    name = request.json["name"]
    score = request.json["score"]
    print ("Received score " + str(score) + " from " + name)
    leaderboard.submit_score(name, score)
    return json.dumps({"status": "OK", "scores": leaderboard.scores})

if __name__ == "__main__":
    app.run()
