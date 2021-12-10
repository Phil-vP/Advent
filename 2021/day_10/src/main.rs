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
    let opener = ['(', '[', '{', '<'];
    let mut lookup_openclose: HashMap<char, char> = HashMap::new();
    lookup_openclose.insert(')', '(');
    lookup_openclose.insert(']', '[');
    lookup_openclose.insert('}', '{');
    lookup_openclose.insert('>', '<');

    let mut lookup_value: HashMap<char, i32> = HashMap::new();
    lookup_value.insert(')', 3);
    lookup_value.insert(']', 57);
    lookup_value.insert('}', 1197);
    lookup_value.insert('>', 25137);

    let mut score = 0;

    for line in all_lines {
        let mut stack: Vec<char> = Vec::new();
        for c in line.chars() {
            if opener.contains(&c) {
                stack.push(c);
            }
            else {
                let last = stack.pop().unwrap();
                if lookup_openclose[&c] != last {
                    println!("{} is invalid due to {}", line, lookup_openclose[&c]);
                    score += lookup_value[&c];
                    break;
                }
            }
        }
    }

    println!("Score: {}", score);
}

fn _two(all_lines: &Vec<String>) {
    let opener = ['(', '[', '{', '<'];
    let mut lookup_openclose: HashMap<char, char> = HashMap::new();
    lookup_openclose.insert(')', '(');
    lookup_openclose.insert(']', '[');
    lookup_openclose.insert('}', '{');
    lookup_openclose.insert('>', '<');

    let mut lookup_value: HashMap<char, i64> = HashMap::new();
    lookup_value.insert('(', 1);
    lookup_value.insert('[', 2);
    lookup_value.insert('{', 3);
    lookup_value.insert('<', 4);

    let mut scores: Vec<i64> = Vec::new();

    'outer_loop: for line in all_lines {

        let mut score: i64 = 0;
        let mut stack: Vec<char> = Vec::new();
        for c in line.chars() {
            if opener.contains(&c) {
                stack.push(c);
            }
            else {
                let last = stack.pop().unwrap();
                if lookup_openclose[&c] != last {
                    continue 'outer_loop;
                }
            }
        }

        while stack.len() > 0 {
            let last = stack.pop().unwrap();
            score *= 5;
            score += lookup_value[&last];
        }
        scores.push(score);
    }

    scores.sort();

    let scores_len = scores.len();
    let scores_len_half = scores_len / 2;

    println!("Median: {}", scores[scores_len_half]);
    
}