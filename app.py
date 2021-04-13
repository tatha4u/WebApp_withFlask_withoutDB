from flask import Flask, render_template, request

app = Flask(__name__)

# defining function to render html page of index.html when visiting the main web page/URL
@app.route("/")
def index():
    return render_template("index.html")

# defining function to render html page of success.html when visiting the 'success' web page/URL
# @app.route("/success")    --> by default is get method, so it cannot send and data
@app.route("/success", methods=['POST'])
def success():
    # Capture the values of email id, height, weight in the following function
    if request.method == 'POST':
        email = request.form["email_name"]
        height = request.form["height_name"]
        weight = request.form["weight_name"]
        print(request.form)
        print(email,height,weight)
        ht_sqr = (int(height)/100)** 2
        bmi = int(weight)/ht_sqr
        print(bmi)
        return render_template("success.html")


# For getting debug logs of running app.py
if __name__ == '__main__':
    app.debug = True
    app.run()