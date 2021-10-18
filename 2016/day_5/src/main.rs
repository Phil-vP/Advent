use md5;


fn main() {
    /*
    let mut all_lines: Vec<String> = Vec::new();

    let file = File::open("input.txt").unwrap();
    for line in BufReader::new(file).lines() {
        all_lines.push(line.unwrap());
    }
    */

    // _one();
    _two();
}


fn _one() {

    let door_id = "uqwqemis";

    let mut _compute_cut = "";

    let mut counter = 0;

    let mut password = "".to_owned();

    for _i in 0..8 {
        loop {
            counter += 1;
            let mut hash_id = door_id.to_owned();
            hash_id.push_str(&counter.to_string());
            let compute = format!("{:X}", md5::compute(&hash_id));
            let _compute_cut = &compute[..5];

            if _compute_cut == "00000" {
                println!("{}: {}", counter, compute);
                password.push(compute.chars().nth(5).unwrap());
                break
            }
        }

    }

    println!("Password: {}", password.to_lowercase());

    
}

fn _two() {
    
    let door_id = "uqwqemis";

    let mut _compute_cut = "";

    let mut counter = 0;

    let mut password: Vec<char> = vec!['_', '_', '_', '_', '_', '_', '_', '_'];

    while password.contains(&'_') {
        counter += 1;
        let mut hash_id = door_id.to_owned();
        hash_id.push_str(&counter.to_string());
        let compute = format!("{:X}", md5::compute(&hash_id));
        let _compute_cut = &compute[..5];

        if _compute_cut == "00000" {
            println!("{}: {}", counter, compute);
            let index_res = compute.chars().nth(5).unwrap().to_digit(10);
            let password_char = compute.chars().nth(6).unwrap();

            let index = match index_res {
                Some(index_num) => index_num,
                None => continue
            } as usize;

            if index < 8 {
                if password[index] == '_' {
                    password[index] = password_char;
                }
            }
        }

    }

    let password_str: String = password.into_iter().collect();
    println!("Password: {}", password_str.to_lowercase());

}