class Clients():
    def __init__(self, base):
        self.method = "getClients"
        self.base = base

    def fetch(self, params={}):
        return self.base.request(self.method, params=params)

    def client_threshold(self, params={}):
        return self.base.request("getClientThreshold", params=params)

    def get_client(self, client_id):
        from voipms.api.reseller import Client
        return Client(self.base, client_id)

    def get_all_clients(self):
        from voipms.api.reseller import Client
        clients = {}
        for client in self.fetch()['clients']:
            clients[client['client']] = Client(self.base, client['client'])
        return clients

