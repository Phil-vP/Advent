use std::collections::HashMap;
use std::io::{BufReader,BufRead};
use std::fs::File;



fn main() {
    let mut all_lines: Vec<String> = Vec::new();

    let testing = false;

    let file: File = if testing {
        File::open("test_input.txt").unwrap()
    }
    else{
        File::open("input.txt").unwrap()
    };
	
    for line in BufReader::new(file).lines() {
        all_lines.push(line.unwrap());
    }

    _one(&all_lines);
    // _two(&all_lines);
}


fn _one(all_lines: &Vec<String>) {
    let input_string = "11111111111111".to_string();
    
    let registers = _alu(&input_string, &all_lines);
    
    println!(" => {:?}", registers);
}

fn _two(all_lines: &Vec<String>) {
    
}

fn _alu(input_string: &str, all_lines: &Vec<String>) -> HashMap<char, i32> {
    let mut input_vec: Vec<i32> = input_string.chars().map(|c| c.to_digit(10).unwrap() as i32).collect();
    let mut registers: HashMap<char, i32> = HashMap::new();
    registers.insert('w', 0);
    registers.insert('x', 0);
    registers.insert('y', 0);
    registers.insert('z', 0);

    for line in all_lines.iter() {
        let split: Vec<&str> = line.split(" ").collect();
        let command = split[0];
        let target_register = split[1].chars().nth(0).unwrap();
        print!(" => {:?}\n{}, {:?}", registers, line, registers);
        match command {
            "inp" => {
                registers.insert(target_register, input_vec.pop().unwrap());
            },
            "add" => {
                let b_register = split[2].chars().nth(0).unwrap();
                let b = if b_register.is_alphabetic() {
                    registers.get(&b_register).unwrap().clone()
                } else {
                    split[2].parse::<i32>().unwrap()
                };
                let a = registers.get(&target_register).unwrap().clone();
                registers.insert(target_register, a + b);
            },
            "mul" => {
                let b_register = split[2].chars().nth(0).unwrap();
                let b = if b_register.is_alphabetic() {
                    registers.get(&b_register).unwrap().clone()
                } else {
                    split[2].parse::<i32>().unwrap()
                };
                let a = registers.get(&target_register).unwrap().clone();
                registers.insert(target_register, a * b);
            },
            "div" => {
                let b_register = split[2].chars().nth(0).unwrap();
                let b = if b_register.is_alphabetic() {
                    registers.get(&b_register).unwrap().clone()
                } else {
                    split[2].parse::<i32>().unwrap()
                };
                let a = registers.get(&target_register).unwrap().clone();
                registers.insert(target_register, a / b);
            },
            "mod" => {
                let b_register = split[2].chars().nth(0).unwrap();
                let b = if b_register.is_alphabetic() {
                    registers.get(&b_register).unwrap().clone()
                } else {
                    split[2].parse::<i32>().unwrap()
                };
                let a = registers.get(&target_register).unwrap().clone();
                registers.insert(target_register, a % b);
            },
            "eql" => {
                let b_register = split[2].chars().nth(0).unwrap();
                let b = if b_register.is_alphabetic() {
                    registers.get(&b_register).unwrap().clone()
                } else {
                    split[2].parse::<i32>().unwrap()
                };
                let a = registers.get(&target_register).unwrap().clone();
                if a == b {
                    registers.insert(target_register, 1);
                } else {
                    registers.insert(target_register, 0);
                }
            },
            _ => { println!("error"); break;},
        }
    }
    return registers;
}