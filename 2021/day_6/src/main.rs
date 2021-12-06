use std::io::{BufReader,BufRead};
use std::fs::File;


fn main() {
    let mut all_lines: Vec<String> = Vec::new();

    let file = File::open("input.txt").unwrap();
    for line in BufReader::new(file).lines() {
        all_lines.push(line.unwrap());
    }

    let num_vec = all_lines[0].split(",").map(|x| x.parse::<i16>().unwrap()).collect::<Vec<i16>>();

    // _one(num_vec.clone());
    _two(num_vec.clone());
}


fn _one(mut num_vec: Vec<i16>) {
    let mut num_zeroes = 0;
    for i in 1..=80 {
        // Replace the zeroes in num_vec with 7s
        for j in 0..num_vec.len() {
            if num_vec[j] == 0 {
                num_vec[j] = 7;
            }
        }
        // Decrease the value of every element by 1
        num_vec.iter_mut().for_each(|x| *x -= 1);
        // Add the new elements to the list
        num_vec.extend(vec![8; num_zeroes]);
        
        println!("After {:2} days: {:4} elements", i, num_vec.len());
        
        // count the number of zeroes in the list
        num_zeroes = num_vec.iter().filter(|x| **x == 0).count();
    }
}

fn _two(num_vec: Vec<i16>) {
    let mut numbers: Vec<i64> = vec![0; 9];
    for num in num_vec {
        numbers[num as usize] += 1;
    }

    println!("Initial: {:?}", numbers);

    for i in 1..=256 {
        let x = numbers.remove(0);
        numbers[6] += x;
        numbers.push(x);
        println!("After {:2} days: {:?}", i, numbers);
    }

    let sum: i64 = numbers.iter().sum();
    println!("Final: {}", sum);

    println!("{:?}", numbers);
}