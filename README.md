# HotRestart

Create scripts to monitor the source code for `login.local` for any changes and automatically reflect the changes in the docker container and restart the containers. You cannot use tools like inotify or any libraries in Python which do file monitoring. Implement it yourself.