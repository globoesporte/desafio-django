import threading
from threading import Timer
from api.models import Voto

class VotoWorker(object):
    _instance = None
    _lista_votos = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(VotoWorker, cls).__new__(cls, *args, **kwargs)
            cls._lista_votos = []
            cls._lock = threading.RLock()
            cls.__iniciar_timer(cls)
            
        
        return cls._instance

    def adicionar_voto(self, voto):
        with self._lock:
            self._lista_votos.append(voto)
        
    def __executar_schedule(self):
         nova_lista = None
         with self._lock:
            nova_lista = self._lista_votos[:]
            self._lista_votos.clear()

         self.__salvar_votos(nova_lista)

    def __iniciar_timer(self):
        Timer(30000, self.__executar_schedule, ()).start()

    def __salvar_votos(lista_votos):
        for voto in lista_votos:
            voto.save()
