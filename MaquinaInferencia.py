#EQUIPO "LOS INGES 2" 
#INTEGRANTES: Rodríguez Tiscareño,González Escobedo, Flores Ojeda, Ortega Villalobos
class MaquinaInferencia:
    def __init__(self):
        self.base_conocimientos = {
           #equipo Los Inges2
            "Pera": [("¿Es verde por fuera?", 0.5), ("¿Es blanca por dentro?", 0.5)],
            "Manzana": [("¿Es roja por fuera?", 0.33), ("¿Su forma es redonda?", 0.33), ("¿Se puede morder?", 0.34)],
            "Kiwi": [("¿Es café por fuera?", 0.33), ("¿Es verde por dentro?", 0.33), ("¿Tiene textura áspera?", 0.34)],
            "Platano": [("¿Es amarillo por fuera?", 0.25), ("¿Tiene un ligero color amarillo por dentro?", 0.25), ("¿Tiene semillas pequeñas?", 0.25), ("¿Se puede pelar?", 0.25)],
            "Mandarina": [("¿Es naranja por fuera?", 0.2), ("¿Es naranja por dentro?", 0.3), ("¿Su textura por fuera tiene poros?", 0.3), ("¿Tiene gajos?", 0.2)],
            "Durazno": [("¿Por fuera su color es una combinación de tonos amarillo y rojo?", 0.2), ("¿Su piel es aterciopelada?", 0.4), ("¿Tiene semilla en medio de la fruta?", 0.4)],
            "Uva": [("¿Su pulpa es transparente?", 0.4), ("¿Es agridulce?", 0.2),("¿Tiene una capa cerosa?",0.4)],
            "Higo": [("¿Es morado por fuera?", 0.33), ("¿Tiene semillas en el centro?", 0.33), ("¿Es dulce por dentro?", 0.34)],
            "Toronja": [("¿Es naranja por fuera?", 0.25), ("¿Es naranja por dentro?", 0.25), ("¿Es redonda?", 0.25), ("¿Es agria?", 0.25)],
            "Lima": [("¿Es amarillo verdoso por fuera?", 0.25), ("¿Es agridulce?", 0.25), ("¿Es cítrica?", 0.25), ("¿Tiene forma esferica u ovalada?", 0.25)],
            #equipo DDJA
            "Pitaya": [("¿Tiene semillas comestibles?",0.33),("¿La textura de su cáscara es escamoza?",0.33),("¿Su pulpa es jugosa y de color blanco?",0.34)],
            "Fruta estrella": [("¿La fruta tiene una forma de estrella?",0.5),("¿Sus semillas se ubican en el centro de los gajos?",0.3),("Tiene un sabor dulce",0.2)],
            "Aguacate": [("¿Tiene una semilla grande también conocida como hueso?",0.33),("¿Tiene una forma ovalada o de pera?",0.33),("¿Su pulpa es de color verde?",0.34)],
            "Tamarindo": [("¿Tiene una cáscara que al estar seca se quiebra fácilmente?",0.25),("¿Su cáscara es de color café?",0.25),("¿Tiene una pulpa de color marrón?",0.25),("¿Su sabor puede llegar a ser ligeramente picante o agridulce?",0.25)],
            "Grosella": [("¿La fruta tiene un tamaño pequeño y redondo?",0.33),("¿Su pulpa es carnosa?",0.33),("¿Tiene un ligero sabor ácido?",0.34)],
            "Chirimoya": [("¿Es blanco cremoso por dentro?",0.34),("¿Tiene semillas en el centro de color negro?",0.33),("¿Tiene un ligero aroma a cítiricos?",0.33)],
            "Guanábana": [("¿Tiene una forma ovalada con espinas en la piel?",0.),("¿Es ?",0.)],
            "Tejocote": [("¿Tiene un ligero sabor agridulce?",0.34),("¿Su tamaño es pequeño y su forma redonda?",0.33),("¿Su color es amarillo y rojo?",0.33)],
            "Níspero": [("¿La piel es de color amarillo anaranjado?", 0.4),("¿La pulpa es suave y jugosa?", 0.4),("¿Tiene un sabor dulce y aromático?", 0.2)],
            # #equipo Navitas
            # "Carambola": [("¿?",0.),("¿?",0.)],
            "Granada": [("¿Tiene una cáscara dura con apariencia leñosa?", 0.4),("¿Las semillas están rodeadas de una pulpa jugosa?", 0.5),("¿Tiene un sabor agridulce?", 0.1)],
            "Piña": [("¿Tiene una corona en la parte superior?", 0.4),("¿La cáscara tiene escamas?", 0.4),("¿La pulpa es fibrosa?", 0.2)],
            "Rambután": [("¿Tiene una cáscara peluda?", 0.5),("¿La pulpa es translúcida y jugosa?", 0.4),("¿Tiene un sabor dulce y ligeramente ácido?", 0.1)],
            "Cereza": [("¿Es una fruta pequeña y redonda?", 0.6),("¿Su textura es jugosa y carnosa?", 0.3),("¿Tiene un sabor dulce?", 0.1)],
            "Baya": [("¿Es una fruta pequeña?", 0.5),("¿Tiene una apariencia lustrosa?", 0.4),("¿Tiene un sabor dulce y ligeramente ácido?", 0.1)
            ],
            "Chabacano": [("¿Tiene una textura fibrosa cerca del hueso?", 0.5),("¿La pulpa es jugosa y de color anaranjado?", 0.4),("¿Tiene un sabor dulce?", 0.1)
            ],
            "Ciruela": [("¿Es una fruta pequeña y redonda?", 0.5),("¿Es de color rojo intenso?", 0.4),("¿Tiene un sabor dulce y ligeramente ácido?", 0.1)
            ],
            # #equipo Thanos
            "Chayote": [("¿Tiene forma de bombilla?", 0.4),("¿Es de color verde pálido?", 0.4),("¿Tiene una textura firme?", 0.2)],
            "Granadilla": [("¿Tiene una cáscara dura y naranja intenso?", 0.4),("¿Las semillas están rodeadas de una pulpa gelatinosa y transparente?", 0.5),("¿Tiene un sabor dulce y aromático?", 0.1)],
            "Pómelo": [("¿Es una fruta grande y redonda?", 0.4),("¿La cáscara es de color rosado?", 0.4),("¿La pulpa es jugosa y ligeramente amarga?", 0.2)],
            "Zapote blanco": [("¿Es una fruta grande y ovalada?", 0.4),("¿La cáscara es suave y un poco rugosa?", 0.4),("¿La pulpa es blanca y cremosa?", 0.2)],
            "Pasa": [("¿Es una fruta pequeña y arrugada?", 0.6), ("¿Es de color oscuro, generalmente marrón o morado?", 0.3),("¿Tiene un sabor dulce?", 0.1)],
            "Pepino dulce": [("¿Es una fruta alargada y cilíndrica?", 0.4),("¿La cáscara es de color verde claro?", 0.4),("¿La pulpa es crujiente y jugosa?", 0.2)],
            "Berenjena": [("¿Es una fruta alargada y de forma ovalada?", 0.4),("¿La piel es de color morado oscuro?", 0.4),("¿La textura es firme y carnosa?", 0.2)],
            "Kiwi Dorado": [("¿La piel es de color amarillo dorado?", 0.4),("¿La pulpa es de color verde amarillento?", 0.4),("¿Tiene un sabor dulce y ácido?", 0.2)],
            "Habanero": [("¿Es una fruta pequeña y de forma cónica?", 0.4),("¿La piel es de color naranja intenso?", 0.4),("¿Tiene un sabor muy picante?", 0.2)],
            "Plátano macho": [("¿Es una fruta grande y alargada?", 0.4),("¿La cáscara es de color verde?", 0.4),("¿La pulpa es firme y de sabor suave?", 0.2)],
            "Uchuva": [("¿Es una fruta pequeña y redonda, similar a una cereza?", 0.2),("¿La cáscara es de color naranja amarillento?", 0.4),("¿Tiene un sabor agridulce?", 0.2),("¿Viene cubierta en una bolsita similar al tomate verde ?",0.2)],
            # #equipo Los Magaly
            "Jitomate": [("¿Es una fruta roja y redonda?", 0.5),("¿Es jugoso y tiene semillas en su interior?", 0.2),("¿Se utiliza principalmente en ensaladas o salsas?", 0.3)],
            "Mora": [("¿Es una fruta pequeña y redonda?", 0.2),("¿Es de color púrpura profundo?", 0.3),("¿Tiene un sabor dulce y ligeramente ácido?", 0.1),("¿Al comerlas pueden manchar fácilmente?",0.4)],
            "Frambuesa": [("¿Su piel es delgada y tierna?", 0.3),("¿Es de color rojo brillante?", 0.2),("¿Es pequeña y redondeada con una forma cónica que se estrecha hacia la punta?", 0.4)],
            "Naranja": [("¿Es una fruta redonda y de color naranja?", 0.4),("¿Tiene una piel gruesa y rugosa?", 0.2),("¿Es jugosa y tiene un sabor ligeramente ácido?", 0.2)],
            "Papaya": [("¿Es una fruta grande y alargada?", 0.4),("¿El centro donde se encuentran las semillas es amarillo pálido?", 0.3),
            ("¿La pulpa es jugosa y tiene un sabor dulce?", 0.1,("¿Sus semillas son redondasy negras?",0.2))],
            #equipo Juanines
            "Tangelo": [("¿Tiene un sabor ácido refrescante?",0.3),("¿Es fácil de pelar?",0.2),("¿Es una fruta híbrida entre una mandarina y un pómelo?",0.2),("¿Es de color naranja brillante?",0.3)],
            "Nectarina": [("¿Su piel es lisa y brillante?",0.2),("¿Tienen un hueso central grande?",0.5),("¿La pulpa es jugosa y tiene un sabor dulce?", 0.1),("¿La piel es suave y de color amarillo, naranja o rojo?", 0.2)],
            "Mamey": [("¿Tiene una cáscara áspera y rugosa?",0.3),("¿En su interior tiene un color naranja?",0.1),("¿Su pulpa es suave, dulce y cremosa?",0.3),("¿Su forma es ovalada?",0.3)],
            "Dátil": [("¿Es una fruta pequeña y alargada?", 0.7),("¿La piel es de color marrón y arrugada?", 0.2),("¿La pulpa es dulce y pegajosa?", 0.1)],
            "Salak": [  ("¿Es una fruta pequeña y ovalada?", 0.6),("¿La piel es de color marrón y tiene escamas?", 0.3),("¿La pulpa es jugosa y tiene un sabor dulce y ácido?", 0.1)],
            "Lulo": [("¿Es una fruta tropical?",0.3),("¿Es una mezcla de limón y kiwi?",0.1),("¿Su pulpa es jugosa y gelatinosa?",0.3),("¿Tiene pequeñas semillas blancas?",0.3)],
            "Pitanga": [("¿Por fuera es color rojo?",0.25),("¿Por dentro su pulpa es color amarillo?",0.25),("¿Es jugosa y a la vez suave?",0.25),("¿Tiene una forma ovalada y una corona en la parte superior donde se encuentra el tallo?",0.25)],
            "Luruma": [("¿Tiene una cáscara rugos?",0.3),("¿Tiene la apariencia de una calabaza?",0.3),("Su sabor es dulce como un caramelo",0.4)],
            "Longan": [("¿Tiene una cáscara delgada y de color marrón?",0.4),("¿Es translúcido y tiene un color blanco opaco?",0.4,("¿Su sabor tiene un toque floral?",0.2))],
            #equipo Los Yaqui's
            "Tuna": [("¿Es una fruta grande y ovalada?", 0.5),("¿La piel es de color verde o amarillo y tiene espinas?", 0.4),("¿La pulpa es jugosa y tiene un sabor dulce y ligeramente ácido?", 0.1)],
            "Mora azul": [("¿Es una fruta pequeña y redonda?", 0.6),
                ("¿Es de color azul o morado?", 0.3),
                ("¿Tiene un sabor dulce y ligeramente ácido?", 0.1)],
            "Jícama": [ ("¿Es una raíz comestible?", 0.4),
                ("¿La piel es de color marrón claro y tiene textura rugosa?", 0.3),
                ("¿La pulpa es crujiente y tiene un sabor suave y ligeramente dulce?", 0.1)],
            "Lichi": [ ("¿Es una fruta pequeña y redonda?", 0.5),
                ("¿La piel es roja y tiene una textura rugosa?", 0.4),
                ("¿La pulpa es jugosa y tiene un sabor dulce y floral?", 0.1)],
            "Coco": [("¿Es de tamaño grande y redondo?",0.3),("¿Tiene una capa dura de color café?",0.4),("¿Por dentro tiene una capa gruesa color blanco?",0.3)],
            "Zarzamora": [("¿Es una fruta pequeña y redonda?", 0.5),("¿Es de color negro y tiene un brillo característico?", 0.4),("¿Tiene un sabor dulce y ligeramente ácido?", 0.1)],
            #equipo Tigres Tigres
            "Arándano": [("¿Es una fruta pequeña y redonda?", 0.5),("¿Es de color azul oscuro o morado?", 0.4),("¿Tiene un sabor dulce y ácido?", 0.1)],
            "Fresa": [  ("¿Es una fruta pequeña y con forma de corazón?", 0.6),("¿Es de color rojo brillante?", 0.3),("¿Tiene un sabor dulce y ligeramente ácido?", 0.1)],
            "Limón": [("¿Es una fruta pequeña y ovalada?", 0.5),("¿La cáscara es de color verde y tiene una textura rugosa?", 0.4),("¿Tiene un sabor ácido?", 0.1)],
            "Melón": [ ("¿Es una fruta grande y redonda?", 0.25),("¿La textura tiene relieve o surcos?",0.5),("¿Su pulpa es jugosa, dulce y de un ligero color naranja?",0.25)],
            "Sandía": [ ("¿Es una fruta grande y ovalada?", 0.4),("¿La cáscara es de color verde con rayas verdes oscuras?", 0.5),("¿La pulpa es jugosa y tiene un sabor dulce?", 0.1)],
            "Almendra": [ ("¿Es una semilla comestible?", 0.6),("¿La cáscara es dura y tiene una forma ovalada?", 0.3),("¿El interior es suave y tiene un sabor dulce y almendrado?", 0.1)],
            #equipo reloj
             "Cacao": [("¿Es una semilla que se utiliza para hacer chocolate?", 0.8),("¿La semilla es de color marrón oscuro?", 0.1),("¿Tiene un sabor amargo?", 0.1)
            ],
            "Ejote": [("¿Es una verdura larga y verde?", 0.7),("¿Es comúnmente conocida como judía verde o habichuela?", 0.2),("¿Se come principalmente cocida o cruda?", 0.1)
            ],
            "Pepino": [("¿Es una hortaliza larga y de forma cilíndrica?", 0.6),("¿La piel es verde y tiene una textura rugosa?", 0.3),("¿La pulpa es jugosa y tiene un sabor suave y refrescante?", 0.1)
            ],
            "Chile serrano": [("¿Es un tipo de chile pequeño y picante?", 0.7),("¿Es de color verde cuando está fresco?", 0.2),("¿Se utiliza comúnmente en la cocina mexicana?", 0.1)],
            "Membrillo": [("¿Es una fruta parecida a una manzana?", 0.6),("¿La piel es amarilla y tiene una textura cerosa?", 0.3),("¿Su pulpa tiene una textura granulosa?", 0.1)],
            #equipo Sailor seauk
              "Mango": [("¿Es una fruta grande y ovalada con una piel de color naranja o amarillo?", 0.2),("¿La pulpa es jugosa y tiene un sabor dulce y afrutado?", 0.2),("¿Es común encontrarlo en climas tropicales?", 0.1),
            ("¿Tiene un hueso grande que es cubierto por la pulpa de la fruta?",0.5)],
            "Maracuya": [("¿Es una fruta redonda con una cáscara dura y arrugada?", 0.6),("¿La pulpa es jugosa y tiene un sabor agridulce intenso?", 0.3),("¿Es comúnmente utilizada para hacer jugos y postres?", 0.1)
            ],
            #equipo Funados
            "Capulín": [("¿Es una pequeña fruta roja o morada similar a la cereza?", 0.7),("¿La pulpa es jugosa y tiene un sabor dulce y ligeramente ácido?", 0.2),("¿Es comúnmente utilizada para hacer mermeladas y licores?", 0.1)],
            "Tamarillo": [("¿Es una fruta ovalada con una piel de color rojo, naranja o amarillo?", 0.6),("¿La pulpa es jugosa y tiene un sabor dulce y ligeramente ácido?", 0.3),("¿Es comúnmente conocida como tomate de árbol?", 0.1)],
            "Bergamota": [("¿Es una fruta pequeña y redonda con una piel de color amarillo o naranja?", 0.6),("¿La pulpa es jugosa y tiene un sabor cítrico y ligeramente amargo?", 0.3),("¿Es comúnmente utilizada para hacer aceite esencial?", 0.1) ],
            "Zapote negro": [("¿Es una fruta grande y redonda con una piel de color negro?", 0.7),("¿La pulpa es suave y de color naranja oscuro?", 0.2),("¿Tiene un sabor dulce y terroso?", 0.1)],
            "Kiwano o kiwario": [("¿Es una fruta ovalada con una piel espinosa de color amarillo o naranja?", 0.6),("¿La pulpa es gelatinosa y tiene un sabor ligeramente ácido y refrescante?", 0.3),("¿Es comúnmente conocida como melón africano?", 0.1)],
            "Akebia": [("¿Es una fruta alargada con una piel de color púrpura o marrón?", 0.6),("¿La pulpa es jugosa y tiene un sabor dulce y floral?", 0.3),("¿Es comúnmente conocida como chocolate de los pobres?", 0.1)],
            "Yaca": [("¿Es una fruta grande y ovalada con una piel de color verde o marrón?", 0.7),("¿La pulpa es fibrosa y tiene un sabor dulce y aromático?", 0.2),("¿Es comúnmente utilizada en la cocina asiática?", 0.1)],
            "Nashi": [("¿Es una fruta redonda con una piel de color amarillo o marrón claro?", 0.6),("¿La pulpa es jugosa y tiene un sabor dulce y crujiente?", 0.3),("¿Es comúnmente conocida como pera asiática?", 0.1)],
            "Pineberry": [("¿Es una pequeña fruta redonda con una piel blanca y semillas rojas?", 0.6),("¿La pulpa es jugosa y tiene un sabor dulce y ligeramente ácido?", 0.3),("¿Es una variedad de fresa con sabor a piña?", 0.1)],
            "Nuez": [("¿Es una semilla grande y ovalada con una cáscara dura?", 0.7),("¿La semilla es comestible y tiene un sabor rico y aceitoso?", 0.2),("¿Es comúnmente utilizada en la repostería y como snack?", 0.1)],
     
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

    



      