import pickle

from django.shortcuts import render

def home(request):    
    return render(request, 'index.html')


def getPredictions(age,sibsp,parch,fare,embarked,sex,pclass):
    
    model = pickle.load(open("titanic_survival_ml_model.sav", "rb"))
    prediction = model.predict(list(age,sibsp,parch,fare,embarked,sex,pclass))
    
    if prediction == 0:
        return "not survived"
    elif prediction == 1:
        return "survived"
    else:
        return "error"
        


def result(request):
    age = int(request.GET['age'])
    sibsp = int(request.GET['sibsp'])
    parch = int(request.GET['parch'])
    fare = float(request.GET['fare'])
    embarked = int(request.GET('embarked'))
    sex = int(request.GET['sex'])
    pclass = int(request.GET['pclass'])
    
    
    result = getPredictions(age,sibsp,parch,fare,embarked,sex,pclass)
    return render(request, 'result.html', {'result':result})
