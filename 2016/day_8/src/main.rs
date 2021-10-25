use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let mut all_lines: Vec<String> = Vec::new();

    let file = File::open("input.txt").unwrap();
    for line in BufReader::new(file).lines() {
        all_lines.push(line.unwrap());
    }

    _solve(&all_lines);
}

fn _solve(all_lines: &Vec<String>) {

    let mut display = [[false; 50]; 6];
    
    for line in all_lines {
        let mut split = line.split_ascii_whitespace();
        let command = split.next().unwrap();

        match command {
            "rect" => {
                let mut dim = split.next().unwrap().split('x');
                let x_dim = dim.next().unwrap().parse::<usize>().unwrap();
                let y_dim = dim.next_back().unwrap().parse::<usize>().unwrap();
                make_rect(&mut display, x_dim, y_dim);
            }
            "rotate" => {
                let col_or_row = split.next().unwrap();
                let amount = split.next_back().unwrap().parse::<usize>().unwrap();
                let row_col_num = split.next().unwrap().split('=').next_back().unwrap().parse::<usize>().unwrap();
                match col_or_row {
                    "column" => rotate_col(&mut display, row_col_num, amount),
                    "row" => rotate_row(&mut display, row_col_num, amount),
                    _ => continue
                }
            }
            _ => continue
        }
    }

    let counter = show_display(display);
    print!("Counter: {}", counter);

}

fn rotate_col(display: &mut [[bool; 50]; 6], col_num: usize, amount: usize) {
    let mut col = [false; 6];
    for i_row in 0..6 {
        col[i_row] = display[i_row][col_num];
    }

    col.rotate_right(amount);
    
    for i_row in 0..6 {
        display[i_row][col_num] = col[i_row];
    }
}

fn rotate_row(display: &mut [[bool; 50]; 6], row_num: usize, amount: usize) {
    let mut row = display[row_num];
    
    row.rotate_right(amount);
    
    for i_col in 0..50 {
        display[row_num][i_col] = row[i_col];
    }
}

fn make_rect(display: &mut [[bool; 50]; 6], x: usize, y: usize) {
    for i_x in 0..x {
        for i_y in 0..y {
            display[i_y][i_x] = true;
        }
    }
}

fn show_display(display: [[bool; 50]; 6]) -> i32 {
    let mut counter = 0;
    for line in display {
        for c in line {
            print!(
                "{}",
                match (c) {
                    true => {
                        counter += 1;
                        '#'
                    },
                    false => '.',
                }
            );
        }
        print!("\n");
    }
    print!("\n");

    counter
}
