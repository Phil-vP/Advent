use std::fs::File;
use std::io::{BufRead, BufReader};

mod types;
use types::{Monkey, Operation};

mod types_two;
use types_two::{Monkey as MonkeyTwo, Operation as OperationTwo};

fn main() {
    let mut all_lines: Vec<String> = Vec::new();

    let testing = false;

    let file: File = if testing {
        File::open("test_input.txt").unwrap()
    } else {
        File::open("input.txt").unwrap()
    };

    for line in BufReader::new(file).lines() {
        all_lines.push(line.unwrap());
    }

    let mut monkeys: Vec<Monkey> = Vec::new();
    let mut monkeys_two: Vec<MonkeyTwo> = Vec::new();

    let mut div_value = 1;

    for i in 0..((all_lines.len() + 1) / 7) {
        let current_zero_index = i * 7;
        let list_string = all_lines[current_zero_index + 1].replace("  Starting items: ", "");
        let mut current_list: Vec<i64> = Vec::new();
        println!("{}: {}", i, list_string);
        list_string
            .split(", ")
            .for_each(|x| current_list.push(x.parse::<i64>().unwrap()));

        let operation_split = all_lines[current_zero_index + 2]
            .split(" ")
            .collect::<Vec<&str>>();
        let (op_1, op_2) = match operation_split[operation_split.len() - 2] {
            "+" => (Operation::Add, OperationTwo::Add),
            "*" => (Operation::Multiply, OperationTwo::Multiply),
            _ => panic!("Unknown operation"),
        };
        let mut current_op_value = 0;
        let current_op_on_own_value = match operation_split[operation_split.len() - 1] {
            "old" => true,
            n => {
                current_op_value = n.parse::<i64>().unwrap();
                false
            }
        };

        let modulo_test = all_lines[current_zero_index + 3]
            .split(" ")
            .last()
            .unwrap()
            .parse::<i64>()
            .unwrap();
        div_value *= modulo_test;
        let true_monkey = all_lines[current_zero_index + 4]
            .split(" ")
            .last()
            .unwrap()
            .parse::<usize>()
            .unwrap();
        let false_monkey = all_lines[current_zero_index + 5]
            .split(" ")
            .last()
            .unwrap()
            .parse::<usize>()
            .unwrap();

        monkeys.push(Monkey::new(
            i,
            current_list.clone(),
            modulo_test,
            false_monkey,
            true_monkey,
            op_1,
            current_op_on_own_value,
            current_op_value,
        ));
        monkeys_two.push(MonkeyTwo::new(
            i,
            current_list,
            modulo_test,
            false_monkey,
            true_monkey,
            op_2,
            current_op_on_own_value,
            current_op_value,
        ));
    }
    
    _one(&mut monkeys, 20);
    _two(&mut monkeys_two, div_value, 10000);
}

fn _one(all_monkeys: &mut Vec<Monkey>, number_of_runs: usize) {
    let number_of_monkeys = all_monkeys.len();

    for _ in 0..number_of_runs {

        for i in 0..number_of_monkeys {
            let length = all_monkeys[i].get_item_list_len();
            for _ in 0..length {
                let (new_monkey, new_value) = all_monkeys[i].make_operation();
                all_monkeys[new_monkey].add_item(new_value);
            }
        }

    }

    _print_monkeys(all_monkeys);

    let mut inspection_count_vec: Vec<i64> = all_monkeys
        .iter()
        .map(|x| x.get_inspection_count())
        .collect();
    inspection_count_vec.sort();
    inspection_count_vec.reverse();

    let mut count = 1;
    count *= inspection_count_vec[0];
    count *= inspection_count_vec[1];


    println!("Count: {}", count);
}

fn _two(all_monkeys: &mut Vec<MonkeyTwo>, div_value: i64, number_of_runs: usize) {
    let number_of_monkeys = all_monkeys.len();

    for monkey in all_monkeys.iter_mut() {
        monkey.set_div_value(div_value);
    }

    for _ in 0..number_of_runs {

        for i in 0..number_of_monkeys {
            let length = all_monkeys[i].get_item_list_len();
            for _ in 0..length {
                let (new_monkey, new_value) = all_monkeys[i].make_operation();
                all_monkeys[new_monkey].add_item(new_value);
            }
        }

    }

    _print_monkeys_two(all_monkeys);

    let mut inspection_count_vec: Vec<i64> = all_monkeys
        .iter()
        .map(|x| x.get_inspection_count())
        .collect();
    inspection_count_vec.sort();
    inspection_count_vec.reverse();

    let mut count = 1;
    count *= inspection_count_vec[0];
    count *= inspection_count_vec[1];


    println!("Count: {}", count);
}

fn _print_monkeys(all_monkeys: &Vec<Monkey>) {
    for monkey in all_monkeys.iter() {
        println!("Monkey {}:", monkey.get_id());
        println!("    Inspection count: {}", monkey.get_inspection_count());
        // println!("    Item list: {:?}\n", monkey.get_item_list());
    }
}

fn _print_monkeys_two(all_monkeys: &Vec<MonkeyTwo>) {
    for monkey in all_monkeys.iter() {
        println!("Monkey {}:", monkey.get_id());
        println!("    Inspection count: {}", monkey.get_inspection_count());
        // println!("    Item list: {:?}\n", monkey.get_item_list());
    }
}