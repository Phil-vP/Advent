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
    let mut depth = 0;
    let mut forward = 0;

    for line in all_lines {
        let mut split = line.split_ascii_whitespace();
        let operator = split.next().unwrap();
        let num = split.next().unwrap().parse::<i32>().unwrap();
        if operator == "forward" {
            forward += num;
        }
        else if operator == "down" {
            depth += num;
        }
        else if operator == "up" {
            depth -= num;
        }
        else{
            println!("Error: Operator {} can't be understood", operator);
            return
        }
    }

    println!("Final: {}m forward, {}m depth, mult is {}", forward, depth, forward * depth);
}

fn _two(all_lines: &Vec<String>) {
    let mut depth = 0;
    let mut forward = 0;
    let mut aim = 0;

    for line in all_lines {
        let mut split = line.split_ascii_whitespace();
        let operator = split.next().unwrap();
        let num = split.next().unwrap().parse::<i32>().unwrap();
        if operator == "forward" {
            forward += num;
            depth += num * aim;
        }
        else if operator == "down" {
            aim += num;
        }
        else if operator == "up" {
            aim -= num;
        }
        else{
            println!("Error: Operator {} can't be understood", operator);
            return
        }
    }

    println!("Final: {}m forward, {}m depth, mult is {}", forward, depth, forward * depth);
}