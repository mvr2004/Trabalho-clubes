from django.apps import AppConfig
from django.db.utils import OperationalError

class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'BD2_Trabalhofinal.App'  
    
    def ready(self):
        import BD2_Trabalhofinal.App.signals  # Importa os sinais
        
        # Inserir dados iniciais se não houver
        try:
            from .models import P_Associacao  # importa um dos teus models
            if not P_Associacao.objects.exists():
                # importa e executa o teu comando inserir_dados
                from .management.commands.inserir_dados import Command
                cmd = Command()
                cmd.handle()
        except OperationalError:
            # A base ainda não existe ou as migrações não foram aplicadas
            pass
