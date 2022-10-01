from flask import Flask, render_template, url_for, flash, redirect
from forms import DataForm, NewJobForm, TestForm
from datetime import datetime
from rejects import store_rejects
from aam import store_aam
import psycopg2
import os

app = Flask(__name__, template_folder='templates')

app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/data_entry', methods=['GET', 'POST'])
def data_entry():
    form = DataForm()

    conn = psycopg2.connect(f"dbname=mydb user={os.environ['DB_USER']} password={os.environ['DB_PASSWORD']}")
    cur = conn.cursor()

    cur.execute("SELECT * FROM jobs ORDER BY date_started DESC LIMIT 1")    
    
    try:
        job_number, date_started, active = cur.fetchone()
    except:
        current_job = 'No active job'
        date_started = ''
        active = False

    if active == True:
        current_job = job_number
    else:
        current_job = 'No active job'

    if date_started:
        date_started = date_started.strftime('%Y-%m-%d')
    cur.close()
    conn.close()

    if form.validate_on_submit():
        aam_dict_l1 = {
            'total_commenced_parts': form.commenced_parts_l1.data,
            'good_parts': form.good_parts_l1.data,
            'line': 1,
            'job_number': current_job
        }
        aam_dict_l2 = {
            'total_commenced_parts': form.commenced_parts_l2.data,
            'good_parts': form.good_parts_l2.data,
            'line': 2,
            'job_number': current_job
        }

        rejects_dict_l1 = {
            'optic_press': form.optic_press_l1.data,
            'vision1': form.vision_1_l1.data,
            'vision1_1': form.vision_1_1_l1.data,
            'pcb_press': form.pcb_press_l1.data,
            'vision2': form.vision_2_l1.data,
            'rh_press': form.rh_press_l1.data,
            'vision3': form.vision_3_l1.data,
            'bc_press': form.bc_press_l1.data,
            'vision4': form.vision_4_l1.data,
            'vision5': form.vision_5_l1.data,
            'line': 1,
            'job_number': current_job
        }
        rejects_dict_l2 = {
            'optic_press': form.optic_press_l2.data,
            'vision1': form.vision_1_l2.data,
            'vision1_1': form.vision_1_1_l2.data,
            'pcb_press': form.pcb_press_l2.data,
            'vision2': form.vision_2_l2.data,
            'rh_press': form.rh_press_l2.data,
            'vision3': form.vision_3_l2.data,
            'bc_press': form.bc_press_l2.data,
            'vision4': form.vision_4_l2.data,
            'vision5': form.vision_5_l2.data,
            'line': 2,
            'job_number': current_job
        }
        
        store_aam(aam_dict_l1)
        store_aam(aam_dict_l2)
        store_rejects(rejects_dict_l1)
        store_rejects(rejects_dict_l2)
        flash('Data Saved!', 'success')
        return redirect(url_for('data_entry'))
   
    return render_template('data_entry.html', title='Data Entry', form=form, current_job=current_job, date_started=date_started)

@app.route('/new_job', methods=['GET', 'POST'])
def new_job():
    form = NewJobForm()
    if form.validate_on_submit():
        conn = psycopg2.connect(f"dbname=mydb user={os.environ['DB_USER']} password={os.environ['DB_PASSWORD']}")
        cur = conn.cursor()

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        scanned_code = form.scan_box.data
        
        # Extract the job number
        job_number = scanned_code.split(';')[0][3:]
        cur.execute(f"INSERT INTO jobs(job_number, date_started, active) VALUES ('{job_number}', '{timestamp}', 'True')")
        
        conn.commit()
        cur.close()
        conn.close()
        
        flash('New job loaded!', 'success')
        return redirect(url_for('data_entry'))

    return render_template('new_job.html', title='New Job', form=form)

if __name__ == '__main__':
    app.run(debug=True)