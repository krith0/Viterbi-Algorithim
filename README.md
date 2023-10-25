# Viterbi-Algorithim
This repo consists of Convolutional Encoder and decoding part is done using Viterbi Algorithm. The code is written with k = 7, code rate = 1/2 as constraints. 

The input.py simply convert the image file into a binary file which is then fed to the encoder which encodes the input file and saves it as encoded_bits.txt. the encodd_bits.txt is then fed to the decoder which is constructed w.r.t the constraints mentioned above. The decoded_bits.txt consists of the decoded bits. The comparision.py compares the input_bits_txt and decoded_bits.txt for match percentage. There are no noise added in this code so the input bits and the output bits must remain same. the analysis.py consist of all the information regarding the performance of the code. 
