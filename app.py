from flask import Flask, jsonify, request, url_for, redirect, session

app =  Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = "Thisisasecret"

@app.route('/')
def index():
    return '<h1>Hello World</h1>'

@app.route('/home', methods=['POST', 'GET'], defaults={'name': 'Default'})
@app.route('/home/<string:name>', methods=['POST', 'GET'])
def home(name):
    session['name'] = name
    return '<h1>Hello {}, you are on the home page!</h1>'.format(name)

@app.route('/json')
def json():
    name = session['name']
    return jsonify({"name":name, "key": 'value', "key2": [1,2,3,4]})

#http://127.0.0.1:5050/query?name=sara&location=morroco
@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return '<h1>Hi {}. You are from {}. You are on the query page!</h1>'.format(name, location)

@app.route('/theform')
def theform():
    return '''<form method="POST" action="/theform">
        <input type="text" name="name">
        <input type="text" name="location">
        <input type="submit" value="submitar">
            </form>'''

@app.route('/theform', methods=['POST'])
def process():

    

    name = request.form['name']
    location = request.form['location']

    #return redirect(url_for('home', name=name))
    return f'Hello {name}. You are from {location}. Submit Successfull'


@app.route('/processjson', methods=['POST'])
def processjson():

    data = request.get_json()

    name = data['name']
    location = data['location']

    randomlist = data['randomlist']

    return jsonify({'result': 'Success', 'name':name, 'location':location, 'randomkeyinlist':randomlist[1] })

if __name__ == '__main__':
    app.run(port=5050)