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
#     def __init__(self):
#         # names contains the names of the user
#         # items contains the names of the options
#         # cats contains the names of the catergories
#         # data contains tuples of (catergory, weight)
#         # ordered by score (maximum to minimum)
#         self.names = []
#         self.cats = []
#         self.data = [][][]
#         # self.capacity = 10 # maximum leaderboard capacity

#     def submit_names(self, names):
#         self.cats.append(names)
#         # self.cats = sorted(self.scores, key=itemgetter(1), reverse=True)
#         # if len(self.scores) > self.capacity:
#         #     # Remove lowest score if over capacity
#         #     self.scores.pop(self.capacity)

#     def submit_categories(self, criteria[], weights[]):
#         var i = 0
#         while i in range(len(criteria)):
#             self.cats.append({criteria[i], weights[i]})
    
    var name1
    var name2
    var name3
    var name4
    
    var item1
    var item2
    var item3
    var item4
    
    var cri1
    var cri2
    var cri3
    var cri4
    
    var weight1
    var weight2
    var weight3
    var weight4
    
    var ascore1
    var ascore2
    var ascore3
    var ascore4
    var ascore5
    var ascore6
    var ascore7
    var ascore8
    var ascore9
    var ascore10
    var ascore11
    var ascore12
    var ascore13
    var ascore14
    var ascore15
    var ascore16
    
    var bscore1
    var bscore2
    var bscore3
    var bscore4
    var bscore5
    var bscore6
    var bscore7
    var bscore8
    var bscore9
    var bscore10
    var bscore11
    var bscore12
    var bscore13
    var bscore14
    var bscore15
    var bscore16
    
    var cscore1
    var cscore2
    var cscore3
    var cscore4
    var cscore5
    var cscore6
    var cscore7
    var cscore8
    var cscore9
    var cscore10
    var cscore11
    var cscore12
    var cscore13
    var cscore14
    var cscore15
    var cscore16
    
    var dscore1
    var dscore2
    var dscore3
    var dscore4
    var dscore5
    var dscore6
    var dscore7
    var dscore8
    var dscore9
    var dscore10
    var dscore11
    var dscore12
    var dscore13
    var dscore14
    var dscore15
    var dscore16
    
    var atotal1 = weight1*ascore1
    var atotal2 = weight2*ascore2
    var atotal3 = weight3*ascore3
    var atotal4 = weight4*ascore4
    var atotal5 = weight1*ascore5
    var atotal6 = weight2*ascore6
    var atotal7 = weight3*ascore7
    var atotal8 = weight4*ascore8
    var atotal9 = weight1*ascore9
    var atotal10 = weight2*ascore10
    var atotal11 = weight3*ascore11
    var atotal12 = weight4*ascore12
    var atotal13 = weight1*ascore13
    var atotal14 = weight2*ascore14
    var atotal15 = weight3*ascore15
    var atotal16 = weight4*ascore16

    var btotal1 = weight1*bscore1
    var btotal2 = weight2*bscore2
    var btotal3 = weight3*bscore3
    var btotal4 = weight4*bscore4
    var btotal5 = weight1*bscore5
    var btotal6 = weight2*bscore6
    var btotal7 = weight3*bscore7
    var btotal8 = weight4*bscore8
    var btotal9 = weight1*bscore9
    var btotal10 = weight2*bscore10
    var btotal11 = weight3*bscore11
    var btotal12 = weight4*bscore12
    var btotal13 = weight1*bscore13
    var btotal14 = weight2*bscore14
    var btotal15 = weight3*bscore15
    var btotal16 = weight4*bscore16 
    
    var ctotal1 = weight1*cscore1
    var ctotal2 = weight2*cscore2
    var ctotal3 = weight3*cscore3
    var ctotal4 = weight4*cscore4
    var ctotal5 = weight1*cscore5
    var ctotal6 = weight2*cscore6
    var ctotal7 = weight3*cscore7
    var ctotal8 = weight4*cscore8
    var ctotal9 = weight1*cscore9
    var ctotal10 = weight2*cscore10
    var ctotal11 = weight3*cscore11
    var ctotal12 = weight4*cscore12
    var ctotal13 = weight1*cscore13
    var ctotal14 = weight2*cscore14
    var ctotal15 = weight3*cscore15
    var ctotal16 = weight4*cscore16
    
    var dtotal1 = weight1*dscore1
    var dtotal2 = weight2*dscore2
    var dtotal3 = weight3*dscore3
    var dtotal4 = weight4*dscore4
    var dtotal5 = weight1*dscore5
    var dtotal6 = weight2*dscore6
    var dtotal7 = weight3*dscore7
    var dtotal8 = weight4*dscore8
    var dtotal9 = weight1*dscore9
    var dtotal10 = weight2*dscore10
    var dtotal11 = weight3*dscore11
    var dtotal12 = weight4*dscore12
    var dtotal13 = weight1*dscore13
    var dtotal14 = weight2*dscore14
    var dtotal15 = weight3*dscore15
    var dtotal16 = weight4*dscore16
    
    var item1avg = atotal1 + atotal2 + atotal3 + atotal4 + btotal1 + btotal2 + btotal3 + btotal4 + ctotal1 + ctotal2 + ctotal3 + ctotal4 + dtotal1 + dtotal2 + dtotal3 + dtotal4
    var item2avg = atotal5 + atotal6 + atotal7 + atotal8 + btotal5 + btotal6 + btotal7 + btotal8 + ctotal5 + ctotal6 + ctotal7 + ctotal8 + dtotal5 + dtotal6 + dtotal7 + dtotal8
    var item3avg = atotal9 + atotal10 + atotal11 + atotal12 + btotal9 + btotal10 + btotal11 + btotal12 + ctotal9 + ctotal10 + ctotal11 + ctotal12 + dtotal9 + dtotal10 + dtotal11 + dtotal12
    var item4avg = atotal13 + atotal14 + atotal15 + atotal16 + btotal13 + btotal14 + btotal15 + btotal16 + ctotal13 + ctotal14 + ctotal15 + ctotal16 + dtotal13 + dtotal14 + dtotal15 + dtotal16

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
