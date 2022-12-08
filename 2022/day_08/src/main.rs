use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let mut array: Vec<Vec<i16>> = Vec::new();

    let testing = false;

    let file: File = if testing {
        File::open("test_input.txt").unwrap()
    } else {
        File::open("input.txt").unwrap()
    };

    for line in BufReader::new(file).lines() {
        array.push(
            line.unwrap()
                .chars()
                .map(|x| x.to_digit(10).unwrap() as i16)
                .collect(),
        );
    }

    // _one(array);
    // _two(array);
}

fn _one(array: Vec<Vec<i16>>) {
    let mut trees_visible: Vec<String> = Vec::new();

    let col_length: usize = array[0].len();
    let row_length: usize = array.len();

    for row_num in 0..row_length {
        let mut max_height_looking_from_left = -1;
        let mut current_height_looking_from_left;

        let mut max_height_looking_from_right = -1;
        let mut current_height_looking_from_right;

        let row = &array[row_num];

        for col_num in 0..col_length {
            // Looking from left to right
            current_height_looking_from_left = row[col_num];
            if current_height_looking_from_left > max_height_looking_from_left {
                max_height_looking_from_left = current_height_looking_from_left;
                let id: String = format!("{}-{}", row_num, col_num);
                if !trees_visible.contains(&id) {
                    trees_visible.push(id);
                }
            }
            // Looking from right to left
            current_height_looking_from_right = row[col_length - col_num - 1];
            if current_height_looking_from_right > max_height_looking_from_right {
                max_height_looking_from_right = current_height_looking_from_right;
                let id: String = format!("{}-{}", row_num, col_length - col_num - 1);
                if !trees_visible.contains(&id) {
                    trees_visible.push(id);
                }
            }
        }
    }

    for col_num in 0..col_length {
        let mut max_height_looking_from_top = -1;
        let mut current_height_looking_from_top;

        let mut max_height_looking_from_bottom = -1;
        let mut current_height_looking_from_bottom;

        for row_num in 0..row_length {
            // Looking from top to bottom
            current_height_looking_from_top = array[row_num][col_num];
            if current_height_looking_from_top > max_height_looking_from_top {
                max_height_looking_from_top = current_height_looking_from_top;
                let id: String = format!("{}-{}", row_num, col_num);
                if !trees_visible.contains(&id) {
                    trees_visible.push(id);
                }
            }
            // Looking from bottom to top
            current_height_looking_from_bottom = array[row_length - row_num - 1][col_num];
            if current_height_looking_from_bottom > max_height_looking_from_bottom {
                max_height_looking_from_bottom = current_height_looking_from_bottom;
                let id: String = format!("{}-{}", row_length - row_num - 1, col_num);
                if !trees_visible.contains(&id) {
                    trees_visible.push(id);
                }
            }
        }
    }

    println!("Trees visible: {}", trees_visible.len());
}

fn _two(array: Vec<Vec<i16>>) {
    let mut max_scenic_score: i32 = 0;
    let mut max_scenic_id: (usize, usize) = (0, 0);
    let col_length: usize = array[0].len();
    let row_length: usize = array.len();

    for row_num in 0..row_length {
        for col_num in 0..col_length {
            let current_scenic_id = (row_num, col_num);
            let current_scenic_score = _get_scenic_score(&array, current_scenic_id);
            if current_scenic_score > max_scenic_score {
                max_scenic_score = current_scenic_score;
                max_scenic_id = current_scenic_id;
            }
        }
    }

    println!(
        "Max scenic score: {} at {:?}",
        max_scenic_score, max_scenic_id
    );
}

fn _get_scenic_score(array: &Vec<Vec<i16>>, id: (usize, usize)) -> i32 {
    let mut scenic_score_left: i32 = 0;
    let mut scenic_score_right: i32 = 0;
    let mut scenic_score_top: i32 = 0;
    let mut scenic_score_bottom: i32 = 0;
    let row_num: usize = id.0;
    let col_num: usize = id.1;
    let current_height: i16 = array[row_num][col_num];
    let row_length: usize = array.len();
    let col_length: usize = array[0].len();

    // Check left
    for i in (0..col_num).rev() {
        scenic_score_left += 1;
        if array[row_num][i] >= current_height {
            break;
        }
    }
    // Check right
    for i in (col_num + 1)..col_length {
        scenic_score_right += 1;
        if array[row_num][i] >= current_height {
            break;
        }
    }
    // Check top
    for i in (0..row_num).rev() {
        scenic_score_top += 1;
        if array[i][col_num] >= current_height {
            break;
        }
    }
    // Check bottom
    for i in (row_num + 1)..row_length {
        scenic_score_bottom += 1;
        if array[i][col_num] >= current_height {
            break;
        }
    }

    scenic_score_left * scenic_score_right * scenic_score_top * scenic_score_bottom
}
