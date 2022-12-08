use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let mut all_plays: Vec<(char, char)> = Vec::new();

    let testing = false;

    let file: File = if testing {
        File::open("test_input.txt").unwrap()
    } else {
        File::open("input.txt").unwrap()
    };

    for line in BufReader::new(file).lines() {
        let line = line.unwrap();
        let mut chars = line.chars();
        let first = chars.next().unwrap();
        chars.next();
        let second = chars.next().unwrap();
        all_plays.push((first, second));
    }

    // _one(&all_plays);
    // _two(&all_plays);
}

fn _one(all_plays: &Vec<(char, char)>) {
    let mut final_sum = 0;

    for play in all_plays {
        let first: i32 = (play.0 as u32 - 64) as i32;
        let second: i32 = (play.1 as u32 - 87) as i32;

        let difference = second - first;

        final_sum += second + (difference + 4) % 3 * 3;
    }

    println!("Final score: {}", final_sum);
}

fn _two(all_plays: &Vec<(char, char)>) {
    let mut final_sum = 0;

    // Rock = 1, Paper = 2, Scissors = 3
    for play in all_plays {
        let first: i32 = (play.0 as u32 - 64) as i32;
        let second: i32 = (play.1 as u32 - 87) as i32;

        // let my_card = ((first + 2) + (second - 2)) % 3 + 1;
        let my_card = (first + second) % 3 + 1;

        final_sum += (second - 1) * 3 + my_card;
    }

    println!("Final score: {}", final_sum);
}
