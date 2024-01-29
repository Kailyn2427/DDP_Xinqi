#import sys

a = 0
b = 0
c = 0
list_A = []
list_B = []
list_C = []

pos_dict = {"BankService": list_A,
            "InsureService": list_B,
            "FinanceService": list_C}


def append_queue():
    """
    :Pick-up system
    :return:
    """
    global a, b, c

    while True:
        choice = int(input('Please select business type: 1. Bank card business 2. Social security card business 3. Financial card business 4. Exit\n'))

        if choice == 1:
            a += 1
            A_num = "A" + str(a)
            list_A.append(A_num)
            pos_dict["BankService"] = list_A
            print("Your queue number is A%d. Currently, you have selected a bank card service。\n" % a)

        elif choice == 2:
            b += 1
            B_num = "B" + str(b)
            list_B.append(B_num)
            pos_dict["InsureService"] = list_B
            print("Your queue number is B%d. Currently, you have selected a social security card service.\n" % b)

        elif choice == 3:
            c += 1
            C_num = "C" + str(c)
            list_C.append(C_num)
            pos_dict["FinanceService"] = list_C
            print("Your queue number is B%d. Currently, you have selected a financial card service\n" % c)
        else:
            # sys.exit() and break
            return


def pop_queue():
    """
    :call signalling system
    :return:
    """

    while True:
        choice = int(input('Please enter the current window type: 1. Bank card business 2. Social security card business 3. Financial card business 4. Exit \n'))

        if choice == 1:
            if len(list_A) == 0:
                print("At present, the bank card business window is idle and no one is queuing up")
            else:
                pop_num = list_A.pop(0)
                print("Please go to the bank card service window for customer% s to process the transaction. The current queue is% d people\n" % (pop_num, len(list_A)))

        elif choice == 2:
            if len(list_B) == 0:
                print("At present, the social security card business window is idle and no one is queuing up")
            else:
                pop_num = list_B.pop(0)
                print("Please go to the social security card service window for customer% s to process the transaction. The current queue size is% d people\n" % (pop_num, len(list_B)))

        elif choice == 3:
            if len(list_C) == 0:
                print("At present, the financial card business window is idle and no one is queuing up")
            else:
                pop_num = list_C.pop(0)
                print("Please ask customer% s to go to the financial card business window to process the transaction. The current queue size is% d people\n" % (pop_num, len(list_C)))
        else:
            return


if __name__ == '__main__':
    """
    main program
    """
    while True:
        choice = int(input('Please select your requirements:1.Take a number 2.Calling Number 3.Exit \n'))

        if choice == 1:
            append_queue()
        elif choice == 2:
            pop_queue()
        else:
            break
