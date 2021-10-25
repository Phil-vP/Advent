use std::io::{BufReader,BufRead};
use std::fs::File;
use std::collections::HashMap;


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
    let word_length = all_lines[0].len();
    let mut letter_vec: Vec<HashMap<char, i32>> = Vec::new();

    for _i in 0..word_length {
        let mut hm: HashMap<char, i32> = HashMap::new();
        for c in "abcdefghijklmnopqrstuvwxyz".chars() { hm.insert(c, 0); }
        letter_vec.push(hm);
    }

    for line in all_lines {
        let mut chars = line.chars();
        for i in 0..word_length {
            let c = chars.nth(0).unwrap();
            let hm = &mut letter_vec[i];
            if !hm.contains_key(&c) {
                hm.insert(c, 0);
            }
            *hm.get_mut(&c).unwrap() += 1;
        }
    }

    'main_loop: for i in 0..word_length {
        let hm = &letter_vec[i];
        let max_val = hm.values().max().unwrap();
        for k in hm.keys() {
            if hm.get(k).unwrap() == max_val {
                print!("{}", k);
                continue 'main_loop
            }
        }
    }
}

fn _two(all_lines: &Vec<String>) {
    let word_length = all_lines[0].len();
    let mut letter_vec: Vec<HashMap<char, i32>> = Vec::new();

    for _i in 0..word_length {
        let mut hm: HashMap<char, i32> = HashMap::new();
        letter_vec.push(hm);
    }

    for line in all_lines {
        let mut chars = line.chars();
        for i in 0..word_length {
            let c = chars.nth(0).unwrap();
            let hm = &mut letter_vec[i];
            if !hm.contains_key(&c) {
                hm.insert(c, 0);
            }
            *hm.get_mut(&c).unwrap() += 1;
        }
    }

    'main_loop: for i in 0..word_length {
        let hm = &letter_vec[i];
        let min_val = hm.values().min().unwrap();
        for k in hm.keys() {
            if hm.get(k).unwrap() == min_val {
                print!("{}", k);
                continue 'main_loop
            }
        }
    }
    
}