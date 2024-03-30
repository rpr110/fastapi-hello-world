import socket
import random
import time
import subprocess
from fastapi import FastAPI

app = FastAPI(
    title="FastAPI - System and AWS Info",
    description="Returns system and AWS-related information along with a random number.",
    version="1.0.0",
)



@app.get("/")
def get_info():
    user_ip = socket.gethostbyname(socket.gethostname())
    system_ip = socket.gethostbyname(socket.getfqdn())
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    random_number = random.randint(1, 1000)
    return {
        "User IP": user_ip,
        "System IP": system_ip,
        "AWS Region": None,
        "AWS Availability Zone": None,
        "Current Time": current_time,
        "Random Number": random_number
    }
