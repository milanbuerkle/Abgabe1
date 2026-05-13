import numpy as np
import matplotlib.pyplot as plt
import os

from sort import bubble_sort

def main():
    # Pfad zum Ordner mit den Daten
    data_folder = 'data'
    
    # Liste aller Dateien im Ordner
    files = os.listdir(data_folder)
    
    # Dictionary, um die Daten zu speichern
    data_dict = {}
    
    # Einlesen der Daten aus den Dateien
    for file in files:
        if file.endswith('.txt'):
            with open(os.path.join(data_folder, file), 'r') as f:
                data = [float(line.strip()) for line in f]
                data_dict[file] = data
    
    # Sortieren der Daten und Plotten der Power Curves
    plt.figure(figsize=(10, 6))
    
    for file, data in data_dict.items():
        sorted_data = bubble_sort(data)
        plt.plot(sorted_data, label=file)
    
    plt.title('Power Curves')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.legend()
    plt.grid()
    plt.show()