class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if self.__instance != None:
            raise "The class is a singleton class pattern.\n"
        else:
            Singleton.__instance = self

def main():
    print("From the main function..\n")
    SingletonInstance = Singleton()
    print(SingletonInstance)

if __name__ == "__main__":
    main()