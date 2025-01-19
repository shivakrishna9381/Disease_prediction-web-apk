from django.shortcuts import render
import pickle
import numpy as np

# Create your views here.
def Diabetes_validate(request):
    if request.method == 'POST':
        pregnancies = int(request.POST.get('pregnancies'))
        glucose = float(request.POST.get('glucose'))
        blood_pressure = float(request.POST.get('blood_pressure'))
        skin_thickness = float(request.POST.get('skin_thickness'))
        insulin = float(request.POST.get('insulin'))
        bmi = float(request.POST.get('bmi'))
        diabetes_pedigree_function = float(request.POST.get('diabetes_pedigree_function'))
        age = int(request.POST.get('age'))

        # Prepare input for the model
        final_input = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin,
                                  bmi, diabetes_pedigree_function, age]])
        # Load the model from file
        with open('random_forest_model.pkl', 'rb') as model_file:
            loaded_model = pickle.load(model_file)

        # Make predictions using the loaded model
        prediction = loaded_model.predict(final_input)
        print(prediction)

        # Render results page with the prediction result
        return render(request, "Diabetes-Resultspage.html", {'prediction': prediction})

    # If not POST, you can render the input form page (optional)
    return render(request, "Diabetes-Formpage.html")
