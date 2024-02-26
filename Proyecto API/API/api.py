import pandas as pd
from sodapy import Socrata
from tabulate import tabulate

def api_casos(limit_records, departament):
    client = Socrata ("www.datos.gov.co", None )

    selected_data = "ciudad_municipio_nom, departamento_nom, edad, fuente_tipo_contagio, estado, pais_viajo_1_nom"
    results = client . get ("gt2j-8ykr", limit = limit_records , departamento_nom = departament, select = selected_data )

    results_df = pd.DataFrame(results)
    print(results_df.columns)
    
    return results_df

