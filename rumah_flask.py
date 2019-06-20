from flask import Flask, render_template, request, redirect, url_for, abort
import joblib

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        luas = int(request.form['luas'])
        jml_kamar = int(request.form['jml_kamar'])
        usia_bangunan = int(request.form['usia_bangunan'])
        
        reg = joblib.load('model_joblib')
        harga = reg.predict([[luas, jml_kamar, usia_bangunan]])

        return redirect(url_for('show_prediction', harga = harga))
    else:
        return render_template('home.html')

@app.route('/prediction/<int:harga>')
def show_prediction(harga):
    return render_template('prediction.html', harga = harga)

if __name__ == '__main__':
    app.run(debug = True)