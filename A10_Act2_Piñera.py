if __name__ == "__main__":
    num_States = int(input("Enter the number of states: "))
    inputAlpha = input("Enter the input alphabet (comma separated): ").split(",")
    Output = input("Enter the output alphabet (comma separated): ").split(",")

    transition_table = {}
    for i in range(num_States):
        transition_table[i] = {}
        for char in inputAlpha:
            while True:
                    transition_input = input(f"Transition (q{i},{char}) to transition q")
                    transition = int(transition_input)
                    if 0 <= transition < num_States:
                        break
                    else:
                        print(f"Invalid transition. Enter a state between 0 and {num_States - 1}.")
            while True:
                output = input("Output: ")
                if output in Output:
                    break
                else:
                    print(f"Invalid output. Enter an output from {Output}.")

            transition_table[i][char] = (transition, output)

    while True:
        input_string = input("Enter input sequence (or 'x' to quit): ")
        if input_string == 'x':
            break

        current_state = 0
        output_string = ""

        for char in input_string:
            if char not in inputAlpha:
                output_string = "Invalid input character."
                break

            next_state, output = transition_table[current_state][char]
            current_state = next_state
            output_string += output

        if output_string == "Invalid input character.":
            print(output_string)
        else:
            print(f"Output Sequence: {output_string}")
