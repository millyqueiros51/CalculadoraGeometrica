#C:\\Users\\Seven\\PycharmProjects\\pythonProject\\venv


def print_header(title):
    print("Content-type:text/html\r\n\r\n")
    print("""<html>
                <head>
                    <meta charset="UTF-8">
                    <title>{}</title>
                </head>
                <body>""".format(title))


def print_footer():
    print("</body></html>")