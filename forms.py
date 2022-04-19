from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms import  BooleanField, StringField, IntegerField, TextAreaField
from wtforms import DateField
from wtforms import PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length, NumberRange

class RegistrationForm(FlaskForm):
    Fname= StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)] )
    Lname= StringField('Last Name', validators=[Length(min=2, max=20)] )
    email=StringField('Email',validators=[DataRequired(), Email() ])
    password= PasswordField('Password' , validators=[DataRequired()])
    confirm_password=PasswordField('Confirm Password' , validators=[DataRequired(), EqualTo('password')])
    role= SelectField("Role", choices=[('Professor'),('Student')] )
    submit= SubmitField('Register')
class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(), Email() ])
    password= PasswordField('Password' , validators=[DataRequired()])
    remember= BooleanField('Remember Me')
    submit= SubmitField('Sign In')

class CreatClassroom_JoinClassroom(FlaskForm):
    ClassName= StringField('Class Name', validators=[DataRequired(), Length(min=2)] )
    ClassDiscriptio=StringField('Class Discription', validators=[DataRequired(), Length(min=10)] )
    Type= SelectField("Class Type", choices=[('Private'),('Open')] )
    NumberOfStudents=IntegerField('Size of the Class', validators=[DataRequired(), NumberRange(min=0)])
    password= PasswordField('Password' , validators=[DataRequired()])
    confirm_password=PasswordField('Confirm Password' , validators=[DataRequired(), EqualTo('password')])
    submit= SubmitField('Create Classroom')
    JClassName=StringField('Class Name', validators=[DataRequired(), Length(min=2, max=20)] )
    Jpassword= PasswordField('Code (Blank if there is no code)' , validators=[])
    Jsubmit= SubmitField('Join Classroom')

class AnnouncementForm(FlaskForm):
    Title = StringField('Announcement Title', validators=[DataRequired(), Length(min=2)])
    Content = TextAreaField('Announcement Content', validators=[DataRequired(), Length(min=3)])
    Submit= SubmitField('Create')

class ClassWork(FlaskForm):
    Title = StringField('Title', validators=[DataRequired(), Length(min=2)])
    Description = TextAreaField('Description', validators=[DataRequired(), Length(min=3)])

