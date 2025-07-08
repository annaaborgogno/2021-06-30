import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_creaGrafo(self, e):
        self._model.buildGraph()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Grafo correttamente creato", color="green"))
        nNodes, nEdges = self._model.getGraphDetails()
        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi: {nNodes}, numero di archi {nEdges}"))
        self._view.update_page()

    def handle_statistiche(self, e):
        loc = self._view._ddLocalization.value
        if loc is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(f"Selezionare una localizzazione", color="red"))
            self._view.update_page()
            return
        neigh = self._model.getNeighbors(loc)
        risultato = {}

        for v in neigh:
            if self._model._graph.has_edge(loc, v):
                # per ogni vicino recupero il peso dell'arco e lo aggiungo al dizionario che poi stampo
                pesoArco = self._model._graph[loc][v]["weight"]
                risultato[v] = pesoArco

        res_ordinato = dict(sorted(risultato.items(), key=lambda x: x[0]))
        self._view.txt_result.controls.append(ft.Text(f"Le componenti adiacenti a {loc} sono:"))
        for n, p in res_ordinato.items():
                self._view.txt_result.controls.append(ft.Text(f"{n} -- {p}"))
        self._view.update_page()

    def fillDDLoc(self):
        nodes = self._model.getNodes()
        for n in nodes:
            self._view._ddLocalization.options.append(ft.dropdown.Option(n))
        self._view.update_page()

    def handle_ricorsione(self, e):
        loc = self._view._ddLocalization.value
        if loc is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(f"Selezionare una localizzazione", color="red"))
            self._view.update_page()
            return
        bestPath, bestWeight = self._model.getBestPath(loc)
        self._view.txt_result.controls.append(
            ft.Text(f"Il cammino migliore a partire da {loc} è stato trovato, con peso {bestWeight}", color="green"))
        self._view.txt_result.controls.append(ft.Text(f"I nodi che lo compongono sono:"))
        for n in bestPath:
            self._view.txt_result.controls.append(ft.Text(n))
        self._view.update_page()
