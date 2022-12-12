echo Enter day:
read day
if [ ${#day} -eq 1 ];
then
day_string="day_0${day}"
else
day_string="day_${day}"
fi
echo Creating project $day_string
cargo new $day_string
cp template.txt $day_string/src/main.rs
touch $day_string/input.txt
touch $day_string/test_input.txt