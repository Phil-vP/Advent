package com.company;

public class ampThread extends Thread {

    private Amplifier amp;

    public ampThread(Amplifier amp) {
        this.amp = amp;
    }

    @Override
    public void run() {
        amp.intcodeComputer();
    }

    public Amplifier getAmp() {
        return amp;
    }
}
