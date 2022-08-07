
print("File name: ", end='')
x = input()
x = x.replace(" ", "").casefold()
x = x.split(".")[-1]



dicto = {
"gif" : "image/gif",
"jpg" : "image/jpeg",
"jpeg" : "image/jpeg",
"png" : "image/png",
"pdf" : "application/pdf",
"txt" : "text/plain",
"zip" : "application/zip"
}



if dicto.get(x):
    print(dicto.get(x))
else:
    print('application/octet-stream')