class Contador:
    # Atributo de clase para contar instancias
    contadores_creados = 0
    
    def __init__(self, valor_inicial=0):
        # Inicializa el valor del contador con el valor proporcionado
        self.valor = valor_inicial
        # Incrementa el contador de instancias creadas
        Contador.contadores_creados += 1
        
    def incrementar(self):
        """
        Incrementa el valor del contador en 1 y devuelve el nuevo valor.
        """
        self.valor += 1
        return self.valor
    
    def decrementar(self):
        """
        Disminuye el valor del contador en 1 y devuelve el nuevo valor.
        El contador nunca debe ser negativo.
        """
        if self.valor > 0:
            self.valor -= 1
        return self.valor
    
    @classmethod
    def reiniciar_contador_global(cls):
        """
        Método de clase que reinicia el contador de instancias creadas.
        """
        cls.contadores_creados = 0
    
    @staticmethod
    def es_par(numero):
        """
        Método estático que verifica si un número es par.
        
        Args:
            numero: El número a verificar.
            
        Returns:
            True si el número es par, False en caso contrario.
        """
        return numero % 2 == 0