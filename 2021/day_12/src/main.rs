use std::io::{BufReader,BufRead};
use std::fs::File;

use std::collections::HashMap;

#[derive(Debug, Clone)]
struct NodeOne {
    id: String,
    neighbors: Vec<String>,
    visited: bool,
    small: bool,
}

#[derive(Debug, Clone)]
struct SituationOne {
    nodes: HashMap<String, NodeOne>,
    current_path: Vec<String>,
}

impl NodeOne {
    fn new(id: String) -> NodeOne {
        NodeOne {
            id: id.clone(),
            neighbors: Vec::new(),
            visited: false,
            small: id.to_ascii_lowercase() == id,
        }
    }

    fn mark_visited(&mut self) {
        if self.small {
            self.visited = true;
        }
    }
}

impl SituationOne {
    fn new(node_map: HashMap<String, NodeOne>, path: Vec<String>) -> SituationOne {
        SituationOne {
            nodes: node_map,
            current_path: path,
        }
    }
}

#[derive(Debug, Clone)]
struct NodeTwo {
    id: String,
    neighbors: Vec<String>,
    visited: i16,
    small: bool,
}

#[derive(Debug, Clone)]
struct SituationTwo {
    nodes: HashMap<String, NodeTwo>,
    current_path: Vec<String>,
    already_visited_small_node: bool,
}

impl NodeTwo {
    fn new(id: String) -> NodeTwo {
        NodeTwo {
            id: id.clone(),
            neighbors: Vec::new(),
            visited: 0,
            small: id.to_ascii_lowercase() == id,
        }
    }

    fn mark_visited(&mut self) -> i16 {
        if self.small {
            self.visited += 1;
        }
        self.visited
    }
}

impl SituationTwo {
    fn new(node_map: HashMap<String, NodeTwo>, path: Vec<String>, already_visited_small: bool) -> SituationTwo {
        SituationTwo {
            nodes: node_map,
            current_path: path,
            already_visited_small_node: already_visited_small,
        }
    }
}


fn main() {
    let mut all_lines: Vec<String> = Vec::new();

    let file = File::open("input.txt").unwrap();
    for line in BufReader::new(file).lines() {
        all_lines.push(line.unwrap());
    }

    // _one(&all_lines);
    _two(&all_lines);
}


fn _one(all_lines: &Vec<String>) {

    let mut all_nodes: HashMap<String, NodeOne> = HashMap::new();

    for line in all_lines {
        let split_line: Vec<&str> = line.split("-").collect();
        let first: &str = split_line[0];
        let second: &str = split_line[1];

        if !all_nodes.contains_key(first) {
            let new_node = NodeOne::new(first.to_string());
            all_nodes.insert(first.to_string(), new_node);
        }

        if !all_nodes.contains_key(second) {
            let new_node = NodeOne::new(second.to_string());
            all_nodes.insert(second.to_string(), new_node);
        }
        
        // Two scopes are being created so we can push the neigbors to the respective NodeOne
        {
        let first_node = all_nodes.get_mut(first).unwrap();
        first_node.neighbors.push(second.to_string());
        }

        {
        let second_node = all_nodes.get_mut(second).unwrap();
        second_node.neighbors.push(first.to_string());
        }
    }

    for key in all_nodes.keys() {
        let node = all_nodes.get(key).unwrap();
        println!("NodeOne: {}, small? {}, neighbors: {:?}", node.id, node.small, node.neighbors);
    }

    let mut situations: Vec<SituationOne> = Vec::new();

    {

    let current_node = all_nodes.get_mut("start").unwrap();
    current_node.mark_visited();

    for neighbor in current_node.neighbors.clone() {
        let current_path: Vec<String> = vec!["start".to_string(), neighbor.to_string()];
        let situation = SituationOne::new(all_nodes.clone(), current_path);
        situations.push(situation);
    }

    }

    let mut count = 0;

    while situations.len() > 0 {
        let mut situation = situations.remove(0);
        let current_node_id = situation.current_path.last().unwrap();

        if current_node_id == "end" {
            println!("Found path: {:?}", situation.current_path);
            count += 1;
            continue;
        }

        situation.nodes.get_mut(current_node_id).unwrap().mark_visited();

        let neighbors = situation.nodes.get(current_node_id).unwrap().neighbors.clone();

        for neighbor in neighbors {
            // If this neighbor has already been visited, skip it
            if situation.nodes.get(&neighbor).unwrap().visited {
                continue;
            }
            // Else, we add the new branch to all situations
            let mut new_path = situation.current_path.clone();
            new_path.push(neighbor.to_string());
            let situation = SituationOne::new(situation.nodes.clone(), new_path);
            situations.push(situation);
        }
    }

    println!("Count: {}", count);



    
}

