use std::fs;
fn main() {
    println!("Hello, world!");
    let _ = fs::create_dir("./output");
}
