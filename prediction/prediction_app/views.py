import os
from django.shortcuts import render
from prediction_app import forms
from django.contrib import messages
import pandas as pd
import numpy as np
import datetime
from sklearn.externals import joblib
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR, 'static')

etc = joblib.load(STATIC_DIR+'/paidoutmodel.pkl')
# Create your views here.

def index(request):
    return render(request, 'prediction_app/index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            # Do something Code
            #print("VALIDATION SUCCESS!")
            #print("House: "+ form.cleaned_data['house'])
            #print("Age: "+ str(form.cleaned_data['age']))

            todays_date = datetime.datetime.now().date()
            index = pd.date_range(todays_date-datetime.timedelta(1), periods=1, freq='D')
            columns = ['A','B', 'C']
            df_ = pd.DataFrame(index=index, columns=columns)
            df_ = df_.fillna(0) # with 0s rather than NaNs
            data = np.array([np.arange(1)]*3).T
            df = pd.DataFrame(data, index=index, columns=columns)
            df['A'] = form.cleaned_data['house']
            df['B'] = form.cleaned_data['age']
            df['C'] = form.cleaned_data['money']
            df2 = df.copy().reset_index()
            df2 = df2.drop(["index"],axis=1)
            answer = (etc.predict_proba(df2.values))[0][1]

            messages.success(
            request,
             str(answer))



    return render(request, 'prediction_app/form_page.html', {'form':form})
