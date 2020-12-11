package com.company;

import org.paukov.combinatorics3.Generator;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

import static java.lang.Thread.sleep;

public class Main {

    public static ArrayList<String> values = new ArrayList<String>();
    public static boolean testing = false;


    public static void main(String[] args) {
        //System.out.println("Ja moin");
        //System.out.println(values);

        //makeAmps(1,0,4,3,2);
        Generator gen = new Generator();

        ArrayList col = new ArrayList();
        for(int i = 5; i < 10; i++){
            col.add(i);
        }

        gen.permutation(col).simple().stream().forEach((set -> doSomething(set.toString())));

        getMax();

    }

    private static void doSomething(String in){
        //System.out.println(in);
        in = in.substring(1,in.length()-1);
        //System.out.println(in);

        String[] list = in.split(",");
        int[] intList = new int[5];
        for(int i = 0; i < 5; i++){
            String x = list[i].strip();
            intList[i] = Integer.parseInt(x);
        }

        System.out.println(in);

        makeAmps(intList[0], intList[1], intList[2], intList[3], intList[4]);

    }

    private static void makeAmps(int i1, int i2, int i3, int i4, int i5) {
        Amplifier amp1 = new Amplifier(i1, testing);
        Amplifier amp2 = new Amplifier(i2, testing);
        Amplifier amp3 = new Amplifier(i3, testing);
        Amplifier amp4 = new Amplifier(i4, testing);
        Amplifier amp5 = new Amplifier(i5, testing);

        amp1.setNachfolger(amp2);
        amp2.setNachfolger(amp3);
        amp3.setNachfolger(amp4);
        amp4.setNachfolger(amp5);
        amp5.setNachfolger(amp1);

        ampThread[] threads = new ampThread[5];
        threads[0] = new ampThread(amp1);
        threads[1] = new ampThread(amp2);
        threads[2] = new ampThread(amp3);
        threads[3] = new ampThread(amp4);
        threads[4] = new ampThread(amp5);

        for (int i = 0; i < 5; i++) {
            threads[i].start();
        }

        try {
            sleep(200);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        amp1.setInput(0);

        while (true) {
            System.out.println("----------" + threads[4].getAmp().isRunning());

            if (!threads[4].getAmp().isRunning()) {

                try {
                    sleep(200);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }

                //System.out.println("Vor dem stoppen");

                for (int j = 0; j < 5; j++) {
                    threads[j].stop();
                }

                //System.out.println("Nach dem stoppen");

                int i = threads[4].getAmp().getOutput();
                String s = "" + i;
                values.add(s);

                //getMax();

                return;
            }
        }

    }

    private static void getMax() {
        System.out.println("In getMax()");
        int max = 0;
        for (String s : values) {
            int x = Integer.parseInt(s);
            if (x > max) {
                max = x;
            }
        }
        System.out.println("Max: " + max);
    }
}
