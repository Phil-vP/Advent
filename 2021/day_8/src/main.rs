use std::io::{BufReader,BufRead};
use std::fs::File;
use std::collections::HashMap;

use std::cmp;


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
        let first_split: Vec<&str> = line.split(" | ").collect();

        // First part can be disregarded

        let relevant = first_split[1].split_whitespace();

        for element in relevant {
            let length = element.len();
            
            counter += match length {
                2 | 3 | 4 | 7 => 1,
                _ => 0
            }
        }

    }

    println!("Counter: {}", counter);
    
}

fn _two(all_lines: &Vec<String>) {

    // let number_lookup: HashMap<String, i32>
    let mut number_lookup: HashMap<String, char> = HashMap::new();
    number_lookup.insert("abcefg".to_string(), '0');
    number_lookup.insert("cf".to_string(), '1');
    number_lookup.insert("acdeg".to_string(), '2');
    number_lookup.insert("acdfg".to_string(), '3');
    number_lookup.insert("bcdf".to_string(),'4');
    number_lookup.insert("abdfg".to_string(), '5');
    number_lookup.insert("abdefg".to_string(), '6');
    number_lookup.insert("acf".to_string(), '7');
    number_lookup.insert("abcdefg".to_string(), '8');
    number_lookup.insert("abcdfg".to_string(), '9');

    let mut segment_display_lookup: HashMap<i32, Vec<char>> = HashMap::new();
    segment_display_lookup.insert(2, vec!['c', 'f']);
    segment_display_lookup.insert(3, vec!['a', 'c', 'f']);

    let mut counter = 0;

    for line in all_lines {
        counter += compute_number(line, &mut number_lookup);
    }

    println!("Counter: {}", counter);
    
}


