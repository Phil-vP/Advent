package com.company;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

import static java.lang.Thread.sleep;

public class Amplifier {

    private ArrayList<String> values;
    private boolean testing;
    private int number;
    private boolean numberUsed = false;
    private int input = 0;
    private Amplifier nachfolger;
    private boolean running = true;
    private int output;
    private boolean inputSet = false;

    public Amplifier(int number, boolean test) {
        this.number = number;
        this.testing = test;

        readFile();
    }

    public void setNachfolger(Amplifier nachfolger) {
        this.nachfolger = nachfolger;
    }

    public boolean isRunning() {
        return running;
    }

    public void setInput(int input) {
        this.input = input;
        inputSet = true;
    }

    public void intcodeComputer() {
        //Scanner sc = new Scanner(System.in);
        int opcode = 0;
        int pointer = 0;

        while (opcode != 99) {
            String full = String.format("%05d", Integer.parseInt(values.get(pointer)));
            opcode = Integer.parseInt(full.substring(3, 5));

            int val1 = 0;
            int val2 = 0;
            int target = 0;

            if (opcode == 1) { // Addieren
                val1 = Integer.parseInt(values.get(pointer + 1));
                if (full.charAt(2) == '0') {
                    int v = val1;
                    val1 = Integer.parseInt(values.get(v));
                }

                val2 = Integer.parseInt(values.get(pointer + 2));
                if (full.charAt(1) == '0') {
                    int v = val2;
                    val2 = Integer.parseInt(values.get(v));
                }

                target = Integer.parseInt(values.get(pointer + 3));
                int ergebnis = val1 + val2;
                values.set(target, "" + ergebnis);

                pointer += 4;
            } else if (opcode == 2) { // Multiplizieren
                val1 = Integer.parseInt(values.get(pointer + 1));
                if (full.charAt(2) == '0') {
                    int v = val1;
                    val1 = Integer.parseInt(values.get(v));
                }

                val2 = Integer.parseInt(values.get(pointer + 2));
                if (full.charAt(1) == '0') {
                    int v = val2;
                    val2 = Integer.parseInt(values.get(v));
                }

                target = Integer.parseInt(values.get(pointer + 3));
                int ergebnis = val1 * val2;
                values.set(target, "" + ergebnis);

                pointer += 4;
            } else if (opcode == 3) { // Input
                //System.out.println("Input: ");
                //String input = sc.nextLine();
                //System.out.println("Wert eingegeben: " + input);

                int in = 0;
                if (!numberUsed) {
                    in = number;
                    numberUsed = true;
                } else {
                    while(!inputSet) {
                        try {
                            sleep(100);
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                    }
                    inputSet = false;
                    in = input;
                }

                target = Integer.parseInt(values.get(pointer + 1));
                values.set(target, "" + in);

                System.out.println("Input " + in + " taken");

                pointer += 2;
            } else if (opcode == 4) { // Output
                val1 = Integer.parseInt(values.get(pointer + 1));
                if (full.charAt(2) == '0') {
                    int v = val1;
                    val1 = Integer.parseInt(values.get(v));
                }

                System.out.println("Output von Amp " + number + ": " + val1);
                nachfolger.setInput(val1);
                output = val1;
                pointer += 2;
            } else if (opcode == 5) { // Jump if true
                val1 = Integer.parseInt(values.get(pointer + 1));
                if (full.charAt(2) == '0') {
                    int v = val1;
                    val1 = Integer.parseInt(values.get(v));
                }

                val2 = Integer.parseInt(values.get(pointer + 2));
                if (full.charAt(1) == '0') {
                    int v = val2;
                    val2 = Integer.parseInt(values.get(v));
                }

                if (val1 != 0) {
                    pointer = val2;
                } else {
                    pointer += 3;
                }
            } else if (opcode == 6) { // Jump if false
                val1 = Integer.parseInt(values.get(pointer + 1));
                if (full.charAt(2) == '0') {
                    int v = val1;
                    val1 = Integer.parseInt(values.get(v));
                }

                val2 = Integer.parseInt(values.get(pointer + 2));
                if (full.charAt(1) == '0') {
                    int v = val2;
                    val2 = Integer.parseInt(values.get(v));
                }

                if (val1 == 0) {
                    pointer = val2;
                } else {
                    pointer += 3;
                }
            } else if (opcode == 7) { // less than
                val1 = Integer.parseInt(values.get(pointer + 1));
                if (full.charAt(2) == '0') {
                    int v = val1;
                    val1 = Integer.parseInt(values.get(v));
                }

                val2 = Integer.parseInt(values.get(pointer + 2));
                if (full.charAt(1) == '0') {
                    int v = val2;
                    val2 = Integer.parseInt(values.get(v));
                }
                int ergebnis = 0;
                if (val1 < val2) {
                    ergebnis = 1;
                }

                target = Integer.parseInt(values.get(pointer + 3));
                values.set(target, "" + ergebnis);

                pointer += 4;
            } else if (opcode == 8) { // equals
                val1 = Integer.parseInt(values.get(pointer + 1));
                if (full.charAt(2) == '0') {
                    int v = val1;
                    val1 = Integer.parseInt(values.get(v));
                }

                val2 = Integer.parseInt(values.get(pointer + 2));
                if (full.charAt(1) == '0') {
                    int v = val2;
                    val2 = Integer.parseInt(values.get(v));
                }
                int ergebnis = 0;
                if (val1 == val2) {
                    ergebnis = 1;
                }

                target = Integer.parseInt(values.get(pointer + 3));
                values.set(target, "" + ergebnis);

                pointer += 4;
            } else if (opcode == 99) { // Ende
                System.out.println("HALT STOPP");
                running = false;
                return;
            } else {
                System.out.println("Alarm, fremder opcode " + opcode);
                return;
            }
        }
        System.out.println("Ende");
    }


    public void readFile() {
        String name = "input.txt";
        if (testing) {
            name = "inputTest.txt";
        }

        values = new ArrayList();

        try {
            FileInputStream fi = new FileInputStream(name);
            BufferedReader r = new BufferedReader(new InputStreamReader(fi));

            String line = r.readLine();
            //System.out.println(line);

            String[] allLines = line.split(",");
            //System.out.println(allLines);

            for (String s : allLines) {
                //System.out.println(s);
                //System.out.println(s.getClass().getName());
                if (s != null) {
                    values.add(s);
                }
            }

            r.close();
            fi.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public int getOutput() {
        return output;
    }
}
