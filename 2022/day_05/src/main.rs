use std::io::{BufReader,BufRead};
use std::fs::File;


fn main() {
    let testing = false;

    let file: File = if testing {
        File::open("test_input.txt").unwrap()
    }
    else{
        File::open("input.txt").unwrap()
    };

    let mut first_part = true;
    let mut first_ever = true;

    let mut all_stacks: Vec<Vec<char>> = Vec::new();
    let mut instructions: Vec<(usize, usize, usize)> = Vec::new();

    let mut number_of_stacks: usize = 0;
	
    for line in BufReader::new(file).lines() {
        let mut line_str = line.unwrap();
        if line_str == "" {
            continue;
        }
        if first_part {    
            if !line_str.contains('[') {
                first_part = false;
                continue;
            }
            line_str += " ";
            let chars: Vec<char> = line_str.chars().collect();
            number_of_stacks = chars.len() / 4;
            
            if first_ever {
                first_ever = false;
                for i in 0..number_of_stacks {
                    all_stacks.push(Vec::new());
                    println!("Created stack {}", i);
                }
            }

            for i in 0..number_of_stacks {
                let char_in_question = chars[1 + i*4];
                if char_in_question != ' ' {
                    all_stacks[i].push(char_in_question);
                }
            }
        }
        else{
            let split: Vec<&str> = line_str.split(" ").collect();
            let mut instruction: (usize, usize, usize) = (0, 0, 0);
            instruction.0 = split[1].parse::<usize>().unwrap();
            instruction.1 = split[3].parse::<usize>().unwrap();
            instruction.2 = split[5].parse::<usize>().unwrap();
            instructions.push(instruction);
            println!("Instruction: {:?}", instruction);
        }
    }

    for i in 0..number_of_stacks {
        all_stacks[i].reverse();
    }

    // _one(&all_stacks, &instructions);
    _two(&all_stacks, &instructions);
}


fn _one(stacks: &Vec<Vec<char>>, instructions: &Vec<(usize, usize, usize)>) {
    let mut stacks = stacks.clone();
    for instruction in instructions {
        let number_to_move = instruction.0;
        let stack_origin = instruction.1 - 1;
        let stack_destination = instruction.2 - 1;

        for _ in 0..number_to_move {
            let char_to_move = stacks[stack_origin].pop().unwrap();
            stacks[stack_destination].push(char_to_move);
        }
        for stack in &stacks {
            println!("{:?}", stack);
        }
    }
}

fn _two(stacks: &Vec<Vec<char>>, instructions: &Vec<(usize, usize, usize)>) {
    let mut stacks = stacks.clone();
    for instruction in instructions {
        let number_to_move = instruction.0;
        let stack_origin = instruction.1 - 1;
        let origin_size = stacks[stack_origin].len();
        let stack_destination = instruction.2 - 1;

        let mut storage: Vec<char> = stacks[stack_origin][origin_size-number_to_move..origin_size].to_vec();
        stacks[stack_origin].truncate(origin_size-number_to_move);
        stacks[stack_destination].append(&mut storage);
    }

    for stack in &stacks {
        print!("{}", stack.last().unwrap());
    }
}