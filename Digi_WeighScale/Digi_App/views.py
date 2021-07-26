from django.shortcuts import render
import pickle
import requests


def home(request):
    if request.method == "POST":
        chest = float(request.POST.get("chest"))
        bicep = float(request.POST.get("bicep"))
        forearm = float(request.POST.get("forearm"))
        wrist = float(request.POST.get("wrist"))
        abdomen = float(request.POST.get("abdomen"))
        hip = float(request.POST.get("hip"))
        thigh = float(request.POST.get("thigh"))
        knee = float(request.POST.get("knee"))
        ankle = float(request.POST.get("ankle"))
        height = float(request.POST.get("height"))
        age = float(request.POST.get("age"))

        #Loading model to compare the results
        with open('/home/yashpanchal/Desktop/Projects/Weight scale project/Digi_WeighScale/Digi_WeighScale/Digi_App/model.pkl', 'rb') as file_model:
            model = pickle.load(file_model)

        #Predicting the weight
        weight = model.predict([[chest,bicep,forearm,wrist,abdomen,hip,thigh,knee,ankle,height,age]])
        weight = round(weight[0], 2)
        weight = str(weight)
        ans = f"Hi your weight is approximately {weight} kgs"
        print(ans)

        return render(request, 'base.html', {'weight':ans})
    else:
        return render(request, 'base.html')


