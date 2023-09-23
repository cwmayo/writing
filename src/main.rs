use std::fs;
use std::fs::File;
use std::io::Write;

struct CSSElements {
    color: String,
    position: String,
}

struct PageInfo {
    author: String,
    keywords: Vec<String>,
    elements: CSSElements,
}
fn main() -> std::io::Result<()> {
    println!("Starting build process");

    // read files in docs directory
    for file in fs::read_dir("./docs").expect("Unable to read 'docs' directory") {
        let file_name = file.unwrap().path();
        let source: String = fs::read_to_string(file_name.clone()).expect("Unable to read file");

        // println!("{}", source);

        let mut page_info: Option<PageInfo> = None;

        if source.contains("---\n") {
            page_info = parse_yaml(&source);
        }


        let file_without_dir: Vec<&str> = file_name.as_path().to_str().unwrap().split("/").collect();
        let h_name: Vec<&str> = file_without_dir[2].split(".").collect();
        let html_name = h_name[0];


        if html_name != "template" {
            build_html(html_name, page_info.unwrap());
        }
    }
    


    

    Ok(())
}

// Parses YAML on the top of document
fn parse_yaml(source: &String) -> Option<PageInfo> {
    let mut page_info = PageInfo {
        author: String::from(""),
        keywords: Vec::new(),
        elements: CSSElements {
            color: String::from(""), 
            position: String::from("")}
    };

    let split_source: Vec<&str> = source.split("---\n").collect();
    let yaml_content = split_source[1];

    let lines: Vec<&str> = yaml_content.split("\n").collect();

    for line in lines {
        if line != "" {
            let split_line: Vec<&str> = line.split(": ").collect();

        // Match YAML elements to css
        match split_line[0] {
            "author" => page_info.author = split_line[1].to_string(),
            "keywords" => {
                for key in split_line[1].split(", ") {
                    page_info.keywords.push(key.to_string());
                }
            }

            "color" => page_info.elements.color = split_line[1].to_string(),
            "position" => page_info.elements.position = split_line[1].to_string(),

            // if not a current key, we println and keep going
            _ => println!("----- {} is currently an unsupported CSS style key -----", split_line[0]),
        }

        }
    }
    
    return Option::Some(page_info);
}

// Builds html
fn build_html(name: &str, info: PageInfo) {
    fs::copy("./docs/template.html", format!("./output/{}.html", name)).expect(format!("Couldn't create {}.html file", name).as_str());
}


