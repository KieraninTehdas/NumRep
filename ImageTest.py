from scipy import misc
import matplotlib.pyplot as plt
import numpy as np
import sys

# This file contains functions to read an image from a file to a numpy array,
# calculate the cross correlation between lines in the image, and use the
# phase difference between lines to correct shifted lines.

# N.B!!! Image name is hard coded, not read in from user input!!

# Function to read the image into an np array.
# Takes name of image as argument. Returns the image array.
# Originally provided by Will Hossack, with a few modifications.

def read_image(file_name):


    # Read file into np array
    image = misc.imread(file_name)
    print("Reading image {0}".format(file_name))

    return image

# Function to calculate the cross correlation between two lines of an image.
# Takes two lines as arguments and returns the phase difference between the lines.

def cross_correlate(line1, line2):

    # Fourier transform each line

    f = np.fft.fft(line1)
    g = np.fft.fft(line2)

    # Shift the zero frequency component of each spectrum to centre of array.
    # Example from np.fft documentation : array([ 0.,  1.,  2.,  3.,  4., -5., -4., -3., -2., -1.])
    # is shifted to array([-5., -4., -3., -2., -1.,  0.,  1.,  2.,  3.,  4.]) by function.

    f_shift = np.fft.fftshift(f)
    g_shift = np.fft.fftshift(g)

    # Take the complex conjugate of the first shifted transform.

    f_star = np.conj(f_shift)

    # Take the product of the transforms.

    fourier_space_correlation = [a*b for a,b  in zip(f_star, g_shift)]

    # Inverse Fourier transform the product to get the cross correlation.

    correlation = np.fft.ifft(fourier_space_correlation)

    # Find the index of the position of the maximum of the cross correlation power spectrum.
    # This is the phase of the correlation.

    phase = np.argmax(correlation)

    return phase

#############################################################################################
#############################################################################################

def main():

    # Name of image to be read. "image" is original image, used for comparison.

    image_name = "desync2.pgm"

    image = read_image(image_name)

    corrected_image = read_image(image_name)


    #print(len(corrected_image))


    for i in range(0, len(corrected_image)-2):

        # This block is just to show a progress bar, so it's obvious something is happening.
        # Can be commented out if required. Shouldn't cause problems!
        progress = 10*i/(len(corrected_image)-3)
        sys.stdout.write('\r')
        sys.stdout.write("Correlating lines [%-10s] %d%%" % ('='*progress, 10*progress))
        sys.stdout.flush()

        # Find phases of cross correlations for three consecutive lines.

        phase_12 = cross_correlate(corrected_image[i], corrected_image[i+1])
        #print("Phase12 ={0}".format(phase_12))
        phase_13 = cross_correlate(corrected_image[i], corrected_image[i+2])
        # print("Phase13 ={0}".format(phase_13))
        phase_23 = cross_correlate(corrected_image[i+1], corrected_image[i+2])
        # print("Phase23 ={0}".format(phase_23))

        # Corrects shifted middle line shifted
        ###################
            ####################
        ###################

        if ((phase_13 ==0) and (phase_12 != 0) and (np.abs(phase_23) == len(corrected_image[0])-phase_12)):

            corrected_image[i+1] = np.roll(corrected_image[i+1], -phase_12)
            #print("CASE 1 !!!!!!!!!!!!!!!!!!!!!!!!!!!")

        # Corrects when both lines shifted wrt first
        #######################
           ########################
               #########################

        if ((phase_12 !=0) and (phase_13 !=0) and (phase_23 != 0)):
            corrected_image[i+1] = np.roll(corrected_image[i+1], -phase_12)
            corrected_image[i+2] = np.roll(corrected_image[i+2], -(phase_12+phase_23))
            #print("CASE 2 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

        # Corrects if third line is shifted wrt first two
        ##########################
        ##########################
            #############################

        if ((phase_12 ==0) and (phase_23 != 0) and (phase_13 == phase_23)):
            corrected_image[i+2] = np.roll(corrected_image[i+2], -phase_13)

            #print("CASE 3!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

        # Check if no lines shifted.
        ############################
        ############################
        ############################

        #if ((phase_12 == 0) and (phase_23 == 0) and (phase_13 ==0)):
            #print("CASE 4. ALL GOOD BRUH.")


    print("\n Done!") # Gives carriage return after progress bar.

    # Show original and corrected images for comparison.

    plt.figure(1)
    plt.subplot(121)
    plt.imshow(image, cmap = 'gray')
    plt.subplot(122)
    plt.imshow(corrected_image, cmap = 'gray')
    #plt.subplot(133)
    #plt.hist()

    plt.show()

main()
