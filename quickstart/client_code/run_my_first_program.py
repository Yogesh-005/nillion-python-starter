from nada_dsl import *

def nada_main():
    alice = Party(name="Alice")  # party 0
    bob = Party(name="Bob")  # party 1
    charlie = Party(name="Charlie")  # party 2

    alice_salary = SecretInteger(Input(name="alice_salary", party=alice))
    bob_salary = SecretInteger(Input(name="bob_salary", party=bob))
    charlie_salary = SecretInteger(Input(name="charlie_salary", party=charlie))

    # Find the median using conditional logic
    median = (alice_salary > bob_salary).if_else(
        (bob_salary > charlie_salary).if_else(bob_salary, 
                                              (alice_salary > charlie_salary).if_else(charlie_salary, alice_salary)),
        (alice_salary > charlie_salary).if_else(alice_salary,
                                                (bob_salary > charlie_salary).if_else(charlie_salary, bob_salary))
    )

    out = Output(median, "median_salary", alice)

    return [out]
