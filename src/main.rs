use std::fs;
use std::fs::File;
use std::io::Write;
fn main() -> std::io::Result<()> {
    println!("Hello, world!");
    let mut file = File::create("./output/test.txt")?;
    file.write_all(b"Hello?")?;
    
    Ok(())
}
