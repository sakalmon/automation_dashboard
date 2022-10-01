from flask_wtf import FlaskForm
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class DataForm(FlaskForm):

    commenced_parts_l1 = IntegerField('Commenced Parts', default=0)
    good_parts_l1 = IntegerField('Good Parts', default=0)
    optic_press_l1 = IntegerField('Optic Press', default=0)
    vision_1_l1 = IntegerField('Vision 1', default=0)
    vision_1_1_l1 = IntegerField('Vision 1.1', default=0)
    pcb_press_l1 = IntegerField('PCB Press', default=0)
    vision_2_l1 = IntegerField('Vision 2', default=0)
    rh_press_l1 = IntegerField('RH Press', default=0)
    vision_3_l1 = IntegerField('Vision 3', default=0)
    bc_press_l1 = IntegerField('BC Press', default=0)
    vision_4_l1 = IntegerField('Vision 4', default=0)
    vision_5_l1 = IntegerField('Vision 5', default=0)

    commenced_parts_l2 = IntegerField('Commenced Parts', default=0)
    good_parts_l2 = IntegerField('Good Parts', default=0)
    optic_press_l2 = IntegerField('Optic Press', default=0)
    vision_1_l2 = IntegerField('Vision 1', default=0)
    vision_1_1_l2 = IntegerField('Vision 1.1', default=0)
    pcb_press_l2 = IntegerField('PCB Press', default=0)
    vision_2_l2 = IntegerField('Vision 2', default=0)
    rh_press_l2 = IntegerField('RH Press', default=0)
    vision_3_l2 = IntegerField('Vision 3', default=0)
    bc_press_l2 = IntegerField('BC Press', default=0)
    vision_4_l2 = IntegerField('Vision 4', default=0)
    vision_5_l2 = IntegerField('Vision 5', default=0)

    submit = SubmitField('Submit')
    
class NewJobForm(FlaskForm):
    scan_box = StringField('Scan QR Code', validators=[DataRequired()])
    submit = SubmitField('Accept')

class TestForm(FlaskForm):
    submit = SubmitField('Test')