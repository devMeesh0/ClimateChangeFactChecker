# import MySQLdb
# from MySQLdb.cursors import DictCursor
from flask import Flask, render_template
from database import database as DB

db = ''

def init():
    global db
    db = DB()

app = Flask(__name__)

@app.route("/")
def index():
    arr = (db.get_category('conspiracy')[0])
    # arr = []
    # #db.get_category('conspiracy')
    # for i in range(6):
    #     arr.append(i+15)
    return render_template("index.html", misrepresent_0 = arr)

if __name__ == "__main__":
    init()
    app.run()


'''
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            image_path = os.path.join('static', uploaded_file.filename)
            uploaded_file.save(image_path)
            class_name = model.get_prediction(image_path)
            result = {
                'class_name': class_name,
                'image_path': image_path,
            }
            return render_template('result.html', result = result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)
'''