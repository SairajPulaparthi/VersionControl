from console_gfx import ConsoleGfx

#SairajPulaparthi
#RLE PART A
from console_gfx import ConsoleGfx
#create definition
def menu_display():
    print("Welcome to the RLE image encoder")
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)
    print('1. Load Image')
    print('2. Test Image')
    print("3. Read RLE String")
    print('4. Read RLE Hex String')
    print('5. Read Data Hex String')
    print('6. Display Image')
    print("7. Display RLE string")
    print("8. Display Hex RLE data")
    print("9. Display Hex Flat data")


def to_hex_string(data):
    string = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']
    hex_string = ("")
    for number in data:
        hex_string += str(string[number])
    return hex_string


# definition of number of runs in data set
def count_runs(flat_data):
    difference = flat_data[0]
    equal = 0
    keep =1
    for number in flat_data:
        if number == difference:
            equal += 1
        if number != difference:
            keep += 1
            equal = 0

        if equal == 15:
            equal= 0
            keep += 1
        difference = number
    return keep

# returns encoding in RLE raw data that is passed
def encode_rle(flat_data):

    count = 1
    bit = flat_data[0]
    rle= []
    for num in range(1, len(flat_data)):
        if flat_data[num-1] == flat_data[num] and count < 15:
            count += 1
        else:
            rle.extend([count, bit])
            bit = flat_data[num]
            count = 1
    rle.extend([count, bit])
    return rle

#returns decompressed size RLE data
def get_decoded_length(rle_data):
    i = 0
    length = 0


    while i < len(rle_data):
        keep = rle_data[i]
        i += 2
        length += keep


    return length


#returns the decoded data set from RLE data

def decode_rle(rle_data):
    end = []
    for i in range(0, len(rle_data), 2):
        for keep in range(rle_data[i]):
            end.append(rle_data[i+1])
    return end

#translates hexadecimal string to byte data
def string_to_data(data_string):
    data = list(data_string)
    i = 0

    while i < len(data):

        data[i]= int(data[i],16)
        i = i+1

    return data


def to_rle_string(rle_data):

    rle = ""
    for i in range(0, len(rle_data), 2):
        rle += str(rle_data[i])
        if rle_data[i+1] == 10:
            rle += 'a'
        elif rle_data [i+1] == 11:
            rle += 'b'
        elif rle_data[i+1] == 12:
            rle += 'c'
        elif rle_data[i+1] == 13:
            rle += 'd'
        elif rle_data[i+1] == 14:
            rle += 'e'
        elif rle_data[i+1]== 15:
            rle += 'f'
        else:
            rle += str(rle_data[i+1])
        if not i + 1 == len(rle_data) -1:
            rle += ":"
    return rle





def string_to_rle(rle_string):
    rle =[]
    data = rle_string.split(':')
    for i in data:
        if len(i) == 3:
            length = int(i[0:2])
        else:
            length = int(i[0])
        if i[-1] == "a":
            data = 10
        elif i[-1] == "b":
            data = 11
        elif i[-1] == "c":
            data = 12
        elif i[-1] == 'd':
            data = 13
        elif i[-1]== 'e':
            data = 14
        elif i[-1] == 'f':
            data = 15
        else:
            data = int(i[-1])
        rle.extend([length,data])
    return rle


#define the function underneath
if __name__ == '__main__':
    image_data = None
    user = 0
    while True:

        print("")
        print("")
        print("")
        print("")
        menu_display()
        user = input("Select Menu Option")
        if user == "0":
            print("goodbye")
            break
        elif user == "1":
                enter_file = input("Enter the file:")
                image_data = ConsoleGfx.load_file(enter_file)
        elif user == "2":
                image_data = ConsoleGfx.load_file("testfiles/gator.gfx")
                print('Test data Loaded')
        elif user == "3":
                rle_string = input("Enter an Rle string to decode")
                image_data = decode_rle(string_to_data(rle_string))
        elif user == '4':
                rle_string = input("Enter the Hex String that has RLE data")
                image_data = decode_rle(string_to_data(rle_string))
        elif user == "5":
                rle_string = input("Enter the Hex string that has flat data")
        elif user == "6":
                print("Displaying image...")
                ConsoleGfx.display_image(image_data)
        elif user == "7":
                print(f'Rle Representation: {to_rle_string(encode_rle(image_data))}')
        elif user == "8":
                print(f'RLE Hex values: {to_hex_string(encode_rle(image_data))}')
        elif user == "9":
                flat = to_hex_string(image_data)
                print(f'Flat hex values: {(flat)}')
        else:
                print("Error! Invalid Input.")











