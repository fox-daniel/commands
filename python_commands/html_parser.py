from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):  
        print(f"Start: {tag}")
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")

    def handle_endtag(self, tag):   
        print(f"End: {tag}")

    def handle_data(self, data):    
        pass
        # print(f"Data: {data}")

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")

parser = MyHTMLParser()

with open("html_example.html") as reader:
    html_text ="".join(reader.readlines())
    parser.feed(html_text)

