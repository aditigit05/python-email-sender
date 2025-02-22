from flask import Flask, request, render_template_string
from flask_mail import Mail, Message
app = Flask(_name_)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'aditi05544@gmail.com'
app.config['MAIL_PASSWORD'] = 'qern ufsc wpbh ukxz'

mail = Mail(app)

@app.route('/send', methods=['POST', 'GET'])
def send_email():
    if request.method == 'POST':
        subject = request.form.get('subject')
        body = request.form.get('body')
        receivers = request.form.get('receivers').split(',')

        msg = Message(subject=subject,
                      sender=app.config['MAIL_USERNAME'],
                      recipients=receivers,
                      body=body)

        mail.send(msg)
        return 'Email sent successfully!'
    
    return render_template_string('''
        <form method="post">
            Subject: <input type="text" name="subject"><br>
            Body: <textarea name="body"></textarea><br>
            Receivers (comma separated): <input type="text" name="receivers"><br>
            <input type="submit" value="Send Email">
        </form>
    ''')

if _name_ == '_main_':
    app.run(debug=True)
