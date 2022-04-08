class Employee:
    
    def __init__(self, name, id, money_movimentation):
        self.name = name
        self.id = id
        self.money_movimentation = money_movimentation
    

    def check_good_salary(self):
        return self.money_movimentation >= 50000


class Employer:
    
    def __init__(self, name, id, money_movimentation):
        self.name = name
        self.id = id
        self.money_movimentation = money_movimentation


    def check_big_boss(self):
        return self.money_movimentation >= 1000000


class Citizen(Employee, Employer):
    """
        Classe com herança múltipla.
    """
    
    def __init__(self, name, id, money_movimentation):
        super().__init__(name, id, money_movimentation)

    
    def check_rich(self):
        """
            Método que faz uso das implementações das superclasses
            utilizando o método super(). Cada um dos dois supermétodos
            utilizados é de uma superclasse diferente. Ou seja, essa
            classe tem acesso a ambos namespaces.
        """
        
        good_salary = super().check_good_salary()
        big_boos = super().check_big_boss()
        return good_salary and big_boos


def run():
    """
        Roda teste da classe com múltiplas heranças.
    """
    
    john = Citizen('John', 157, 2000000)
    if john.check_rich():
        print('John profits a lot and pay good salaries for his employees!')
    else:
        print('John is not an excelent businessman.')


if __name__ == '__main__':
    run()