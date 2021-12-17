use std::io::{BufReader,BufRead};
use std::fs::File;

struct Binary {
    data: Vec<u8>,
}


fn main() {
    let mut all_lines: Vec<String> = Vec::new();

    let file = File::open("input.txt").unwrap();
    for line in BufReader::new(file).lines() {
        all_lines.push(line.unwrap());
    }

    let input_line = all_lines[0].clone();

    // _one(input_line);
    _two(input_line);
}


fn _one(input_line: String) {
    println!("{}", input_line);
    let binary_vec = parse_hex_to_binary(input_line);

    println!("{:?}", binary_vec);

    let final_number = eval_packet(binary_vec, false, 0);

    println!("Sum of all version numbers: {}", final_number.2);
}

fn _two(input_line: String) {
    println!("{}", input_line);
    let binary_vec = parse_hex_to_binary(input_line);

    println!("{:?}", binary_vec);

    let final_number = eval_packet(binary_vec, false, 0);

    println!("Final number: {:?}", final_number.0);
    println!("Final number parsed: {}", isize::from_str_radix(&final_number.0[0], 16).unwrap());
}

fn eval_packet(binary_vec: Vec<u8>, count: bool, number_of_packets: i32) -> (Vec<String>, i32, i32) {
    let mut binary_vec = binary_vec.clone();

    let mut packet_values: Vec<String> = Vec::new();

    let mut number_of_drained_bits: i32 = 0;

    let mut number_of_visited_packets = 0;

    let mut sum_version_number = 0;

    while binary_vec.contains(&1) {
        let packet_version = parse_binary_to_dec(binary_vec[0..3].to_vec());
        sum_version_number += packet_version;
        binary_vec.drain(0..3);
        let type_id = parse_binary_to_dec(binary_vec[0..3].to_vec());
        binary_vec.drain(0..3);

        number_of_drained_bits += 6;

        match type_id {
            4 => {
                // Representing literal value
                let mut last_number = false;

                let mut literal_value: String = String::new();
                
                loop {
                    if binary_vec[0] == 0 {
                        last_number = true;
                    }
                    let number = binary_vec[1..5].to_vec();
                    binary_vec.drain(0..5);
                    number_of_drained_bits += 5;

                    literal_value.push_str(&parse_binary_to_hex(number));

                    if last_number {
                        break;
                    }
                }
                packet_values.push(literal_value);
                
            },
            _ => {
                let length_type_id = binary_vec[0];
                binary_vec.drain(0..1);
                number_of_drained_bits += 1;

                let all_packets: Vec<String> = match length_type_id {
                    0 => {
                        let length = parse_binary_to_dec(binary_vec[0..15].to_vec());
                        println!("Found a subpacket with length: {}", length);
                        binary_vec.drain(0..15);
                        number_of_drained_bits += 15;
                        let evaluation = eval_packet(binary_vec[0..length as usize].to_vec(), false, 0);
                        binary_vec.drain(0..length as usize);
                        number_of_drained_bits += length;
                        sum_version_number += evaluation.2;
                        evaluation.0
                    },
                    1 => {
                        let number_of_subpackets = parse_binary_to_dec(binary_vec[0..11].to_vec());
                        println!("Found {} subpacket(s)", number_of_subpackets);
                        binary_vec.drain(0..11);
                        number_of_drained_bits += 11;
                        let evaluation = eval_packet(binary_vec.clone(), true, number_of_subpackets);
                        binary_vec.drain(0..evaluation.1 as usize);
                        number_of_drained_bits += evaluation.1;
                        sum_version_number += evaluation.2;
                        evaluation.0
                    },
                    _ => {
                        println!("Error, length_type_id: {}", length_type_id);
                        Vec::new()
                    }
                };

                packet_values.push( match type_id {
                    0 => {
                        // Sum Packets
                        println!("Found a sum packet with values: {:?}", all_packets);
                        let mut sum: String = "0".to_string();
                        for packet in all_packets {
                            sum = add_hex_strings(sum, packet);
                        }
                        println!("Sum: {}", sum);
                        sum
                    }
                    1 => {
                        // Product packets
                        println!("Found a product packet with values: {:?}", all_packets);
                        let mut product: String = "1".to_string();
                        for packet in all_packets {
                            product = mult_hex_strings(product, packet);
                        }
                        println!("Product: {}", product);
                        product
                    }
                    2 => {
                        // Minimum packet
                        println!("Found a minimum packet with values: {:?}", all_packets);
                        let mut min: String = "FFFFFFFF".to_string();
                        for packet in all_packets {
                            if hex1_greater(min.clone(), packet.clone()) {
                                min = packet;
                            }
                        }
                        println!("min: {}", min);
                        min
                    }
                    3 => {
                        // Maximum packet
                        println!("Found a maximum packet with values: {:?}", all_packets);
                        let mut max: String = "0".to_string();
                        for packet in all_packets {
                            if hex1_greater(packet.clone(), max.clone()) {
                                max = packet;
                            }
                        }
                        println!("max: {}", max);
                        max
                    }
                    5 => {
                        // Greater than packet
                        println!("Found a greater than packet with values: {:?}", all_packets);
                        if hex1_greater(all_packets[0].clone(), all_packets[1].clone()) {
                            println!("{} > {}", all_packets[0], all_packets[1]);
                            "1".to_string()
                        } else {
                            println!("{} <= {}", all_packets[0], all_packets[1]);
                            "0".to_string()
                        }
                    }
                    6 => {
                        // Less than packet
                        println!("Found a less than packet with values: {:?}", all_packets);
                        if hex1_greater(all_packets[1].clone(), all_packets[0].clone()) {
                            println!("{} <= {}", all_packets[0], all_packets[1]);
                            "1".to_string()
                        } else {
                            println!("{} > {}", all_packets[0], all_packets[1]);
                            "0".to_string()
                        }
                    }
                    7 => {
                        // Equal to packet
                        println!("Found an equal to packet with values: {:?}", all_packets);
                        if all_packets[0] == all_packets[1] {
                            println!("Equal, result is 1");
                            "1".to_string()
                        } else {
                            println!("NotEqual, result is 0");
                            "0".to_string()
                        }
                    }
                    _ => {
                        println!("Error, type_id: {}", type_id);
                        String::new()
                    }
                });
                println!("");
            },
        }
        number_of_visited_packets += 1;
        if count && number_of_visited_packets == number_of_packets {
            break;
        }
        
    }

    (packet_values, number_of_drained_bits, sum_version_number)
}


