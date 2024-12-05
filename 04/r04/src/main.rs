use std::fs;
// use regex; // 1.5.4
use regex::Regex;

fn main() {
    println!("Hello, world!");

    let contents = fs::read_to_string("../input")
        .expect("Should have been able to read the file");

    let _contens_split = contents.split("\r\n");

    // for part in contens_split {
    //     let splits = part.split("  ");
        
    //     println!("{} {}", x, y)
    // }

}
