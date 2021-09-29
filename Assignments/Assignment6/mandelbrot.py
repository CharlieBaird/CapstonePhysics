import numpy

class Complex:
    def __init__(self, a, b):
        self.real = a
        self.imag = b

def multiply(this, that):
    term1 = this.real*that.real
    term2 = this.real*that.imag + this.imag*that.real
    term3 = this.imag*that.imag*-1

    return Complex(term1 + term3, term2)


def generate_fractal():

    x = numpy.linspace(0,5,10)
    print(x)

    # plt.figure(figsize=(10,10))
    # plt.scatter(xx, yy, 1, c=color_array, cmap="binary")
    # plt.show()

generate_fractal()