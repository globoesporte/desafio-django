import threading
import time
from threading import Timer
from api.models import Voto
import _thread

import logging

class VotoWorker(object):
    _instance = None
    _lista_votos = None

    logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(VotoWorker, cls).__new__(cls, *args, **kwargs)
            cls._lista_votos = []
            cls.thread = None
            cls._lock = threading.RLock()

        return cls._instance

    def adicionar_voto(self, voto):
        
        if not self.thread:
            self.__iniciar_timer()

        with self._lock:
            self._lista_votos.append(voto)
        
    def __executar_schedule(self):
        while True:
            logging.debug("Iniciando inclusão de votos...")
            nova_lista = None

            with self._lock:
                nova_lista = self._lista_votos[:]
                self._lista_votos.clear()

            if(len(nova_lista) > 0):
                self.__salvar_votos(nova_lista)
            
            time.sleep(60.0)

    def __iniciar_timer(self):
        logging.debug('start thread....')
        self.thread = threading.Thread(target=self.__executar_schedule,name="loop_voto")
        self.thread.start()
       
    def __salvar_votos(self, lista_votos):
        logging.debug("Total de votos: %s", len(lista_votos))
        for voto in lista_votos:
           voto = Voto.objects.create(**voto)
        logging.debug("Finalizando inclusão de votos...")
