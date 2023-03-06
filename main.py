import numpy as np
import sys

def split_msg(msg: str):
    stripped_msg = msg.replace(" ", "").upper()
    return_arr = []
    temp_arr = []
    for i in range(len(stripped_msg)):
        if i % 2 == 0 and i != 0:
            return_arr.append(temp_arr)
            temp_arr = []
        temp_arr.append(stripped_msg[i])
    if len(temp_arr) == 1:
        temp_arr.append(temp_arr[0])
    return_arr.append(temp_arr)
    return return_arr

def msg_to_vectors(split_msg):
    return_array = []
    letters = list("ZABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for block in split_msg:
        vector = [None, None]
        vector[0] = [int(letters.index(block[0]))]
        vector[1] = [int(letters.index(block[1]))]
        return_array.append(vector)
    return np.array(return_array)

def vectors_to_msg(vectors):
    return_string = "" 
    letters = "ZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for vector in vectors:
        return_string += letters[vector[0][0]]
        return_string += letters[vector[1][0]]
    return return_string

def encode(vectors):
    return_arr = []
    for vector in vectors:
        result = np.matmul(np.array([[1, 1], [0, 3]]), np.array([vector[0], vector[1]]))
        return_arr.append(result)
    return np.remainder(return_arr, 26)

def decode(vectors):
    return_arr = []
    for vector in vectors:
        result = np.matmul(np.array([[1, 17], [0, 9]]), np.array([vector[0], vector[1]]))
        return_arr.append(result)
    return np.remainder(return_arr, 26)

if __name__ == "__main__":
    if sys.argv[1] == "-e" or sys.argv[1] == "-encode":
        print(vectors_to_msg(encode(msg_to_vectors(split_msg(sys.argv[2])))))
    elif sys.argv[1] == "-d" or sys.argv[1] == "-decode":
        print(vectors_to_msg(decode(msg_to_vectors(split_msg(sys.argv[2])))))
