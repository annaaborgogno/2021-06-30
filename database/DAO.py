from database.DB_connect import DBConnect
from model.edge import Edge


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getLocalizations():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """select distinct c.Localization as localization
                    from classification c"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row["localization"])
        cursor.close()
        conn.close()
        return res

    @staticmethod
    def getEdges():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """select least(c1.Localization, c2.Localization) as loc1, greatest(c1.Localization, c2.Localization) as loc2, count(distinct i.`Type`) as peso
                    from classification c1, interactions i, classification c2
                    where c1.GeneID = i.GeneID1 
                    and c2.GeneID = i.GeneID2
                    and c1.GeneID != c2.GeneID
                    and c1.Localization != c2.Localization
                    group by loc1, loc2"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Edge(**row))
        cursor.close()
        conn.close()
        return res