fn parse_binary_to_dec(binary_vec: Vec<u8>) -> i32 {
    let bin_str: String = binary_vec.iter().map(|x| x.to_string()).collect();
    let dec_num: i32 = i32::from_str_radix(&bin_str, 2).unwrap();
    dec_num
}

fn parse_binary_to_hex(binary_vec: Vec<u8>) -> String {
    let bin_str: String = binary_vec.iter().map(|x| x.to_string()).collect();
    let dec_num: i32 = i32::from_str_radix(&bin_str, 2).unwrap();
    let hex_num = format!("{:x}", dec_num);
    hex_num
}

fn parse_hex_to_binary(input_string: String) -> Vec<u8> {
    let mut out_vec: Vec<u8> = Vec::new();
    for c in input_string.chars() {
        let binary_str = format!("{:04b}", c.to_digit(16).unwrap());
        // println!("{}: {}", c, binary_str);
        out_vec.extend(binary_str.chars().map(|c| c.to_digit(10).unwrap() as u8));
    }
    out_vec
}

fn add_hex_strings(input_1: String, input_2: String) -> String {
    if input_1 == "0" {
        return input_2;
    }
    if input_2 == "0" {
        return input_1;
    }
    let mut out_vec: Vec<u8> = Vec::new();
    let mut carry = 0;
    let mut input_1_vec = input_1.chars().map(|x| x.to_digit(16).unwrap() as u8).collect::<Vec<u8>>();
    let mut input_2_vec = input_2.chars().map(|x| x.to_digit(16).unwrap() as u8).collect::<Vec<u8>>();
    input_1_vec.reverse();
    input_2_vec.reverse();

    let input_1_len = input_1_vec.len();
    let input_2_len = input_2_vec.len();

    if input_1_len > input_2_len {
        input_2_vec.extend(vec![0; input_1_len - input_2_len]);
    } else if input_1_len < input_2_len {
        input_1_vec.extend(vec![0; input_2_len - input_1_len]);
    }

    for i in 0..input_1_vec.len() {
        let sum = input_1_vec[i] + input_2_vec[i] + carry;
        out_vec.push(sum % 16);
        carry = sum / 16;
    }
    if carry > 0 {
        out_vec.push(carry);
    }
    out_vec.reverse();
    let out_str = out_vec.iter().map(|x| format!("{:X}", x)).collect::<Vec<String>>().join("");
    out_str
}

fn mult_hex_strings(input_1: String, input_2: String) -> String {
    if input_1.eq(&"0") || input_2.eq(&"0") {
        return "0".to_string();
    }
    if input_1 == "1" {
        return input_2;
    }
    if input_2 == "1" {
        return input_1;
    }
    let input_1_val = i64::from_str_radix(&input_1, 16).unwrap();
    let input_2_val = i64::from_str_radix(&input_2, 16).unwrap();

    let out_val = input_1_val * input_2_val;
    let out_str = format!("{:X}", out_val);
    out_str
}

fn hex1_greater(input_1: String, input_2: String) -> bool{
    if input_1.len() > input_2.len() {
        return true;
    } else if input_1.len() < input_2.len() {
        return false;
    }
    for i in 0..input_1.len() {
        let input_1_c = input_1.chars().nth(i).unwrap();
        let input_2_c = input_2.chars().nth(i).unwrap();
        if input_1_c == input_2_c {
            continue;
        }
        else{
            return input_1_c > input_2_c;
        }
    }
    false
}