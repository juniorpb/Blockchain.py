import hashlib
import binascii

class Transaction:
    def __init__(self):
        self.id = None
        self.inputs = None
        self.outputs = None

class Output:
    def __init__(self, address, amount):
        self.address = address
        self.amount = amount

class Input:
    def __init__(self):
        self.outputId = None
        self.outputIndex = None
        self.signature = None

class UnspentOutput:
    def __init__(self, outputId, outputIndex, address, amount):
        self.outputId = outputId
        self.outputIndex = outputIndex
        self.address = address
        self.amount = amount

class UnspentOutputs:
    def __init__(self):
        self.__listUtxo = []

    def updateListUtxo(self, lista):
        self.__listUtxo = lista

    def newUnspentOutputs(self, transactions):
        lista = []
        for transaction in transactions:
            for inpt in transaction.input:
                utxo = UnspentOutput(transaction.id, inpt.outputId, inpt.outputIndex, inpt.address, inpt.amount)
                lista.append(utxo)

        self.updateListUtxo(lista)                

def findUnspentOutput(outputId, outputIndex, listUnspentOutputs):
    for utxo in listUnspentOutputs:
        if utxo.outputId == outputId and utxo.outputIndex == outputIndex:
            return True
        
        return False

def idTransaction(transaction):
    inputContents = ""
    outputContents = ""

    for inpt for transaction.inputs:
        inputContents += (inpt.outputId + inpt.outputIndex)

    for output for transaction.outputs:
        outputContents += (output.address + output.amount)
    
    return hashlib.sha256((str(inputContents) + str(outputContents)).encode('utf-8')).hexdigest()
