import time
import random



def random_numbers():
    """
    This function generates a random number
    """
    selected_number = random.randint(1, 100)
    return selected_number

def ticket_gen(n):
    """
    This function generates tickets with random numbers
    Takes as an argument how many numbers we want in the ticket
    """
    numbers_list = list(range(1, 100))
    random.shuffle(numbers_list)
    ticket = []
    i = 0
    while i <= n:
        ticket.append(numbers_list[i])
        i += 1
    print(len(ticket))
    return ticket




ticket = ticket_gen(2)
ticket_2 = ticket_gen(2)

# print(ran_num)
print("this is the initial ticket", ticket)
def check_ticket(ticket):
    """
    This is a function to generate random number
    and check if the number is in one ticket
    """
    j = 0
    while len(ticket) > 0:
        for i in ticket:
            ran_num = random_numbers()
            j+=1
            print("this is the random number", ran_num)
            if ran_num == i:
                print(ticket)
                ticket.remove(i)
                print(ticket)
            else:
                print(ran_num, "is not in the ticket")
    print("Rounds to find the winning ticket:", j)



def gen_bundle(quantity, ticket_len):
    """
    This is the bundle generator.
    Takes as arguments the number of tickets we want in a bundle
    and the number of numbers in a ticket
    """
    bundle = []
    for j in range(quantity):
        ticket = ticket_gen(ticket_len)
        bundle.append(ticket)

    return bundle

# print(gen_bundle(5, 5))


def check_bundle_t(bundle):
    j = 0
    print("The start bundle is:", bundle)
    for tick in bundle:
        while len(tick)>0:
            for i in tick:
                ran_num = random_numbers()
                j+=1
                print("this is the random number", ran_num)
                if ran_num == i:
                    print(tick)
                    ticket.remove(i)
                    print(tick)
                else:
                    print(ran_num, "is not in the bundle")
    print("Rounds to find the winning ticket:", j)
    print("The end bundle is:", bundle)

check_bundle_t(gen_bundle(3, 3))