from django.shortcuts import render

# Create your views here.
import joblib
import numpy as np
from django.shortcuts import render
from django.http import JsonResponse

# Load the saved model
model = joblib.load("Heart-Disease-Model.pkl")

def predict_heart(request):
    if request.method == 'POST':
        # Extract input data from the form
        age = int(request.POST.get('age'))
        sex = int(request.POST.get('sex'))
        cp = int(request.POST.get('cp'))
        trestbps = int(request.POST.get('trestbps'))
        chol = int(request.POST.get('chol'))
        fbs = int(request.POST.get('fbs'))
        restecg = int(request.POST.get('restecg'))
        thalach = int(request.POST.get('thalach'))
        exang = int(request.POST.get('exang'))
        oldpeak = float(request.POST.get('oldpeak'))
        slope = int(request.POST.get('slope'))
        ca = int(request.POST.get('ca'))
        thal = int(request.POST.get('thal'))

        # Prepare data for the model
        input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        input_data = input_data.reshape(1, -1)

        
        # Make prediction
        model = joblib.load('Heart-Disease-Model.pkl')
        prediction = model.predict(input_data)
        result = 1 if prediction[0] == 1 else 0
        print(result)
        return render(request,'heartresult.html', {'prediction': result})
    
    return render(request, 'heartinput.html')

