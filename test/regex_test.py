import re



def main():
    regex = "<img size=750x792>//img.alicdn.com/imgextra/i2/1025314846/O1CN011lfVnTb22pRewBH_!!1025314846.jpg</img>"
    result = re.match("//img.alicdn.com/",regex).group(0)
    print(result)

if __name__ == '__main__':
    main()