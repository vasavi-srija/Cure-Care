#import libraries
from flask import Flask, render_template,request
import pickle
from flask_mysqldb import MySQL
from smtplib import SMTP

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
model2 = pickle.load(open('model2.pkl', 'rb'))
#default page of our web-app
@app.route('/')
def home():
    return render_template('mainpage.html')

#To use the predict button in our web-app
@app.route('/predict',methods=['POST'])
def predict():
    #For rendering results on HTML GUI
    int_features = [int(x) for x in request.form.getlist('symptom_check')]
    final_features = [0]*7
    for i in int_features:
        final_features[i] = 1
    prediction = model.predict([final_features])
    output = round(prediction[0], 2)
    if output:
        out = "You are most probably positive! Please take the necessary actions."
    else:
        out = "You are most probably negative! But advised to stay home isolated."
    return render_template('dummy.html', prediction_text=out )

@app.route('/predict2',methods=['POST','GET'])
def predict2():
    #For rendering results on HTML GUI
    int_features=[]
    for i in range(1,17):
        int_features.append(request.form[str(i)])
    final_features = [0]*11
    feature_no=[5,6,7,8,9,10,11,12,13,14,15]
    j=0
    for i in feature_no:
        final_features[j] = int_features[i]
        j=j+1
    prediction = model2.predict([final_features])
    output = round(prediction[0], 2)
    if output == 0:
        out="Not Severe. Home isolation recommended!"
        ward="Normal"
    elif output == 1:
        out="Mildly Severe. Please get admitted immediately."
        ward="Special"
    elif output == 2:
        out="Severe. ICU allocated!"
        ward="ICU"

    server = SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.ehlo()
    server.login("eyrc.vb.0450@gmail.com", "Eyrc_vb@0450")
    sent_from = "eyrc.vb.0450@gmail.com"
    to = int_features[2]
    subject = 'Admitted in Cure & Care!'
    body = "Dear "+int_features[0]+"! You have been admitted into the "+ward+" ward.\nWe hope you have a speed recovery!"
    server.sendmail(sent_from, to, body)

    if(output!=0):
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO patients_list (name,address,email,phone_no,covid_status,age,gender,temperature,weakness,breath_prob,drowsiness,chest_pain,immunity_history,diabetic,bp,smell_loss) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
                   ([x for x in int_features]))
        mysql.connection.commit()
        cursor.close()
    return render_template('pop_up.html', prediction=out)

@app.route('/symptom')
def symptom():
    return render_template('symptom_check.html')

@app.route('/contribute')
def contribute():
    return render_template('contribute.html')

@app.route('/vaccination')
def vaccination():
    return render_template('vaccination_slot.html')

@app.route('/helpline')
def helpline():
    return render_template('helpline.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/oxygen')
def oxygen():
    return render_template('oxygen_plasma_blood_form.html')

@app.route('/money')
def money():
    return render_template('money_form.html')

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Raksha2000'
app.config['MYSQL_DB'] = 'sys'

mysql = MySQL(app)


@app.route('/login_sql', methods=['POST','GET'])
def login_sql():
        user = request.form['UserID']
        passw = request.form['pass']
        cursor = mysql.connection.cursor()
        cursor.execute(''' SELECT * from doctors_list WHERE UserID=(%s) and Password=%s ''', (int(user), passw))
        output = cursor.fetchall()
        cursor.close()
        if output:
            return render_template('after_login.html')
        else:
            return render_template('login.html')

@app.route('/signup_sql', methods=['POST','GET'])
def signup_sql():
    return render_template('signup.html')

@app.route('/after_login', methods=['POST','GET'])
def after_login():
    return render_template('after_login.html')

@app.route('/signup_sql2', methods=['POST','GET'])
def signup_sql2():
        user = request.form['UserID']
        email = request.form['email']
        passw = request.form['psw']
        ph = request.form['phnnumber']
        dsg = request.form['dsg']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO doctors_list (UserID,Email,Password,Phno,Designation) VALUES (%s,%s,%s,%s,%s)''', (int(user), email, passw, ph, dsg))
        mysql.connection.commit()
        cursor.close()
        return render_template('login_output.html', output="Account successfully created!")

@app.route('/add_patient', methods=['POST','GET'])
def add_patient():
    return render_template('add_patient.html')

@app.route('/dashboard')
def dashboard():
    cursor = mysql.connection.cursor()
    cursor.execute(''' SELECT * from patients_list ''')
    output = cursor.fetchall()
    cursor.close()
    if output:
        return render_template('curve2.html', output=output)
    else:
        return render_template('login.html')

@app.route('/dashboard2')
def dashboard2():
    cursor = mysql.connection.cursor()
    cursor.execute(''' SELECT * from patients_list WHERE PatientID="1"''')
    output = cursor.fetchall()
    cursor.close()
    return render_template('curve.html',output=output)

@app.route('/Future_predict')
def Future_predict():
    return render_template('future_predict.html')

@app.route('/inventory')
def inventory():
    cursor = mysql.connection.cursor()
    cursor.execute(''' SELECT COUNT(*) from patients_list''')
    output = cursor.fetchall()
    cursor.close()
    output = int(output[0][0])
    inventory_beds = 35
    oxy = inventory_oxygen = 10000000
    beds = (inventory_beds - output)
    oxy_days = oxy-(output*50000)
    return render_template('inventory.html', inventory_beds=inventory_beds, inventory_oxygen=inventory_oxygen, output=output,  beds=int(beds), oxy_days=oxy_days)

@app.route('/patients_list', methods=['POST','GET'])
def patients_list():
        cursor = mysql.connection.cursor()
        cursor.execute(''' SELECT * from patients_list ''')
        output = cursor.fetchall()
        cursor.close()
        if output:
            return render_template('patient_list.html',output=output)
        else:
            return render_template('login.html')


@app.route('/oxy_bed', methods=['POST','GET'])
def oxy_bed():
    freq = request.form['freq']
    cursor = mysql.connection.cursor()
    cursor.execute(''' SELECT COUNT(*) from patients_list''')
    output = cursor.fetchall()
    cursor.close()
    output=int(output[0][0])
    inventory_beds=35
    oxy=inventory_oxygen=10000000
    beds=(inventory_beds-output)/int(freq)
    i=output
    oxy_days=0
    while oxy>=0:
        oxy=oxy-(i*50000)
        i=i+int(freq)
        oxy_days+=1

    return render_template('oxy-bed.html',inventory_beds=inventory_beds, inventory_oxygen=inventory_oxygen, output=output, freq=freq, beds=int(beds), oxy_days=oxy_days)

if __name__ == "__main__":
    app.run(debug=True)
