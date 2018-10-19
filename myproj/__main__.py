
def run():
    print("Yep, I'm running!")
    user_in = input("type stop then you want me to stop")
    if user_in == "stop":
        stop()
    
def stop():
    print("stopped")
    exit()
        
    
    
  


if __name__ == '__main__':
    run()
