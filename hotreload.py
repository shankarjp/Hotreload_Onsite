import os
import time

last_mod = 0
try:
    while True:
        result = os.stat('./node/server.js')
        if(result.st_mtime > last_mod):
            last_mod = result.st_mtime
            print("Restarting Docker Containers...")
            os.system('sudo docker-compose down')
            os.system('sudo docker rmi -f delta-onsite-hotreload_node')
            os.system('sudo docker-compose up -d')
except KeyboardInterrupt:
    pass
