class MaquinaInferencia:
    def _init_(self):
        self.base_conocimientos = {
            "Pera": [("¿Es verde por fuera?", 0.5), ("¿Es blanca por dentro?", 0.5)],
            "Manzana": [("¿Es roja por fuera?", 0.33), ("¿Es blanca por dentro?", 0.33), ("¿Se puede morder?", 0.34)],
            "Kiwi": [("¿Es cafe por fuera?", 0.33), ("¿Es verde por dentro?", 0.33), ("¿Tiene textura aspera?", 0.34)],
            "Platano": [("¿Es amarillo por fuera?", 0.25), ("¿blanco por dentro?", 0.25), ("¿Tiene semillas pequeñas?", 0.25), ("¿Se puede pelar?", 0.25)],
            "Mandarina": [("¿Es naranja por fuera?", 0.2), ("¿Es naranja por dentro?", 0.4), ("¿Se puede pelar?", 0.2), ("¿Tiene gajos?", 0.2)],
            "Durazno": [("¿Es naranja y amarillo por fuera?", 0.2), ("¿Tiene pelitos?", 0.4), ("¿Tiene semilla en medio de la fruta?", 0.4)],
            "Uva": [("¿Tiene cascara morada o verde?", 0.5), ("¿es agridulce?", 0.5)],
            "higo": [("¿Es morado por fuera?", 0.33), ("¿Tiene semillas en el centro?", 0.33), ("¿Es dulce por dentro?", 0.34)],
            "Toronja": [("¿Es naranja por fuera?", 0.25), ("¿Es naranja por dentro?", 0.25), ("¿es redonda?", 0.25), ("¿Es agria?", 0.25)],
            "lima": [("¿Es amarilla por dentro y fuera?", 0.25), ("¿Es agridulce?", 0.25), ("¿Es citrica?", 0.25), ("¿Tiene forma esferica u ovalada?", 0.25)],
        }
        self.frutas = list(self.base_conocimientos.keys())

    # Método para realizar las preguntas del objeto
    def hacer_preguntas(self):
        for fruta in self.frutas:
            respuestas = {}
            for pregunta, probabilidad in self.base_conocimientos[fruta]:
                respuesta = input(f"{pregunta}: Sí o No? ").lower()
                # Si la respuesta es sí, guardar la probabilidad; de lo contrario, 0
                respuestas[pregunta] = probabilidad if respuesta == "sí" else 0

            # Calcular la probabilidad total
            probabilidad_total = sum(respuestas.values())

            if probabilidad_total > 0:
                return fruta, probabilidad_total

        return None, 0

if _name_ == "_main_":
    maquina = MaquinaInferencia()

    print("Por favor, responde las siguientes preguntas con Sí o No:")

    fruta_diagnosticada, probabilidad = maquina.hacer_preguntas()

    if fruta_diagnosticada:
        print(
            f"\nBasado en tus respuestas, hay un {probabilidad * 100}% de probabilidad de tener {fruta_diagnosticada}"
        )
    else:
        print(
            "\nNo se pudo determinar la fruta. Consulta a un profesional de la salud para un diagnóstico preciso."
        )