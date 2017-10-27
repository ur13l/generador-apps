from config import Config
import handlers.handler
import inspect,sys

class Generador:
    'Clase encargada de generar el nuevo proyecto'
    default_config_path = "./config/config.ini"
    config = None
    handlers = []

    def __init__(self, config_path = default_config_path):
        print("Generador iniciado")
        config = Config(config_path)
        self.preparar_handlers()

    def generar_app(self):
        print("Generando app...")

    def preparar_handlers(self):
        for h, obj in inspect.getmembers(sys.modules['handlers.handler'], inspect.isclass):
            print(obj)



    
