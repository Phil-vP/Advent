use std::collections::HashMap;
use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let mut all_lines: Vec<String> = Vec::new();

    let testing = false;

    let file: File = if testing {
        // File::open("test_input.txt").unwrap()
        File::open("test_input_2.txt").unwrap()
    } else {
        File::open("input.txt").unwrap()
    };

    for line in BufReader::new(file).lines() {
        all_lines.push(line.unwrap());
    }

    // _one(&all_lines);
    _two(&all_lines);
}

fn parse_line_one(line: &String) -> i16 {
    let mut first = 0;
    let mut second = 0;

    for c in line.chars() {
        if c.is_digit(10) {
            let digit = c.to_digit(10).unwrap() as i16;
            if first == 0 {
                first = digit;
            }
            second = digit;
        }
    }

    return first * 10 + second;
}

fn parse_line_two(line: &String, list_of_numbers: &Vec<String>) -> i16 {
    let mut occurence_map: HashMap<usize, &String> = HashMap::new();

    for number_string in list_of_numbers {
        if let Some(index) = line.find(number_string) {
            occurence_map.insert(index, number_string);
        }
        if let Some(index) = line.rfind(number_string) {
            occurence_map.insert(index, number_string);
        }
    }

    // Sort occurence map by key
    let mut sorted_occurence_map: Vec<_> = occurence_map.iter().collect();
    sorted_occurence_map.sort_by_key(|k| k.0);

    // First number is at the front of the list
    // Second number is at the back of the list
    let first_number_string = sorted_occurence_map[0].1;
    let second_number_string = sorted_occurence_map[sorted_occurence_map.len() - 1].1;

    let first = match first_number_string.as_str() {
        "one" => 1,
        "two" => 2,
        "three" => 3,
        "four" => 4,
        "five" => 5,
        "six" => 6,
        "seven" => 7,
        "eight" => 8,
        "nine" => 9,
        "1" => 1,
        "2" => 2,
        "3" => 3,
        "4" => 4,
        "5" => 5,
        "6" => 6,
        "7" => 7,
        "8" => 8,
        "9" => 9,
        _ => 0,
    };

    let second = match second_number_string.as_str() {
        "one" => 1,
        "two" => 2,
        "three" => 3,
        "four" => 4,
        "five" => 5,
        "six" => 6,
        "seven" => 7,
        "eight" => 8,
        "nine" => 9,
        "1" => 1,
        "2" => 2,
        "3" => 3,
        "4" => 4,
        "5" => 5,
        "6" => 6,
        "7" => 7,
        "8" => 8,
        "9" => 9,
        _ => 0,
    };

    return first * 10 + second;
}

fn _one(all_lines: &Vec<String>) {
    let mut sum: i32 = 0;
    for line in all_lines {
        let parsed = parse_line_one(line);
        println!("Parsed number: {}", parsed);
        sum += parsed as i32;
    }
    println!("Sum: {}", sum)
}

fn _two(all_lines: &Vec<String>) {
    let list_of_numbers: Vec<String> = [
        "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "one", "two", "three", "four", "five",
        "six", "seven", "eight", "nine",
    ]
    .iter()
    .map(|s| s.to_string())
    .collect();

    let mut sum: i32 = 0;
    for line in all_lines {
        let parsed = parse_line_two(line, &list_of_numbers);
        println!("Parsed number: {}", parsed);
        sum += parsed as i32;
    }
    println!("Sum: {}", sum)
}
