use std::io::{BufReader,BufRead};
use std::fs::File;


fn main() {
    let target_area = ((155, 182), (-117, -67));
    // let target_area = ((20, 30), (-10, -5));

    // _one(target_area);
    _two(target_area);
}


fn _one(target_area: ((i32, i32), (i32, i32))) {

    let mut max_height = 0;
    let mut max_vels = (0, 0);

    let limit = 1000;

    for vel_x in 1..=limit {
        for vel_y in 1..=limit {

            let target_range_x = target_area.0.0..=target_area.0.1;
            let target_range_y = target_area.1.0..=target_area.1.1;

            let mut velocity: (i32, i32) = (vel_x, vel_y);

            // println!("velocity: {:?}", velocity);

            let mut current_position = (0,0);

            let mut max_y = 0;

            loop {
                current_position.0 += velocity.0;
                current_position.1 += velocity.1;

                max_y = current_position.1.max(max_y);
                
                velocity.0 += -1 * velocity.0.signum();
                velocity.1 -= 1;

                if velocity.1 == 0 && max_y < max_height {
                    // If the apex of the parabola is reached and we don't have a new max yet, we can stop calculating
                    break;
                }

                if current_position.1 < target_area.1.0 || current_position.0 > target_area.0.1 {
                    // Overshot target area
                    break;
                }

                if target_range_x.contains(&current_position.0) && target_range_y.contains(&current_position.1) {
                    println!("Hit target at {:?} with max_height {} (velocity {:?})", current_position, max_y, (vel_x, vel_y));

                    if max_y > max_height {
                        max_height = max_y;
                        max_vels = (vel_x, vel_y);
                    }
                    break;
                }
            }
        }
    }

    println!("max_height {} reached with {:?}", max_height, max_vels);
    
}

fn _two(target_area: ((i32, i32), (i32, i32))) {

    let limit = 1000;

    let mut possible_x_velocities: Vec<i32> = Vec::new();

    for starting_x_velocity in 0..limit {
        if starting_x_velocity > target_area.0.1 {
            break;
        }
        let mut current_x_position = 0;
        for x_add in (0..=starting_x_velocity).rev() {
            current_x_position += x_add;
            if current_x_position > target_area.0.1 {
                break;
            }
            if current_x_position < target_area.0.0 {
                continue;
            }
            possible_x_velocities.push(starting_x_velocity);
            break;
        }
    }

    println!("possible x velocities: {:?}", possible_x_velocities);

    let mut all_distinct_shots = 0;

    for vel_x in possible_x_velocities {
        for vel_y in -limit..=limit {

            let target_range_x = target_area.0.0..=target_area.0.1;
            let target_range_y = target_area.1.0..=target_area.1.1;

            let mut velocity: (i32, i32) = (vel_x, vel_y);

            let mut current_position = (0,0);

            loop {
                current_position.0 += velocity.0;
                current_position.1 += velocity.1;
                
                velocity.0 += -1 * velocity.0.signum();
                velocity.1 -= 1;

                if current_position.1 < target_area.1.0 || current_position.0 > target_area.0.1 {
                    // Overshot target area
                    break;
                }

                if target_range_x.contains(&current_position.0) && target_range_y.contains(&current_position.1) {
                    println!("Hit target at {:?} (velocity {:?})", current_position, (vel_x, vel_y));
                    all_distinct_shots += 1;
                    break;
                }
            }
        }
    }

    println!("all_distinct_shots: {}", all_distinct_shots);
    
}