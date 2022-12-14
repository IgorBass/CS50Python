fname=input('File name: ')

fname=fname.casefold().strip()
#x = fname[fname.find(".") + 1:]
y=(fname.split('.'))
x=y[-1]


if x == 'jpg' or x =='jpeg':
    print("image/jpeg")
elif x=='png' or x=='gif':
    print('image/'+x)
elif x=='pdf' or x=='zip':
    print("application/"+x)
elif x=='txt':
    print("text/plain")
else:
    print("application/octet-stream")