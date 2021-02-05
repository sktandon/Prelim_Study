import flask, random
from flask import redirect, url_for, session
from flask_mysqldb import MySQL


from training.routes import training_bp
from first_set.routes import first_set_bp
from second_set.routes import second_set_bp
from third_set.routes import third_set_bp
from SpAb.routes import SpAb_bp

# Create the application.
app = (flask.Flask(__name__, instance_relative_config=True))
app.config["MYSQL_HOST"] = "mysql2.nms.kcl.ac.uk"
#app.config["MYSQL_HOST"] = "137.73.113.158"
app.config["MYSQL_PORT"] = 33306
app.config["MYSQL_USER"] = "k1758447"
app.config["MYSQL_PASSWORD"] = "REDACTED"
app.config["MYSQL_DB"] = "k1758447_survey"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
mysql = MySQL(app)

app.secret_key="dev"
app.register_blueprint(training_bp, url_prefix='/tr')
app.register_blueprint(first_set_bp, url_prefix='/fir')
app.register_blueprint(second_set_bp, url_prefix='/sec')
app.register_blueprint(third_set_bp, url_prefix='/th')
app.register_blueprint(SpAb_bp, url_prefix='/Sp')

@app.route("/")
def home():
        cursor = mysql.connection.cursor()
        query = 'INSERT INTO demographics (id) VALUES ("testgin");'
        cursor.execute(query)
        mysql.connection.commit()
        return flask.render_template("home.html")


@app.route("/dems/")
def dems():
    return flask.render_template("dems.html")

# @app.route("/getDems", methods = ['POST'])
# def getDems():
        ## need to update dems database
        # cursor = mysql.connection.cursor()
        # query = 'UPDATE demographics SET xxxxx'
        # cursor.execute(query)
        # mysql.connection.commit()
        # return ''
    

@app.route("/transition")
def transition():
    return flask.render_template("transition.html")

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

@app.route("/quest/end")
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


if __name__ == '__main__':
    app.debug=True
    app.run()