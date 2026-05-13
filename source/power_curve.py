from load_data import load_data
from sort import bubble_sort
import matplotlib.pyplot as plt
import os

if __name__ == "__main__":
    # Daten laden 
    power_W = load_data('activity.csv')['PowerOriginal']

    # Sortieren mit Bubble Sort
    sorted_power = bubble_sort(power_W)
    
    # Power Curve plotten
    plt.plot(sorted_power[::-1])

    plt.xlabel("Time [s]")
    plt.ylabel("Power [W]")
    plt.title("Power Curve")

    # Ordner erstellen & Speichern in einem Rutsch
    os.makedirs("figures", exist_ok=True)
    plt.savefig("figures/power_curve.png")
    plt.show()