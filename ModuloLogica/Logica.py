import json

class ManagerLogica():
    def __init__(self):
        pass

    def getUUIdPage(self, url: str):
        idPage: str = url.split("/")[3]
        if idPage == None:
            return None

        direId = idPage[-32:]

        return direId

        # if (idPage.count("-") > 0):
        #     encabezado = idPage.split("-")[0] + "-"
        #     direId = idPage.split("-")[1]
        # else:
        #     direId = idPage
        
        # return direId

        # # uuid = direId[0:8] + "-" + direId[8:12] + "-" + \
        # #     direId[12:16] + "-" + direId[16:20] + "-" + direId[20:]
        # # return encabezado + uuid

    def convertirJsonObjecto(self, datajs):
        as_str = datajs.decode("utf-8")
        if as_str == None or as_str == None:
            return None
        
        data = json.loads(as_str)
        if data == None or data == "":
            return None

        if "apiToken" in data or "idPage" in data or "codigo" in data:
            if data["apiToken"] == "" or data["apiToken"] == "":
                return None

        return data

        
