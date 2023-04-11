# importing Flask and other modules
from flask import Flask, request, render_template
 
# Flask constructor
app = Flask(__name__)  
 
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET"])
def main():
    return render_template("form.html")
    
@app.route('/fortune', methods =["POST"])
def fortune():    
    name = request.form.get("user")
    color = request.form.get("color")
    number = request.form.get("number")
    return render_template("fortune.html", name=name, color=color)

if __name__=='__main__':
   app.run()

