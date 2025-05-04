from flask import Flask, render_template, request, redirect, flash
from utils.email import send_confirmation_email
from utils.crm_google_sheets import add_lead_to_sheet
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "defaultsecret")

leads = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        company = request.form['company']
        interest = request.form['interest']

        lead = {'name': name, 'email': email, 'phone': phone, 'company': company, 'interest': interest}
        leads.append(lead)
        
        send_confirmation_email(email, name)
        add_lead_to_sheet(lead)
        
        flash('Lead submitted successfully!', 'success')
        return redirect('/')
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', leads=leads)

if __name__ == "__main__":
    app.run(debug=True)