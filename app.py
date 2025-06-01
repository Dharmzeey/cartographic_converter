from flask import Flask, request, render_template, redirect
from utilities.UTM_converter import UTM_to_DMS, UTM_to_latlon

app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template("index.html")

@app.route('/utm-dms/',methods = ['POST', 'GET'])
def utm_dms():
   if request.method == 'POST':
      easting = request.form['easting']
      northing = request.form['northing']
      zone = request.form['zone']
      
      if easting and northing and zone:
         result = UTM_to_DMS(zone, easting, northing)     
         return render_template('utm-dms.html', output=result)
      else:
         return "An Error Occured"
   else:
      return render_template('utm-dms.html')
   

@app.route('/utm-latlon/',methods = ['POST', 'GET'])
def utm_latlon():
   if request.method == 'POST':
      easting = request.form['easting']
      northing = request.form['northing']
      zone = request.form['zone']
      
      if easting and northing and zone:
         result = UTM_to_latlon(zone, easting, northing)     
         return render_template('utm-latlon.html', output=result)
      else:
         return "An Error Occured"
   else:
      return render_template('utm-latlon.html')


if __name__ == "__main__":
#   app.debug = True
#   app.run()
  app.run(debug = True)