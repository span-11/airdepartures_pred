import pickle
import pandas as pd
import numpy as np
from xgboost import XGBRegressor
from flask import Flask,render_template,request,redirect,url_for,Response
import io

model=pickle.load(open('final_model_rr.pkl','rb'))

app=Flask(__name__)

prediction_features=['Fixed telephone subscriptions','Services, value added (current US$)','Manufacturing, value added (current US$)']

@app.route('/',methods=['GET','POST'])
def index():
        if request.method=='POST':
            val_nm=request.form.get('Entry_Type')
            if val_nm=='1':
                return redirect(url_for('manual_entry'))
            else:
                return redirect(url_for('user_file_upload'))
        else:
            return render_template('index.html')

@app.route('/file_upload',methods=['GET','POST'])
def user_file_upload():
    if request.method=='POST':
        uploaded_file=request.files["uploaded_file"]
        filename_file=uploaded_file.filename
        if request.form.get("Main_Menu")=='Go to Main Menu':
            return redirect(url_for('index'))
        elif request.form.get("Manual_Entry")=='Predict using Manual Entry':
            return redirect(url_for('manual_entry'))
        elif request.form.get("Predict_View")=='Predict & View' or request.form.get("Predict_Download")=='Predict & Download':
            if '.xls' in filename_file:
                input_file=pd.read_excel(uploaded_file)
                if input_file.shape[0]!=0:
                    if len(set(input_file.columns).intersection(prediction_features))==3:
                        input_for_prediction=input_file[prediction_features]
                        input_for_prediction=input_for_prediction.apply(lambda x: pd.to_numeric(x,downcast='float',errors='coerce')).fillna(-1)
                        input_file['Air transport, registered carrier departures worldwide']=np.exp(model.predict(input_for_prediction)+1)
                        input_file['Air transport, registered carrier departures worldwide']=input_file['Air transport, registered carrier departures worldwide'].apply(lambda x:round(x))
                        input_file.fillna('',inplace=True)
                        if request.form.get("Predict_View")=='Predict & View':
                            return render_template('file_upload_output.html',  tables=[input_file.to_html(classes='data',header=True,index=False)], titles=input_file.columns.values)
                        else:
                            return Response(input_file.to_csv(index=False),mimetype="text/csv",headers={"Content-disposition":"attachment; filename=Aircraft_Departures-Prediction.csv"})
                    else:
                        return redirect(url_for('user_file_upload_error'))
                else:
                    return redirect(url_for('user_file_upload_error'))
            else:
                return redirect(url_for('user_file_upload_error'))
    else:
        return render_template('file_upload.html')

@app.route('/single_entry',methods=['GET','POST'])
def manual_entry():
    if request.method=='GET':
        return render_template('manual_entry.html')
    else:
        if request.form.get("Main_Menu")=='Go to Main Menu':
            return redirect(url_for('index'))
        elif request.form.get("Upload_File")=='Predict using File Upload':
            return redirect(url_for('user_file_upload'))
        elif request.form.get("Predict")=='Predict':
            form_inputs=pd.DataFrame(request.form.to_dict(),index=[0])
            form_inputs=form_inputs.apply(lambda x:pd.to_numeric(x,downcast='float',errors='coerce')).fillna(-1)
            prediction=np.exp(model.predict(form_inputs[prediction_features])+1)
            return render_template('manual_entry_output.html', dataToRender=round(prediction[0]))
        else:
            return None

@app.route('/file_upload_error',methods=['GET','POST'])
def user_file_upload_error():
    if request.method=='GET':
        return render_template('file_upload_error.html')
    else:
        if request.form.get("Main_Menu")=='Go to Main Menu':
            return redirect(url_for('index'))
        elif request.form.get("Manual_Entry")=='Predict using Manual Entry':
            return redirect(url_for('manual_entry'))
        elif request.form.get("Upload_File")=='Go back to File Upload':
            return redirect(url_for('user_file_upload'))            
        else:
            return None

if __name__=="__main__":
    app.run(debug=True)