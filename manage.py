#!/usr/bin/env python
"""
Arquivo principal de comando do Django.
É através dele que rodamos o servidor, migrations, apps, etc.
"""

import os
import sys

def main():
    # Define qual arquivo de configurações será usado
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        # Importa a função que executa os comandos do Django
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Não foi possível importar o Django. "
            "Verifique se o ambiente virtual está ativado."
        ) from exc
    # Executa o comando digitado no terminal
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
