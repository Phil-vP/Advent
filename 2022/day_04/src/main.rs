use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let mut all_ranges: Vec<((u32, u32), (u32, u32))> = Vec::new();

    let testing = false;

    let file: File = if testing {
        File::open("test_input.txt").unwrap()
    } else {
        File::open("input.txt").unwrap()
    };

    for line in BufReader::new(file).lines() {
        // Parse line in format a-b,x-y into ((a,b),(x,y))
        let line = line.unwrap();
        let mut split = line.split(",");
        let mut range1_str = split.next().unwrap().split("-");
        let mut range2_str = split.next().unwrap().split("-");
        let range1 = (
            range1_str.next().unwrap().parse::<u32>().unwrap(),
            range1_str.next().unwrap().parse::<u32>().unwrap(),
        );
        let range2 = (
            range2_str.next().unwrap().parse::<u32>().unwrap(),
            range2_str.next().unwrap().parse::<u32>().unwrap(),
        );
        all_ranges.push((range1, range2));
    }

    // _one(&all_ranges);
    _two(&all_ranges);
}

fn _one(all_ranges: &Vec<((u32, u32), (u32, u32))>) {
    let mut counter = 0;
    for line in all_ranges {
        if _overlaps_1(line.0, line.1) {
            counter += 1;
        }
    }
    println!("Overlapping lines: {}", counter);
}

fn _two(all_ranges: &Vec<((u32, u32), (u32, u32))>) {
    let mut counter = 0;
    for line in all_ranges {
        if _overlaps_2(line.0, line.1) {
            counter += 1;
        }
    }
    println!("Overlapping lines: {}", counter);
}

fn _overlaps_1(range1: (u32, u32), range2: (u32, u32)) -> bool {
    if range1.0 == range2.0 || range1.1 == range2.1 {
        return true;
    } else if range1.0 < range2.0 {
        range1.1 >= range2.1
    } else {
        range2.1 >= range1.1
    }
}

fn _overlaps_2(range1: (u32, u32), range2: (u32, u32)) -> bool {
    if range1.0 < range2.0 {
        range1.1 >= range2.0
    } else if range2.0 < range1.0 {
        range2.1 >= range1.0
    } else {
        _overlaps_1(range1, range2)
    }
}

fn _print_range(range1: (u32, u32), range2: (u32, u32)) {
    let mut line_1 = String::new();
    let mut line_2 = String::new();
    for _ in 0..range1.0 {
        line_1.push_str(".");
    }
    for _ in range1.0..=range1.1 {
        line_1.push_str("#");
    }
    for _ in range1.1..100 {
        line_1.push_str(".");
    }
    for _ in 0..range2.0 {
        line_2.push_str(".");
    }
    for _ in range2.0..=range2.1 {
        line_2.push_str("#");
    }
    for _ in range2.1..100 {
        line_2.push_str(".");
    }
    println!("{}", line_1);
    println!("{}", line_2);
    println!();
}
