# Variable = menyimpan nilai 
# type data
# 1. string = karakter -> p,r,a,b,o,w,o
# 2. integer = bilangan bulat -> 1,2,3,4,5,6,7,8,9
# 3. float = bilangan desimal -> 1.2, 2.3, 3.4, 4.5, 5.6
# 4. boolean = true/false -> benar/salah
x = 7 
print ("x")
# Mengubah tipe data
# a = 10, adalah variable dengan 10 
# tipe data: 99
data_integer = 99
print ("data :", data_integer)
print ("- bertipe ", type (data_integer))
# tipe data: 0.20
data_float = 0.20
print ("data : ", data_float)
print ("- bertipe ", type(data_float))
# tipe data: hidup jokowi
data_string = "hidup jokowi"
print ("data : ", data_string)
print ("- bertipe ", type (data_string))
# tipe data: true
data_bool = "true"
print ("data : ", data_bool)
print ("- bertipe ", type(data_bool))
## tipe data khusus
# bilangan kompleks
data_complex = 5,6,7,8
print ("data : ", data_complex)
print ("-bertipe ", type(data_complex))
data_integer = 1000699
print("data : ", data_integer)
print("- bertipe ", type(data_integer))

data_float = 45678.78
print("data : ", data_float)
print("- bertipe ", type(data_float))

data_string = "Gulai Kambing"
print("data : ", data_string)
print("- bertipe ", type(data_string))

data_bool = False
print("data : ", data_bool)
print("- bertipe ", type(data_bool))

x = 705
y = 345
print(x-y)
print(type(x))

a = 357.51
b = 222.59
print(a+b)
print(type(a+b))

c = "pria"
d = "solo"
e = c+d
print(e)

data_int = 100
data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)
print("data = ", data_float, ", type = ", type(data_float))
print("data = ", data_str, ", type = ", type(data_str))
print("data = ", data_bool, ", type = ", type(data_bool))

data_float = 100.2
data_int = float(data_float)
data_str = str(data_float)
data_bool = bool(data_float)
print("data = ", data_int, ", type = ", type(data_int))
print("data = ", data_str, ", type = ", type(data_str))
print("data = ", data_bool, ", type = ", type(data_bool))

data_str = "100.2"
data_int = float(data_str)
data_float = str(data_str)
data_bool = bool(data_str)
print("data = ", data_int, ", type = ", type(data_int))
print("data = ", data_float, ", type = ", type(data_float))
print("data = ", data_bool, ", type = ", type(data_bool))

data = input("Masukkan data: ")
print("data ",data,",type =",type(data))

angka = int(input("Masukkan angka: "))
print("data ",angka,",type =",type(angka))