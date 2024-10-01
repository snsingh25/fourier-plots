import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Define the square wave function
def square_wave(x):
    return np.where((x % (2 * np.pi)) < np.pi, 1, -1)

# Compute the Fourier by the series partial sum  formula
def fourier_series_square_wave(x, N):
    sum = np.zeros_like(x)
    for k in range(1, N + 1):
        n = 2 * k - 1  # Only odd harmonics
        sum += (4 / (np.pi * n)) * np.sin(n * x)
    return sum

term_counts = [10, 20, 30, 40, 50]

# Function to format x-axis ticks as multiples of pi
## https://stackoverflow.com/questions/40642061/how-to-set-axis-ticks-in-multiples-of-pi-python-matplotlib
x = np.linspace(-2 * np.pi, 4 * np.pi, 1000)
def multiple_pi_formatter(x, pos):
    n = int(np.round(x / np.pi))
    if n == 0:
        return '0'
    elif n == 1:
        return r'$\pi$'
    elif n == -1:
        return r'$-\pi$'
    else:
        return r'${0}\pi$'.format(n)

# Optional: Save the exact square wave as a separate PDF
plt.figure(figsize=(12, 4))
plt.plot(x, square_wave(x), label='Square Wave', color='black')
plt.title('Exact Square Wave')
plt.ylim(-2, 2)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xticks(np.arange(-2 * np.pi, 4.5 * np.pi, np.pi), [r'$-2\pi$', r'$-\pi$', '0', r'$\pi$', r'$2\pi$', r'$3\pi$', r'$4\pi$'])     
plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(multiple_pi_formatter))
plt.legend(loc='upper right')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

plt.savefig('square_wave.pdf')
plt.close()

# Plotting and Saving Individual Fourier Series Approximations
for N in term_counts:
    plt.figure(figsize=(12, 4))
    plt.plot(x, square_wave(x), label='Square Wave', color='lightgray', linestyle='--')
    plt.plot(x, fourier_series_square_wave(x, N), label=f'N={N}')
    plt.title(f'Fourier Series Approximation with {N} Terms')
    plt.ylim(-2, 2)
    plt.xlabel('x')
    plt.ylabel(f'$f_{{N={N}}}(x)$')
    plt.xticks(np.arange(-2 * np.pi, 4.5 * np.pi, np.pi), [r'$-2\pi$', r'$-\pi$', '0', r'$\pi$', r'$2\pi$', r'$3\pi$', r'$4\pi$'])
    plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(multiple_pi_formatter))
    plt.legend(loc='upper right')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()

    # Save each plot as a separate PDF file
    plt.savefig(f'fourier_square_wave_N{N}.pdf')
    plt.close()
