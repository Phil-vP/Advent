use std::io::{BufReader,BufRead};
use std::fs::File;


fn main() {
    let mut all_lines: Vec<String> = Vec::new();

    let file = File::open("input.txt").unwrap();
    for line in BufReader::new(file).lines() {
        all_lines.push(line.unwrap());
    }

    // assert!(_is_abba("abba"));
    // assert!(_is_abba("yzhhzo"));
    // assert!(!_is_abba("aaaa"));
    // assert!(_is_abba("azza"));
    // assert!(_is_abba("sgjjqocmmcccpem"));

    // _one(&all_lines);
    _two(&all_lines);
}


fn _one(all_lines: &Vec<String>) {

    let mut counter = 0;

    for line in all_lines {
        let mut split = line.split("[");
        let front = split.next().unwrap();
        let mut has_abba_normal = _is_abba(front);

        let mut has_abba_hyper = false;

        for mid_back in split {
            let mut sec_split = mid_back.split("]");
            has_abba_hyper |= _is_abba(sec_split.next().unwrap());
            has_abba_normal |= _is_abba(sec_split.next().unwrap());
        }

        if has_abba_normal && !has_abba_hyper {
            counter += 1;
        }

    }

    println!("Counter: {}", counter);
    
}

fn _two(all_lines: &Vec<String>) {
    
    let mut counter = 0;

    for line in all_lines {
        let mut split = line.split("[");

        let mut vec_normal: Vec<String> = Vec::new();
        let mut vec_hyper: Vec<String> = Vec::new();

        let front = split.next().unwrap();
        vec_normal.extend(_is_aba(front));

        for mid_back in split {
            let mut sec_split = mid_back.split("]");
            vec_hyper.extend(_is_aba(sec_split.next().unwrap()));
            vec_normal.extend(_is_aba(sec_split.next().unwrap()));
        }

        // println!("\nline: {}\nvec_normal: {:?}, vec_hyper: {:?}", line, vec_normal, vec_hyper);
        
        'main_loop: for entry_normal in vec_normal {
            let mut normal_chars = entry_normal.chars();
            let c_1_n = normal_chars.next().unwrap();
            let c_2_n = normal_chars.next().unwrap();

            for entry_hyper in &vec_hyper {
                let mut hyper_chars = entry_hyper.chars();
                let c_1_h = hyper_chars.next().unwrap();
                let c_2_h = hyper_chars.next().unwrap();

                if c_1_n == c_2_h && c_2_n == c_1_h {
                    counter += 1;
                    // println!("Found {} and {}", entry_normal, entry_hyper);
                    break 'main_loop
                }
            }
        }
    }

    println!("\nCounter: {}", counter);
    
}


fn _is_aba(input: &str) -> Vec<String> {

    let mut chars = input.chars();
    let mut final_vec: Vec<String> = Vec::new();

    let mut c_1 = chars.next().unwrap();
    let mut c_2 = chars.next().unwrap();

    let length = input.len() - 2;

    for _i in 0..length {
        let c_3 = chars.next().unwrap();

        if c_1 == c_2 {
            // Skip this turn
        }
        else if c_1 == c_3 {
            let string: String = vec![c_1, c_2, c_3].into_iter().collect();
            final_vec.push(string);
        }
        c_1 = c_2;
        c_2 = c_3;
    }


    final_vec

}


fn _is_abba(input: &str) -> bool {

    let mut chars = input.chars();

    let mut c_1 = chars.nth(0).unwrap();
    let mut c_2 = chars.nth(0).unwrap();
    let mut c_3 = chars.nth(0).unwrap();

    let length = input.len() - 3;

    // println!("input: {}, length: {}", input, length);

    let mut found = false;

    for _i in 0..length {
        let c_4 = chars.next().unwrap();

        if c_1 == c_2 {
            // Skip this turn
        }
        else if c_1 == c_4 && c_2 == c_3 {
            found = true;
            break
        }

        c_1 = c_2;
        c_2 = c_3;
        c_3 = c_4;
    }

    found
}