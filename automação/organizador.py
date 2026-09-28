import os
import shutil
from zipfile import ZipFile


class Organizador:
    
    def __init__(self, pasta_bagunça, destino):
        self.pasta_bagunça = pasta_bagunça
        self.destino = destino

    def organizar(self):
        lista = os.listdir(self.pasta_bagunça)
        for file in lista:
            if "." in file:
            
                ext = file.split(".")[-1]
                
                if ext in ['pdf', 'doc', 'docx', 'txt', 'ppt', 'pptx']:
                    os.makedirs(os.path.join(self.pasta_bagunça, 'Documentos'), exist_ok=True)
                    destino = os.path.join(self.pasta_bagunça, 'Documentos', file)
                    
                elif ext in ['jpg', 'jpeg', 'png', 'gif', 'mp4', 'mp3']:
                    os.makedirs(os.path.join(self.pasta_bagunça, 'Midia'), exist_ok=True)
                    destino = os.path.join(self.pasta_bagunça, 'Midia', file)
                    
                elif ext in ['xls', 'xlsx', 'csv']:
                    os.makedirs(os.path.join(self.pasta_bagunça, 'Planilhas'), exist_ok=True)
                    destino = os.path.join(self.pasta_bagunça, 'Planilhas', file)
                    
                elif ext == 'zip':
                    os.makedirs(os.path.join(self.pasta_bagunça, 'Zip'), exist_ok=True)
                    destino = os.path.join(self.pasta_bagunça, 'Zip', file)
                    
                elif ext in ['exe', 'msi']:
                    os.makedirs(os.path.join(self.pasta_bagunça, 'Aplicativos'), exist_ok=True)
                    destino = os.path.join(self.pasta_bagunça, 'Aplicativos', file)
                    
                else:
                    os.makedirs(os.path.join(self.pasta_bagunça, 'Outros'), exist_ok=True)
                    destino = os.path.join(self.pasta_bagunça, 'Outros', file)
                    
                origem = os.path.join(self.pasta_bagunça, file)
                shutil.move(origem, destino)
                
    def descompactar(self, pasta_bagunça, destino):
         pasta_zip = os.path.join(self.pasta_bagunça, 'Zip')
         zipados = os.listdir(pasta_zip)
         for file in zipados:
             if file.endswith('.zip'):
                 caminho_zip = os.path.join(pasta_zip, file)
                 with ZipFile(caminho_zip, 'r') as zip:
                     zip.extractall(pasta_zip)
                      