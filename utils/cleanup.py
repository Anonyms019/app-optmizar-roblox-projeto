import os
import shutil
import tempfile

def clear_temp_files():
    temp_dir = tempfile.gettempdir()
    print(f"Limpando arquivos temporários em {temp_dir}...")
    try:
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                try:
                    os.remove(os.path.join(root, file))
                except:
                    pass
        print("Limpeza concluída!")
    except Exception as e:
        print(f"Erro ao limpar arquivos: {e}")
