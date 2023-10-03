# try:
#     num = int(input("Sayı girin: "))
#     result = 10 / num
#     print("Result: ",result)
# except TypeError:
#     print("Tip Hatası")
# except ValueError:
#     print("Deger Hatası")
# except ZeroDivisionError:
#     print("Sıfıra bölünmez Hatası")    

# try:
#     file =open("example.txt","r")
#     content = file.read()
#     file.close()
#     num = int(content)
#     result = 10/num
# except FileNotFoundError:
#     print("Dosya Bulunamadı Hatası")  
# except (TypeError,ValueError):     
#     print("Invalid Hatası")  
# except ZeroDivisionError:
#     print("Sıfıra bölünmez Hatası")
# else:
#     print("Başarılı çalışma: ",result)   
# finally:
#     print("İşlemler tamamlandı.")   

# class CustomError(Exception):
#     def __init__(self, message):
#         super().__init__(message)

# try:
#     age = int(input("Enter your age: "))
#     if age < 0:
#         raise CustomError("Age cannot be negative!")
# except CustomError as e:
#     print("Error:", e)
# else:
#     print("Age entered:", age)

num = int(input("Enter a number: "))
assert num >= 0, "Number cannot be negative!"
print("Entered number:", num)
