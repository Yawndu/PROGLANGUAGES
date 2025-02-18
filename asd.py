class MealyMachine:
    def __init__(self, states, initial_state, transitions):
        self.states = states
        self.current_state = initial_state
        self.transitions = transitions

    def process_input(self, input_value):
        if (self.current_state, input_value) in self.transitions:
            next_state, output = self.transitions[(self.current_state, input_value)]
            self.current_state = next_state
            return output
        else:
            return None


def get_mealy_machine_definition():
    states_str = input("Enter states (comma-separated): ")
    states = set(states_str.split(","))

    initial_state = input("Enter initial state: ")

    inputs_str = input("Enter inputs (comma-separated): ")
    inputs = set(inputs_str.split(","))

    outputs_str = input("Enter outputs (comma-separated): ")
    outputs = set(outputs_str.split(","))

    transitions = {}
    print(f"Enter transitions in the format: Current State,Input,Next State,Output (one per line, type 'done' to finish):")
    while True:
        transition_str = input()
        if transition_str.lower() == 'done':
            break
        try:
            current_state, input_val, next_state, output = transition_str.split(",")
            if current_state in states and input_val in inputs and next_state in states and output in outputs:
                transitions[(current_state, input_val)] = (next_state, output)
            else:
                print("Invalid transition: State or input/output value is not defined.")
        except ValueError:
            print("Invalid transition format. Please use: Current State,Input,Next State,Output")

    return states, initial_state, transitions, inputs, outputs


def main():
    states, initial_state, transitions, inputs, outputs = get_mealy_machine_definition()

    mealy_machine = MealyMachine(states, initial_state, transitions)

    while True:
        input_sequence_str = input("Enter input sequence (comma-separated, or 'exit' to quit): ")
        if input_sequence_str.lower() == 'exit':
            break

        input_sequence = input_sequence_str.split(",")

        # Validate input sequence against defined inputs
        valid_input = all(input_val in inputs for input_val in input_sequence)
        if not valid_input:
            print(f"Invalid input sequence. Inputs must be from the set: {inputs}")
            continue

        output_sequence = []

        print("Input\tOutput")
        for input_value in input_sequence:
            output = mealy_machine.process_input(input_value)
            output_sequence.append(output)
            print(f"{input_value}\t{output}")

        print("Output Sequence:", output_sequence)


if __name__ == "__main__":
    main()