def main():
    num_states = int(input("Enter the number of states: "))
    alphabet = input("Enter the input alphabet (comma-separated): ").split(",")  # Split by comma
    alphabet = [s.strip() for s in alphabet] # Remove extra spaces

    transition_table = {}
    print(f"Enter the next state for each state and input (state,input,next_state). Type 'done' when finished.")
    while True:
        transition_str = input()
        if transition_str.lower() == 'done':
            break
        try:  # Added try-except for better error handling
            state_str, input_char, next_state_str = transition_str.split(",")
            state = int(state_str.strip())
            input_char = input_char.strip()
            next_state = int(next_state_str.strip())

            if state not in transition_table:
                transition_table[state] = {}
            transition_table[state][input_char] = next_state
        except ValueError:
            print("Invalid transition format. Please use 'state,input,next_state'.")
        except Exception as e:
            print(f"An error occurred: {e}")

    initial_state = int(input("Enter the initial state: "))

    num_accepting_states = int(input("Enter the number of accepting states: "))
    accepting_states_str = input("Enter the accepting states (separated by spaces): ").split()
    accepting_states = set(int(s.strip()) for s in accepting_states_str)

    while True:
        input_string = input("Enter input string (or 'q' to quit): ")
        if input_string.lower() == 'q':
            break

        current_state = initial_state
        for char in input_string:
            if char not in alphabet:
                print("REMARKS: Invalid input string (symbol not in alphabet)")
                break
            if current_state not in transition_table or char not in transition_table[current_state]:
                print("REMARKS: Undefined transition")
                break

            current_state = transition_table[current_state][char]
        else:  # The else executes if the loop completes without a break
            if current_state in accepting_states:
                print("REMARKS: Accepted")
            else:
                print("REMARKS: Rejected")

if __name__ == "__main__":
    main()