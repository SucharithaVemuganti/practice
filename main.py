from flask import Flask,render_template,request
app  = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/register', methods = ['POST'])
def register():
    if request.method == 'POST':
        name1 = request.form['name']
        email = request.form['email']
        password = request.form['password']
        return render_template('success.html',name = name1,email = email,password = password)
    else:
        return render_template('index.html')
if __name__ == '__main__':
    print("running")
    app.run(debug=True)