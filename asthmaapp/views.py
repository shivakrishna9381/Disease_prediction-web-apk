from django.shortcuts import render
import numpy as np
import pickle

# Create your views here.
def asthmainput(request):
    return render(request, 'asthmainput.html')

def predictasthma(request):
    if request.method == 'POST':
        try:
            # Convert inputs to appropriate types
            Tiredness = float(request.POST.get('Tiredness', 0))
            drycough = float(request.POST.get("drycough", 0))
            dib = float(request.POST.get("dib", 0))
            sorethroat = float(request.POST.get("sorethroat", 0))
            Pains = float(request.POST.get("Pains", 0))
            stuffynose = float(request.POST.get("stuffynose", 0))
            runnynose = float(request.POST.get("runnynose", 0))
            age = int(request.POST.get("age", 0))
            gender = int(request.POST.get("gender", 0))

            # Age group encoding
            if age >= 0 and age < 10:
                Age_0to9, Age_10to19, Age_20to24, Age_25to59, Age_60 = 1, 0, 0, 0, 0
            elif age >= 10 and age < 20:
                Age_0to9, Age_10to19, Age_20to24, Age_25to59, Age_60 = 0, 1, 0, 0, 0
            elif age >= 20 and age < 25:
                Age_0to9, Age_10to19, Age_20to24, Age_25to59, Age_60 = 0, 0, 1, 0, 0
            elif age >= 25 and age < 60:
                Age_0to9, Age_10to19, Age_20to24, Age_25to59, Age_60 = 0, 0, 0, 1, 0
            else:
                Age_0to9, Age_10to19, Age_20to24, Age_25to59, Age_60 = 0, 0, 0, 0, 1

            # Gender encoding
            Gender_Female, Gender_Male = (0, 1) if gender == 1 else (1, 0)
            count = 0
            if Tiredness == 1:
                count+=1
            if drycough == 1:
                count+=1
            if dib == 1:
                count+=1
            if sorethroat == 1:
                count+=1
            if Pains == 1:
                count+=1
            if stuffynose == 1:
                count+=1
            if runnynose == 1:
                count+=1
            if gender == 1:
                count+=1

            if count >= 5:
                prediction = 1
            else:
                prediction = 0

            # Prepare final input array
            # finalinput = np.array([[Tiredness, drycough, dib, sorethroat, Pains, stuffynose, runnynose, 
            #                         Age_0to9, Age_10to19, Age_20to24, Age_25to59, Age_60, Gender_Female, Gender_Male]])
            # print(finalinput)
            # # Load model and predict
            # with open('asthmadet.pkl', 'rb') as model_file:
            #     loaded_model = pickle.load(model_file)

            # prediction = loaded_model.predict(finalinput)
            # print(prediction)

            return render(request, 'asthmaoutput.html', {'prediction': prediction})
        
        except ValueError:
            return render(request, 'asthmainput.html', {'error': "Invalid input: Please enter valid numbers."})
