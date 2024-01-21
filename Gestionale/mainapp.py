from db_connection import Database
from dbOperations import *
from partecipants import *
from alcohols import *
from flask import Flask, render_template, request

db = Database

app = Flask(__name__, template_folder='templates')

# homepage


@app.route('/')
def home():
    return render_template('homepage.html')

# area pagine accoglienza


@app.route('/people')
def people_page():
    participants = persons()
    return render_template('people.html', participants=participants)


@app.route('/update_presence', methods=['POST'])
def update_presence_route():
    participant_id = request.form['participant_id']
    presence = request.form['presence']
    update_presence(participant_id, presence)

    return 'Success'


# area inventari


@app.route('/inventory')
def inventory():
    return render_template('inventory.html')


@app.route('/alcohol_inventory')
def alcohol_inventory():
    alcohol = alcohols()
    return render_template('alcohol_inventory.html', alcohol=alcohol)


@app.route('/manage_quantity', methods=['POST'])
def manage_quantity():
    item_id = request.form['id']
    new_quantity = request.form['quantity']
    manage_qt(item_id, new_quantity)
    return 'Success'


# area bar


'''@app.route('/bar')
def cocktail_orders():

    return render_template()'''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
