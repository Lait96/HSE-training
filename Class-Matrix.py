from sys import stdin


class MatrixError(BaseException):
    def __init__(self, other1, other2):
        self.matrix1 = other1
        self.matrix2 = other2


class Matrix:
    def __init__(self, params):
        self.content = []
        for i in range(len(params)):
            self.content.append(params[i].copy())

    def size(self):
        a = 0
        b = 0
        resultB = 0
        for i in range(len(self.content)):
            a += 1
            for j in range(len(self.content[i])):
                b += 1
                if b > resultB:
                    resultB = b
            b = 0
        resultSize = (a, resultB)
        return resultSize

    def __str__(self):
        resultSTR = str()
        for i in range(len(self.content)):
            for j in range(len(self.content[i])):
                resultSTR += str(self.content[i][j]) \
                             + ("\t" if j + 1 < len(self.content[i]) else "")
            resultSTR += ("\n" if i + 1 < len(self.content) else "")
        return resultSTR

    def __add__(self, other):
        contentADD = []
        if len(self.content) == len(other.content):
            for i in range(len(self.content)):
                if len(self.content[i]) == len(other.content[i]):
                    contentADDI = []
                    for j in range(len(self.content[i])):
                        a = (self.content[i][j])
                        b = (other.content[i][j])
                        contentADDI.append(a + b)
                    contentADD.append(contentADDI)
                else:
                    raise MatrixError(self, other)
        else:
            raise MatrixError(self, other)
        return Matrix(contentADD)

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            contentMUL = []
            for i in range(len(self.content)):
                contentMULI = []
                for j in range(len(self.content[i])):
                    a = (self.content[i][j])
                    contentMULI.append(a * other)
                contentMUL.append(contentMULI)
            return Matrix(contentMUL)
        elif type(other) == Matrix:
            contentMUL = []
            contentMULProm = []
            if len(self.content[0]) != len(other.content):
                raise MatrixError(self, other)
            else:
                for i in range(len(self.content)):
                    result = 0
                    StopWhile = 0
                    while StopWhile < len(other.content[0]):
                        for j in range(len(self.content[i])):
                            sum1 = self.content[i][j]
                            sum2 = other.content[j][StopWhile]
                            result += sum1 * sum2
                        StopWhile += 1
                        contentMULProm.append(result)
                        result = 0
                    StopWhile = 0
                    contentMUL.append(contentMULProm)
                    contentMULProm = []
                return Matrix(contentMUL)
        else:
            raise MatrixError(self, other)

    __rmul__ = __mul__

    def transpose(self):
        result = []
        promResult = []
        a = len(self.content)
        for i in range(len(self.content[0])):
            while a != 0:
                promResult.append(self.content[-a][i])
                a -= 1
            a = len(self.content)
            result.append(promResult)
            promResult = []
        self.content = result
        return self

    @staticmethod
    def transposed(matrix):
        result = []
        promResult = []
        a = len(matrix.content)
        for i in range(len(matrix.content[0])):
            while a != 0:
                promResult.append(matrix.content[-a][i])
                a -= 1
            a = len(matrix.content)
            result.append(promResult)
            promResult = []
        matrix = result
        return Matrix(matrix)


exec(stdin.read())
