class ArrayList:
    def __init__(self):
        self.array = []
        self.size = 0
    
    def add(self, element):
        """Añade un elemento al final de la lista"""
        self.array.append(element)
        self.size += 1
    
    def get(self, index):
        """Obtiene el elemento en el índice especificado"""
        if 0 <= index < self.size:
            return self.array[index]
        raise IndexError("Índice fuera de rango")
    
    def set(self, index, element):
        """Establece el elemento en el índice especificado"""
        if 0 <= index < self.size:
            self.array[index] = element
            return self.array[index]
        raise IndexError("Índice fuera de rango")
    
    def remove(self, index):
        """Elimina el elemento en el índice especificado"""
        if 0 <= index < self.size:
            element = self.array.pop(index)
            self.size -= 1
            return element
        raise IndexError("Índice fuera de rango")
    
    def size(self):
        """Retorna el tamaño actual de la lista"""
        return self.size
    
    def clear(self):
        """Elimina todos los elementos de la lista"""
        self.array = []
        self.size = 0
         

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una nueva instancia de ArrayList
    lista = ArrayList()
    
    # Añadir elementos
    lista.add("Python")
    lista.add("Java")
    lista.add("C++")
    
    # Obtener elementos
    print("Elemento en índice 0:", lista.get(0))  # Python
    print("Elemento en índice 1:", lista.get(1))  # Java
    
    # Modificar un elemento
    lista.set(1, "JavaScript")
    print("Elemento modificado:", lista.get(1))  # JavaScript
    
    # Eliminar un elemento
    eliminado = lista.remove(2)
    print("Elemento eliminado:", eliminado)  # C++
    
    # Intentar acceder a un índice fuera de rango generará una excepción
    try:
        lista.get(5)
    except IndexError as e:
        print("Error:", str(e))