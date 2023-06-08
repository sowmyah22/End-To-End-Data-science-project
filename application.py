from flask import Flask,render_template,request,url_for,redirect
from src.pipeline.predict_pipeline import PredictPipeline,CustomData
application = Flask(__name__)
app=application

## Route to the home page
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result/<float:res>')
def result(res):
    return render_template('results.html',res=res)

@app.route('/prediction',methods=['GET','POST'])
def prediction():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('Ethnicity'),
            parental_level_of_education=request.form.get('Parental Level of Education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            math_score=float(request.form.get('Math score')),
            reading_score=float(request.form.get('Reading Score')),
            writing_score=float(request.form.get('Writing score'))
            
        )
        predictions_df=data.get_data_as_dataframe()
        print(predictions_df)

        predict_pipeline=PredictPipeline()
        results=predict_pipeline.predict(predictions_df)
        return redirect(url_for('result',res=results[0]))
        
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

