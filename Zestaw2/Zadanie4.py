import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sympify, lambdify, sin

# Function to plot the polynomial using eval()
def rysuj_wielomian(wejscie):
    # Split input into function and range
    funkcja, przedzial = wejscie.split(",")
    x_min, x_max = map(float, przedzial.split())
    
    # Generate x values
    x_val = np.linspace(x_min, x_max, 200)
    
    # Calculate y values using eval()
    y_val = eval(f"[{funkcja.strip()} for x in x_val]")
    
    # Plot the graph
    plt.plot(x_val, y_val, label="Polynomial (eval)", color="blue")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Polynomial Graph (eval)")
    plt.grid(True)
    plt.legend()
    
    # Return values at the boundaries of the interval
    return y_val[0], y_val[-1]

# Function to plot the polynomial using SymPy and lambdify()
def rysuj_wielomian_sympy(wejscie):
    # Split input into function and range
    funkcja, przedzial = wejscie.split(",")
    x_min, x_max = map(float, przedzial.split())

    # Replace np.sin() with sympy.sin() for compatibility
    funkcja = funkcja.replace("np.sin", "sin")
    
    # Define the symbol and convert to a numerical function using SymPy
    x = symbols('x')
    wyrazenie = sympify(funkcja.strip())  # Now sympy will understand sin(x)
    funkcja_numeryczna = lambdify(x, wyrazenie, modules="numpy")
    
    # Generate x values
    x_val = np.linspace(x_min, x_max, 200)
    
    # Calculate y values using the numerical function
    y_val_sympy = funkcja_numeryczna(x_val)
    
    # Plot the graph
    plt.plot(x_val, y_val_sympy, label="Polynomial (SymPy)", color="orange")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Polynomial Graph (SymPy)")
    plt.grid(True)
    plt.legend()
    
    # Return values at the boundaries of the interval
    return y_val_sympy[0], y_val_sympy[-1]

if __name__ == '__main__':
    # Example input for eval
    wejscie1 = "x**3 + 3*x + 1, -10 10"
    
    # First graph using eval
    wynik_eval = rysuj_wielomian(wejscie1)
    print("Result (eval):", wynik_eval)
    
    # Example input for SymPy - more complex function with np.sin
    wejscie2 = "x**4 - 5*x**2 + 3*np.sin(x), -10 10"  
    
    # Second graph using SymPy
    wynik_sympy = rysuj_wielomian_sympy(wejscie2)
    print("Result (SymPy):", wynik_sympy)
    
    # Display both graphs
    plt.show()
