use std::io::{BufReader,BufRead};
use std::fs::File;


fn main() {
    let mut all_lines: Vec<i32> = Vec::new();

    let file = File::open("input.txt").unwrap();
    for line in BufReader::new(file).lines() {
        all_lines.push(line.unwrap().parse::<i32>().unwrap());
    }

    // _one(&all_lines);
    _two(&all_lines);
}


fn _one(all_lines: &Vec<i32>) {
    let mut number = all_lines[0];
    let mut counter = 0;

    for line in all_lines {
        let number_new = line;
        if number_new > &number {
            counter += 1;
        }
        number = *number_new;
        // println!("Num: {}", number);
    }

    println!("Counter: {}", counter);
}

fn _two(all_lines: &Vec<i32>) {
    let mut window_old = 1000000;
    let mut counter = 0;

    for index in 2..all_lines.len() {
        let window: i32 = all_lines[index-2..index+1].to_vec().iter().sum();
        if window > window_old {
            counter += 1;
        }
        window_old = window;
        // println!("Vec: {:?}\n", window);
    }

    println!("Counter: {}", counter);
}