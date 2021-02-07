from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    arr = []
    for i in range(6):
        arr.append(i+15)
    return render_template("index.html", cat1_0=arr[0], cat1_1=arr[1], cat1_2=arr[2],
                           cat1_3=arr[3], cat1_4=arr[4], cat1_5=arr[5])


if __name__ == "__main__":
    app.run()
