from flask import Flask,render_template,request
import mysql.connector
import yaml
app = Flask(__name__)
db=yaml.load(open("db.yaml"))
print(db)
host=db["host"]
user=db["user"]
password=db["password"]
database=db["db"]
@app.route('/')
@app.route('/dashboard')
def dashboard():
    return render_template("index.html")

@app.route('/services')
def services():
        mydb = mysql.connector.connect(host=host, user=user, password=password,database=database)
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM Services")
        data1 = mycursor.fetchall()
        return render_template("services.html",data=data1)

@app.route('/aboutus')
def AboutUs():
    return render_template("AboutUs.html")

@app.route("/Prov_services", methods=['GET', 'POST'])
def Prov_services():
    if request.method=="POST":
        service_details = request.form
        Service=service_details["Service"]
        Name=service_details["Name"]
        Phone_No=service_details["Phone_No"]
        Address=service_details["Address"]
        Email=service_details["Email"]
        Comments=service_details["Comments"]
        s=[]
        s.append(Service)
        s.append(Name)
        s.append(Phone_No)
        s.append(Address)
        s.append(Email)
        s.append(Comments)
        s=tuple(s)
        try:
            mydb = mysql.connector.connect(host=host, user=use, password=password, database=database)
            mycursor = mydb.cursor()
            a=("INSERT INTO Services (Service,Name,Phone_No,Address,Email,Comments) values (%s,%s,%s,%s,%s,%s)")
            mycursor.execute(a,s)
            mydb.commit()
        except mysql.connector.Error as error:
            print("parameterized query failed {}".format(error))

    return render_template("Prov_services.html")

if __name__ == '__main__':
    app.run()
