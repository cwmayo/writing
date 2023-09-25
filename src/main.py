import os
import json

def parse_yaml(filename):
    f = open("./docs/" + filename, 'r')
    source = f.read()

    author = "Mayo CW Student"
    title = "Untitled"
    search_keys = []
    css_properties = []

    if(source.find("---\n") != -1):
        source = source.split("---\n")
        yaml = source[1]

        yaml = yaml.split("\n")

        for yaml_line in yaml:
            if(yaml_line != ""):
                if(yaml_line.find(",") == -1):
                    yaml_line = yaml_line.split(": ")
                    if yaml_line[0] == "author":
                        author = yaml_line[1]
                    elif yaml_line[0] == "title":
                        title = yaml_line[1]
                    else:
                        css_properties.append([yaml_line[0], yaml_line[1]])
                else:
                    if(yaml_line.lower().find("keywords:") != -1):
                        for s in yaml_line.split(": ")[1].split(", "): search_keys.append(s)

    return (title, author, css_properties, search_keys)

    
    
def build_html(filename):
    html_string = ""

    file = open("./docs/" + filename, "r")
    file = file.read()

    if(file.find("---\n") != -1):
        file = file.split("---\n")[2]

    file = file.split("\n")

    for text in file:
        # Tabs make the html in a more human readable format
        html_string += "\t\t\t<p>" + text + "</p>\n"

    return html_string

def create_html_file():
    f = open("./output/" + str(file)[:-4] + ".html", "w")

     # All \t and \n are just to make html more readable
    # config[0] and 1 are title and author
    title_bar_str = "\t\t<div class=\"title-bar\">\n\t\t\t<span>" + config[0] + "</span>\n\t\t\t<span>" + config[1] + "</span>\n\t\t</div>\n"

    # Split html to isolate CSS
    style = base_html[0].split("<style>")[1].split("</style>")[0] + "\n\tp {"

    # Add new CSS elements based on file
    for style_string in config[2]:
        style += "\n\t\t" + style_string[0] + ": " + style_string[1] + ";"
            
    style += "\n\t}\n"

    f.write(base_html[0].split("<style>\n")[0] + "<style>\n" + style + "\n\t\t</style>\n" + 
            base_html[0].split("</style>\n")[1].split("%%Page-Content")[0] + title_bar_str + 
            build_html(file) + base_html[1])
    f.close()


if __name__ == "__main__":
    files = os.listdir("./docs")
    base_html = open("./docs/template.html", "r")
    base_html = base_html.read().split("%%Page-Content")

    for file in files:
        if not ".html" in file:
            # parse yaml in .txt file in docs
            config = parse_yaml(file)
            # create ./output html file
            create_html_file()
            

            