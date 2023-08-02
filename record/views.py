from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, FileResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import AudioForm, LoginForm
import pandas as pd
import os
import zipfile


PROJECT_DIR = os.path.dirname(os.path.abspath(__file__)) + '/../'

@login_required(login_url='login')
def recording_page(request):
    number = -1
    # Get list of all audio files in directory
    audio_files = os.listdir(PROJECT_DIR + "audios")
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
    df = pd.read_csv(PROJECT_DIR + 'metadata.csv', skiprows=number-1, nrows=1, names=['filename', 'transcript'], delimiter='|', quotechar='\0', index_col=False)
    return render(request, 'recording_page.html', {'new_file_name' : str(df['filename']), 'sentence' : df['transcript'].to_list()[0], 'number' : str(number)})


def go_to(request):
    if request.method == 'POST':
        number = int(request.POST.get('number', 0))
        df = pd.read_csv(PROJECT_DIR + 'metadata.csv', skiprows=number-1, nrows=1, names=['filename', 'transcript'], delimiter='|', quotechar='\0', index_col=False)
        return JsonResponse({'new_file_name' : str(df['filename']), 'sentence' : df['transcript'].to_list()[0], 'number' : str(number)})


def upload_audio(request):
    if request.method == 'POST':
        number = int(request.POST['number'])
        handle_uploaded_file(request.FILES['audio_file'], number)
        df = pd.read_csv(PROJECT_DIR + 'metadata.csv', skiprows=number, nrows=1, names=['filename', 'transcript'], delimiter='|', quotechar='\0', index_col=False)
        return JsonResponse({'new_file_name' : str(df['filename']), 'sentence' : df['transcript'].to_list()[0], 'number' : str(number+1)})
    return render(request, 'recording_page.html')


def handle_uploaded_file(f, number):
    with open(f'{PROJECT_DIR}audios/audio{int(number):0>6}.wav', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('recording_page')
            
    return render(request, 'login.html', context={'form': form})

@login_required(login_url='login')
def audio_list(request):
    storage = FileSystemStorage(location=settings.MEDIA_ROOT)
    audio_files = storage.listdir('')[1] # Get only the files in the directory
    return render(request, 'audio_list.html', {'audio_files': audio_files[::-1]})


def download_all(request):
    # Define the name of the zip file
    zip_filename = "all_audios.zip"

    # Open the zip file in write mode
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        # Iterate over all files in the media directory
        for foldername, subfolders, filenames in os.walk(settings.MEDIA_ROOT):
            for filename in filenames:
                # Get the full path of the file
                file_path = os.path.join(foldername, filename)
                # Add the file to the zip file
                zipf.write(file_path, arcname=filename)

    # Open the zip file in read mode and return it as a FileResponse
    response = FileResponse(open(zip_filename, 'rb'), as_attachment=True, filename=zip_filename)
    return response