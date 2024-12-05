// use std::env;
use std::fs;

fn main() {
    let contents = fs::read_to_string("../input")
        .expect("Should have been able to read the file");
    let contens_split = contents.split("\r\n");

    for part in contens_split {
        let splits = part.split("  ");
        
        println!("{} {}", x, y)
    }
    // let contents_length = contens_split.len();
    // println!("With text:\n{contents_length}");
}
