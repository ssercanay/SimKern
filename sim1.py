from __future__ import division
from Sim1FileProcessingService import Sim1FileProcessingService
from ThirdPartyProgramCaller import ThirdPartyProgramCaller
import os


class sim1(object):

    def __init__(self, data_file, file_type, number_of_genomes, number_of_trials, path=os.getcwd()):
        self.data_file = data_file
        self.file_type = file_type
        self.number_of_genomes = int(number_of_genomes)
        self.trials = int(number_of_trials)
        self.path = path

    def generateSimilarityMatrix(self):
        sim1FileProcessor = Sim1FileProcessingService(self.data_file, self.file_type, self.number_of_genomes, self.trials)
        sim1_file_list = sim1FileProcessor.createTrialFiles()
        programCaller = ThirdPartyProgramCaller(self.path, self.file_type, sim1_file_list)
        if self.file_type == "m":
            sim1_response_list = programCaller.getOctaveSim1Responses()
        elif self.file_type == "r":
            sim1_response_list = programCaller.getRSim1Responses()
        response_matrix  = self.generateResponseMatrix(sim1_response_list)
        similarity_matrix = self.computeSimilarityScores(response_matrix)
        return similarity_matrix


    def generateResponseMatrix(self, response_list):
        response_matrix = []
        for genome in range(self.number_of_genomes):
            response_matrix.append([])
        pos = 0
        for trial in range(self.trials):
            for genome in range(self.number_of_genomes):
                response_matrix[genome].append(response_list[pos])
                pos += 1
        return response_matrix


    def computeSimilarityScores(self, response_matrix):
        kernel = range(self.number_of_genomes)
        for i in range(0, self.number_of_genomes):
            kernel[i] = range(self.number_of_genomes)
            kernel[i][i] = 1

        for i in range(0, self.number_of_genomes - 1):
            for j in range(i + 1, self.number_of_genomes):
                numValid = 0
                count = 0
                for k in range(0, self.trials):
                    if response_matrix[i][k] is not int(-1) and response_matrix[j][k] is not int(-1):
                        numValid = numValid+1
                        if response_matrix[i][k] == response_matrix[j][k]:
                            count = count + 1
                if numValid==0:
                    score=None
                else:
                    score = count / numValid
                kernel[i][j] = score
                kernel[j][i] = score

        return kernel
