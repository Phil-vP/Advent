use std::io::{BufReader,BufRead};
use std::fs::File;
use std::collections::HashMap;

#[derive(Debug, Hash, PartialEq, Clone)]
enum Heading {
    Up,
    Down,
    Left,
    Right
}
impl Eq for Heading {}

fn main() {
    let mut all_lines: Vec<String> = Vec::new();

    let file = File::open("input.txt").unwrap();
    for line in BufReader::new(file).lines() {
        all_lines.push(line.unwrap());
    }

    let mut grid: Vec<Vec<i16>> = Vec::new();

    for line in all_lines {
        // Parse line to Vec of integers
        let mut line_vec: Vec<i16> = Vec::new();
        for c in line.chars() {
            line_vec.push(c.to_digit(10).unwrap() as i16);
        }
        grid.push(line_vec);
    }

    // _one(&grid);
    _two(&grid);
}


fn _one(grid: &Vec<Vec<i16>>) {
    make_dijkstra(grid);
}

fn _two(grid: &Vec<Vec<i16>>) {
    let mut full_grid_line: Vec<Vec<i16>> = Vec::new();

    for row in grid {
        let mut append_row: Vec<i16>  = Vec::new();
        for i in 0..5 {
            let added_row: Vec<i16> = row.iter().map(|x| (x + i - 1) % 9 + 1).collect();
            append_row.extend(added_row);
        }
        full_grid_line.push(append_row);
    }

    let mut full_grid: Vec<Vec<i16>> = Vec::new();

    for i in 0..5 {
        full_grid.extend(full_grid_line.iter().map(|x| x.iter().map(|y| (y + i - 1) % 9 + 1).collect()));
    }

    make_dijkstra(&full_grid);
}

fn make_dijkstra(grid: &Vec<Vec<i16>>) {
    


    // Positions are given as (row, col)

    let mut delta_headings: HashMap<Heading, (i16, i16)> = HashMap::new();
    delta_headings.insert(Heading::Up, (-1, 0));
    delta_headings.insert(Heading::Down, (1, 0));
    delta_headings.insert(Heading::Left, (0, -1));
    delta_headings.insert(Heading::Right, (0, 1));

    let mut distance_grid: Vec<Vec<(bool, i16)>> = vec![vec![ (false, std::i16::MAX); grid[0].len()]; grid.len()];

    distance_grid[0][0] = (true, 0);

    let mut current_position: (i16, i16) = (0,0);
    let final_position = ((grid.len()-1) as i16, (grid[0].len()-1) as i16);

    // (distance, position.x, position.y)
    let mut queue: Vec<(i16, i16, i16)> = Vec::new();
    let mut queue_map: HashMap<(i16, i16), i16> = HashMap::new();
    queue_map.insert(current_position, 0);

    queue.push((0, current_position.0, current_position.1));

    while current_position != final_position {
        queue.sort_by(|a, b| a.0.cmp(&b.0));
        
        if queue.len() == 0 {
            break;
        }

        // Find the entry in queue_map with the smallest distance
        let mut smallest_pos: (i16, i16) = (std::i16::MAX, std::i16::MAX);
        let mut smallest_distance: i16 = std::i16::MAX;
        for (pos, dist) in queue_map.iter() {
            if *dist < smallest_distance {
                smallest_pos = *pos;
                smallest_distance = *dist;
            }
        }

        // Remove the entry from queue_map
        queue_map.remove(&smallest_pos);

        current_position = smallest_pos;
        let current_distance = smallest_distance;
        distance_grid[current_position.0 as usize][current_position.1 as usize] = (true, current_distance);

        for (_, delta) in &delta_headings {
            let new_position = (current_position.0 + delta.0, current_position.1 + delta.1);
            // If this were to go out of the grid, we can skip it
            if new_position.0 < 0 || new_position.1 < 0 || new_position.0 >= grid.len() as i16 || new_position.1 >= grid[0].len() as i16 {
                continue;
            }
            // If this has already been visited, we can skip it
            if distance_grid[new_position.0 as usize][new_position.1 as usize].0 {
                continue;
            }

            let new_distance = current_distance + grid[new_position.0 as usize][new_position.1 as usize];

            // Else, we can add it to the queue
            if queue_map.contains_key(&new_position) {
                if queue_map[&new_position] > new_distance {
                    queue_map.remove(&new_position);
                    queue_map.insert(new_position, new_distance);
                }
            } else {
                queue_map.insert(new_position, new_distance);
            }
        }
    }

    println!("Final distance: {}", distance_grid[distance_grid.len() - 1 as usize][distance_grid[0].len() - 1 as usize].1);
}