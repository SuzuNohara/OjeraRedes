import pickle
import requests
# Leer el archivo PDF
with open('documento.pdf', 'rb') as f:
    pdf_data = f.read()
# Serializar el contenido del PDF
serialized_data = pickle.dumps(pdf_data)
# Enviar el contenido serializado al servidor
response = requests.post('http://localhost:8080/prueba_serializacion',
files={'file': ('prueba.pdf', serialized_data)})
print(response.text)