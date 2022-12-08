use itertools::Itertools;
use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let mut line: String = "".to_string();

    let testing = false;

    let file: File = if testing {
        File::open("test_input.txt").unwrap()
    } else {
        File::open("input.txt").unwrap()
    };

    BufReader::new(file).read_line(&mut line).unwrap();

    _both(&line, 4); // one
    _both(&line, 14); // two
}

fn _both(input_line: &String, window_size: usize) {
    let mut counter = window_size;
    for window in input_line
        .chars()
        .collect::<Vec<char>>()
        .windows(window_size)
    {
        let unique_count = window.into_iter().unique().count();
        if unique_count == window_size {
            println!(
                "Found marker ({}) for window size {} at counter {}",
                window.into_iter().collect::<String>(),
                window_size,
                counter
            );
            return;
        }
        counter += 1;
    }
}
