class MaquinaInferencia:
    def __init__(self):
        self.base_conocimientos = {
           #equipo Los Inges2
            "Pera": [("¿Es verde por fuera?", 0.5), ("¿Es blanca por dentro?", 0.5)],
            "Manzana": [("¿Es roja por fuera?", 0.33), ("¿Su forma es redonda?", 0.33), ("¿Se puede morder?", 0.34)],
            "Kiwi": [("¿Es café por fuera?", 0.33), ("¿Es verde por dentro?", 0.33), ("¿Tiene textura spera?", 0.34)],
            "Platano": [("¿Es amarillo por fuera?", 0.25), ("¿Tiene un ligero color amarillo por dentro?", 0.25), ("¿Tiene semillas pequeñas?", 0.25), ("¿Se puede pelar?", 0.25)],
            "Mandarina": [("¿Es naranja por fuera?", 0.2), ("¿Es naranja por dentro?", 0.4), ("¿Se puede pelar?", 0.2), ("¿Tiene gajos?", 0.2)],
            "Durazno": [("¿Es naranja y amarillo por fuera?", 0.2), ("¿Tiene pelitos?", 0.4), ("¿Tiene semilla en medio de la fruta?", 0.4)],
            "Uva": [("¿Tiene cascara morada o verde?", 0.5), ("¿es agridulce?", 0.5)],
            "Higo": [("¿Es morado por fuera?", 0.33), ("¿Tiene semillas en el centro?", 0.33), ("¿Es dulce por dentro?", 0.34)],
            "Toronja": [("¿Es naranja por fuera?", 0.25), ("¿Es naranja por dentro?", 0.25), ("¿es redonda?", 0.25), ("¿Es agria?", 0.25)],
            "Lima": [("¿Es amarilla por dentro y fuera?", 0.25), ("¿Es agridulce?", 0.25), ("¿Es citrica?", 0.25), ("¿Tiene forma esferica u ovalada?", 0.25)],
            #equipo DDJA
            "Pitaya": [("¿Tiene semillas comestibles?",0.33),("¿La textura de su cáscara es escamoza?",0.33),("¿Su pulpa es jugosa y de color blanco?",0.34)],
            "Fruta estrella": [("¿La fruta tiene una forma de estrella?",0.5),("¿Es de color amarillo?",0.3),("Tiene un sabor dulce",0.2)],
            "Aguacate": [("¿Tiene una semilla grande también conocida como hueso?",0.33),("¿Tiene una forma ovalada o de pera?",0.33),("¿Su pulpa es de color verde?",0.34)],
            "Tamarindo": [("¿Tiene una cáscara que al estar seca se quiebra fácilmente?",0.25),("¿Su cáscara es de color café?",0.25),("¿Tiene una pulpa de color marrón?",0.25),("¿Su sabor puede llegar a ser ligeramente picante o agridulce?",0.25)],
            "Grosella": [("¿La fruta tiene un tamaño pequeño y redondo?",0.33),("¿Es de un color rojo o negro?",0.33),("¿Tiene un ligero sabor ácido?",0.34)],
            "Chirimoya": [("¿Es blanco cremoso por dentro?",0.34),("¿Tiene semillas en el centro de color negro?",0.33),("¿Tiene un ligero aroma a cítiricos?",0.33)],
            "Guanábana": [("¿Tiene una forma ovalada con espinas en la piel?",0.),("¿Es ?",0.)],
            "Tejocote": [("¿Tiene un ligero sabor agridulce?",0.34),("¿Su tamaño es pequeño y su forma redonda?",0.33),("¿Su color es amarillo y rojo?",0.33)],
            "Níspero": [("¿La piel es de color naranja o amarillo?", 0.4),("¿La pulpa es suave y jugosa?", 0.4),("¿Tiene un sabor dulce y aromático?", 0.2)],
            # #equipo Navitas
            # "Carambola": [("¿?",0.),("¿?",0.)],
            "Granada": [("¿Tiene una cáscara dura y de color rojo o amarillo?", 0.4),("¿Las semillas están rodeadas de una pulpa jugosa?", 0.5),("¿Tiene un sabor agridulce?", 0.1)],
            "Piña": [("¿Tiene una corona en la parte superior?", 0.4),("¿La cáscara es de color amarillo y tiene espinas?", 0.4),("¿La pulpa es amarilla y jugosa?", 0.2)],
            "Rambután": [("¿Tiene una cáscara roja y peluda?", 0.5),("¿La pulpa es translúcida y jugosa?", 0.4),("¿Tiene un sabor dulce y ligeramente ácido?", 0.1)],
            "Cereza": [("¿Es una fruta pequeña y redonda?", 0.6),("¿Es de color rojo o negro?", 0.3),("¿Tiene un sabor dulce?", 0.1)],
            "Baya": [
                ("¿Es una fruta pequeña y redonda?", 0.5),
                ("¿Es de color rojo, morado o negro?", 0.4),
                ("¿Tiene un sabor dulce y ligeramente ácido?", 0.1)
            ],
            "Chabacano": [
                ("¿La cáscara es de color naranja o amarillo?", 0.4),
                ("¿La pulpa es jugosa y de color anaranjado?", 0.5),
                ("¿Tiene un sabor dulce?", 0.1)
            ],
            "Ciruela": [
                ("¿Es una fruta pequeña y redonda?", 0.5),
                ("¿Es de color morado, rojo o amarillo?", 0.4),
                ("¿Tiene un sabor dulce y ligeramente ácido?", 0.1)
            ],
            # #equipo Thanos
            "Chayote": [
                ("¿Tiene forma de pera?", 0.4),
                ("¿Es de color verde pálido?", 0.4),
                ("¿Tiene una textura firme?", 0.2)
            ],
            "Granadilla": [
                ("¿Tiene una cáscara dura y de color amarillo o naranja?", 0.4),
                ("¿Las semillas están rodeadas de una pulpa gelatinosa y transparente?", 0.5),
                ("¿Tiene un sabor dulce y aromático?", 0.1)
            ],
            "Pómelo": [
                ("¿Es una fruta grande y redonda?", 0.4),
                ("¿La cáscara es de color amarillo o rosado?", 0.4),
                ("¿La pulpa es jugosa y ligeramente amarga?", 0.2)
            ],
            "Zapote blanco": [
                ("¿Es una fruta grande y ovalada?", 0.4),
                ("¿La cáscara es de color verde o marrón?", 0.4),
                ("¿La pulpa es blanca y cremosa?", 0.2)
            ],
            "Pasa": [
                ("¿Es una fruta pequeña y arrugada?", 0.6),
                ("¿Es de color oscuro, generalmente marrón o morado?", 0.3),
                ("¿Tiene un sabor dulce?", 0.1)
            ],
            "Pepino dulce": [
                ("¿Es una fruta alargada y cilíndrica?", 0.4),
                ("¿La cáscara es de color verde claro?", 0.4),
                ("¿La pulpa es crujiente y jugosa?", 0.2)
            ],
            "Berenjena": [
                ("¿Es una fruta alargada y de forma ovalada?", 0.4),
                ("¿La piel es de color morado oscuro?", 0.4),
                ("¿La textura es firme y carnosa?", 0.2)
            ],
            "Kiwi Dorado": [
                ("¿La piel es de color marrón o dorado?", 0.4),
                ("¿La pulpa es de color verde o amarillo?", 0.4),
                ("¿Tiene un sabor dulce y ácido?", 0.2)
            ],
            "Habanero": [
                ("¿Es una fruta pequeña y de forma cónica?", 0.4),
                ("¿La piel es de color verde, naranja o rojo?", 0.4),
                ("¿Tiene un sabor muy picante?", 0.2)
            ],
            "Plátano macho": [
                ("¿Es una fruta grande y alargada?", 0.4),
                ("¿La cáscara es de color verde?", 0.4),
                ("¿La pulpa es firme y de sabor suave?", 0.2)
            ],
            "Uchuva": [
                ("¿Es una fruta pequeña y redonda, similar a una cereza?", 0.4),
                ("¿La cáscara es de color naranja o amarillo?", 0.4),
                ("¿Tiene un sabor agridulce?", 0.2)
            ],
            # #equipo Los Magaly
              "Jitomate": [
                ("¿Es una fruta roja y redonda?", 0.7),
                ("¿Es jugoso y tiene semillas en su interior?", 0.2),
                ("¿Se utiliza principalmente en ensaladas o salsas?", 0.1)
            ],
            "Mora": [
                ("¿Es una fruta pequeña y redonda?", 0.6),
                ("¿Es de color morado oscuro o negro?", 0.3),
                ("¿Tiene un sabor dulce y ligeramente ácido?", 0.1)
            ],
            "Frambuesa": [
                ("¿Es una fruta pequeña y redonda?", 0.5),
                ("¿Es de color rojo o rosa?", 0.4),
                ("¿Tiene un sabor dulce y ácido?", 0.1)
            ],
            "Naranja": [
                ("¿Es una fruta redonda y de color naranja?", 0.8),
                ("¿Tiene una piel gruesa y rugosa?", 0.1),
                ("¿Es jugosa y tiene un sabor ligeramente ácido?", 0.1)
            ],
            "Papaya": [
                ("¿Es una fruta grande y alargada?", 0.6),
                ("¿La piel es de color naranja o amarillo?", 0.3),
                ("¿La pulpa es jugosa y tiene un sabor dulce?", 0.1)
            ],
            #equipo Juanines
            "Tangelo": [("¿?",0.),("¿?",0.)],
            "Nectarina": [("¿?",0.),("¿?",0.)],
            "Mamey": [()],
            "Dátil": [()],
            "Salak": [()],
            "Lulo": [()],
            "Pitanga": [()],
            "Luruma": [()],
            "Longar": [()],
            #equipo Los Yaqui's
            "Tuna": [()],
            "Mora azul": [()],
            "Jícama": [()],
            "Lichi": [()],
            "Coco": [()],
            "Zarzamora": [()],
            #equipo Tigres Tigres
            "Arándano": [()],
            "Fresa": [()],
            "Limón": [()],
            "Melón": [()],
            "Sandía": [()],
            "Almendra": [()],
            #equipo reloj
            "Cacao": [()],
            "Ejote": [()],
            "Pepino": [()],
            "Chile serrano": [()],
            "Membrillo": [()],
            #equipo Sailor seauk
            "Mango": [()],
            "Maracuya": [()],
            #equipo Funados
            "Capulín": [()],
            "Tamarillo": [()],
            "Bergamota": [()],
            "Zapote negro": [()],
            "*Kiwano o kiwario": [()],
            "Akebia": [()],
            "Yaca": [()],
            "Nashi": [()],
            "Pineberry": [()],
            "Nuez": [()],
        }
        self.frutas = list(self.base_conocimientos.keys())

    # Método para realizar las preguntas del objeto
    def hacer_preguntas(self):
        self.fruta_encontrada = False
        for fruta in self.frutas:
            respuestas = {}
            for pregunta, probabilidad in self.base_conocimientos[fruta]:
                respuesta = input(f"{pregunta}: Sí o No? ").lower()
                # Si la respuesta es sí, guardar la probabilidad; de lo contrario, 0
                respuestas[pregunta] = probabilidad if respuesta == "sí" else 0

            # Calcular la probabilidad total
            probabilidad_total = sum(respuestas.values())

            if probabilidad_total > 0:
                self.fruta_encontrada=True
                return fruta, probabilidad_total

        return None, 0
    


if __name__ == "__main__":
    maquina = MaquinaInferencia()

    print("Por favor, responde las siguientes preguntas con Sí o No:")
    while True:
        fruta_diagnosticada, probabilidad = maquina.hacer_preguntas()
        if not fruta_diagnosticada:
            print("\nNo se pudo determinar la fruta. ¿Deseas intentar con otra?")
            respuesta = input().lower()
        else:
            print(
        f"\nBasado en tus respuestas, hay un {probabilidad * 100}% de probabilidad de tener {fruta_diagnosticada}"
      )
            break
        print("\n¡Gracias por usar el sistema experto para la identificación de frutas!")

    



      