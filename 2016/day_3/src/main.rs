use std::io::{BufReader,BufRead};
use std::fs::File;


fn main() {
    let mut all_lines: Vec<String> = Vec::new();

    let file = File::open("input.txt").unwrap();
    for line in BufReader::new(file).lines() {
        all_lines.push(line.unwrap());
    }

    // _one(&all_lines);
    _two(&all_lines);
}


fn _one(all_lines: &Vec<String>) {
    let mut counter = 0;

    for line in all_lines {
        // Get vector of numbers
        let mut num_vec: Vec<i32> = Vec::new();
        for num in line.split_ascii_whitespace() {
            num_vec.push(num.parse::<i32>().unwrap());
        }
        // Sort vector
        num_vec.sort();

        // Check if vec[0] + vec[1] > vec[2]
        if (num_vec[0] + num_vec[1]) > num_vec[2] {
            counter += 1;
        }
    }
    println!("Counter: {}", counter);
}

fn _two(all_lines: &Vec<String>) {
    let mut counter = 0;

    let max_index: usize = all_lines.len() / 3;

    for i in 0..max_index{

        let slice = &all_lines[i*3..(i+1)*3];

        let mut line_1 = slice[0].split_ascii_whitespace();
        let mut line_2 = slice[1].split_ascii_whitespace();
        let mut line_3 = slice[2].split_ascii_whitespace();

        for _j in 0..3 {
            // Get vector of numbers
            let mut num_vec: Vec<i32> = Vec::new();
            num_vec.push(line_1.next().unwrap().parse::<i32>().unwrap());
            num_vec.push(line_2.next().unwrap().parse::<i32>().unwrap());
            num_vec.push(line_3.next().unwrap().parse::<i32>().unwrap());

            // Sort vector
            num_vec.sort();

            // Check if vec[0] + vec[1] > vec[2]
            if (num_vec[0] + num_vec[1]) > num_vec[2] {
                counter += 1;
            }
        }
    }
    println!("Counter: {}", counter);
}