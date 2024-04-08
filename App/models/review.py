from App.database import db
from .student import Student
from datetime import datetime

class Review(db.Model):
  __tablename__ = 'review'
  ID = db.Column(db.Integer, primary_key=True)
  studentID = db.Column(db.Integer, db.ForeignKey('student.ID'))
  createdByStaffID = db.Column(db.Integer,db.ForeignKey('staff.ID'))
  isPositive = db.Column(db.Boolean, nullable=False)
  dateCreated = db.Column(db.DateTime, default=datetime.utcnow)
  points = db.Column(db.Integer, nullable=False)
  details = db.Column(db.String(400), nullable=False)

  def __init__(self, staff, student, isPositive, points,details):
    self.createdByStaffID = staff.ID
    # self.student= student
    self.studentID = student.ID
    self.isPositive = isPositive
    self.points= points
    self.details= details
    self.dateCreated = datetime.now()

  def get_id(self):
    return self.ID

  # def deleteReview(self, staff):
  #   if self.reviewer == staff:
  #     db.session.delete(self)
  #     db.session.commit()
  #     return True
  #   return None
    
  def to_json(self, student, staff):
    return {
        "reviewID": self.ID,
        "reviewer": staff.firstname + " " + staff.lastname,
        "studentID": student.ID,
        "studentName": student.firstname + " " + student.lastname,
        "created":self.dateCreated.strftime("%d-%m-%Y %H:%M"),  #format the date/time
        "isPositive": self.isPositive,
        "points": self.points,
        "details": self.details
    }