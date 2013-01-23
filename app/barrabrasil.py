from flask import Flask, url_for, render_template, request, Response, make_response
import hashlib
app = Flask(__name__)

@app.route('/')
def pagina_teste():
    # apos o desenvolvimento substituir por redirect para e-pwg
    bootstrap = '''
    <html>
    <head></head>
    <body>
    <div id="barra-brasil"><a href="http://brasil.gov.br" style="background:#7F7F7F; height: 20px; padding:4px 0 4px 10px; display: block; font-family:sans,sans-serif; text-decoration:none; color:white; ">Portal do Governo Brasileiro</a></div>
    <script src="barra.js?cor=verde" type="text/javascript"></script>
    </body>
    </html>
    '''
    return bootstrap # % url_for('static', filename='barra-brasil.js')

@app.route('/barra.js')
def barra():
    nome_cor = request.args.get('cor', 'azul')
    paleta = {
        'azul': '#004B82',
        'preta': '#000000',
        'cinza': '#7F7F7F',
        'verde': '#00500F',
    }
    cor = paleta.get(nome_cor, '#004B82')
    conteudo = render_template('barra-brasil.js', cor=cor)
    etag = hashlib.sha1(conteudo.encode('utf-8')).hexdigest()
    if request.if_none_match and \
              etag in request.if_none_match:
        resposta = Response(status=304)
    else: # nao esta em cache do navegador
        resposta = make_response(conteudo)
        resposta.set_etag(etag)
        resposta.headers['Content-type'] = 'application/javascript'
    resposta.headers['Cache-control'] = 'max-age: 3600'
    return resposta

if __name__ == '__main__':
    app.run(debug=True)