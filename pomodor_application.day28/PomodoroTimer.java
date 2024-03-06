import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.*;

public class PomodoroTimer {
    private JFrame frame;
    private JLabel timerLabel;
    private JLabel checkMarks;
    private Timer timer;
    private int secondsLeft;
    private int reps = 0;
    private static final String WORK_TEXT = "Work";
    private static final String BREAK_TEXT = "Break";
    private static final int WORK_MIN = 25;
    private static final int SHORT_BREAK_MIN = 5;
    private static final int LONG_BREAK_MIN = 20;
    private static final Color GREEN = new Color(155, 222, 172);
    private static final Color PINK = new Color(226, 151, 156);
    private static final Color RED = new Color(231, 48, 91);
    private static final Color YELLOW = new Color(247, 245, 221);
    private static final String FONT_NAME = "Courier";
    private static final ImageIcon TOMATO_ICON = new ImageIcon("tomato.png");

    public PomodoroTimer() {
        frame = new JFrame("Pomodoro");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 400);
        frame.setLayout(new GridBagLayout());
        frame.getContentPane().setBackground(YELLOW);

        timerLabel = new JLabel("00:00");
        timerLabel.setForeground(GREEN);
        timerLabel.setFont(new Font(FONT_NAME, Font.BOLD, 50));

        checkMarks = new JLabel();
        checkMarks.setForeground(GREEN);
        checkMarks.setFont(new Font(FONT_NAME, Font.PLAIN, 24));

        JButton startButton = new JButton("Start");
        startButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                startTimer();
            }
        });

        JButton resetButton = new JButton("Reset");
        resetButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                resetTimer();
            }
        });

        JLabel tomatoLabel = new JLabel(TOMATO_ICON);

        GridBagConstraints constraints = new GridBagConstraints();
        constraints.gridx = 0;
        constraints.gridy = 0;
        constraints.gridwidth = 3;
        constraints.anchor = GridBagConstraints.CENTER;
        frame.add(tomatoLabel, constraints);

        constraints.gridy = 1;
        frame.add(timerLabel, constraints);

        constraints.gridwidth = 1;
        constraints.gridy = 2;
        frame.add(startButton, constraints);

        constraints.gridx = 2;
        frame.add(resetButton, constraints);

        constraints.gridx = 1;
        constraints.gridy = 3;
        frame.add(checkMarks, constraints);

        frame.setVisible(true);
    }

    private void resetTimer() {
        if (timer != null) {
            timer.stop();
        }
        timerLabel.setText("00:00");
        timerLabel.setForeground(GREEN);
        checkMarks.setText("");
        reps = 0;
    }

    private void startTimer() {
        reps++;
        int minutes;
        if (reps % 8 == 0) {
            minutes = LONG_BREAK_MIN;
            timerLabel.setForeground(RED);
        } else if (reps % 2 == 0) {
            minutes = SHORT_BREAK_MIN;
            timerLabel.setForeground(PINK);
        } else {
            minutes = WORK_MIN;
            timerLabel.setForeground(GREEN);
        }
        secondsLeft = minutes * 60;
        if (timer != null) {
            timer.stop();
        }
        timer = new Timer(1000, new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                countDown();
            }
        });
        timer.start();
    }

    private void countDown() {
        int minutes = secondsLeft / 60;
        int seconds = secondsLeft % 60;
        timerLabel.setText(String.format("%02d:%02d", minutes, seconds));
        if (secondsLeft == 0) {
            timer.stop();
            startTimer();
            String marks = "";
            for (int i = 0; i < reps / 2; i++) {
                marks += "✔";
            }
            checkMarks.setText(marks);
        }
        secondsLeft--;
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new PomodoroTimer();
            }
        });
    }
}
