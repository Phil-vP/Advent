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
    // assert!(is_valid("aaaaa-bbb-z-y-x-123[abxyz]").0);
    // assert!(is_valid("a-b-c-d-e-f-g-h-987[abcde]").0);
    // assert!(is_valid("not-a-real-room-404[oarel]").0);
    // assert!(!is_valid("totally-real-room-200[decoy]").0);

    let mut counter = 0;

    for line in all_lines {
        let result = is_valid(line);
        if result.0 {
            counter += result.1;
        }
    }

    println!("Counter: {}", counter);
}

fn _two(all_lines: &Vec<String>) {

    let mut valid_lines: Vec<&str> = Vec::new();
    
    for line in all_lines {
        if is_valid(line).0 {
            valid_lines.push(line);
        }
    }

    for line in valid_lines {
        let mut initial_split = line.split('[');
        initial_split.next_back();

        let name_init = initial_split.next().unwrap();
        let mut name_split = name_init.split('-');

        let id = name_split.next_back().unwrap().parse::<i32>().unwrap();

        let name_vec: Vec<&str> = name_split.collect();
        let name = name_vec.join(" ");

        let mut name_final = "".to_owned();
        for c in name.chars() {
            name_final.push(match c {
                ' ' => ' ',
                _ => (((c as u8) as i32 - 97 + id) % 26 + 97) as u8 as char
            })
        }

        if name_final.contains("north") {
            println!("{}", line);
            println!("{}: {}\n", id, name_final);
        }

    }

}




fn is_valid(input_str: &str) -> (bool, i32) {

    let mut initial_split = input_str.split('[');

    let name_init = initial_split.next().unwrap();
    let mut name_split = name_init.split('-');

    let id = name_split.next_back().unwrap().parse::<i32>().unwrap();

    let name_vec: Vec<&str> = name_split.collect();
    let name = name_vec.join("");

    let mut checksum_chars = initial_split.next().unwrap().chars();
    checksum_chars.next_back();
    let checksum = checksum_chars.as_str();

    let mut char_map: HashMap<char, i32> = HashMap::new();

    for c in name.chars() {
        if !char_map.contains_key(&c) {
            char_map.insert(c, 0);
        }
        *char_map.get_mut(&c).unwrap() += 1;
    }
    
    let mut check_str = "".to_owned();

    while check_str.len() < 5 {
        let max: i32 = *char_map.values().max().unwrap();

        let mut key_vec: Vec<char> = Vec::new();

        for k in char_map.keys(){
            if *char_map.get(k).unwrap() == max {
                key_vec.push(*k);
            }
        }

        key_vec.sort();

        for k in key_vec {
            check_str.push(k);
            char_map.remove(&k);
        }

    }

    check_str = check_str[..5].to_string();


    (check_str == checksum, id)
}