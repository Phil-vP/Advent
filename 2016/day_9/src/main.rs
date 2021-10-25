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

        let final_string = decompress(line.to_owned());

        counter += final_string.len()
    }

    println!("Counter: {}", counter);
}

fn _two(all_lines: &Vec<String>) {
    let mut counter = 0;
    
    for line in all_lines {

        let length = decompress_number(line);

        counter += length;
    }

    println!("Counter: {}", counter);
}


fn decompress(input: String) -> String {
    let mut full_vec: Vec<char> = Vec::new();
    let mut chars = input.chars();

    while let Some(c) = chars.next() {
        match c {
            '(' => {
                let mut num_1_parse = "".to_owned();
                let mut num_1_char = chars.next().unwrap();
                while num_1_char != 'x' {
                    num_1_parse.push(num_1_char);
                    num_1_char = chars.next().unwrap();
                }
                let num_1 = num_1_parse.parse::<usize>().unwrap();

                // num_1_char is now x

                let mut num_2_parse = "".to_owned();
                let mut num_2_char = chars.next().unwrap();
                
                while num_2_char != ')' {
                    num_2_parse.push(num_2_char);
                    num_2_char = chars.next().unwrap();
                }
                let num_2 = num_2_parse.parse::<usize>().unwrap();

                // num_2_char is now )

                let mut slice_to_repeat: Vec<char> = Vec::new();
                for _i in 0..num_1 {
                    slice_to_repeat.push(chars.next().unwrap());
                }

                for _i in 0..num_2 {
                    full_vec.extend(&slice_to_repeat);
                }

            },
            _ => full_vec.push(c),
        }
    }

    let final_string: String = full_vec.iter().collect();

    final_string
}

fn decompress_number(input: &str) -> i64 {
    let mut length = 0;
    let mut chars = input.chars();

    while let Some(c) = chars.next() {
        match c {
            '(' => {
                let mut num_1_parse = "".to_owned();
                let mut num_1_char = chars.next().unwrap();
                while num_1_char != 'x' {
                    num_1_parse.push(num_1_char);
                    num_1_char = chars.next().unwrap();
                }
                let num_1 = num_1_parse.parse::<usize>().unwrap();

                // num_1_char is now x

                let mut num_2_parse = "".to_owned();
                let mut num_2_char = chars.next().unwrap();
                
                while num_2_char != ')' {
                    num_2_parse.push(num_2_char);
                    num_2_char = chars.next().unwrap();
                }
                let num_2 = num_2_parse.parse::<usize>().unwrap();

                // num_2_char is now )

                let mut slice_to_parse: String = "".to_owned();
                for _i in 0..num_1 {
                    slice_to_parse.push(chars.next().unwrap());
                }

                length += num_2 as i64 * decompress_number(&slice_to_parse);

            },
            _ => length += 1
        }
    }


    length
}