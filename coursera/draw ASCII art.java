public class main {
    public static void main(String[] args) {
    	int size = 4;
        String line_output, figure;
        line_output = "|";
        figure = "";
        for (int line_number=1; line_number < 2 * size; line_number++)
        {
            line_output = "|";
            int number_of_space = Math.abs(line_number - size);
            String repeated_space = new String (new char[number_of_space]).replace("\0"," ");
            line_output = line_output + repeated_space;

            // half: 0 = middle, 1= upper, -1 = lower
            int half;
            if (line_number - size > 0)
            {
                half = -1;
            }
            else if (line_number - size < 0)
            {
                half = 1;
            }
            else
            {
                half = 0;
            }

            // add the slashes
            if (half == 1)
            {
                line_output = line_output + "/";
            }
            else if (half == -1)
            {
                line_output = line_output + "\\";
            }
            else
            {
                line_output = line_output + "<";
            }

            String middle_character;
            if (line_number % 2 == 0)
            {
                middle_character = "-";
            }
            else
            {
                middle_character = "=";
            }
            String repeated_middle;
            if (half == 1 || half == 0)
            {
                repeated_middle = new String (new char[2 * line_number - 2]).replace("\0",middle_character);
            }
            else
            {
                repeated_middle = new String (new char[2 * (size - 1) + (2 * (size - 1) - 2 * (line_number - 1))]).replace("\0",middle_character);
            }
            line_output = line_output + repeated_middle;

            // add the slashes
            if (half == -1)
            {
                line_output = line_output + "/";
            }
            else if (half == 1)
            {
                line_output = line_output + "\\";
            }
            else
            {
                line_output = line_output + ">";
            }

            line_output = line_output + repeated_space + "|";
            figure = figure + line_output + "\n";
        }
        int top_bottom_dashes = 2 * size;
        String dashes = "";
        for (int i=0; i < top_bottom_dashes; i++)
        {
        	dashes = dashes + '-';
        }
        figure = "+" + dashes + "+\n" + figure + "+" + dashes + "+\n";
        System.out.println(figure);
    }
}
