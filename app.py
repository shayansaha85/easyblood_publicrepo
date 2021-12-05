from flask import *
import insert_data as id
import delete_null as dn
import fetch_data as fd
import generating_html_table as ght
import pdf_downloadable as pd

app = Flask(__name__,  static_url_path='/static')

@app.route("/", methods = ["GET", "POST"])
def landing_page():
    return render_template("index.html")


@app.route("/register", methods = ["GET", "POST"])
def register_page():
    dn.delete_null()
    if request.method == "POST":
        data = []
        firstname = request.form.get("firstname")
        data.append(str(firstname))
        blood_group = request.form.get("blood_group")
        data.append(str(blood_group))
        district = request.form.get("district")
        data.append(str(district))
        phone = request.form.get("phone")
        data.append(str(phone))
        try:
            id.insert_data(data)
            print("Successfully inserted data in aws")
            dn.delete_null()
        except:    
            print("Error while sending data in aws")
        finally:
            dn.delete_null()    
    return render_template("register.html", firstname=firstname)


@app.route("/find", methods = ["GET", "POST"])
def find_page():
    if request.method == "POST":
        data = []
        blood_group = request.form.get("blood_group")
        data.append(str(blood_group))
        district = request.form.get("district")
        data.append(str(district))
        fdata = fd.fetch_data(data)
        if bool(fdata):
            ght.generating_html_table(fdata)
            pd.create_pdf(str(blood_group))
            
        elif str(blood_group) != 'None' and not bool(fdata):
            blood_group = 'noblood'
        
    return render_template("find.html", blood_group=blood_group)

if __name__ == '__main__':
    app.run(threaded=True,port=5000)