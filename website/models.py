from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')


class WorkoutPhase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15))

class ExerciseDiscipline(db.Model):
    # Discipline - Bodyweight, Weightlifting, or Cardio
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(15))
    discipline_id = db.Column(db.Integer, db.ForeignKey(Exercise.id))
    exercises = db.relationship('Exercise', backref='discipline')

class IntensityUnit(db.Model):
    # Intensity unit - lbs, single/double unders, fan setting on rower, etc
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(15))
    exercises = db.relationship('Exercise', backref='intensity_unit')
    intensity_unit_id = db.Column(db.Integer, db.ForeignKey(Exercise.id))

class DurationUnit(db.Model):
    # Duration unit - reps, seconds, minutes, laps, miles, etc
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(15))
    exercises = db.relationship('Exercise', backref='duration_unit')
    duration_unit_id = db.Column(db.Integer, db.ForeignKey(Exercise.id))
