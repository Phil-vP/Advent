#[derive(Debug, Copy, Clone)]
pub struct BingoField {
    field: [[(i32, bool); 5]; 5],
    pub id: i32,
}

impl BingoField {
    pub fn new(vec: Vec<Vec<i32>>, id: i32) -> BingoField {
        let mut field = [[(0, false); 5]; 5];
        for i in 0..5 {
            for j in 0..5 {
                field[i][j].0 = vec[i][j];
            }
        }
        BingoField { field, id }
    }

    fn get_sum(&self) -> i32 {
        let mut sum = 0;
        for i in 0..5 {
            for j in 0..5 {
                if !self.field[i][j].1 {
                    sum += self.field[i][j].0;
                }
            }
        }
        sum
    }

    pub fn cross_out_number(&mut self, number: i32) {
        let field = self.field;
        for i in 0..5 {
            for j in 0..5 {
                if field[i][j].0 == number {
                    self.field[i][j].1 = true;
                    // println!("Crossing out number {}", number);
                }
            }
        }
    }

    pub fn check_field(&self) -> (i32, bool) {
        let field = self.field;

        // Check if a row is crossed out
        for i in 0..5 {
            let mut crossed_out = true;
            for j in 0..5 {
                crossed_out &= field[i][j].1;
            }
            if crossed_out {
                return (self.get_sum(), true);
            }
        }


        // Check if a column is crossed out
        for j in 0..5 {
            let mut crossed_out = true;
            for i in 0..5 {
                crossed_out &= field[i][j].1;
            }
            if crossed_out {
                return (self.get_sum(), true);
            }
        }

        (0, false)
    }

    pub fn pretty_print(&self) {
        println!("ID: {}", self.id);
        for i in 0..5 {
            for j in 0..5 {
                if !self.field[i][j].1 {
                    print!("{:02} ", self.field[i][j].0);
                } else {
                    print!("{} ", "--");
                }
            }
            println!();
        }
    }
}