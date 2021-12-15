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
    let mut line_iter = all_lines.iter();
    let mut polymer = line_iter.next().unwrap().to_string();

    line_iter.next();

    let mut lookup: HashMap<String, char> = HashMap::new();
    for line in line_iter {
        let mut line_split = line.split(" -> ");
        lookup.insert(line_split.next().unwrap().to_string(), line_split.next().unwrap().chars().next().unwrap());
    }

    for i in 1..=10 {
        let mut new_polymer = String::new();
        let mut left_char = polymer.chars().next().unwrap();
        new_polymer.push(left_char);

        for right_char in polymer.chars().skip(1) {
            let key = format!("{}{}", left_char, right_char);
            let value = lookup.get(&key).unwrap();

            new_polymer.push(*value);
            new_polymer.push(right_char);

            left_char = right_char;
        }

        polymer = new_polymer;

        println!("After step {:2}, its length is {:4}", i, polymer.len());
    }

    let mut min_count: i16 = std::i16::MAX;
    let mut min_char: char = ' ';
    let mut max_count: i16 = 0;
    let mut max_char: char = ' ';

    let mut chars_counted: Vec<char> = Vec::new();

    // Find the most common and least common character in polymer
    for c in polymer.chars() {
        if chars_counted.contains(&c) {
            continue;
        }
        chars_counted.push(c);
        let count = polymer.chars().filter(|&x| x == c).count() as i16;
        if count > max_count {
            max_count = count;
            max_char = c;
        }
        if count < min_count {
            min_count = count;
            min_char = c;
        }
    }

    println!("Most common char is {} with count {}", max_char, max_count);
    println!("Least common char is {} with count {}", min_char, min_count);

    println!("Difference: {}", max_count - min_count);
    

}

fn _two(all_lines: &Vec<String>) {
    let mut line_iter = all_lines.iter();
    let polymer = line_iter.next().unwrap().to_string();

    line_iter.next();

    let mut lookup: HashMap<String, char> = HashMap::new();
    for line in line_iter {
        let mut line_split = line.split(" -> ");
        lookup.insert(line_split.next().unwrap().to_string(), line_split.next().unwrap().chars().next().unwrap());
    }

    let combinations: Vec<String> = lookup.keys().map(|x| x.to_string()).collect();

    let mut count_map: HashMap<String, i64> = HashMap::new();
    for c in combinations.clone() {
        count_map.insert(c.to_string(), 0);
    }

    let mut left_char = polymer.chars().next().unwrap();
    for right_char in polymer.chars().skip(1) {
        let key = format!("{}{}", left_char, right_char);
        
        count_map.entry(key).and_modify(|x| *x += 1);

        left_char = right_char;
    }


    for i in 1..=40 {

        let old_map = count_map.clone();

        for key in &combinations {
            let value = old_map.get(key).unwrap().clone();
            if value == 0 {
                continue;
            }
            let lookup_value = lookup.get(key).unwrap();

            let left = format!("{}{}", key.chars().nth(0).unwrap(), lookup_value);
            let right = format!("{}{}", lookup_value, key.chars().nth(1).unwrap());

            count_map.entry(left).and_modify(|x| *x += value);
            count_map.entry(right).and_modify(|x| *x += value);

            count_map.entry(key.clone()).and_modify(|x| *x -= value);

        }
    }

    let mut count: HashMap<char, i64> = HashMap::new();
    for (key, value) in count_map {
        let char_left = key.chars().nth(0).unwrap();
        let char_right = key.chars().nth(1).unwrap();

        // If count doesn't contain the char, add it
        if !count.contains_key(&char_left) {
            count.insert(char_left, 0);
        }
        if !count.contains_key(&char_right) {
            count.insert(char_right, 0);
        }
        
        count.entry(char_left).and_modify(|x| *x += value);
        count.entry(char_right).and_modify(|x| *x += value);
    }

    let mut polymer_chars = polymer.chars();
    let first_char = polymer_chars.next().unwrap();
    let last_char = polymer_chars.last().unwrap();

    count.entry(first_char).and_modify(|x| *x += 1);
    count.entry(last_char).and_modify(|x| *x += 1);

    // Divide every entry in count by 2
    for (_, value) in &mut count {
        *value /= 2;
    }

    // Print count
    for (k, v) in &count {
        println!("{}: {}", k, v);
    }

    let min = count.values().min().unwrap();
    let max = count.values().max().unwrap();

    println!("Difference: {}", max - min);
    
}