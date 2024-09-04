#MIME types/media types multipurpose internet mail extensions
# image/ .gif .jpg .jpeg .png
# application/ .pdf .zip
# text/plain .txt
# application/octact-stream  nothing or .others

type = input("Enter your media name with extension:\n").casefold().strip()

if type.endswith (".gif"):
    print ("image/gif")
elif type.endswith (".jpg") or (".jpeg"):
    print ("image/jpeg")
elif type.endswith (".png"):
    print ("image/png")
elif type.endswith (".pdf"):
    print ("application/pdf")
elif type.endswith (".zip"):
    print ("application/zip")
elif type.endswith (".txt"):
    print ("text/plain")
else:
    print ("application/octet-stream")
