use std::io::{BufReader,BufRead};
use std::fs::File;

use std::cmp;

#[derive(Debug)]
struct Position {
    x: i32,
    y: i32,
}

#[derive(Debug)]
struct Line {
    start: Position,
    end: Position,
}

impl Line {
    fn new(start: Position, end: Position) -> Line {
        Line {
            start: start,
            end: end,
        }
    }

    fn get_max_x(&self) -> i32 {
        if self.start.x > self.end.x {
            self.start.x
        } else {
            self.end.x
        }
    }

    fn get_max_y(&self) -> i32 {
        if self.start.y > self.end.y {
            self.start.y
        } else {
            self.end.y
        }
    }

    fn is_straight(&self) -> bool {
        self.start.x == self.end.x || self.start.y == self.end.y
    }
}

fn main() {
    let mut all_lines: Vec<String> = Vec::new();

    let file = File::open("input.txt").unwrap();
    for line in BufReader::new(file).lines() {
        all_lines.push(line.unwrap());
    }
    
    let mut lines: Vec<Line> = Vec::new();
    
    for line in all_lines {
        // split line at ' -> '
        let mut split_line: Vec<&str> = line.split(" -> ").collect();
        let pos_1_vec = split_line[0].split(",").collect::<Vec<&str>>();
        // create a new position from the values in pos_1_vec
        let pos_1 = Position {
            x: pos_1_vec[0].parse::<i32>().unwrap(),
            y: pos_1_vec[1].parse::<i32>().unwrap(),
        };
        let pos_2_vec = split_line[1].split(",").collect::<Vec<&str>>();
        // create a new position from the values in pos_2_vec
        let pos_2 = Position {
            x: pos_2_vec[0].parse::<i32>().unwrap(),
            y: pos_2_vec[1].parse::<i32>().unwrap(),
        };

        let line = Line::new(pos_1, pos_2);

        lines.push(line);
    }

    // _one(&lines);
    _two(&lines);
}


fn _one(lines: &Vec<Line>) {

    let mut max_x = 0;
    let mut max_y = 0;

    for line in lines {
        // If the line is straight, we use it to find the max x and y
        if line.is_straight() {
            max_x = cmp::max(max_x, line.get_max_x());
            max_y = cmp::max(max_y, line.get_max_y());
            println!("{:?} - {:?}", line.start, line.end);
        }
    }

    max_x += 1;
    max_y += 1;

    let mut grid: Vec<Vec<i16>> = Vec::new();
    // Init grid with 0
    for _ in 0..max_y {
        let mut row: Vec<i16> = Vec::new();
        for _ in 0..max_x {
            row.push(0);
        }
        grid.push(row);
    }

    for line in lines {
        if line.is_straight() {
            let start_x = cmp::min(line.start.x,line.end.x);
            let end_x = cmp::max(line.start.x,line.end.x);
            let start_y = cmp::min(line.start.y,line.end.y);
            let end_y = cmp::max(line.start.y,line.end.y);
            for x in start_x..=end_x {
                for y in start_y..=end_y {
                    grid[y as usize][x as usize] += 1;
                }
            }
        }
    }

    // Count all fields where the value is 2 or greater
    let mut count = 0;
    for row in grid {
        count += row.iter().filter(|&x| *x >= 2).count();
    }

    println!("Count: {}", count);

}

fn _two(lines: &Vec<Line>) {
    
    let mut max_x = 0;
    let mut max_y = 0;

    for line in lines {
        // We find the max x and y
        max_x = cmp::max(max_x, line.get_max_x());
        max_y = cmp::max(max_y, line.get_max_y());
    }

    max_x += 1;
    max_y += 1;

    let mut grid: Vec<Vec<i16>> = Vec::new();
    // Init grid with 0
    for _ in 0..max_y {
        let mut row: Vec<i16> = Vec::new();
        for _ in 0..max_x {
            row.push(0);
        }
        grid.push(row);
    }

    for line in lines {
        if line.is_straight() {
            let start_x = cmp::min(line.start.x,line.end.x);
            let end_x = cmp::max(line.start.x,line.end.x);
            let start_y = cmp::min(line.start.y,line.end.y);
            let end_y = cmp::max(line.start.y,line.end.y);
            for x in start_x..=end_x {
                for y in start_y..=end_y {
                    grid[y as usize][x as usize] += 1;
                }
            }
        }
        else{
            let delta_x = (line.end.x - line.start.x).signum();
            let delta_y = (line.end.y - line.start.y).signum();

            for i in 0..((line.end.x - line.start.x).abs() + 1) {
                grid[(line.start.y + i * delta_y) as usize][(line.start.x + i * delta_x) as usize] += 1;
            }
        }
    }

    // pretty_print_grid(&grid);

    // Count all fields where the value is 2 or greater
    let mut count = 0;
    for row in grid {
        count += row.iter().filter(|&x| *x >= 2).count();
    }

    println!("Count: {}", count);

}


fn pretty_print_grid(grid: &Vec<Vec<i16>>) {
    for row in grid {
        for col in row {
            print!("{} ", col);
        }
        println!("");
    }
}