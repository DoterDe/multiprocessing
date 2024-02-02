from multiprocessing import Pipe, Process, Pool, Queue , Lock, Value
import time
import requests
import random


def save_data(url):
    response = requests.get(url)
    data = response.json()
   
    with open(f"photo_{data['id']}.json", "w") as file:
        file.write(response.text)
        print(f"{data} файл сохранен ")

    
start=time.time()
if __name__ == "__main__":
    with Pool(processes=10) as pool:
        pool.map(save_data, [f'https://jsonplaceholder.typicode.com/todos/{i}' for i in range(1,1001)])
end=time.time()
print(f"время выполнения : {end-start}")