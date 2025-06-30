# Ruby Code Analyzer

## **Descripción**
Este proyecto implementa un analizador léxico, sintáctico y semántico para el lenguaje de programación Ruby, utilizando la librería PLY (Python Lex-Yacc).
El sistema reconoce los componentes básicos del código Ruby, valida la estructura gramatical y verifica errores lógicos como incompatibilidades de tipo o uso incorrecto de las estructuras del lenguaje.

## **Características**
- **Analizador Léxico:** Convierte el código Ruby en tokens, identificando variables, operadores, palabras reservadas, delimitadores, comentarios y literales.

- **Analizador Sintáctico:** Valida que la secuencia de tokens forme una estructura válida del lenguaje Ruby (asignaciones, estructuras de control, funciones, clases, arrays, hashes, etc.).

- **Analizador Semántico:** Detecta errores de lógica y tipos, como uso de variables no definidas, asignaciones incompatibles, uso incorrecto de break, conversiones de tipo inválidas, y condiciones no booleanas.

- **Generación de Logs:** Los tokens, errores sintácticos y errores semánticos se almacenan en archivos de log para facilitar la depuración y evaluación.
