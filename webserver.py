from flask import Flask, request, render_template
import requests
import os
app = Flask(__name__,static_url_path="/static")

@app.route('/')
@app.route('/index')
def home():
  """day_of_week = request.form.get("day_of_week")
  if (day_of_week != None):
    return render_template("index.html", content = "The quote for " + day_of_week + ": " + quote_db[day_of_week])
  else:
    return render_template('index.html') """
  return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html') 

@app.route('/contact')
def contact():
  return render_template('contact.html')

@app.route('/email', methods=['GET','POST'])
def send_email():
  message = request.form.get("message")
  name = request.form.get("name")
  subject = request.form.get("subject")
  notifications = []
  """data = {
        "from": os.environ["INFO253_MAILGUN_FROM_EMAIL"],
        "to": os.environ["INFO253_MAILGUN_TO_EMAIL"],
        "subject": "You just was sent a message",
        "text": message
  }""" 
  auth = (os.environ["INFO253_MAILGUN_USER"], os.environ["INFO253_MAILGUN_PASSWORD"])
  """requests.post(
        os.environ["INFO253_MAILGUN_DOMAIN"],
        auth=auth,
        data=data)"""
  if (message != None):
    requests.post(
        "https://api.mailgun.net/v3/sandbox587f872de88f4507bb9d812476fbc7b6.mailgun.org/messages",
        #auth=("api", "key-5f903146264eae708f15db0113662706"),
        auth=auth,
        data={"from": "Mailgun Sandbox <postmaster@sandbox587f872de88f4507bb9d812476fbc7b6.mailgun.org>",
              "to": os.environ["INFO253_MAILGUN_TO_EMAIL"],
              "subject": subject,
              "text": "New message from " + name + ": " + message})
  """if r.status_code == requests.codes.ok:
    notifications.append("Your email was sent")
  else:
    notifications.append("You email was not sent. Please try again later")"""
  notifications.append("Hi " + name +", your message has been sent.")
  return render_template("contact.html", notifications=notifications)
  #return render_template("contact.html")

"""def mail():
  key = "key-5f903146264eae708f15db0113662706"
  #sandbox = 'YOUR SANDBOX URL HERE'
  #recipient = 'YOUR EMAIL HERE'

  request_url = "https://api.mailgun.net/v3/sandbox587f872de88f4507bb9d812476fbc7b6.mailgun.org/messages"
  request = requests.post(request_url, auth=('api', key), data={
      'from': "Mailgun Sandbox <postmaster@sandbox587f872de88f4507bb9d812476fbc7b6.mailgun.org>",
      'to': "Laura Smith <smithlaura@berkeley.edu>",
      'subject': 'Hello',
      'text': 'Hello from Mailgun'
  })
  """
"""return requests.post(
        "https://api.mailgun.net/v3/sandbox587f872de88f4507bb9d812476fbc7b6.mailgun.org/messages",
        auth=("api", key),
        data={"from": "Mailgun Sandbox <postmaster@sandbox587f872de88f4507bb9d812476fbc7b6.mailgun.org>",
              "to": "Laura Smith <smithlaura@berkeley.edu>",
              "subject": "Hello Laura Smith",
              "text": "Congratulations Laura Smith, you just sent an email with Mailgun!  You are truly awesome!"})"""

@app.route('/blog/8-experiments-in-motivation')
def blog0():
  return render_template('blog0.html') 

@app.route('/blog/a-mindful-shift-of-focus')
def blog1():
  return render_template('blog1.html') 

@app.route('/blog/how-to-develop-an-awesome-sense-of-direction')
def blog2():
  return render_template('blog2.html') 

@app.route('/blog/training-to-be-a-good-writer')
def blog3():
  return render_template('blog3.html') 

@app.route('/blog/what-productivity-systems-wont-solve')
def blog4():
  return render_template('blog4.html') 

if __name__ == '__main__':
	app.run(debug = True)