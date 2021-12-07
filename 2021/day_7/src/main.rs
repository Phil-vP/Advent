use std::io::{BufReader,BufRead};
use std::fs::File;


fn main() {
    let mut all_lines: Vec<String> = Vec::new();

    let file = File::open("input.txt").unwrap();
    for line in BufReader::new(file).lines() {
        all_lines.push(line.unwrap());
    }

    let number_list = all_lines[0].split(",").map(|x| x.parse::<i32>().unwrap()).collect::<Vec<i32>>();

    // _one(&number_list);
    _two(&number_list);
}


fn _one(number_list: &Vec<i32>) {
    let mut num_list = number_list.clone();
    num_list.sort();
    println!("num_list: {:?}", num_list);

    let mut min_dev = i32::max_value();
    let mut min_dev_number = 0;
    for i in num_list[0]..=num_list[num_list.len() - 1] {
        let dev = calc_deviation(&num_list, i);
        println!("dev: {}, i: {}", dev, i);
        if dev < min_dev {
            min_dev = calc_deviation(&num_list, i);
            min_dev_number = i;
        }
    }
    println!("min_dev: {}, min_dev_number: {}", min_dev, min_dev_number);
}

fn _two(number_list: &Vec<i32>) {
    let mut num_list = number_list.clone();
    num_list.sort();
    println!("num_list: {:?}", num_list);

    let mut min_dev = i32::max_value();
    let mut min_dev_number = 0;
    for i in num_list[0]..=num_list[num_list.len() - 1] {
        let dev = calc_deviation(&num_list, i);
        println!("dev: {}, i: {}", dev, i);
        if dev < min_dev {
            min_dev = calc_deviation(&num_list, i);
            min_dev_number = i;
        }
    }
    println!("min_dev: {}, min_dev_number: {}", min_dev, min_dev_number);
}

fn calc_deviation(number_list: &Vec<i32>, check_num: i32) -> i32 {
    let mut dev = 0;
    for num in number_list {
        dev += (0..=(num - check_num).abs()).collect::<Vec<i32>>().iter().sum::<i32>();
    }
    dev
}

fn calc_deviation_2(number_list: &Vec<i32>, check_num: i32) -> i32 {
    let mut dev = 0;
    for num in number_list {
        dev += (num - check_num).abs();
    }
    dev
}