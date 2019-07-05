class Bridge:
    def __init__(self, id, status, next_arrival):
        self.id = id
        self.status = status
        self.next_arrival = next_arrival

    def toJsonString(self):
        return '{ "id" : "' + self.id + '", "status" : "' + self.status+'" , "next_arrival": "'+self.next_arrival + '" }'
