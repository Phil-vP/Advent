use std::io::{BufReader,BufRead};
use std::fs::File;
use std::cmp;

fn main() {
    let mut all_lines: Vec<String> = Vec::new();

    let file = File::open("input.txt").unwrap();
    for line in BufReader::new(file).lines() {
        all_lines.push(line.unwrap());
    }

    // one(&all_lines);
    two(&all_lines);
}


fn one(all_lines: &Vec<String>) {
    let mut row = 2;
    let mut col = 2;

    for line in all_lines {
        let mut chars = line.chars();
        for c in chars {
            match c {
                'U' => row = 1.max(row - 1),
                'D' => row = 3.min(row + 1),
                'L' => col = 1.max(col - 1),
                'R' => col = 3.min(col + 1),
                _ => println!("Error"),
            };
        }
        let number = (row - 1) * 3 + col;
        print!("{}", number);
    }
}

fn two(all_lines: &Vec<String>) {
    let mut row: i32 = 3;
    let mut col: i32 = 1;

    let num_vec = vec![
        vec![0, 0, 49, 0, 0],
        vec![0, 50, 51, 52, 0],
        vec![53, 54, 55, 56, 57],
        vec![0, 65, 66, 67, 0],
        vec![0, 0, 68, 0, 0],
    ];

    for line in all_lines {
        let mut chars = line.chars();
        for c in chars {
            let min_row = 1 + (3 - col).abs();
            let max_row = 5 - (3 - col).abs();
            let min_col = 1 + (3 - row).abs();
            let max_col = 5 - (3 - row).abs();
            // println!("Row: {}, Col: {}\nc: {}", row, col, c);
            // println!("min/max col: {}, {}\nmin/max row: {}, {}", min_col, max_col, min_row, max_row);
            match c {
                'U' => row = min_row.max(row - 1),
                'D' => row = max_row.min(row + 1),
                'L' => col = min_col.max(col - 1),
                'R' => col = max_col.min(col + 1),
                _ => println!("Error"),
            };
            // println!("Row: {}, Col: {}\n", row, col);
        }
        let number_ascii: u8 = num_vec[(row - 1) as usize][(col - 1) as usize];
        print!("{}", number_ascii as char);
    }
}