'''
web application devlopment with Flask

1. install flask library
2. create the object of flask and run it in the main function 
3. display some index content to the user 

'''

from flask import *
from flask1 import User
from session3 import Patient
from session2 import mongoDBhelper
import hashlib

web_app = Flask('app')
db = mongoDBhelper()
db.select_db(db_name='Auribises' , collection='users')    

#this function is for sign up page
@web_app.route('/') #decorator
def index():
    return render_template('index.html')

#this funtion is for the login page
@web_app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # handle login
         return "Login POST"
    return render_template('login.html')

# this funtion is for the home when doctor register or login
@web_app.route('/home',methods=['GET'])
def home():
    if len(session['user_id']) > 0:
      return render_template ('home.html', name = session['name'], email = session['email'])
    else:
        return redirect('/')

#this is to add patient
@web_app.route('/add-patient',methods=['GET'])
def add_patient():
    if len(session['user_id']) > 0 :
        return render_template ('add-patient.html', name = session['name'], email = session['email'])
    else:
        return redirect('/')
#this is 
@web_app.route('/adduser', methods=['POST','GET'])
def add_user_in_db():
    print("testing")
    user = User()
    user.name = request.form['name']
    user.email = request.form['email']
    # encryption
    user.password = hashlib.sha256(request.form['password'].encode('utf-8')).hexdigest()
    user.show()
    db.select_db(collection='users')
    result = db.insert(document=user.to_document())
    if len(str(result.inserted_id)) >0 :
         session['user_id'] = str(result.inserted_id)
         session['name'] = user.name
         session['email'] = user.email
        
         return render_template('/home.html', name = user.name , email = user.email)
  
    else:
          return'somrthing went wrong'
      

#this is for add patients in database      
@web_app.route('/add-patient-in-db', methods=['POST','GET'])
def add_pateint_in_db():
     if len(session['user_id']) > 0:
        print("testing")
        patient = Patient()
        patient.name = request.form['name']
        patient.phone = request.form['phone']
        patient.email = request.form['email']
        patient.address = request.form['address']
        patient.gender = request.form['gender']
        patient.age = request.form['age']
        patient.doctor_id = session['user_id'] # from session we have taken the doctor id
        
        print(patient.to_document())
        db.select_db(collection='patients')
        result = db.insert(document=patient.to_document())
        
        if len(str(result.inserted_id)) >0 :
        
            return render_template('/home.html', name = session['name'] , email = session['email'])
    
        else:
            return'somrthing went wrong'
    
     else:
         return redirect('/')
    
        
      
@web_app.route('/fetch-user', methods=['POST'])
def fetch_user_from_db():
    query = {
        'email': request.form['email'],
        'password': hashlib.sha256(request.form['password'].encode('utf-8')).hexdigest()
    }

    documents = db.fetch(query)

    user = documents[0]
    print(user)

    if len(documents) > 0:
         session['user_id'] = str(user['_id'])
         session['name'] = user['name']
         session['email'] = user['email']
         return render_template('home.html', name = user['name'], email = user['email'])
    else:
        return 'Username or Password Invalid. Please Try Again'
 
@web_app.route('/logout')
def logout():
     session['user_id'] = ''
     session['name'] = ''
     session['email'] = ''
     
     return redirect('/')
   
   
@web_app.route('/fetch-patients')
def fetch_patients_from_db():
    
     if len(session['user_id']) > 0:
        query = {
            'doctor_id': session['user_id']
        }
        db.select_db(collection='patients')
        documents = db.fetch(query)

        if len(documents) > 0:
            return render_template('show-patients.html', name = session['name'], 
                                    email = session['email'], total = len(documents), patients = documents)
        else:
            return 'Patients not found'   
    
     else:
        return redirect('/')
    


def main():
    # Secret Key, we have to create manually of our choice
    # It is required for Session Management
    web_app.secret_key='doctorsappv1'
    web_app.run(debug=True)

if __name__ == '__main__':
  
    main()