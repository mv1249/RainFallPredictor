from flask import Flask,render_template,request
import pickle

file = open('weather.pkl','rb')
rf = pickle.load(file)
file.close()


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    

@app.route('/parameters')
def parameters():
    return render_template('parameters.html')
    
@app.route('/predict',methods = ['GET','POST'])
def predict():
    if request.method == 'POST':
        my_dict = request.form
        meanrad = float(my_dict['meanrad'])
        meanper = float(my_dict['meanper'])
        meanarea = float(my_dict['meanarea'])
        meancon = float(my_dict['meancon'])
        concavemean= float(my_dict['concavemean'])
        concavepoints = float(my_dict['concavepoints'])
        radworst= float(my_dict['radworst'])
        perworst= float(my_dict['perworst'])
        concaveworst= float(my_dict['concaveworst'])
        concaveworst1= float(my_dict['concaveworst1'])
        concaveworst2= float(my_dict['concaveworst2'])
        concaveworst3= float(my_dict['concaveworst3'])
        concaveworst4= float(my_dict['concaveworst4'])
        concaveworst5= float(my_dict['concaveworst5'])
        input_features = [meanrad,meanper,meanarea,meancon,concavemean,concavepoints,radworst,perworst,concaveworst,concaveworst1,concaveworst2,concaveworst3,concaveworst4,concaveworst5]
        inf = rf.predict([input_features])
        if inf == 1:
            inf = 'NO'
        else:
            inf = 'YES'
        return render_template('show.html',inf = inf)
    return render_template('predict.html')




if __name__ == "__main__":
    app.run(debug = True)