from bs4 import BeautifulSoup
import os

# Get main content of file, skip YAML if present
def get_file_text(source: str):
    if source.find("---\n") != -1:
        return source.split("---\n")[2]
    return source

if __name__ == "__main__":
    files = os.listdir("./docs")

    files_href = []
    
    # Build html files from parsed .txt in docs directory
    for file_name in files:
        html = BeautifulSoup(open("./docs/template.html").read(), "html.parser")
        content_div = html.find(id="page-content")
        if file_name.find(".css") == -1 and file_name.find(".html") == -1:
            src_content = get_file_text(open("./docs/" + file_name).read())
            files_href.append(file_name[:-3] + "html")
            # Separate text based on paragraphs
            src_content = src_content.split("\n")
            
            for content_paragraph in src_content:
                paragraph = html.new_tag("p")
                paragraph.string = content_paragraph
                content_div.append(paragraph)
            
            open("./output/" + file_name[:-3] + "html", "w").write(html.prettify())

    # Html of index file

    # Below Code for putting pages on index
    # html = BeautifulSoup(open("./output/index.html", "r").read(), "html.parser")
    # featured_pages = html.find(id="featured-pages")

    # for ref in files_href:
    #     a = html.new_tag("a")
    #     a.string = ref
    #     a["href"] = ref
    #     featured_pages.append(a)

    # open("./output/index.html", "w").write(html.prettify())

            


