'''Nhập một số n có tối đa 2 chữ số. Hãy cho biết cách đọc ra dạng chữ.
(vd: n=35 => Ba mươi lăm, n=5 => năm).'''
so=int(input("Nhập một số có hai chữ số):"))
while(so>99):
   so=int(input("Nhập lại một số có hai chữ số):"))
hangchuc=int(so/10)
chuc=''
if(hangchuc==1):chuc ='Muoi'
elif(hangchuc==2):chuc= 'Hai Muoi'
elif(hangchuc==3):chuc= 'Ba Muoi'
elif(hangchuc==4):chuc= 'Bon Muoi'
elif(hangchuc==5):chuc= 'Nam Muoi'
elif(hangchuc==6):chuc= 'Sau Muoi'
elif(hangchuc==7):chuc= 'Bay Muoi'
elif(hangchuc==8):chuc= 'Tam Muoi'
elif(hangchuc==9):chuc= 'Chin Muoi'
hangdonvi=so%10
donvi=''
if(hangdonvi==1):donvi ='Mot'
elif(hangdonvi==2):donvi= 'Hai'
elif(hangdonvi==3):donvi= 'Ba'
elif(hangdonvi==4):donvi= 'Bon'
elif(hangdonvi==5):donvi= 'Nam'
elif(hangdonvi==6):donvi= 'Sau'
elif(hangdonvi==7):donvi= 'Bay'
elif(hangdonvi==8):donvi= 'Tam'
elif(hangdonvi==9):donvi= 'Chin'
print(chuc ,donvi)