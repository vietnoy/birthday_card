from flask import Flask, request, jsonify, render_template
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# Email credentials (Use a real email & enable SMTP for this to work)
EMAIL_ADDRESS = "khangdo0110200401102004@gmail.com"
EMAIL_PASSWORD = "ncqi uklx kstu oyhk"

def send_email(to_email, time):
    """ Sends an email invitation to the selected recipient """
    subject = "🎉 You're Invited to a Birthday Movie Date!"
    body = f"Hey iem! ❤️\n\nI'm so excited to celebrate with you! We've got a movie date set for {time} on Tuesday(4/3/2025)! 🍿\n\nI can't wait to see you! 😘\n\nLove,\nDo Vinh Khang"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email

    # Send email
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())
        return True
    except Exception as e:
        print("Error sending email:", e)
        return False

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send-invite", methods=["POST"])
def send_invite():
    data = request.json
    time = data["time"]
    email = data["email"]

    if send_email(email, time):
        return jsonify({"message": "Email sent successfully!"}), 200
    else:
        return jsonify({"error": "Failed to send email"}), 500

if __name__ == "__main__":
    app.run(debug=True)