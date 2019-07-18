import hashlib
import time
import binascii


class Block:
    def __init__(self, index, previousHash, timestamp, data, hash, difficulty, nonce):
        self.index = index
        self.previousHash = previousHash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash
        self.difficulty = difficulty
        self.nonce = nonce

class Blockchain:
    
    # add block in Blockchain
    def __init__(self, genesisBlock):
        self.__chain = []
        
        # add first block 
        self.__chain.append(genesisBlock)

    # get last block in Blockchain
    def getLatesBlock(self):
        return self.__chain[-1] # -1 return last element of list

    # generetes new block
    def generateNextBlock(self, data):
        previousBlock       = self.getLatesBlock()
        nextIndex           = previousBlock.index + 1
        nextTimesTamp       = int(round(time.time() * 1000))
        nextPreviousHash    = previousBlock.hash
        newBlock = Block(nextIndex, nextPreviousHash, nextTimesTamp, data, calculateHash(nextIndex, nextPreviousHash, nextTimesTamp, data))

        if self.validatingBlock(newBlock) == True:
            self.__chain.append(newBlock)
    
    # validation new block
    def validatingBlock(self, newBlock):
        previousBlock = self.getLatesBlock()

        # validation the index of new block with previous 
        if previousBlock.index + 1 != newBlock.index:
            return False
        
        # equality validation of previous hash
        elif previousBlock.hash != newBlock.previousHash:
            return False

        return True

    # the difficulty level is based on the quantity 
    # of digits 0 (zeros) at the start of the hash on binary basis.
    def hashMatchesDefficulty(self, hash, difficulty):

        # translate hash of binary
        hashBinary = binascii.unhexlify(hash)

        # create level of difficulty
        requiredPrefix = '0' * int(difficulty)

        return hashBinary.startswith(requiredPrefix)

    def findBlock(self, index, previousHash, timestamp, data, difficulty):
        nonce = 0
        while True:
            hash = self.calculateHash(index, previousHash, timestamp, data, difficulty, nonce)
            if self.hashMatchesDefficulty(hash, difficulty):
                block = Block(index, previousHash, timestamp, data, difficulty, nonce)
                return block
            
            nonce += 1
         

def calculateHash(index, previousHash, timestamp, data, difficulty, nonce):
    return hashlib.sha256((str(index) + previousHash + str(timestamp) + data + str(difficulty) + str(nonce)).encode('utf-8')).hexdigest()


timesTampVar = int(round(time.time() * 1000))
genesisBlock = Block(0, "", timesTampVar, "Genesis Block", calculateHash(0, "", timesTampVar, "Genesis Block"))
