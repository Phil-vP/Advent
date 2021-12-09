use std::io::{BufReader,BufRead};
use std::fs::File;


fn main() {
    let mut input_field: Vec<Vec<i16>> = Vec::new();

    let file = File::open("input.txt").unwrap();
    for line in BufReader::new(file).lines() {
        let mut input_field_line: Vec<i16> = Vec::new();
            for c in line.unwrap().chars() {
                input_field_line.push(c.to_digit(10).unwrap() as i16);
            }
            // println!("{:?}", input_field_line);
            input_field.push(input_field_line);
    }

    // _one(&input_field);
    _two(&input_field);
}


fn _one(input_field: &Vec<Vec<i16>>) {

    let low_points: Vec<(i16, i16)> = find_low_points(input_field);

    let mut counter = 0;

    for point in low_points {
        counter += input_field[point.0 as usize][point.1 as usize] + 1;
    }

    println!("{}", counter);
}

fn _two(input_field: &Vec<Vec<i16>>) {
    // Get the low points
    let low_points: Vec<(i16, i16)> = find_low_points(input_field);

    let mut basins: Vec<i16> = Vec::new();

    // Just for visualization
    let mut vis = vec![vec!['#'; input_field[0].len()]; input_field.len()];

    // To find the basins, we have to spread out from the low points
    // We will use a queue to do this
    for point in low_points {
        let mut queue: Vec<(i16, i16)> = Vec::new();
        queue.push(point);
        let mut visited: Vec<(i16, i16)> = Vec::new();
        visited.push(point);

        while queue.len() > 0 {
            let current_point = queue.pop().unwrap();

            // Top
            if current_point.0 > 0 {
                let top = (current_point.0 - 1, current_point.1);
                if !visited.contains(&top) && input_field[top.0 as usize][top.1 as usize] != 9 {
                    queue.push(top);
                    visited.push(top);
                }
            }
            
            // Bottom
            if current_point.0 < input_field.len() as i16 - 1 {
                let bottom = (current_point.0 + 1, current_point.1);
                if !visited.contains(&bottom) && input_field[bottom.0 as usize][bottom.1 as usize] != 9 {
                    queue.push(bottom);
                    visited.push(bottom);
                }
            }

            // Left
            if current_point.1 > 0 {
                let left = (current_point.0, current_point.1 - 1);
                if !visited.contains(&left) && input_field[left.0 as usize][left.1 as usize] != 9 {
                    queue.push(left);
                    visited.push(left);
                }
            }

            // Right
            if current_point.1 < input_field[0].len() as i16 - 1 {
                let right = (current_point.0, current_point.1 + 1);
                if !visited.contains(&right) && input_field[right.0 as usize][right.1 as usize] != 9 {
                    queue.push(right);
                    visited.push(right);
                }
            }
        }
        
        basins.push(visited.len() as i16);

        for point in visited {
            vis[point.0 as usize][point.1 as usize] = '.';
        }
    }

    // Print every line in vis
    for line in vis {
        for c in line {
            print!("{}", c);
        }
        println!("");
    }

    // Sort the basins by size in descending order
    basins.sort_by(|a, b| b.cmp(a));

    // Multiply the sizes of the three largest basins
    let mut result: i32 = 1;
    for i in 0..3 {
        result *= basins[i] as i32;
    }

    println!("{}", result);
    
}

fn find_low_points(input_field: &Vec<Vec<i16>>) -> Vec<(i16, i16)> {
    let mut low_points: Vec<(i16, i16)> = Vec::new();
    for row in 0..input_field.len() {
        for col in 0..input_field[row].len() {
            let num = input_field[row][col];
            let mut smaller = true;

            // Is above smaller?
            smaller &= if row >= 1 {
                if input_field[row-1][col] > num {
                    true
                } else {
                    false
                }
            }
            else {
                true
            };

            // Is below smaller?
            smaller &= if row < input_field.len()-1 {
                if input_field[row+1][col] > num {
                    true
                } else {
                    false
                }
            }
            else {
                true
            };

            // Is left smaller?
            smaller &= if col >= 1 {
                if input_field[row][col-1] > num {
                    true
                } else {
                    false
                }
            }
            else {
                true
            };

            // Is right smaller?
            smaller &= if col < input_field[row].len()-1 {
                if input_field[row][col+1] > num {
                    true
                } else {
                    false
                }
            }
            else {
                true
            };

            if smaller {
                low_points.push((row as i16, col as i16));
            }
        }
    }
    low_points
}