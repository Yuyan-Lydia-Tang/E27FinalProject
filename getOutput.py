"""
getOutput.py uses computer vision library cv2 and scientific computing library
numpy to process raw input photos downloaded online. Training set data include 
both the color of the image and the edge detected by cv2.

Input includes four files: 
targetFile: data stroing index, category, brand, color of sale item
inputFile: convert image files into numeric version, used as the training set
outputFile: for each image file, create the target set
noiseFile: there are noise input image files when downloading images online,
ignore these files when processing training data
"""

import cv2
import numpy
from defClothes import *

def getTarget(targetFile, imageFilenameRoot, inputFile, outputFile, noiseFile):

        target = open(targetFile, "r")
        outfile = open(outputFile, "w")
        infile = open(inputFile, "w")
        noise = open(noiseFile, "r")

        diversity = len(article_text)
        num_list = [0] * diversity
        noise_list = []

        # max_num sets the limit for each category, maintaining balance of training set
        max_num = 210

        verbose = False

        while 1:

                line = noise.readline().split()
                if len(line) == 0: break
                noise_list.append(line[0])

        while 1:
                line = target.readline().split()
                if len(line) == 0: break

                if line[0] in noise_list:
                        print "noise"
                        continue
                for index in range(diversity):
                        # if index in [3, 4, 5, 6, 7, 8]:
                        #       max_num = 210
                        # else:
                        #       max_num = 1000

                        if line[1].lower() in article_list[index]:
                                if num_list[index] <= max_num:
                                        output = "0 " * index + "1 " + "0 " * (diversity-index-1)
                                        outfile.write( output + "\n")
                                        num_list[index] = num_list[index] + 1

                                        image_rgb = cv2.imread(imageFilenameRoot + line[0]+".jpg")

                                        image_rgb = cv2.resize(image_rgb, (w,h), image_rgb, 0, 0, cv2.INTER_LANCZOS4)
                                        edges = cv2.Canny(image_rgb, 100, 200)

                                        image = image_rgb

                                        for x in range(image.shape[0]):
                                                for y in range(image.shape[1]):
                                                        pixel = float(edges[x][y])/255.0
                                                        infile.write("%.4f " % pixel)

                                                        for c in range(image.shape[2]):
                                                                color = float(image[x][y][c])/255.0

                                                                infile.write("%.4f " % color)

                                        infile.write("\n")


                                        if verbose:
                                                print article_text[index], output, line
                                        break

        for i in range(diversity):
                print article_text[i], num_list[i]

        target.close()
        outfile.close()
        infile.close()
        noise.close()


getTarget("inputs/all.dat","img/lg-", "inputs/inputs2.dat", "inputs/targets2.dat", "inputs/noise.dat")
