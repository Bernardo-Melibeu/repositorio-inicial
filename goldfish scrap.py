import requests
from bs4 import BeautifulSoup
import json

URL="https://www.mtggoldfish.com"
BUSCA="/metagame/standard#paper"


def pega_e_cozinha(endereço=URL+BUSCA):
  response=requests.get(endereço).content
  soup=BeautifulSoup(response,"html.parser")
  return soup
    
def grava_json(arquivo):
  with open("dicio.json","w") as f:
    json.dump(arquivo,f,indent=4)


cont=0
soup=pega_e_cozinha()
lista_l=[]
lista_l=soup.find_all("a")
dicio_cartas={}
lista_final=[]
for i in lista_l:
  if(cont>80):
    break
  try:
    if("/archetype/" in i["href"] and "online" not in i["href"]and i["class"]!="card-image-title-link-overlay"):
      link=i["href"]
    else:
      soup=pega_e_cozinha(URL+link)
      soma=0
      localiza=0
      titulo=soup.find("h1").text
      autor=titulo.split("\n")[2]
      autor=autor[3:]
      titulo=titulo.split("\n")[1]
      lista_deck=[]
      lista_qtd=[]
      lista_nomes=[]
      lista_qtd=soup.find_all("td", class_="text-right")
      lista_nomes=soup.find_all("span",class_="card_id card_name")
      for nomes in range(len(lista_nomes)):
        lista_nomes[nomes]=lista_nomes[nomes].text
      deck=[]
      for l in lista_qtd:
        if (soma<60):
          if("$" not in l.text and "tix" not in l.text and "Unc" not in l.text and "Mythic" not in l.text and "Rare" not in l.text and "Comm" not in l.text):
            soma+=int(l.text)
            deck.append({lista_nomes[localiza]:int(l.text)})
            localiza+=1
      dicio_cartas[titulo]={"autor":autor,"lista":deck,"link":link}
      grava_json(dicio_cartas)
      cont+=1
  except:
    continue
  

print("fim")