fn compute_number(line: &str, number_lookup: &mut HashMap<String, char>) -> i32 {

    let mut first_split = line.split(" | ");
    let mut encoded_strings: Vec<&str> = first_split.next().unwrap().split_whitespace().collect();

    let codes: Vec<&str> = first_split.next().unwrap().split_whitespace().collect();

    let mut decode_map: HashMap<char, char> = HashMap::new();

    // sort encoded_strings by length of string
    encoded_strings.sort_by(|a, b| a.len().cmp(&b.len()));
    
    let mut encoded_strings_chars: Vec<Vec<char>> = Vec::new();
    for encoded_string in encoded_strings.clone() {
        encoded_strings_chars.push(encoded_string.chars().collect());
    }

    // Using the two and 3 letter code, we can now determine the code for 'a'
    let two_code = encoded_strings[0];
    let mut three_code = encoded_strings[1].chars().collect::<Vec<char>>();

    // remove every char in two_code from three_code
    for c in two_code.chars() {
        three_code.retain(|&x| x != c);
    }

    let decoded_a: char = three_code[0];

    // println!("a is encoded as: {}", decoded_a);

    // remove decoded_a from every vec in encoded_strings_chars
    for encoded_string in encoded_strings_chars.iter_mut() {
        encoded_string.retain(|&x| x != decoded_a);
    }
    // Now, we know the code for 'a'
    // To get the next code, we look at numbers 4 and 9 to determine the code for 'g'
    // This is the only combination fromn a 4-letter word and a 6-letter word

    let mut code_duo: (Vec<char>, Vec<char>) = (Vec::new(), Vec::new());
    'first_loop: for first_place in 0..10 {
        for second_place in 1..10 {
            let first_str = encoded_strings[first_place];
            let second_str = encoded_strings[second_place];
            if first_str.len() == 4 && second_str.len() == 6 {
                let first_chars = encoded_strings_chars[first_place].clone();
                let second_chars = encoded_strings_chars[second_place].clone();
                if calc_differences(first_chars.clone(), second_chars.clone()) == 1 {
                    code_duo = (first_chars, second_chars);
                    break 'first_loop;
                }
            }
        }
    }


    // The only diffence between those two words is the letter 'g'
    let four_code = code_duo.0;
    let mut six_code = code_duo.1;

    // remove every char in four_code from six_code
    for c in four_code {
        six_code.retain(|&x| x != c);
    }

    let decoded_g: char = six_code[0];
    
    // remove decoded_g from every vec in encoded_strings_chars
    for encoded_string in encoded_strings_chars.iter_mut() {
        encoded_string.retain(|&x| x != decoded_g);
    }

    // Now, we know the code for 'a' and 'g'
    // To get the next code, we look at numbers 2 and 3 to determine the code for 'd'

    let mut code_duo: (Vec<char>, Vec<char>) = (Vec::new(), Vec::new());
    'first_loop_2: for first_place in 0..10 {
        for second_place in 1..10 {
            let first_str = encoded_strings[first_place];
            let second_str = encoded_strings[second_place];
            if first_str.len() == 2 && second_str.len() == 5 {
                let first_chars = encoded_strings_chars[first_place].clone();
                let second_chars = encoded_strings_chars[second_place].clone();
                if calc_differences(first_chars.clone(), second_chars.clone()) == 1 {
                    code_duo = (first_chars, second_chars);
                    break 'first_loop_2;
                }
            }
        }
    }


    // The only diffence between those two words is the letter 'd'
    let two_code = code_duo.0;
    let mut five_code = code_duo.1;

    // remove every char in two_code from five_code
    for c in two_code {
        five_code.retain(|&x| x != c);
    }

    let decoded_d: char = five_code[0];

    
    // remove decoded_d from every vec in encoded_strings_chars
    for encoded_string in encoded_strings_chars.iter_mut() {
        encoded_string.retain(|&x| x != decoded_d);
    }

    // Now, we know the code for 'a', 'g', and 'd'
    // To get the next code, we look at numbers 1 and 4 to determine the code for 'b'

    let mut code_duo: (Vec<char>, Vec<char>) = (Vec::new(), Vec::new());
    'first_loop_3: for first_place in 0..10 {
        for second_place in 1..10 {
            let first_str = encoded_strings[first_place];
            let second_str = encoded_strings[second_place];
            if first_str.len() == 2 && second_str.len() == 4 {
                let first_chars = encoded_strings_chars[first_place].clone();
                let second_chars = encoded_strings_chars[second_place].clone();
                code_duo = (first_chars, second_chars);
                break 'first_loop_3;
            }
        }
    }


    // The only diffence between those two words is the letter 'b'
    let two_code = code_duo.0;
    let mut four_code = code_duo.1;

    // remove every char in two_code from four_code
    for c in two_code {
        four_code.retain(|&x| x != c);
    }

    let decoded_b: char = four_code[0];

    
    // remove decoded_b from every vec in encoded_strings_chars
    for encoded_string in encoded_strings_chars.iter_mut() {
        encoded_string.retain(|&x| x != decoded_b);
    }

    // Now, 'f' is free in number 5
    // It's the only entry in encoded_strings_chars that has a length of 1
    let mut decoded_f: char = ' ';
    for encoded_string in encoded_strings_chars.iter() {
        if encoded_string.len() == 1 {
            decoded_f = encoded_string[0];
            break;
        }
    }

    
    // remove decoded_f from every vec in encoded_strings_chars
    for encoded_string in encoded_strings_chars.iter_mut() {
        encoded_string.retain(|&x| x != decoded_f);
    }
    

    // Only 'c' and 'e' are left
    // 'c' is the only entry in encoded_strings that has a length of four, it being Number 4
    let mut decoded_c: char = ' ';
    for i in 0..10 {
        if encoded_strings[i].len() == 4 {
            decoded_c = encoded_strings_chars[i][0];
            break;
        }
    }
    
    // remove decoded_c from every vec in encoded_strings_chars
    for encoded_string in encoded_strings_chars.iter_mut() {
        encoded_string.retain(|&x| x != decoded_c);
    }

    // Only 'e' is left, it's for example in Number 8 as that one has all of them
    let mut decoded_e: char = ' ';
    for i in 0..10 {
        if encoded_strings[i].len() == 7 {
            decoded_e = encoded_strings_chars[i][0];
            break;
        }
    }

    let mut final_number_string = "".to_owned();

    let char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g'];

    decode_map.insert('a', decoded_a);
    decode_map.insert('b', decoded_b);
    decode_map.insert('c', decoded_c);
    decode_map.insert('d', decoded_d);
    decode_map.insert('e', decoded_e);
    decode_map.insert('f', decoded_f);
    decode_map.insert('g', decoded_g);

    // Translate to number
    for code in codes {
        let mut new_str = code.to_ascii_uppercase();
        for c in &char_list {
            let old_char: &str = &decode_map[c].to_string().to_ascii_uppercase();
            let new_char = &c.to_string();
            new_str = new_str.replace(old_char, new_char);
        }
        let mut sorted: Vec<char> = new_str.chars().collect();
        sorted.sort();
        let final_string: String = sorted.into_iter().collect();
        
        let append_char: char = number_lookup[&final_string];
        final_number_string.push(append_char);
    }

    final_number_string.parse::<i32>().unwrap()
}

fn calc_differences(str_1: Vec<char>, str_2: Vec<char>) -> i32 {
    let mut differences = cmp::max(str_1.len(), str_2.len());
    for c1 in str_1 {
        if str_2.contains(&c1) {
            differences -= 1;
        }
    }
    differences as i32
}