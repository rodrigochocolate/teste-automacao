import os
import shutil

pastas_caminhos = ('C:/Windows/Temp', 'C:/Users/rodri/AppData/Local/Temp', 'C:/Windows/prefetch')

for pasta_caminho in pastas_caminhos:
    pasta = os.listdir(pasta_caminho)
    print('-' * 30)
    print(pasta_caminho.center(30))
    print('-' * 30)
    for arquivo in pasta:
        caminho = os.path.join(pasta_caminho, arquivo)
        if os.path.isfile(caminho):
            try:
                os.remove(caminho)
                print(f'O arquivo [{arquivo}] foi deletado.')
            except PermissionError:
                print(f'[{arquivo}] permissão negada.')
        elif os.path.isdir(caminho):
            try:
                shutil.rmtree(caminho)
                print(f'A pasta [{arquivo}] foi deletada.')
            except PermissionError:
                print(f'[{arquivo}] permissão negada.')