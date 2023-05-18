from django.shortcuts import render
import pickle

def home(request):
    return render(request, 'BCDetection/index.html')

def getPredictions(ct, ucs, uch, ma, ses, ba, bc, nn, mio):
    model = pickle.load(open('ml_model.sav', 'rb'))

    prediction = model.predict([
        [ct, ucs, uch, ma, ses, ba, bc, nn, mio]
    ])
    print(prediction)
    if prediction == 2:
        return 'low'
    elif prediction == 4:
        return 'high'
    else:
        return 'error'

def result(request):

    ct = int(request.POST.get('ct', False))
    ucs = int(request.POST.get('ucs', False))
    uch = int(request.POST.get('uch', False))
    ma = int(request.POST.get('ma', False))
    ses = int(request.POST.get('ses', False))
    ba = int(request.POST.get('ba', False))
    bc = int(request.POST.get('bc', False))
    nn = int(request.POST.get('nn', False))
    mio = int(request.POST.get('mio', False))

    result = getPredictions(ct, ucs, uch, ma, ses, ba, bc, nn, mio)
    print(result)
    return render(request, 'BCDetection/result.html', {'result': result})