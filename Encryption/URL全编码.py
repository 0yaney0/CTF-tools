import os

def main():
    clearFlag = "y"
    while(1):
        if clearFlag == "y" or clearFlag == "Y":
            os.system("cls")
        clearFlag = ""
        string = input("请输入需要转换的字符串 :")
        type = input("请选择操作类型(1：加密 2：解密) :")
        while(type != "1" and type != "2"):
            type = input("操作类型输入错误，请重新选择(1：加密 2：解密) :")
        if type == "1" :
            encode_string = encode(string)
            print("编码结果为："+encode_string+"\n")
        if type == "2" :
            decode_string = decode(string)
            print("解码结果为："+decode_string+"【请注意前后空格】\n")
        clearFlag = input("按Y/y清空屏幕继续:")

#编码
def encode(string):
    encode_string = ""
    for char in string:
        encode_char = hex(ord(char)).replace("0x","%")
        encode_string += encode_char
    return encode_string

#解码
def decode(string):
    decode_string = ""
    string_arr = string.split("%")
    string_arr.pop(0)           #删除第一个空元素
    for char in string_arr:
        decode_char = chr(eval("0x"+char))
        decode_string += decode_char
    return decode_string

main()
