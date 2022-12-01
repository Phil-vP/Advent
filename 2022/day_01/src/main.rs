use std::i128::MAX;
use std::io::{BufReader,BufRead};
use std::fs::File;


fn main() {
    let mut all_lines: Vec<String> = Vec::new();

    let file = File::open("input.txt").unwrap();
    for line in BufReader::new(file).lines() {
        all_lines.push(line.unwrap());
    }

    // _one(&all_lines);
    // _two(&all_lines);
}


fn _one(all_lines: &Vec<String>) {
    let mut max = 0;
    let mut current = 0;
    for l in all_lines {
        if l.is_empty() {
            max = max.max(current);
            current = 0;
        }
        else {
            current += l.parse::<i32>().unwrap();
        }
    }
    max = max.max(current);
    println!("Max: {}", max);
}

fn _two(all_lines: &Vec<String>) {
    let mut sum_list: Vec<i32> = Vec::new();
    let mut current = 0;
    for l in all_lines {
        if l.is_empty() {
            sum_list.push(current);
            current = 0;
        }
        else {
            current += l.parse::<i32>().unwrap();
        }
    }
    sum_list.push(current);
    sum_list.sort();
    let mut final_sum = 0;
    for _ in 0..3 {
        final_sum += sum_list.pop().unwrap();
    }
    println!("Final sum: {}", final_sum);
}