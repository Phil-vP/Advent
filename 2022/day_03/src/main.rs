use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let mut all_lines: Vec<String> = Vec::new();

    let testing = false;

    let file: File = if testing {
        File::open("test_input.txt").unwrap()
    } else {
        File::open("input.txt").unwrap()
    };

    for line in BufReader::new(file).lines() {
        all_lines.push(line.unwrap());
    }

    // _one(&all_lines);
    _two(&all_lines);
}

fn _one(all_lines: &Vec<String>) {
    let mut sum = 0;
    for line in all_lines {
        let split_index = line.len() / 2;
        let first_half = &line[..split_index];
        let second_half = &line[split_index..];
        let mut both_vec: Vec<char> = Vec::new();
        for c in first_half.chars() {
            if second_half.contains(c) && !both_vec.contains(&c) {
                both_vec.push(c);
                sum += get_val(c);
            }
        }
    }
    println!("{}", sum);
}

fn _two(all_lines: &Vec<String>) {
    let three_chunks = all_lines.chunks(3);
    let mut sum = 0;
    for chunk in three_chunks {
        let mut common_chars: Vec<char> = Vec::new();
        let first = chunk[0].clone();
        let second = chunk[1].clone();
        let third = chunk[2].clone();
        for c in first.chars() {
            if second.contains(c) && third.contains(c) && !common_chars.contains(&c) {
                common_chars.push(c);
                sum += get_val(c);
            }
        }
    }
    println!("{}", sum);
}

fn get_val(c: char) -> i32 {
    let mut val: i32 = (c as u32) as i32 - ('a' as u32) as i32 + 1;
    if val < 0 {
        val += 58;
    }
    val
}
