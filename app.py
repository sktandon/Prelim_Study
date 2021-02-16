import flask, random, json
from flask import redirect, url_for, session, request
#from flask_mysqldb import MySQL


from training.routes import training_bp

# Create the application.
app = (flask.Flask(__name__, instance_relative_config=True))
#app.config["MYSQL_HOST"] = "mysql2.nms.kcl.ac.uk"
#app.config["MYSQL_PORT"] = 33306
#app.config["MYSQL_USER"] = "k1758447"
#app.config["MYSQL_PASSWORD"] = "REDACTED"

""" app.config["MYSQL_HOST"] = "localhost"
#app.config["MYSQL_PORT"] = 8080
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "k1758447_survey"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
mysql = MySQL(app)

app.secret_key="dev" """
app.register_blueprint(training_bp, url_prefix='/tr')

#functions
def generateProgressNum(number):
    number = int(number)
    if number >= 1 and number <= 3:
        return 3
    elif number >= 4 and number <=6:
        return 4
    elif number >= 7 and number <=9:
        return 5

def kick():
    session.pop("id", None)
    return redirect(url_for('home'))


@app.route("/")
def home():
        #cursor = mysql.connection.cursor()
        #query = 'INSERT INTO `demographics`(`ID`) VALUES ("test")'
        #cursor.execute(query)
        #mysql.connection.commit()
        #session["id"]= "test"
        return flask.render_template("home.html")


@app.route("/dems/", methods = ['GET'])
def dems():
    return flask.render_template("dems.html")

""" @app.route("/dems/", methods = ['POST'])
def getDems():
         ## need to update dems database
         gender = request.form.get('gender')
         if gender not in ["Female", "Male", "Other", "Prefer Not to Answer"]:
             return kick()
         taken = request.form.get('taken') #dems.html name
         agegroup = request.form.get('age')
         education = request.form.get('education')
         employment = request.form.get('employment')
         avenue = request.form.get('avenue')
         country1 = request.form.get('country1')
         country2 = request.form.get('country2')
         area = request.form.get('area')
         cursor = mysql.connection.cursor()
         query = 'UPDATE demographics SET gender = %s, taken = %s, agegroup=%s, education=%s, employment=%s, avenue=%s, country1=%s, country2=%s, area=%s WHERE ID = %s'
         cursor.execute(query, (gender, taken, agegroup, education, employment, avenue, country1, country2, area, session.get("id"),))
         mysql.connection.commit()
         return redirect(url_for('training_bp.game')) """


@app.route("/BC/<number>/")
def BC(number):
    return flask.render_template("pre.html", qNumber=number, jsdata='data'+number , nextpage='/m/'+number, progressNum=generateProgressNum(number))

@app.route("/m/<number>/")
def m(number):
    return flask.render_template("mask.html", nextpage='/BG/'+number, progressNum=generateProgressNum(number)) 

@app.route("/BG/<number>/")
def BG(number):

    if number == '9':
        nextpage = '/transition'
    else:
        nextpage = '/bt/'+number

    return flask.render_template("post.html", qNumber=number, jsdata='podata'+number, nextpage=nextpage, progressNum=generateProgressNum(number))

@app.route("/bt/<number>/")
def bt(number):
    return flask.render_template("btwn.html", nextpage='/BC/'+str((int(number)+1)), progressNum=generateProgressNum(number))

#transition to paper folding game
    
@app.route("/transition")
def transition():
    return flask.render_template("transition.html")


@app.route("/inst")
def inst():
    return flask.render_template("instruction.html")


@app.route("/Qs")
def Qs():
    return flask.render_template("Qs.html")


#one last question


@app.route("/quest")
def quest():
    return flask.render_template("quest.html")

# @app.route("/getQuest", methods = ['POST'])
# def getQuest():
        ## could add these two questions to the dems database?
        # cursor = mysql.connection.cursor()
        # query = 'UPDATE demographics SET xxxxx'
        # cursor.execute(query)
        # mysql.connection.commit()
        # return ''

@app.route("/end")
def end():
    return flask.render_template("end.html")

# @app.route("/getemail", methods = ['POST'])
# def getemail():
        ## add to separate emails 'database', attached to new random unique ids 
        # cursor = mysql.connection.cursor()
        # query = 'UPDATE xxxx SET xxxxx'
        # cursor.execute(query)
        # mysql.connection.commit()
        # return ''



#AJAX 

""" @app.route("/datafrompost", methods = ['POST'])
def datafrompost():
        ## get data from post
        qNumber = request.form.get('qNumber')

        FinalValues = json.loads(request.form.get('FinalValues'))
        FinalValue1 = FinalValues[0]['value']
        FinalValue2 = None
        FinalValue3 = None
        if len(FinalValues) >= 2:
            FinalValue2 = FinalValues[1]['value']
        if len(FinalValues) >= 3:
            FinalValue3 = FinalValues[2]['value']
        
        StimulusClicks = request.form.get('StimulusClicks')
        ResponseTime = request.form.get('ResponseTime')

        cursor = mysql.connection.cursor()
        query = 'INSERT INTO `stimuli`(`UserID`, `Question`, `ResponseTime`, `StimulusClicks`, `FinalValue1`, `FinalValue2`, `FinalValue3`) VALUES (%s, %s,%s,%s,%s,%s,%s)'
        cursor.execute(query, (session.get("id"), int(qNumber), ResponseTime, StimulusClicks, FinalValue1, FinalValue2, FinalValue3,))
        mysql.connection.commit()
        return '' """

if __name__ == '__main__':
    app.debug=True
    app.run()