# Introduction
Audio Recording is a software that allows the user to record speech data efficiently on a web interface. It is possible to give a list of sentences and the system displays them in order and allows the user to record themselves saying each of them. This project is created by and for Data Scientists (Ai engineers, Machine Learning engineers, and so on), so it does not necessarily follow the good practices in the field of web developpment. Its only purpose is to be as convenient as possible.
# Installation
When you download audio_recording, make sure that you :
- Add a metadata.csv file, that contains the sentences in the following format for each row : name_of_audio|sentence to record
- Create a folder named audios (at the root), in which the audios will be uploaded.
- Create a superuser using the `python manage.py createsuperuser` command.
- Migrate your new superuser to the database using `python manage.py migrate`.
- Create a user using the python script 'create_user.py' (modify it according to your needs) or via the admin dashboard that can be reached typing 'address_of_your_website/admin' (recommended). It is necessary to be connected as user to be able to reach the main page.
- Add your host to the ALLOWED_HOSTS and in CSRF_TRUSTED_ORIGINS.
Now that everything is ready, you can start the server. If you are on a server, type `python manage.py runserver 0.0.0.0:4000` where 4000 can be changed to any port, you can then access it by going to 'https://name_of_your_serv:4000'. If you want to run it locally, you can simply type  `python manage.py runserver 4000` where, again, 4000 can be replaced with any port, and you can access it by typing '127.0.0.1:4000' in your browser.
# Usage
When trying to reach the website, you should be redirected to the login page. Login and access the main page. From here, you can see the current sentence (if you already recorded 5, it will be the 6th) and a record button. The record button lets you record yourself by clicking and then clicking on the stop button. You can navigate to the next or to the previous sentence with the arrows. Going back to a sentence that is already recorded and record it again allows you to replace the old version. You can see all the recorded audio files by clicking on the folder (top-left). From there, you can directly download all the files with the button or listen to them one by one. You can come back to the main page with the microphone button (top-left).
