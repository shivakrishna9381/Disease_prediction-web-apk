import pickle
from django.shortcuts import render
import numpy as np

# Create your views here.
def stokeinput(request):
    return render(request, "stokeinput.html")

def predictStoke(request):

    if request.method == 'POST':
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        hypertension = request.POST.get('hypertension')
        heartdisease = request.POST.get('heartdisease')
        glucoselevel = float(request.POST.get('averageglucoselevel'))
        bmi = float(request.POST.get('bmi'))
        smokingstatus = request.POST.get('smokingstatus')
        input = np.array([[gender, age, hypertension, heartdisease, glucoselevel, bmi, smokingstatus]])
        print(input)


        with open('strokedet.pkl', 'rb') as model_file:
            loaded_model = pickle.load(model_file)
        
        prediction = loaded_model.predict(input)
        print(prediction)
        return render(request, "stokeoutput.html", {'prediction' : prediction})
    return render(request, "stokeinput.html")