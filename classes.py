class savingsPlan:
    __code = 0
    __model = ""
    __version = ""
    __value = 0
    __payments = 0
    __requiredPayments = 0

    def __init__(self, code, model, version, value, pay, reqPay):
        self.__code = code
        self.__model = model
        self.__version = version
        self.__value = value
        self.__payments = pay
        self.__requiredPayments = reqPay

    # ============ Setters ============ #
    def setValue(self, v):
        self.__value = v
    def setPayRequired(self, v):
        self.__requiredPayments = v

    # ============ Getters ============ #
    def getCode(self):
        return self.__code
    def getModel(self):
        return self.__model
    def getVersion(self):
        return self.__version
    def getValue(self):
        return self.__value
    def getPayment(self):
        return self.__payments
    def getPayRequired(self):
        return self.__requiredPayments

    # ============ Methods ============ #
    def getPayValue(self):
        return (self.__value / self.__payments) + self.__value * 0.1