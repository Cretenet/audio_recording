# Overview
Audio Recording is a web-based software designed for Data Scientists (including AI engineers, Machine Learning engineers, and others) to facilitate efficient speech data recording. It accepts a list of sentences and sequentially presents them for the user to record. It's important to note that this software prioritizes convenience over traditional web development best practices.

# Installation Steps
To set up the Audio Recording software, follow these steps after downloading:
  1. **Install the Python Libraries:** Install the needed libraries using requirements.txt.

  2. **Add Sentences:** Create a metadata.csv file containing sentences in the format: name_of_audio|sentence to record for each row.

  3. **Audio Folder:** Create a folder named audios at the root level. This is where the recorded audio files will be stored.

  4. **Create Superuser:** Use the command `python manage.py createsuperuser` to create a superuser.

  5. **Migrate Superuser:** Use the command `python manage.py migrate` to migrate your new superuser to the database.
  6. **Create User:** Use the python script 'create_user.py' (edit according to your needs) or through the admin dashboard (accessible by typing 'address_of_your_website/admin' - recommended). A user login is required to access the main page.

  7. **Update Hosts:** Add your host to the ALLOWED_HOSTS and CSRF_TRUSTED_ORIGINS fields in audio_recording/settings.py.

Now you're ready to launch the server. If running on a server, use python manage.py runserver 0.0.0.0:4000, replacing 4000 with your preferred port. Access the web interface at 'https://name_of_your_serv:4000'. For local execution, use python manage.py runserver 4000 and access the software at '127.0.0.1:4000' in your web browser.

# User Guide
When accessing the website, you'll be redirected to the login page. After logging in, you'll land on the main page where you can see the current sentence to record (e.g., if you've already recorded 5 sentences, the 6th will be displayed) and a record button.
<br>
<br>
Clicking the record button starts the recording, and clicking the stop button ends it. You can navigate between sentences using the arrow buttons. Recording a sentence that's already been recorded will replace the old version.
<br><br>
The folder icon (top-left) lets you view all recorded audio files, where you can download them all at once or listen to individual files. Click on the microphone icon (top-left) to return to the main recording page.
