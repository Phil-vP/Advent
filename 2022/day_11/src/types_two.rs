pub enum Operation {
    Add,
    Multiply,
}

pub type Id = usize;

pub struct Monkey {
    id: Id,
    item_list: Vec<i64>,
    modulo_test: i64,
    false_monkey: Id,
    true_monkey: Id,
    operation: Operation,
    op_on_old_value: bool,
    op_value: i64,
    inspection_count: i64,
    div_value: i64,
}

impl Monkey {
    pub fn new(
        id: Id,
        item_list: Vec<i64>,
        modulo_test: i64,
        false_monkey: Id,
        true_monkey: Id,
        operation: Operation,
        op_on_own_value: bool,
        op_value: i64,
    ) -> Monkey {
        Monkey {
            id,
            item_list,
            modulo_test,
            false_monkey,
            true_monkey,
            operation,
            op_on_old_value: op_on_own_value,
            op_value,
            inspection_count: 0,
            div_value: 1,
        }
    }

    pub fn make_operation(&mut self) -> (Id, i64) {
        self.inspection_count += 1;
        let mut new_val = self.item_list[0];
        self.item_list.remove(0);
        match self.operation {
            Operation::Add => {
                if self.op_on_old_value {
                    new_val += new_val;
                } else {
                    new_val += self.op_value;
                }
            }
            Operation::Multiply => {
                if self.op_on_old_value {
                    new_val *= new_val;
                } else {
                    new_val *= self.op_value;
                }
            }
        };
        // Worry level decreases by being divided by 3 (in part 1)
        new_val %= self.div_value;

        // If the new value is divisible by modulo_test, return true_monkey
        // Otherwise, return false_monkey
        if new_val % self.modulo_test == 0 {
            (self.true_monkey, new_val)
        } else {
            (self.false_monkey, new_val)
        }
    }

    pub fn get_item_list_len(&self) -> usize {
        self.item_list.len()
    }

    pub fn get_inspection_count(&self) -> i64 {
        self.inspection_count
    }

    pub fn add_item(&mut self, new_item: i64) {
        self.item_list.push(new_item);
    }

    pub fn get_id(&self) -> Id {
        self.id
    }

    pub fn set_div_value(&mut self, new_div_value: i64) {
        self.div_value = new_div_value;
    }
}
