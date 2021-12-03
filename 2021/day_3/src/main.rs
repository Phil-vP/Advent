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
    let all_lines_length: f32 = all_lines.len()as f32;
    let line_length = all_lines[0].len();
    let mut count_vec: Vec<u32> = Vec::new();

    for _i in 0..line_length {
        count_vec.push(0);
    }

    for line in all_lines {
        let mut chars = line.chars();
        for i in 0..line.len() {
            let c = chars.next().unwrap().to_digit(10).unwrap_or(2);
            count_vec[i] += c;
        }
    }

    let mut final_str = "".to_owned();

    for i in 0..all_lines[0].len() {
        println!("Index: {}, count: {}", i, count_vec[i]);
        final_str.push_str(if count_vec[i] > (all_lines_length / 2.0) as u32{
            "1"
        }
        else {
            "0"
        });
    }

    let gamma = isize::from_str_radix(&final_str, 2).unwrap() as i32;

    let mut epsilon: i32 = 2;
    epsilon = epsilon.pow(line_length as u32);
    epsilon -= 1;
    epsilon -= gamma;

    println!("gamma: {}, epsilon: {}, mult: {}", gamma, epsilon, gamma * epsilon);


}

fn _two(all_lines: &Vec<String>) {
    let mut final_rating = 1;
    
    for rating in 0..2{
        let mut counter = 0;
        let mut list_vec: Vec<String> = all_lines.to_owned();
        loop {

            let mut vec_0: Vec<String> = Vec::new();
            let mut vec_1: Vec<String> = Vec::new();

            for bin_num in list_vec {
                let mut chars = bin_num.chars();
                let element = chars.nth(counter);
                match element {
                    Some('0') => vec_0.push(bin_num.to_owned()),
                    Some('1') => vec_1.push(bin_num.to_owned()),
                    _ => panic!("Error"),
                }
            }
            counter += 1;

            list_vec = if vec_0.len() > vec_1.len() {
                if rating == 0 {
                    vec_0
                }
                else {
                    vec_1
                }
            }
            else {
                if rating == 0 {
                    vec_1
                }
                else {
                    vec_0
                }
            };

            if list_vec.len() == 1 {
                let rating_num = isize::from_str_radix(&list_vec[0], 2).unwrap() as i32;
                match rating {
                    0 => println!("Oxygen generator rating: {:?}", rating_num),
                    1 => println!("CO2 scrubber rating: {:?}", rating_num),
                    _ => panic!("Error"),
                }
                final_rating *= rating_num;
                break;
            }
        }
    }

    println!("Final rating: {}", final_rating);
    
}