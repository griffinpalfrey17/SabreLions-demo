# store the standard roots for the website: home page, leader board, etc
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__) # Blueprint means there are multiple files/URL's 

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})




from flask import render_template, request, redirect, url_for
from website.models import Pitcher
@app.route('/dashboard')
def dashboard():
    pitchers = Pitcher.query.all()
    return render_template('dashboard.html', pitchers=pitchers)

@app.route('/add_pitcher', methods=['POST'])
def add_pitcher():
    new_pitcher = Pitcher(
        name=request.form['name'],
        release_velocity=request.form['release_velocity'],
        extension=request.form['extension'],
        tilt=request.form['tilt'],
        vaa=request.form['vaa'],
        spin_rate=request.form['spin_rate'],
        release_height=request.form['release_height'],
        ivb=request.form['ivb'],
        ihb=request.form['ihb']
    )
    db.session.add(new_pitcher)
    db.session.commit()
    return redirect(url_for('dashboard'))

@app.route('/selected_pitcher')
def selected_pitcher():
    pitcher_id = request.args.get('pitchers')
    pitcher = Pitcher.query.get(pitcher_id)
    return render_template('pitcher_detail.html', pitcher=pitcher)


