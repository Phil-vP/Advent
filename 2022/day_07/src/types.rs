use std::cell::RefCell;
use std::collections::HashMap;
use std::rc::Rc;

pub type File = (String, i32);

pub struct Directory {
    name: String,
    files: HashMap<String, File>,
    subdirs: Vec<Rc<RefCell<Directory>>>,
    parent: Option<Rc<RefCell<Directory>>>,
}

impl Directory {
    pub fn new(name: String, parent: Option<Rc<RefCell<Directory>>>) -> Directory {
        Directory {
            name,
            files: HashMap::new(),
            subdirs: Vec::new(),
            parent: parent,
        }
    }

    pub fn add_file(&mut self, file: File) {
        self.files.insert(file.0.clone(), file);
    }

    pub fn add_subdir(&mut self, subdir: Rc<RefCell<Directory>>) {
        self.subdirs.push(subdir);
    }

    pub fn get_subdir(&self, name: &str) -> Option<&Rc<RefCell<Directory>>> {
        for subdir in self.subdirs.iter() {
            if subdir.borrow().get_name() == name {
                return Some(subdir);
            }
        }
        return None;
    }

    pub fn get_name(&self) -> String {
        self.name.clone()
    }

    pub fn subdir_exists(&self, name: &str) -> bool {
        for subdir in self.subdirs.iter() {
            if subdir.borrow().get_name() == name {
                return true;
            }
        }
        false
    }

    pub fn file_exists(&self, name: &str) -> bool {
        self.files.contains_key(name)
    }

    pub fn get_parent(&self) -> &Rc<RefCell<Directory>> {
        self.parent.as_ref().unwrap()
    }

    pub fn get_total_size(&self) -> i32 {
        let mut total_size = 0;
        for file in self.files.values() {
            total_size += file.1;
        }
        for subdir in self.subdirs.iter() {
            total_size += subdir.borrow().get_total_size();
        }
        total_size
    }

    pub fn _pretty_print(&self, level: i32) {
        for _ in 0..level {
            print!("    ");
        }
        println!("{} (dir, size {})", self.name, self.get_total_size());
        for dir in self.subdirs.iter() {
            dir.borrow()._pretty_print(level + 1);
        }
        for file in self.files.values() {
            for _ in 0..=level {
                print!("    ");
            }
            println!("{} ({})", file.0, file.1);
        }
    }

    pub fn _find_directory_size_smaller_than(&self, size: i32, sum: &mut i64) {
        let self_size = self.get_total_size();

        if self_size < size {
            *sum += self_size as i64;
        }

        for dir in self.subdirs.iter() {
            dir.borrow()._find_directory_size_smaller_than(size, sum);
        }
    }

    pub fn _find_directory_size_barely_bigger_than(
        &self,
        size: i32,
        dir_name: &mut String,
        current_min_size: &mut i32,
    ) {
        let self_size = self.get_total_size();

        if self_size < *current_min_size && self_size > size {
            *current_min_size = self_size;
            *dir_name = self.name.clone();
        }

        for dir in self.subdirs.iter() {
            dir.borrow()
                ._find_directory_size_barely_bigger_than(size, dir_name, current_min_size);
        }
    }
}
