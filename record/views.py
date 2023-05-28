from django.shortcuts import render
from django.http import JsonResponse
from .forms import AudioForm
import pandas as pd
import os

# Create your views here.
def recording_page(request):
    number = -1
    # Get list of all audio files in directory
    audio_files = os.listdir("audios")
    # Filter out non-WAV files and remove extension, convert to integer for sorting
    audio_numbers = sorted([int(f.replace("audio","").replace(".wav","")) for f in audio_files if f.endswith('.wav')])
    # Check for first missing file
    if len(audio_numbers) > 0 :
        for i in range(1, audio_numbers[-1]):
            if i not in audio_numbers:
                number = i
                break
    else:
        number = 1
    if number == -1 :
        number = audio_numbers[-1] + 1
    df = pd.read_csv('metadata.csv', skiprows=number-1, nrows=1, names=['filename', 'transcript', 'other'], delimiter='|', quotechar='\0', index_col=False)
    return render(request, 'recording_page.html', {'new_file_name' : str(df['filename']), 'sentence' : df['transcript'].to_list()[0], 'number' : str(number)})


def go_to(request):
    if request.method == 'POST':
        number = int(request.POST.get('number', 0))
        df = pd.read_csv('metadata.csv', skiprows=number-1, nrows=1, names=['filename', 'transcript', 'other'], delimiter='|', quotechar='\0', index_col=False)
        return JsonResponse({'new_file_name' : str(df['filename']), 'sentence' : df['transcript'].to_list()[0], 'number' : str(number)})


def upload_audio(request):
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            number = int(request.POST.get('number'))
            handle_uploaded_file(request.FILES['audio_file'], number)
            df = pd.read_csv('metadata.csv', skiprows=number, nrows=1, names=['filename', 'transcript', 'other'], delimiter='|', quotechar='\0', index_col=False)
            return JsonResponse({'new_file_name' : str(df['filename']), 'sentence' : df['transcript'].to_list()[0], 'number' : str(number+1)})
    return render(request, 'recording_page.html')


def handle_uploaded_file(f, number):
    with open(f'audios/audio{number}.wav', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)