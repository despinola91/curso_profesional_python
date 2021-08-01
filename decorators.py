from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs): #No importa la cantidad de argumentos posicionales, recibirlos todos.
        initial_time = datetime.now() #Fecha y hora exacta en que se ejecuta esta linea
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapse = final_time - initial_time
        print("Pasaron " + str(time_elapse.total_seconds()) + " segundos.")
    return wrapper


@execution_time
def random_func():
    for _ in range(1, 100000000): #1 millon de vueltas
        pass


#random_func()

@execution_time
def suma(a: int, b: int) -> int:
    return a + b


@execution_time
def saludo(nombre="Cesar"):
    print("Hola " + nombre)

random_func()
suma(5, 5)
saludo("Dario")