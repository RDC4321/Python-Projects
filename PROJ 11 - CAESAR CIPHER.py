#project that uses the Caesar Cipher to encrypt & decrypt messages. It basically shifts the letters based on the number the user inputs.
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
end = False
#function that does the encrypting and decrypting of characters
def caesar (original_text,shift_amount, choice):
    output = ""
    #the encrypting part of the function.
    if choice in ['Encode','encode']:
        print(f"Your message: '{text}' has been encrypted:")
        for loop1 in original_text:
            if loop1 not in alphabet:
                output += loop1
            else:
                shift_amount = int(alphabet.index(loop1)) + shift
                shift_amount %= len(alphabet)
                output += alphabet[shift_amount]
        print(f"The {choice}d result is: {output}")
    #the decrypting part of the function.
    elif choice in ['Decode','decode']:
        print(f"Your message '{text}' has been decrypted:")
        for loop2 in original_text:
            if loop2 not in alphabet:
                output += loop2
            else:
                shift_amount = int(alphabet.index(loop2)) - shift
                shift_amount %= len(alphabet)
                output += alphabet[shift_amount]
        print(f"The {choice}d result is: {output}")
    #if the input is none of the choices, the program ends.
    else:
        print("Invalid Input")
        end = True

print("Caesar Cipher!")
#while loop that repeats the program until user specifies it to end.
while end!= True:
    choice = str(input("Type 'encode' to encrypt and 'decode' to decrypt: "))
    text = input("Input your message: \n").lower()
    shift = int(input("Input the shift number: \n"))
    #calls the function after getting the inputs. The inputs will be used in the function
    caesar(text,shift,choice)

    #for loop at the end that asks the user if they want to try again or not.
    repeat = str(input("\nWould you like to try again? (Yes / No): "))
    if repeat in ['No','no']:
        end = True
    elif repeat in ['Yes','yes']:
        end = False
    else:
        print("Invalid Input, ending session")
        end = True