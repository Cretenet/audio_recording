from django.shortcuts import render
from django.http import JsonResponse
from .forms import AudioForm
import pandas as pd

# Create your views here.
def recording_page(request):
    return render(request, 'recording_page.html')
    #return HttpResponse("Hello, world. You're at the recording page.")


def upload_audio(request):
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            number = int(request.POST.get('number'))
            handle_uploaded_file(request.FILES['audio_file'], number)
            test = pd.read_csv('metadata.csv', delimiter='|')
            df = pd.read_csv('metadata.csv', skiprows=number, nrows=1, names=['filename', 'transcript', 'other'], delimiter='|', quotechar='\0', index_col=False)
            t = df['transcript'].to_list()[0]
            return JsonResponse({'new_file_name' : str(df['filename']), 'sentence' : df['transcript'].to_list()[0], 'number' : str(number+1)})
            #return render(request, 'recording_page.html', {'number': number})
    return render(request, 'recording_page.html')


def handle_uploaded_file(f, number):
    with open(f'audios/audio{number}.wav', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)