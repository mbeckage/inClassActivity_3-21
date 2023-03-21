#broken by cjrinald
# Open HTML in write mode
with open("numbers.html") as f:
    # Add even and odd numbers
    f.write("<html>\n<head>\n<title>List of Numbers</title>\n</head>\n<body>\n")
    f.write("<table>\n<tr><th>Even Numbers</th><th>Odd Numbers</th></tr>\n")
    i = 0
    for i in range(50):
        if i % 2 == 0:
            f.write("<tr><td>{}</td><td></td></tr>\n".format(i))
        else:
            f.write("<tr><td></td><td>{}</td></tr>\n".format(i))
    f.write("</table>\n</body>\n</html>")

# Read numbers
with open("numbers.html") as fin:
    print(f.read())
    
