import numpy as np
import matplotlib.pyplot as plt
import math

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
    clean_csvdata = np.sort(csvdata[np.logical_not(np.isnan(csvdata))])
    length = len(clean_csvdata)
    print("Cantidad de datos válidos: {}".format(length))

    # Mediana
    if length%2 == 0:
        median = 0.5*(clean_csvdata[length/2 -1] + clean_csvdata[length/2])
    else:
        median = clean_csvdata[int((length-1)/2)] 

    # Cuartiles por método simple
    if length%4 == 0:
        q1_index        = int(length/4 - 1)
        q3_index        = int(3*length/4 - 1)
    else:
        q1_index        = math.ceil(length/4 - 1)
        q3_index        = math.ceil(3*length/4 - 1)

    q1=clean_csvdata[q1_index]
    q3=clean_csvdata[q3_index]

    # Media
    mean = np.mean(clean_csvdata)

    # Moda
    unique, frequency = np.unique(clean_csvdata, return_counts=True)

    trend = unique[frequency.argmax()]

    print("Medidas de tendencia central:\n\tQ1: {}\n\tMediana: {}\n\tQ3: {}\n\tMedia: {}\n\tModa: {}\n".format(q1, median, q3, mean, trend))


    # Variabilidad
    variance = ((clean_csvdata-mean)**2).sum()/(length-1)
    deviation = math.sqrt(variance)
    var_coefficient = deviation/mean
    sample_range = clean_csvdata.max() - clean_csvdata.min()
    RIC = q3-q1

    print("Medidas de variabilidad:\n\tVarianza: {}\n\tDesviación Estandar: {}\n\tCoeficiente de variación: {}%\n\tRango muestral: {}\n\tRIC: {}\n".format(variance, deviation, var_coefficient*100, sample_range, RIC))


    # Diagrama de cajas
    lim_inferior = q1-1.5*RIC
    lim_superior = q3+1.5*RIC
    valid_data = clean_csvdata[np.where((clean_csvdata >= lim_inferior) & (clean_csvdata <= lim_superior))]
    max_adentro = valid_data.max()
    min_adentro = valid_data.min()
    atypic_data = clean_csvdata[np.where((clean_csvdata < lim_inferior) | (clean_csvdata > lim_superior))]

    print("Datos diagrama de cajas:\n\tLímite inferior: {}\n\tLímite superior: {}\n\tBigote inferior: {}\n\tBigote superior: {}\n\tCantidad de puntos atípicos: {}\n".format(lim_inferior, lim_superior, min_adentro, max_adentro, len(atypic_data)))


    fig_box, ax_box = plt.subplots()

    ax_box.boxplot(clean_csvdata,
            vert=False)

    ax_box.set_title('Diagrama de cajas')
    ax_box.set_xlabel('lws')
    ax_box.set_yticks([])

    fig_box.savefig("diagrama_cajas.svg")
    
if __name__ == "__main__":
    main()
    plt.show()
