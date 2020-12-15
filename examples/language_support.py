from RAKEkeywords import Rake
from pprint import pprint

rake = Rake(lang="pt")

t = """Portugal, oficialmente República Portuguesa, é um país cujo território se situa na zona ocidental da Península Ibérica e em arquipélagos no Atlântico Norte. 
O território português tem uma área total de 92 090 km², sendo delimitado a norte e leste por Espanha e a sul e oeste pelo oceano Atlântico, compreendendo uma parte continental e duas regiões autónomas: os arquipélagos dos Açores e da Madeira. 
Portugal é a nação mais a ocidente do continente europeu."""
print("TEXT:", t)
keywords = rake.extract_keywords(t)
pprint(keywords)
