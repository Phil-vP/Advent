use std::io::{BufReader,BufRead};
use std::fs::File;


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
    // Parse all_lines into a 2D-vec of numbers
    let mut grid: Vec<Vec<i32>> = Vec::new();
    for line in all_lines {
        let mut row: Vec<i32> = Vec::new();
        for num in line.chars() {
            row.push(num.to_digit(10).unwrap() as i32);
        }
        grid.push(row);
    }

    let row_length = grid[0].len();
    let number_rows = grid.len();

    let mut number_flashes = 0;

    for i in 1..=100 {
        let mut add_vec: Vec<Vec<(bool, i32)>> = vec![vec![(false, 1); row_length]; number_rows];
        let mut flashed = true;

        while flashed {
            flashed = false;
            for row in 0..number_rows {
                for col in 0..row_length {
                    // If this octopus already flashed, we can skip it
                    if add_vec[row][col].0 {
                        continue;
                    }
                    // Check if this octopus needs to flash this iteration
                    let mut sum = 0;
                    sum += grid[row][col];
                    sum += add_vec[row][col].1;

                    // If not, we can continue
                    if sum <= 9 {
                        continue;
                    }
                    else{
                        // If yes, this octopus flashes and sets the flash value to true to keep this iteration going
                        flashed = true;
                        add_vec[row][col].0 = true;
                        let row_gt_zero = row > 0;
                        let row_lt_max = row < number_rows - 1;
                        let col_gt_zero = col > 0;
                        let col_lt_max = col < row_length - 1;

                        // First, add to the four adjacent octopuses
                        if row_gt_zero {
                            add_vec[row - 1][col].1 += 1;
                        }
                        if row_lt_max {
                            add_vec[row + 1][col].1 += 1;
                        }
                        if col_gt_zero {
                            add_vec[row][col - 1].1 += 1;
                        }
                        if col_lt_max {
                            add_vec[row][col + 1].1 += 1;
                        }

                        // Then, add to the four diagonals
                        if row_gt_zero && col_gt_zero {
                            add_vec[row - 1][col - 1].1 += 1;
                        }
                        if row_gt_zero && col_lt_max {
                            add_vec[row - 1][col + 1].1 += 1;
                        }
                        if row_lt_max && col_gt_zero {
                            add_vec[row + 1][col - 1].1 += 1;
                        }
                        if row_lt_max && col_lt_max {
                            add_vec[row + 1][col + 1].1 += 1;
                        }
                    }
                }
            }
        }
        for row in 0..number_rows {
            for col in 0..row_length {
                if add_vec[row][col].0 {
                    grid[row][col] = 0;
                    number_flashes += 1;
                }
                else{
                    grid[row][col] += add_vec[row][col].1;
                }
            }
        }
    
        // Print grid
        if i % 10 == 0 {
            println!("\nAfter step {}, {} flashes:", i, number_flashes);
            pretty_print_octupus_grid(&add_vec);
        }
    }
}

fn _two(all_lines: &Vec<String>) {
    // Parse all_lines into a 2D-vec of numbers
    let mut grid: Vec<Vec<i32>> = Vec::new();
    for line in all_lines {
        let mut row: Vec<i32> = Vec::new();
        for num in line.chars() {
            row.push(num.to_digit(10).unwrap() as i32);
        }
        grid.push(row);
    }

    let row_length = grid[0].len();
    let number_rows = grid.len();


    let mut all_flashed = false;
    let mut iteration = 0;

    while !all_flashed {
        let mut add_vec: Vec<Vec<(bool, i32)>> = vec![vec![(false, 1); row_length]; number_rows];
        let mut flashed = true;

        while flashed {
            flashed = false;
            for row in 0..number_rows {
                for col in 0..row_length {
                    // If this octopus already flashed, we can skip it
                    if add_vec[row][col].0 {
                        continue;
                    }
                    // Check if this octopus needs to flash this iteration
                    let mut sum = 0;
                    sum += grid[row][col];
                    sum += add_vec[row][col].1;

                    // If not, we can continue
                    if sum <= 9 {
                        continue;
                    }
                    else{
                        // If yes, this octopus flashes and sets the flash value to true to keep this iteration going
                        flashed = true;
                        add_vec[row][col].0 = true;
                        let row_gt_zero = row > 0;
                        let row_lt_max = row < number_rows - 1;
                        let col_gt_zero = col > 0;
                        let col_lt_max = col < row_length - 1;

                        // First, add to the four adjacent octopuses
                        if row_gt_zero {
                            add_vec[row - 1][col].1 += 1;
                        }
                        if row_lt_max {
                            add_vec[row + 1][col].1 += 1;
                        }
                        if col_gt_zero {
                            add_vec[row][col - 1].1 += 1;
                        }
                        if col_lt_max {
                            add_vec[row][col + 1].1 += 1;
                        }

                        // Then, add to the four diagonals
                        if row_gt_zero && col_gt_zero {
                            add_vec[row - 1][col - 1].1 += 1;
                        }
                        if row_gt_zero && col_lt_max {
                            add_vec[row - 1][col + 1].1 += 1;
                        }
                        if row_lt_max && col_gt_zero {
                            add_vec[row + 1][col - 1].1 += 1;
                        }
                        if row_lt_max && col_lt_max {
                            add_vec[row + 1][col + 1].1 += 1;
                        }
                    }
                }
            }
        }
        
        let mut number_flashes = 0;
        for row in 0..number_rows {
            for col in 0..row_length {
                if add_vec[row][col].0 {
                    grid[row][col] = 0;
                    number_flashes += 1;
                }
                else{
                    grid[row][col] += add_vec[row][col].1;
                }
            }
        }

        iteration += 1;

        if number_flashes == row_length * number_rows {
            all_flashed = true;
        }
    
    }
    // Print grid
    println!("\nAfter step {}, all flashed", iteration);
}

fn pretty_print_octupus_grid(grid: &Vec<Vec<(bool, i32)>>) {
    for row in grid {
        for num in row {
            let char = if num.0 {
                '#'
            }
            else{
                '.'
            };
            print!("{}", char);
        }
        println!();
    }
}