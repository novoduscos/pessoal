from organizador import Organizador as org

pasta_bagunça = input("Digite o caminho da pasta bagunçada: ")
destino = input("Digite o caminho da pasta de destino: ")

a = org(pasta_bagunça, destino)
a.organizar()