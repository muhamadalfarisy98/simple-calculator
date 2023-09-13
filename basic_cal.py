class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a+b
    
    def subtract(self, a, b):
        return a-b
        
    def multiply(self, a, b):
        return a*b

    def divide(self, a, b):
        return a/b
    
    def modulo(self,a,b):
        return a%b

#create a calculator object
calc = Calculator()

print("Selamat datang di kalkulator sederhana \n")
while True:

    print("1: Tambah")
    print("2: Kurang")
    print("3: Kali")
    print("4: Bagi")
    print("5: Modulo")
    print("6: Keluar")
    
    cmd = int(input("Pilih Operasi: "))
    
    #Make sure the user have entered the valid choice
    if cmd in (1, 2, 3, 4, 5):
        
        #first check whether user want to exit
        if(cmd == 6):
            print("Terimakasih telah menggunakan kalkulator sederhana \n")
            break
        
        #If not then ask fo the input and call appropiate methods        
        a = int(input("Angka Pertama: "))
        b = int(input("Angka Kedua: "))
        
        match cmd :
            case 1 :
                print(a, "+", b, "=", calc.add(a, b))

            case 2 :
                print(a, "-", b, "=", calc.subtract(a, b))

            case 3 :
                print(a, "*", b, "=", calc.multiply(a, b))
            
            case 4:
                print(a, "/", b, "=", calc.divide(a, b))
            
            case 5:
                print(a, "%", b, "=", calc.modulo(a, b))
    
    else:
        print("Input tidak valid!")
    print("------------------\n")