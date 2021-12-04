mod types;
use types::BingoField;

use std::io::{BufReader,BufRead};
use std::fs::File;


fn main() {
    let mut all_lines: Vec<String> = Vec::new();

    let file = File::open("input.txt").unwrap();
    for line in BufReader::new(file).lines() {
        all_lines.push(line.unwrap());
    }
    
    // pop first element of all_lines
    let mut lines_iter = all_lines.iter();
    
    // let mut number_list = all_lines.pop().unwrap().split(",").map(|x| x.parse::<i32>().unwrap()).collect::<Vec<i32>>();
    let number_list = lines_iter.next().unwrap().split(",").map(|x| x.parse::<i32>().unwrap()).collect::<Vec<i32>>();

    lines_iter.next();

    let mut field_list: Vec<BingoField> = Vec::new();

    let mut line_list: Vec<Vec<i32>> = Vec::new();

    let mut id_counter = 0;

    for line in lines_iter {
        
        if line.is_empty() {
            field_list.push(BingoField::new(line_list, id_counter));
            id_counter += 1;
            line_list = Vec::new();
            continue;
        }
        
        line_list.push(line.split_whitespace().map(|x| x.parse::<i32>().unwrap()).collect::<Vec<i32>>());
    }
    
    field_list.push(BingoField::new(line_list, id_counter));

    // pretty_print all fields in field_list
    for field in &field_list {
        field.pretty_print();
        println!("");
    }

    // _one(field_list, number_list);
    _two(field_list, number_list);
}


fn _one(bingo_field_list: Vec<BingoField>, number_list: Vec<i32>) {

    let mut field_list = bingo_field_list;

    for number in number_list {
        // iterate over field_list, do method cross_out_number on each field
        println!("\nChecking number {}\n", number);
        for field in &mut field_list {

            field.cross_out_number(number);

            let field_check = field.check_field();
            // field.pretty_print();
            if field_check.1 {
                println!("Bingo field: {}, Number: {}, field sum: {}, mult: {}", field.id, number, field_check.0, number * field_check.0);
                return;
            }
            // println!("");
        }
    }

}

fn _two(bingo_field_list: Vec<BingoField>, number_list: Vec<i32>) {

    let mut field_list = bingo_field_list;
    for number in number_list {
        // iterate over field_list, do method cross_out_number on each field
        println!("\nChecking number {}\n", number);
        let field_list_len = field_list.len();
        let mut remove_list: Vec<i32> = Vec::new();

        for field in &mut field_list {

            field.cross_out_number(number);

            let field_check = field.check_field();
            // field.pretty_print();
            if field_check.1 && (field_list_len - remove_list.len()) == 1{
                println!("Bingo field: {}, Number: {}, field sum: {}, mult: {}", field.id, number, field_check.0, number * field_check.0);
                return;
            }
            else if field_check.1 {
                remove_list.push(field.id);
            }
            // println!("");
        }

        // Remove field from field_list with id in remove_list
        for id in remove_list {
            field_list.retain(|x| x.id != id);
        }
    }
    
}