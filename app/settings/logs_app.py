from flask import Flask
import logging
from logging.handlers import RotatingFileHandler
import os
from datetime import date


class DailyLogHandle:
    """
        Classe responsável por gerenciar o handler de log diário na api Flask
    """
    
    def __init__(self, app:Flask):
        self.app = app
        self.current_date = date.today()
        self.log_dir = f'app/logs/AppLog_{str(self.current_date)}'
        self.log_file = f"{self.log_dir}/flask_app.log"
        self.handler = None
        self.setup_handler()
    
    def setup_handler(self):
        
        if not os.path.exists(f'app/logs/AppLog_{str(date.today())}'):
            os.makedirs(f'app/logs/AppLog_{str(date.today())}')

        self.handler = RotatingFileHandler(self.log_file, maxBytes = 10240, backupCount = 5)
        
        self.handler.setLevel(logging.INFO)
        
        formatter = logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    )

        self.handler.setFormatter(formatter)
        
        self.app.logger.addHandler(self.handler)
        
        self.app.logger.setLevel(logging.INFO)
        
        
    def update_handler_if_needed(self):
        """Verificar se o dia mudou para que possa atualiza o handler"""
        
        today = date.today()
        if today != self.current_date:
            self.current_date = date.today()
            
            self.log_dir = f'app/logs/AppLog_{str(self.current_date)}'
            self.log_file = f"{self.log_dir}/flask_app.log"
            
            self.app.logger.removeHandler(self.handler)
            
            self.setup_handler()
            
def logs_api(app: Flask):
    
    """Configuta logs diários"""
        
    log_handler = DailyLogHandle(app)
    
    @app.before_request
    def update_log_handler():
        """Atualiza o handler antes de processar qualquer requisição"""
        log_handler.update_handler_if_needed()
        
    app.logger.info('Flask app startup')