import os

last_mod = 0
array = []
for filepath in os.listdir('./node'):
    if(os.path.isdir(os.path.join('./node',filepath))):
        for files in os.listdir(os.path.join('./node',filepath)):
            array.append(os.stat(os.path.join('./node',filepath, files)).st_mtime)
    else:
        array.append(os.stat(os.path.join('./node',filepath)).st_mtime)
result = max(array)

try:
    while True:
        if(result > last_mod):
            last_mod = result
            print("Restarting Docker Containers...")
            os.system('sudo docker-compose down')
            os.system('sudo docker rmi -f delta-onsite-hotreload_node')
            os.system('sudo docker-compose up -d')
except KeyboardInterrupt:
    pass
