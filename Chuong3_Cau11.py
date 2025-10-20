''' Kiểm tra số nguyên tố'''
'''Viết chương trình nhập vào một số, kiểm tra xem số này có phải là số nguyên tố
hay không. Hỏi người dùng có tiếp tục sử dụng hay thoát phần mềm.'''
while True:
 n=int(input("Nhập 1 số nguyên dương"))
 dem=0
 for i in range(1,n+1):
  if n % i ==0 :
   dem+=1
 if dem==2:
   print(n,"Là số nguyên tố")
 else: 
  print(n,"Không là số nguyên tố")
 hoi=input("Tiếp không Thím?(c/k):")
 if hoi is "k":
  break
print("BYE!")