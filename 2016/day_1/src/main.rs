use std::io::{BufReader,BufRead};
use std::fs::File;

#[derive(Debug, Eq, PartialEq, Copy, Clone)]
enum Direction {
    North,
    East,
    South,
    West,
}


fn main() {
    // one();
    two();
}


fn one() {
    let mut all_lines: Vec<String> = Vec::new();

    let file = File::open("input.txt").unwrap();
    for line in BufReader::new(file).lines() {
        all_lines.push(line.unwrap());
    }

    let input_line = all_lines.get(0).unwrap().to_string();

    let input_split = input_line.split(", ").collect::<Vec<&str>>();

    let mut current_direction = Direction::North;
    let mut d_x = 0;
    let mut d_y = 1;

    let mut pos_x = 0;
    let mut pos_y = 0;

    for operation in input_split {
        let mut chars = operation.chars();
        let turn_direction = chars.nth(0).unwrap();
        let number = chars.as_str().parse::<i32>().unwrap();

        let action_tuple = action(current_direction, turn_direction);
        current_direction = action_tuple.0;
        d_x = action_tuple.1;
        d_y = action_tuple.2;

        pos_x += d_x * number;
        pos_y += d_y * number;
    }

    let final_distance = pos_x + pos_y;

    println!("Final position:\nX: {}\nY: {}", pos_x, pos_y);
    println!("Distance: {}", final_distance);
}

fn two() {
    let mut all_lines: Vec<String> = Vec::new();

    let file = File::open("input.txt").unwrap();
    for line in BufReader::new(file).lines() {
        all_lines.push(line.unwrap());
    }

    let input_line = all_lines.get(0).unwrap().to_string();

    let input_split = input_line.split(", ").collect::<Vec<&str>>();

    let mut current_direction = Direction::North;
    let mut d_x;
    let mut d_y;

    let mut pos_x: i32 = 0;
    let mut pos_y: i32 = 0;

    let mut visited: Vec<(i32, i32)> = Vec::new();

    'main_loop: for operation in input_split {
        let mut chars = operation.chars();
        let turn_direction = chars.nth(0).unwrap();
        let number = chars.as_str().parse::<i32>().unwrap();
        
        println!("{}", operation);
        println!("Position: {:?}, facing {:?}", (pos_x, pos_y), current_direction);

        let action_tuple = action(current_direction, turn_direction);
        current_direction = action_tuple.0;
        d_x = action_tuple.1;
        d_y = action_tuple.2;
        
        println!("Turning {}, walking {} steps to the {:?}",turn_direction, number, current_direction);

        for _i in 1..=number {
            pos_x += d_x;
            pos_y += d_y;

            let position = (pos_x, pos_y);

            if visited.contains(&position) {
                println!("Found it!");
                break 'main_loop
            }
            else{
                println!("Not in visited, appending\n");
                visited.push(position);
            }
        }
    }

    let final_distance = pos_x + pos_y;

    println!("Final position:\nX: {}\nY: {}", pos_x, pos_y);
    println!("Distance: {}", final_distance);
}

fn action(current_dir: Direction, turn: char) -> (Direction, i32, i32) {
    let dir_vector = vec![Direction::North, Direction::East, Direction::South, Direction::West];
    let current_index = dir_vector.iter().position(|&x| x == current_dir).unwrap() as i32;

    let new_index = (current_index +
    match turn {
        'R' => 1,
        'L' => -1,
        _ => 0,
    } + 4) % 4;

    let new_direction = dir_vector[new_index as usize];

    match new_direction {
        Direction::North => (Direction::North, 0, 1),
        Direction::East => (Direction::East, 1, 0),
        Direction::South => (Direction::South, 0, -1),
        Direction::West => (Direction::West, -1, 0),
    }

}