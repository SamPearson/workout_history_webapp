from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from ..models import Note, WorkoutPhase
from .. import db
import json

admin_blueprint = Blueprint('admin', __name__)

@admin_blueprint.route('/', methods=['GET','POST'])
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


@admin_blueprint.route('/delete-workout-phase', methods=['POST'])
def delete_workout_phase():
    workout_phase = json.loads(request.data)
    workout_phase_ID = workout_phase['id']
    db_target = WorkoutPhase.query.get(workout_phase_ID)
    if db_target:
        db.session.delete(db_target)
        db.session.commit()
    return jsonify({})
