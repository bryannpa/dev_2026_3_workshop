class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):
        """
        Verifica si una cadena es un palíndromo (se lee igual de izquierda a derecha y viceversa).
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si es palíndromo, False en caso contrario
        """
        pass

        inicio = 0
        fin = len(texto) - 1
        while inicio < fin:
            if texto[inicio] != texto[fin]:
                return False
            inicio += 1
            fin -= 1
        return True

    def invertir_cadena(self, texto):
        """
        Invierte una cadena de texto sin usar slicing ni reversed().
        
        Args:
            texto (str): Cadena a invertir
            
        Returns:
            str: Cadena invertida
        """
        pass

        resultado = ""
        for caracter in texto:
            resultado = caracter + resultado
        return resultado
    
    
    def contar_vocales(self, texto):
        """
        Cuenta el número de vocales en una cadena.
        
        Args:
            texto (str): Cadena para contar vocales
            
        Returns:
            int: Número de vocales en la cadena
        """
        pass

        vocales = "aeiouAEIOU"
        contador = 0
        for caracter in texto:
            if caracter in vocales:
                contador += 1
        return contador

    def contar_consonantes(self, texto):
        """
        Cuenta el número de consonantes en una cadena.
        
        Args:
            texto (str): Cadena para contar consonantes
            
        Returns:
            int: Número de consonantes en la cadena
        """
        pass

        consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        contador = 0
        for caracter in texto:
            if caracter in consonantes:
                contador += 1
        return contador
    
    def es_anagrama(self, texto1, texto2):
        """
        Verifica si dos cadenas son anagramas (contienen exactamente los mismos caracteres).
        
        Args:
            texto1 (str): Primera cadena
            texto2 (str): Segunda cadena
            
        Returns:
            bool: True si son anagramas, False en caso contrario
        """
        pass

        if len(texto1) != len(texto2):
            return False
        texto1 = texto1.lower()
        texto2 = texto2.lower()
        for caracter in texto1:
            if texto1.count(caracter) != texto2.count(caracter):
                return False
        return True

        
    def contar_palabras(self, texto):
        """
        Cuenta el número de palabras en una cadena.
        
        Args:
            texto (str): Cadena para contar palabras
            
        Returns:
            int: Número de palabras en la cadena
        """
        pass

        palabras = texto.split()
        return len(palabras)

    
    def palabras_mayus(self, texto):
        """
        Pon en Mayuscula la primera letra de cada palabra en una cadena.
        
        Args:
            texto (str): Cadena
            
        Returns:
            str: Cadena con la primera letra de cada palabra en mayúscula
        """
        pass

        palabras = texto.split()
        palabras_mayus = [palabra.capitalize() for palabra in palabras]
        return ' '.join(palabras_mayus)

    
    def eliminar_espacios_duplicados(self, texto):
        """
        Elimina espacios duplicados en una cadena.
        
        Args:
            texto (str): Cadena con posibles espacios duplicados
            
        Returns:
            str: Cadena sin espacios duplicados
        """
        pass

        palabras = texto.split()
        return ' '.join(palabras)
    
    
    def es_numero_entero(self, texto):
        """
        Verifica si una cadena representa un número entero sin usar isdigit().
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si la cadena representa un número entero, False en caso contrario
        """
        pass

        if texto.startswith('-'):
            texto = texto[1:]

        if not texto:
            return False

        for caracter in texto:
            if caracter < '0' or caracter > '9':
                return False
        return True

    
    def cifrar_cesar(self, texto, desplazamiento):
        """
        Aplica el cifrado César a una cadena de texto.
        
        Args:
            texto (str): Cadena a cifrar
            desplazamiento (int): Número de posiciones a desplazar cada letra
            
        Returns:
            str: Cadena cifrada
        """
        pass

        cifrado = ""
        for caracter in texto:
            if caracter.isalpha():
                base = ord('A') if caracter.isupper() else ord('a')
                cifrado += chr((ord(caracter) - base + desplazamiento) % 26 + base)
            else:
                cifrado += caracter
        return cifrado

    
    def descifrar_cesar(self, texto, desplazamiento):
        """
        Descifra una cadena cifrada con el método César.
        
        Args:
            texto (str): Cadena cifrada
            desplazamiento (int): Número de posiciones que se desplazó cada letra
            
        Returns:
            str: Cadena descifrada
        """
        pass

        descifrado = ""
        for caracter in texto:
            if caracter.isalpha():
                base = ord('A') if caracter.isupper() else ord('a')
                descifrado += chr((ord(caracter) - base - desplazamiento) % 26 + base)
            else:
                descifrado += caracter
        return descifrado

    def encontrar_subcadena(self, texto, subcadena):
        """
        Encuentra todas las posiciones de una subcadena en un texto sin usar find() o index().
        
        Args:
            texto (str): Cadena principal
            subcadena (str): Subcadena a buscar
            
        Returns:
            list: Lista con las posiciones iniciales de cada ocurrencia
        """
        pass

        posiciones = []
        for i in range(len(texto) - len(subcadena) + 1):                

            if texto[i:i + len(subcadena)] == subcadena:
                posiciones.append(i)

        return posiciones

