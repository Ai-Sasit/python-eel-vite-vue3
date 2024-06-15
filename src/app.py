import eel

eel.init('web')

@eel.expose
def say_hello_py():
    print("Hello World") 
    
if __name__ == '__main__':
    eel.start('index.html')