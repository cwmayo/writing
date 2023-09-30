from bs4 import BeautifulSoup
import yaml
import os

# Get main content of file, skip YAML if present
def get_file_text(source: str):
    if source.find("---\n") != -1:
        return source.split("---\n")[2]
    return source

def get_yaml_text(source: str):
    if source.find("---\n") != -1:
        return "---\n" + source.split("---\n")[1]

if __name__ == "__main__":
    files = os.listdir("./docs")

    files_href = []

    index = BeautifulSoup(open("./output/index.html").read(), "html.parser")
    # Build html files from parsed .txt in docs directory
    for file_name in files:
        html = BeautifulSoup(open("./docs/template.html").read(), "html.parser")
        content_div = html.find(id="work-text")
        if file_name.find(".css") == -1 and file_name.find(".html") == -1:

            yaml_dict = yaml.safe_load(get_yaml_text(open("./docs/" + file_name).read()))

            if "author" in yaml_dict:
                html.find(id="author").string = yaml_dict["author"]
            if "title" in yaml_dict:
                html.find(id="work-title").string = yaml_dict["title"]
            
            if "text-style" in yaml_dict:
                text = "\tp {\n"
                for style in yaml_dict["text-style"]:
                    key_str = list(style.keys())[0]
                    text += "\t\t" + key_str + ": " + style[key_str] + ";\n"
                html.find(id="page-style").string = text + "\t}"
                    

            src_content = get_file_text(open("./docs/" + file_name).read())
            # Separate text based on paragraphs
            src_content = src_content.split("\n")
            
            
            for content_paragraph in src_content:
                paragraph = html.new_tag("p")
                paragraph.string = content_paragraph
                content_div.append(paragraph)

            open("./output/" + file_name[:-3] + "html", "w").write(html.prettify())
            type = index.find(id=(yaml_dict.get('type', 'other')))
            link = index.new_tag("a")
            link['href'] = file_name[:-3] + "html"
            link.string = yaml_dict.get('title', 'Untitled')
            type.append(link)


    open("./output/index.html", "w").write(index.prettify())

            


