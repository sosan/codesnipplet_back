import json

class ManagerLogica():
    def __init__(self):
        pass

    def getUUIdPage(self, url: str):
        # https://www.notion.so/cecf1c9de960437c80f4f3b9940a5a6c
        idPage: str = url.split("/")[3]
        if idPage == None:
            return None

        uuid = idPage[0:8] + "-" + idPage[8:12] + "-" + idPage[12:16] + "-" + idPage[16:20] + "-" + idPage[20:]
        return uuid

    def convertirJsonObjecto(self, datajs):
        as_str = datajs.decode("utf-8")
        if as_str == None or as_str == None:
            return None
        
        data = json.loads(as_str)
        if data == None or data == "":
            return None

        if "apiToken" in data and "idPage" in data:
            if data["apiToken"] == "" or data["apiToken"] == "":
                return None

        return data

        
