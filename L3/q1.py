from abc import abstractmethod


class PrintUtils:

    n = 20

    def __init__(self):
        pass


    @staticmethod
    def print_emphasized_text(message):
        """
            Método estático útil para ser usado como utilidade.
            A classe PrintUtils tem métodos estáticos utilitários para prints.
        """

        print(('-' * 20 + '\n') * 3, end='')
        print(message)
        print(('-' * 20 + '\n') * 3)


    @staticmethod
    def print_upper_emphasized_text(message):
        """
            Método estático útil para ser usado como utilidade.
            A classe PrintUtils tem métodos estáticos utilitários para prints.
        """

        print(('-' * 20 + '\n') * 3, end='')
        print(message.upper())
        print(('-' * 20 + '\n') * 3)


    @classmethod
    def print_emphasized_text2(cls, message):
        """
            Método de classe útil para ser usado como utilidade.
            A classe PrintUtils tem métodos estáticos utilitários para prints.
        """

        print(('-' * 20 + '\n') * 3, end='')
        print(message)
        print(('-' * 20 + '\n') * 3)


    @classmethod
    def change_n(cls, new_n):
        """
            Método de classe útil para ser usado como utilidade.
            A classe PrintUtils tem métodos estáticos utilitários para prints.
            O usuário pode definir a quantidade "n" de hífens do print da classe,
            a qual é utilizada no método de classe "print_emphasized_text2".
        """

        cls.n = new_n


class BaseFilter:
    """
        Classe pai para filtros de imagens (matrizes de pixels P/B).
    """


    def __init__(self, image_pixels):
        self.image_pixels = image_pixels
        self.new_image_pixels = [row.copy() for row in image_pixels]
        self.n = len(image_pixels)
        if self.n != 0:
            self.m = len(image_pixels[0])
        else:
            self.m = 0


    def print_pixels(self):
        """
            Método de instância útil e igual para todos os filtros.
            Printa valores de todos os pixels.
        """

        for i in range(self.n):
            for j in range(self.m):
                print(self.new_image_pixels[i][j], end=' ')
            print()
        print()


    def print_pixel_diff(self):
        """
            Método de instância útil e igual para todos os filtros.
            Printa diferença entre os valores de antes e depois dos pixels.
        """

        for i in range(self.n):
            for j in range(self.m):
                print(self.new_image_pixels[i][j] - self.image_pixels[i][j], end=' ')
            print()
        print()


    @abstractmethod
    def apply(self):
        """
            Método abstrato que todos os filtros devem ter.
            É a definição de cada filtro.
        """
        pass


class BlurFilter(BaseFilter):
    
    def __init__(self, image_pixels, filter_size):
        super().__init__(image_pixels)
        self.filterSize = filter_size

    
    def apply(self):
        side_offset = int((self.filterSize - 1)/2)
        for i in range(side_offset, self.n - side_offset):
            for j in range(side_offset, self.m - side_offset):
                pixels_sum = 0
                for k in range(-side_offset, side_offset + 1):
                    for l in range(-side_offset, side_offset + 1):
                        pixels_sum += self.image_pixels[i+k][j+l]
                self.new_image_pixels[i][j] = int(pixels_sum/(self.filterSize**2))


class CrazyFilter(BaseFilter):

    def __init__(self, image_pixels):
        super().__init__(image_pixels)

    
    def apply(self):
        for i in range(self.n):
            self.new_image_pixels[i] = self.image_pixels[self.n - 1 - i]


def run_utils_methods():
    """
        Roda teste com os métodos da classe PrintUtils.
    """
    PrintUtils.print_emphasized_text('Hello World!')
    PrintUtils.print_upper_emphasized_text('Hello World!')
    PrintUtils.print_emphasized_text2('Hello World!')
    PrintUtils.change_n(40)
    PrintUtils.print_emphasized_text2('Hello World!')


def run_filters():
    """
        Roda teste com os métodos das classes de filtro.
    """

    # Image matrix
    n = 10
    m = 5
    image_pixels = [[int(2.5*(i+3)+2*j-(i*j) + 10*(i%2) + 10*(j%3)) for i in range(m)] for j in range(n)]

    # Blur filter example

    blur_filter = BlurFilter(image_pixels, 3)

    print('Original image:\n')
    blur_filter.print_pixels()

    blur_filter.apply()
    print('Filtered image:\n')
    blur_filter.print_pixels()

    print('Difference between images:\n')
    blur_filter.print_pixel_diff()

    # Crazy filter example

    crazy_filter = CrazyFilter(image_pixels)

    print('Original image:\n')
    crazy_filter.print_pixels()

    crazy_filter.apply()
    print('Filtered image:\n')
    crazy_filter.print_pixels()

    print('Difference between images:\n')
    crazy_filter.print_pixel_diff()


if __name__ == '__main__':
    # TESTES
    run_filters()
    run_utils_methods()