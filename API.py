from flask import Flask, render_template,url_for,request
import os
import pymongo

app=Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
def pagina_inicial():
    return render_template("pagina.html")


@app.route("/cadastro", methods=['GET','POST'])
def cadastro():     
    return render_template("paginaCadastro.html")

       
@app.route("/CadastroRealizado", methods=['GET','POST'])
def CadastroRealizado():
    if request.method == 'POST':
        diretorio= "C:\\Users\\edmar\\Meus_codigos\\API\\arquivos"
        conexao = pymongo.MongoClient("localhost",27017)
        db=conexao.api
        colecao=db.cadastro
        formulario= dict(request.form)
        
        #insere dados no banco e recolhe o ID
        _id=colecao.insert_one(formulario).inserted_id
        _id=str(_id)
        arquivo=request.files.get("documento")
        #salva o arquivo com o ID da inclusão em seu nome.
        nomeFile = str(arquivo.filename)
        nomeFile = str(_id + nomeFile)
        arquivo.save(os.path.join(diretorio,nomeFile))
        return render_template("CadastroRealizado.html")
    
    return render_template("pagina.html")

@app.route("/pagina.html",methods=['GET', 'POST'])
def retorno_pagina_inicial():
    return render_template("pagina.html")

#colocar site no ar
if __name__ == "__main__":
    app.run(debug=True)

