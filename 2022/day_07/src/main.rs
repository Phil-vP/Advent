use std::cell::RefCell;
use std::fs::File;
use std::io::{BufRead, BufReader};
use std::rc::Rc;

mod types;
use types::Directory;

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

    let root_directory = build_tree(&all_lines);
    root_directory.borrow()._pretty_print(0);
    // _one(root_directory);
    // _two(root_directory);
}

fn _one(root_directory: Rc<RefCell<Directory>>) {
    let mut sum = 0;
    root_directory
        .borrow()
        ._find_directory_size_smaller_than(100000, &mut sum);
    println!("Sum: {}", sum);
}

fn _two(root_directory: Rc<RefCell<Directory>>) {
    let total_filesystem_size = 70000000;
    let necessary_free_space = 30000000;
    let total_size_currently_used = root_directory.borrow().get_total_size();
    let total_size_available = total_filesystem_size - total_size_currently_used;
    let minimum_necessary_free = necessary_free_space - total_size_available;

    println!("Total size currently used: {}", total_size_currently_used);
    println!("Total size available: {}", total_size_available);
    println!(
        "Space that needs to be freed up: {}",
        minimum_necessary_free
    );

    let mut current_min_size: i32 = i32::MAX;
    let mut dir_name = String::new();
    root_directory
        .borrow()
        ._find_directory_size_barely_bigger_than(
            minimum_necessary_free,
            &mut dir_name,
            &mut current_min_size,
        );

    println!(
        "Space that can be freed up by deleting directory {}: {}",
        dir_name, current_min_size
    );
}

fn build_tree(all_lines: &Vec<String>) -> Rc<RefCell<Directory>> {
    let root_directory: Rc<RefCell<Directory>> =
        Rc::new(RefCell::new(Directory::new("/".to_string(), None)));
    let mut current_directory = Rc::clone(&root_directory);

    for line in all_lines {
        let split = line.split_whitespace().collect::<Vec<&str>>();
        match split[0] {
            "$" => match split[1] {
                "ls" => {
                    continue;
                }
                "cd" => {
                    let new_directory_name = split[2].to_string();
                    let current_clone = Rc::clone(&current_directory);
                    if new_directory_name == ".." {
                        current_directory = Rc::clone(current_clone.borrow().get_parent());
                    } else if new_directory_name == "/" {
                        current_directory = Rc::clone(&root_directory);
                    } else {
                        current_directory = Rc::clone(
                            current_clone
                                .borrow()
                                .get_subdir(&new_directory_name)
                                .unwrap(),
                        );
                    }
                    continue;
                }
                _ => {
                    println!("Unknown command: {}", split[1]);
                    break;
                }
            },
            "dir" => {
                let directory_name = split[1].to_string();
                let subdir_exists = current_directory.borrow().subdir_exists(&directory_name);
                if !subdir_exists {
                    let new_directory = Rc::new(RefCell::new(Directory::new(
                        directory_name.clone(),
                        Some(Rc::clone(&current_directory)),
                    )));
                    current_directory
                        .borrow_mut()
                        .add_subdir(Rc::clone(&new_directory));
                }
            }
            _ => {
                let file_size = split[0].parse::<i32>().unwrap();
                let file_name = split[1].to_string();
                if current_directory.borrow().file_exists(&file_name) {
                    continue;
                }
                current_directory
                    .borrow_mut()
                    .add_file((file_name, file_size));
            }
        }
    }

    root_directory
}
