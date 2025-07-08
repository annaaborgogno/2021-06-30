import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._nodes = []
        self._edges = []
        self._graph = nx.Graph()
        self._bestPath = []
        self._bestWeight = 0

    def getBestPath(self, source):
        self._bestPath = []
        self._bestWeight = 0
        parziale = [source]
        self._ricorsione(parziale)
        return self._bestPath, self._bestWeight

    def _ricorsione(self, parziale):
        if self._calcolaPeso(parziale) > self._bestWeight:
            self._bestPath = copy.deepcopy(parziale)
            self._bestWeight = self._calcolaPeso(parziale)

        for n in self._graph.neighbors(parziale[-1]):
            if n not in parziale:
                parziale.append(n)
                self._ricorsione(parziale)
                parziale.pop()

    def _calcolaPeso(self, listOfNodes):
        pesoTot = 0
        for i in range(1, len(listOfNodes)):
            u = listOfNodes[i - 1]
            v = listOfNodes[i]
            pesoTot += self._graph[u][v]["weight"]
        return pesoTot

    def buildGraph(self):
        self._graph.clear()
        self._nodes = []
        self._edges = []
        self._idMap = {}
        self.getNodes()
        self._graph.add_nodes_from(self._nodes)
        self.addAllEdges()
        return self._graph

    def getNodes(self):
        self._nodes = DAO.getLocalizations()
        return self._nodes

    def getGraphDetails(self):
        nNodes = self._graph.number_of_nodes()
        nEdges = self._graph.number_of_edges()
        return nNodes, nEdges

    def addAllEdges(self):
        self._edges = DAO.getEdges()
        for e in self._edges:
            u = e.loc1
            v = e.loc2
            self._graph.add_edge(v, u, weight=e.peso)

    def getNeighbors(self, loc):
        neigh = nx.neighbors(self._graph, loc)
        return list(neigh)