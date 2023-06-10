# audio_recording
Software allowing to record speech data efficiently on a web interface.

When you download audio_recording, make sure that you add a metadata.csv, create a folder named audios (at the root), create a superuser using the createsuperuser command and create a user using the python script or the admin dashboard. You must also add your host to the ALLOWED_HOSTS.

To make it run on a server, run the command "python manage.py runserver 0.0.0.0:4000" where 4000 can be replaced with any port.
