alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def secure(string,output_type = "any",min="",max=""):
    """ takes in a prompt and runs input with that prompt, 
    checks if the type of the user response matches with the expected output type (str or int),
    if the type is wrong prints 'Invalid' and asks again,
    if type is not int or str, supports mixed inputs,
    has optional min and max values for controling the value of int or the size of str,
    if there is a need for no lower bound but also a need for a higher bound or vice versa-
    input empty string in place of the unbounded constraint"""
    while True:
        a = input(string)
        b = False
        c = False
        if output_type == int:
            if a.isdigit():
                if min == "":
                    b = True
                else:
                    if int(a) >= min:
                        b = True
                if max == "":
                    c = True
                else:
                    if int(a) <= max:
                        c = True
                if c and b:
                    return int(a)
                else:
                    print("Out of range")
                    continue
        else: 
            d = output_type == str
            if a.isalpha() or not d:
                if min == "":
                    b = True
                else:
                    if len(a) >= min:
                        b = True
                if max == "":
                    c = True
                else:
                    if len(a) <= max:
                        c = True
                if c and b:
                    return a
                else:
                    print("Out of range")
                    continue
        # else:
            #raise TypeError(f"Output type {output_type} is not supported")

        print("Invalid")
        