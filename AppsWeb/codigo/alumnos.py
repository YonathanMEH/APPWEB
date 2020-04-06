import web
import csv
import json  


class AlumnosApi:
 
    file = '/static/csv/alumnos.csv' 

    def __init__(self):  
        pass  # Salta a la siguiente ejecución

    def get(self): #Crea al metodo  get  para recibir datos por url
        try:
            data = web.input()  #Recibe los datos por url
            if data['token'] == "1234":  #Valida el token que se recibe por url
                if data['action'] == 'get':  #Evalua la acción get
                    result = self.actionGet(self.app_version, self.file)  #Llama al metodo actionGet(), y almacena el resultado
                    return json.dumps(result)  #Transforma el diccionario result a formato json para poder ser leido
                else:
                    result = {}  #Crea un diccionario vacio
                    result['app_version'] = self.app_version  #Version de la webapp
                    result['status'] = "Command not found"
                    return json.dumps(result)  #Transforma el diccionario result a formato json
            else:
                result = {}  #Crea un nuevo diccionario vacio
                result['app_version'] = self.app_version  #Version de la app
                result['status'] = "Invalid Token"
                return json.dumps(result)  # Transforma el diccionario result a formato json
        except Exception as e:
            print("Error")
            result = {}  #Crea un nuevo diccionario vacio
            result['app_version'] = self.app_version  #Version de la app
            result['status'] = "Values missing, sintaxis: alumnos?action=get&token=XXXX"
            return json.dumps(result)  #Transforma el diccionario result a formato json

    @staticmethod
    def actionGet(app_version, file):
        try: #Se crea el bloque try
            result = {}  #Crea un nuevo diccionario vacio
            result['app_version'] = app_version  #Version de la app
            result['status'] = "Ok"  #Mensaje de status
            
            with open(file, 'r') as csvfile:  #Abre el archivo en modo lectura
                reader = csv.DictReader(csvfile)  #Toma la primer fila para los nombres
                alumnos = []  #Se crea un arreglo para almacenar todos los alumnos
                for row in reader:  #Comienza a leer el archivo CSV fila por fila
                    fila = {}  #Genera un diccionario por cada fila en el csv
                    fila['matricula'] = row['matricula']  #Obtiene la matricula y la agrega al diccionario fila
                    fila['nombre'] = row['nombre']  #Optione el nombre y lo agrega al diccionario
                    fila['primer_apellido'] = row['primer_apellido']  #Obtiene el primer apellido
                    fila['segundo_apellido'] = row['segundo_apellido']  #Obtiene el segundo apellido
                    fila['carrera'] = row['carrera']  #Obtiene la carrera
                    alumnos.append(fila)  #Agrega el diccionario generado al arreglo
                result['alumnos'] = alumnos  #Agrega el arreglo al diccionario result
            return result  #Regresa el diccionario generado
        except Exception as e: #Es la excepcion del bloque try
            result = {}  #Se crear un nuevo diccionario vacio
            print("Error {}".format(e.args())) 
            result['app_version'] = app_version  #Version de la app
            result['status'] = "Error "  #Mensaje de status (alerta de error)
            return result  #Regresa el diccionario que se creo
