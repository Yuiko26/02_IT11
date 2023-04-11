# importing Flask and other modules
from flask import Flask, request, render_template
 
# Flask constructor
app = Flask(__name__)

fortune_dict = {
    ("red", "1"): "Good luck will come your way in unexpected ways.",
    ("red", "2"): "Your creativity will bring you great success.",
    ("red", "3"): "You will find love in unexpected places.",
    ("red", "4"): "You will soon embark on an exciting journey.",
    ("yellow", "1"): "A new opportunity will bring great prosperity.",
    ("yellow", "2"): "Your hard work will pay off in the near future.",
    ("yellow", "3"): "You will overcome any challenges that come your way.",
    ("yellow", "4"): "Your optimism will lead you to great success.",
    ("green", "1"): "You will meet someone who will change your life.",
    ("green", "2"): "A long-awaited goal will finally be achieved.",
    ("green", "3"): "Your kindness will be rewarded in the near future.",
    ("green", "4"): "You will make a positive difference in someone's life.",
    ("blue", "1"): "A new friendship will bring you great joy.",
    ("blue", "2"): "You will find inner peace and contentment.",
    ("blue", "3"): "Your persistence will lead you to achieve great things.",
    ("blue", "4"): "You will be blessed with good health and happiness.",
}
 
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
    color_number = (color, number)
    fortune = fortune_dict.get(color_number)
    return render_template("fortune.html", name=name, fortune=fortune)

if __name__=='__main__':
   app.run()

