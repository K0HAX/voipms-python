class Client():
    def __init__(self, base, client_id):
        self.method = "getClients"
        if client_id != None:
            self.client_id = client_id
        else:
            raise ValueError("client_id cannot be {}".format(type(client_id)))
        self.base = base

    def fetch(self, params={}):
        if params:
            params['client'] = self.client_id
        else:
            params = {'client': self.client_id}
        return self.base.request(self.method, params=params)

    def CDRs(self, params={}):
        if not params:
            raise Exception("params are required")
        keys = params.keys()
        if 'date_from' not in keys or 'date_to' not in keys or 'timezone' not in keys:
            raise KeyError("params date_from, date_to, and timezone are required")
        params['client'] = self.client_id
        return self.base.request("getResellerCDR", params=params)

    def charges(self, params={}):
        if params:
            params['client'] = self.client_id
        else:
            params = {'client': self.client_id}
        return self.base.request("getCharges", params=params)

    def deposits(self, params={}):
        if params:
            params['client'] = self.client_id
        else:
            params = {'client': self.client_id}
        return self.base.request("getDeposits", params=params)

    def packages(self, params={}):
        if params:
            params['client'] = self.client_id
        else:
            params = {'client': self.client_id}
        return self.base.request("getClientPackages", params=params)

    def reseller_balance(self, params={}):
        if params:
            params['client'] = self.client_id
        else:
            params = {'client': self.client_id}
        return self.base.request("getResellerBalance", params=params)

    def threshold(self, params={}):
        if params:
            params['client'] = self.client_id
        else:
            params = {'client': self.client_id}
        return self.base.request("getClientThreshold", params=params)

