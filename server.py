from flask import Flask,  render_template

app = Flask(__name__)  

@app.route('/play')          
def play():
    return render_template('index.html', num=4, color='blue') 

@app.route('/play/<int:num>')          
def play_n(num):
    return render_template('index.html', num=num, color='blue') 

@app.route('/play/<int:num>/<string:color>')          
def play_color(num, color):
    return render_template('index.html', num=num, color=color) 

if __name__=="__main__":      
    app.run(debug=True) 