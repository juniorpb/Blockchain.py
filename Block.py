import hashlib
import time


class Block:
    def __init__(self, index, previousHash, timestamp, data, hash):
        self.index = index
        self.previousHash = previousHash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

class Blockchain:
    
    # adiciona bloco á Blockchain
    def __init__(self, genesisBlock):
        self.__chain = []
        
        # adiciona primeiro block 
        self.__chain.append(genesisBlock)

    # pega ultimo block na Blockchain
    def getLatesBlock(self):
        return self.__chain(-1)

    # gera novo block
    def generateNextBlock():
        previousBlock       = getLatesBlock()
        nextIndex           = previousBlock.index + 1
        nextTimesTamp       = int(round(time.time() * 1000))
        nextPreviousHash    = previousBlock.hash
        newBlock = Block(nextIndex, nextPreviousHash, nextTimesTamp, data, calculateHash(nextIndex, nextPreviousHash, nextTimesTamp, data))

        if validatingBlock(newBlock) == True:
            self.__chain.append(newBlock)
    
    # validação do novo block
    def validatingBlock(self, newBlock):
        previousBlock = self.getLatesBlock()

        # valida index do novo bloco com o anterior
        if previousBlock.index + 1 != newBlock.index:
            return False
        
        # valida igualdade do hash anterior
        elif self.previousBlock.hash != newBlock.previousHash:
            return False

        return True

def calculateHash(index, previousHash, timestamp, data):
    return hashlib.sha256(str(index) + previousHash + str(timestamp) + data).hexdigest()


timesTampVar = int(round(time.time() * 1000))
genesisBlock = Block(0, "", timesTampVar, "Genesis Block", calculateHash(, "", timesTampVar, "Genesis Block"))
