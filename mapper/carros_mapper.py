
class CarroMapper:

    def mapper(self, carros):
        carros_map = []
        if not carros:
            return carros_map

        for tp in carros:
            carros_map.add({
                "marca": tp.get("marca", False),
                "nome": tp.get("nome"),
                "ano": tp.get("ano"),
                "cor": tp.get("cor"),
                "tipo": tp.get("tipo")
            })

        return carros_map
g