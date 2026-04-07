class Card():
    def __init__(self, suite, rank):
        acceptedRanks=["A","K","Q","J","10","9","8","7","6","5","4","3","2"]
        acceptedSuits=["HEART","DIAMOND","SPADE","CLUBS"]


        if not isinstance(suite,str):
            raise TypeError(f"Suite expected to be a string got {type(suite).__name__}")

        if not isinstance(rank,str):
            raise TypeError(f"Suite expected to be a string got {type(rank).__name__}")


        suiteUpper=suite.upper()
        rankUpper=rank.upper()
        if rankUpper in acceptedRanks:
            pass
        else:
            raise TypeError(f"Added rank not in suite list {acceptedRanks}")

        if suiteUpper in acceptedSuits:
            pass
        else:
            raise TypeError(f"Added rank not in suite list {acceptedSuite}")


        self.rank=rankUpper
        self.suite=suiteUpper

    def printCard(self):
        print("Rank", self.rank)
        print("Suite", self.suite)


if __name__=="__main__":
        card1=Card(suite="Heart",rank="A")
        card1.printCard()

        card2=Card(suite="Clubs",rank="5")
        card2.printCard()



        
        
