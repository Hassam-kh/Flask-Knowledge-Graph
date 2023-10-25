from flask import Flask, render_template, request
from rdflib import Graph
import pandas as pd
app= Flask(__name__)

# print("hy")
@app.route('/')
def Start():
    return render_template('index.html')
    # return 'Hello World!'

@app.route('/', methods=['POST'])
def result():
        qry=(request.form.get("query"))
        slt=(request.form.get("select"))
        graph=Graph()
        graph.parse("krr.ttl", format="ttl")
        print("Loaded '" + str(len(graph)) + "' triples.")
        # @app.route('/result')
        w = """
            PREFIX dbp: <http://dbpedia.org/property/'>
            PREFIX dbo: <http://dbpedia.org/ontology/>
            PREFIX : <http://www.Pakistan.com/NationalAssemblyofPakistan#>
            prefix owl: <http://www.w3.org/2002/07/owl#> 
            prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            prefix xsd: <http://www.w3.org/2001/XMLSchema#>
   
"""
        qr = w + """  select """ + slt + """ WHERE {"""+qry+""" }"""
        qy=graph.query(qr)
        # slt=slt.split(' ')
        # if (slt[0]=='*'):
        df=pd.DataFrame(qy)
        # else:    
        #     df=pd.DataFrame(qy,columns=slt)
        return render_template('display.html', tables=[df.to_html(classes='table table-stripped')])

if __name__=="__main__":
    app.run(debug=True)
