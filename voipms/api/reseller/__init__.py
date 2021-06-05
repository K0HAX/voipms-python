from voipms.api.reseller.balance import Balance
from voipms.api.reseller.balance_management import BalanceManagement
from voipms.api.reseller.clients import Clients
from voipms.api.reseller.client import Client
from voipms.api.reseller.records import Records

class Reseller():
    def __init__(self, base):
        self.base = base
        self._balance = None
        self._balance_management = None
        self._charges = None
        self._client_packages = None
        self._clients = None
        self._client = None
        self._records = None
        self.client_id = None

    @property
    def balance(self):
        if self._balance is None:
            self._balance = Balance(self.base)
        return self._balance

    @property
    def balance_management(self):
        if self._balance_management is None:
            self._balance_management = BalanceManagement(self.base)
        return self._balance_management

    @property
    def charges(self):
        if self._charges is None:
            self._charges = Charges(self.base)
        return self._charges

    @property
    def client_packages(self):
        if self._client_packages is None:
            self._client_packages = ClientPackages(self.base)
        return self._client_packages

    @property
    def clients(self):
        if self._clients is None:
            self._clients = Clients(self.base)
        return self._clients

    @property
    def client(self):
        if self.client_id is None:
            raise Exception("client_id cannot be None")
        _client = Client(self.base, self.client_id)
        return _client

    @property
    def records(self):
        if self._records is None:
            self._records = Records(self.base)
        return self._records

