N:int = int(input())
i:int = 1;

def decimalToBinary(num: int) -> str:
    result:str = ""
    while( num >= 1):
        rem: int = num % 2;
        result = result + str(rem);
        num = num // 2
    return result[::-1]

def decimalToOctal(num: int) -> str:
    result:str = ""
    while( num >= 1):
        rem: int = num % 8;
        result = result + str(rem);
        num = num // 8
    return result[::-1]
def decimalToHexaDecimal(num: int) -> str:
    result:str = ""
    while( num >= 1):
        rem: int = num % 16
        if( rem >= 10):
            key:str = str(rem)
            result = result + hexadecimal_dict[key];
        else:
            result = result + str(rem)
        num = num // 16
    return result[::-1]

hexadecimal_dict = {
    "10":"A",
    "11":"B",
    "12":"C",
    "13":"D",
    "14":"E",
    "15":"F",
}
# the order is decimal octal hexadecimal binary
while i <= N:
    print(i,end="\t")
    print(decimalToOctal(i),end="\t")
    print(decimalToHexaDecimal(i),end="\t")
    print(decimalToBinary(i))
    i = i + 1