fn _two(all_lines: &Vec<String>) {

    let mut all_nodes: HashMap<String, NodeTwo> = HashMap::new();

    for line in all_lines {
        let split_line: Vec<&str> = line.split("-").collect();
        let first: &str = split_line[0];
        let second: &str = split_line[1];

        if !all_nodes.contains_key(first) {
            let new_node = NodeTwo::new(first.to_string());
            all_nodes.insert(first.to_string(), new_node);
        }

        if !all_nodes.contains_key(second) {
            let new_node = NodeTwo::new(second.to_string());
            all_nodes.insert(second.to_string(), new_node);
        }
        
        // Two scopes are being created so we can push the neigbors to the respective NodeTwo
        {
        let first_node = all_nodes.get_mut(first).unwrap();
        first_node.neighbors.push(second.to_string());
        }

        {
        let second_node = all_nodes.get_mut(second).unwrap();
        second_node.neighbors.push(first.to_string());
        }
    }

    for key in all_nodes.keys() {
        let node = all_nodes.get(key).unwrap();
        println!("NodeTwo: {}, small? {}, neighbors: {:?}", node.id, node.small, node.neighbors);
    }

    let mut situations: Vec<SituationTwo> = Vec::new();

    {

    let current_node = all_nodes.get_mut("start").unwrap();
    current_node.mark_visited();

    for neighbor in current_node.neighbors.clone() {
        let current_path: Vec<String> = vec!["start".to_string(), neighbor.to_string()];
        let situation = SituationTwo::new(all_nodes.clone(), current_path, false);
        situations.push(situation);
    }

    }

    let mut count = 0;

    while situations.len() > 0 {
        let mut situation = situations.remove(0);
        let current_node_id = situation.current_path.last().unwrap();

        if current_node_id == "end" {
            // println!("Found path: {:?}", situation.current_path);
            count += 1;
            continue;
        }

        let count_visited = situation.nodes.get_mut(current_node_id).unwrap().mark_visited();

        let current_node_small = situation.nodes.get(current_node_id).unwrap().small;

        let already_visited_small_twice = situation.already_visited_small_node;

        // If this is the node in this situation that is small and visited twice, we can set the already_visited_small_node for this situation to true
        if current_node_small && !already_visited_small_twice && count_visited > 1 {
            situation.already_visited_small_node = true;
        }

        let neighbors = situation.nodes.get(current_node_id).unwrap().neighbors.clone();

        for neighbor in neighbors {
            if neighbor.to_string() == "start" {
                continue;
            }
            // If this neighbor has already been visited once and this situation has already had a double small node, we can skip this path
            if situation.nodes.get(&neighbor).unwrap().visited >= 1 && situation.already_visited_small_node {
                continue;
            }
            // Else, we add the new branch to all situations
            let mut new_path = situation.current_path.clone();
            new_path.push(neighbor.to_string());
            let situation = SituationTwo::new(situation.nodes.clone(), new_path, situation.already_visited_small_node);
            situations.push(situation);
        }

    }

    println!("Count: {}", count);
}