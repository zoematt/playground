from flask import Flask, render_template
app = Flask(__name__)

@app.route("/play")
def play():

    return render_template('playground.html', number=3, color= 'green')


@app.route("/play/<int:number>")
def blue(number):

    return render_template('playground.html', number=number, color= 'green')

@app.route("/play/<int:number>/<color>")
def color(number, color):

    return render_template('playground.html', number=number, color= color)



if __name__ == "__main__":
    app.run(debug = True)

    from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                                    

