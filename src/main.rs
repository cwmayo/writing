use std::fs;
use std::fs::File;
use std::io::Write;


fn main() -> std::io::Result<()> {
    println!("Starting build process");

    // remove placeholder file
    fs::remove_file("./output/delete.md")?;

    let mut file = create_file("cool.txt").unwrap();



    

    Ok(())
}

fn create_file(name: &str) -> Result<File, std::io::Error> {
    return File::create(format!("./output/{}", name));
}


