import threading
from multiprocessing import Pipe, Process, Pool, Queue , Lock, Value
import time
import requests


def save_data(url):
    response = requests.get(url)
    data = response.json()
   
    with open(f"photo_{data['id']}.json", "w") as file:
        file.write(response.text)
        print(f"{data} файл сохранен ")

    
start=time.time()
threads = []
if __name__ == "__main__":
    for i in range(1,101):
        thread = threading.Thread(target=save_data, args=[f"https://jsonplaceholder.typicode.com/todos/{i}"])
        thread.start()
        
        
end=time.time()
print(f"время выполнения : {end-start}")
