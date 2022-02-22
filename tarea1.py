import csv
import numpy as np

def main():
    # Variable que queremos analizar
    lws = 15

    # Obtener datos de .csv
    csvdata = np.genfromtxt('Beijing.csv', 
            skip_header=1, 
            missing_values='NA', 
            delimiter=',', 
            autostrip=True, 
            usecols=lws)
    
    # Remover valores inválidos
    clean_csvdata = csvdata[np.logical_not(np.isnan(csvdata))]
    
if __name__ == "__main__":
    main()
