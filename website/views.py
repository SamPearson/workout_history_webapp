from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, WorkoutPhase
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET','POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note must be over 0 characters.', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})

@views.route('/admin', methods=['GET','POST'])
def admin():
    if request.method == 'POST':
        workout_phase = request.form.get('workout_phase_input')
        print(f'wow you input {workout_phase}')
        if len(workout_phase) < 1:
            flash('Workout Phase Name must not be empty.', category='error')
        else:
            new_workout_phase = WorkoutPhase(name=workout_phase)
            db.session.add(new_workout_phase)
            db.session.commit()
            flash(f'Workout Phase "{workout_phase}" added!', category='success')

    phases = WorkoutPhase.query.all()
    return render_template("admin.html", user=current_user, phases=phases)

#@views.route('/exercises', methods=['GET'])
#    return render_template("exercises.html") #maybe define a user or something
