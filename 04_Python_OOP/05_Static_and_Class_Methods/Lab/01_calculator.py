class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def subtract(*args):
        result = args[0]
        for number in args[1:]:
            result = result - number
        return result

    @staticmethod
    def multiply(*args):
        result = args[0]
        for number in args[1:]:
            result = result * number
        return result

    @staticmethod
    def divide(*args):
        result = args[0]
        for number in args[1:]:
            result = result / number
        return result