use std::io::{BufReader,BufRead};
use std::fs::File;

use std::cmp;


fn main() {
    let mut all_lines: Vec<String> = Vec::new();

    let file = File::open("input.txt").unwrap();
    for line in BufReader::new(file).lines() {
        all_lines.push(line.unwrap());
    }

    let mut line_iter = all_lines.iter();

    let grid: Vec<Vec<bool>> = Vec::new();

    let mut coordinates: Vec<(i16, i16)> = Vec::new();

    let mut max_x = 0;
    let mut max_y = 0;

    while line_iter.len() > 0 {
        let line = line_iter.next().unwrap();
        if line.is_empty() {
            break;
        }

        let tuple_vec = line.split(",").map(|x| x.parse::<i16>().unwrap()).collect::<Vec<i16>>();
        coordinates.push((tuple_vec[0], tuple_vec[1]));

        max_x = max_x.max(tuple_vec[0]);
        max_y = max_y.max(tuple_vec[1]);
    }

    let commands: Vec<&String> = line_iter.collect();

    let mut grid: Vec<Vec<bool>> = vec![vec![false; max_x as usize + 1]; max_y as usize + 1];

    for i in 0..coordinates.len() {
        let (x, y) = coordinates[i];
        grid[y as usize][x as usize] = true;
    }

    // _one(&grid, &commands);
    _two(&grid, &commands);
}


fn _one(grid: &Vec<Vec<bool>>, commands: &Vec<&String>) {
    
    let first_command = commands[0];
    let new_grid = fold(&grid, first_command);

    pretty_print_grid(&new_grid);

    println!("{}", count_in_grid(&new_grid));
}

fn _two(grid: &Vec<Vec<bool>>, commands: &Vec<&String>) {
    
    let mut grid = grid.clone();
    for command in commands {
        grid = fold(&grid, command);
    }

    pretty_print_grid(&grid);
}

fn pretty_print_grid(grid: &Vec<Vec<bool>>) {
    for row in grid {
        for cell in row {
            if *cell {
                print!("#");
            } else {
                print!(" ");
            }
        }
        println!("");
    }
}

fn fold(grid: &Vec<Vec<bool>>, command: &String) -> Vec<Vec<bool>> {
    let split_command = command.split(" ");
    let relevant = split_command.last().unwrap();
    let relevant_split = relevant.split("=").collect::<Vec<&str>>();

    let direction = relevant_split[0];
    let value = relevant_split[1].parse::<i16>().unwrap() as usize;

    let mut new_grid: Vec<Vec<bool>> = Vec::new();

    if direction == "y" {
        let limit = cmp::max(grid.len() - value - 1, value) as usize;
        for i in 1..=limit {
            let mut grid_line: Vec<bool> = Vec::new();
            for j in 0..grid[0].len() {
                let top_y = value - i;
                let bot_y = value + i;
                let top_value = if top_y >= 0 {
                    grid[top_y][j]
                } else {
                    false
                };
                let bot_value = if bot_y < grid.len() {
                    grid[bot_y][j]
                } else {
                    false
                };
                grid_line.push(top_value || bot_value);
            }
            new_grid.push(grid_line);
        }
        new_grid.reverse();
    }
    else{
        let limit = cmp::max(grid[0].len() - value - 1, value) as usize;
        for i in 0..grid.len() {
            let mut grid_line: Vec<bool> = Vec::new();
            for j in 1..=limit {
                let left_x = value - j;
                let right_x = value + j;
                let left_value = if left_x >= 0 {
                    grid[i][left_x]
                } else {
                    false
                };
                let right_value = if right_x < grid[0].len() {
                    grid[i][right_x]
                } else {
                    false
                };
                grid_line.push(left_value || right_value);
            }
            grid_line.reverse();
            new_grid.push(grid_line);
        }
    }

    new_grid

}

fn count_in_grid(grid: &Vec<Vec<bool>>) -> i16 {
    let mut count = 0;
    for row in grid {
        for cell in row {
            if *cell {
                count += 1;
            }
        }
    }
    count
}