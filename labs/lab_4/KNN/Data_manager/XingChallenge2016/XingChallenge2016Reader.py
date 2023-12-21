#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 14/09/17

@author: Maurizio Ferrari Dacrema
"""


import zipfile, os

from Data_manager.DataReader import DataReader


class XingChallenge2016Reader(DataReader):

    DATASET_URL = "https://polimi365-my.sharepoint.com/:u:/g/personal/10322330_polimi_it/EcbIq2Iz731KnyWE9-CT-AYBPeIWINqWGMFC4t2TGpX9Tg?e=4nMDEK"

    DATASET_SUBFOLDER = "XingChallenge2016/"
    AVAILABLE_ICM = ["ICM_all"]


    def _get_dataset_name_root(self):
        return self.DATASET_SUBFOLDER



    def _load_from_original_file(self):
        # Load data from original

        print("XingChallenge2016Reader: Loading original data")

        compressed_zip_file_folder = self.DATASET_OFFLINE_ROOT_FOLDER + self.DATASET_SUBFOLDER
        decompressed_zip_file_folder = self.DATASET_SPLIT_ROOT_FOLDER + self.DATASET_SUBFOLDER

        zipFile_name = "xing_challenge_data_2016.zip"

        try:

            dataFile = zipfile.ZipFile(compressed_zip_file_folder + zipFile_name)

            impressions_path = dataFile.extract("data/impressions.csv", path=decompressed_zip_file_folder + "decompressed/")
            interactions_path = dataFile.extract("data/interactions.csv", path=decompressed_zip_file_folder + "decompressed/")

            ICM_path = dataFile.extract("data/items.csv", path=decompressed_zip_file_folder + "decompressed/")
            UCM_path = dataFile.extract("data/users.csv", path=decompressed_zip_file_folder + "decompressed/")

        except (FileNotFoundError, zipfile.BadZipFile):

            print("XingChallenge2016Reader: Unable to find or extract data zip file.")
            print("XingChallenge2016Reader: Automatic download not available, please ensure the ZIP data file is in folder {}.".format(compressed_zip_file_folder))
            print("XingChallenge2016Reader: Data zip file not found or damaged. You may download the data from: {}".format(self.DATASET_URL))

            # If directory does not exist, create
            if not os.path.exists(compressed_zip_file_folder):
                os.makedirs(compressed_zip_file_folder)

            raise FileNotFoundError("Automatic download not available.")




        self.tokenToFeatureMapper_ICM = {}


        # print("XingChallenge2016Reader: Loading Impressions")
        # self.URM_impressions = self._load_impressions(impressions_path, if_new_user = "add", if_new_item = "add")

        print("XingChallenge2016Reader: Loading item content")
        self.ICM_all, self.tokenToFeatureMapper_ICM_all, self.item_original_ID_to_index = self._load_ICM(ICM_path, if_new_item = "add")

        print("XingChallenge2016Reader: Loading Interactions")
        self.URM_all, _, self.user_original_ID_to_index = self._load_interactions(interactions_path, if_new_user = "add", if_new_item = "ignore")



        print("XingChallenge2016Reader: cleaning temporary files")

        import shutil

        shutil.rmtree(decompressed_zip_file_folder + "decompressed/", ignore_errors=True)

        print("XingChallenge2016Reader: loading complete")



    #
    #
    # def _load_impressions(self, impressions_path, if_new_user ="add", if_new_item ="ignore"):
    #
    #
    #
    #     if if_new_user not in ["add", "ignore", "exception"]:
    #         raise ValueError("DataReader: if_new_user parameter not recognized. Accepted values are 'add', 'ignore', 'exception', provided was '{}'".format(if_new_user))
    #
    #     if if_new_item not in ["add", "ignore", "exception"]:
    #         raise ValueError("DataReader: if_new_item parameter not recognized. Accepted values are 'add', 'ignore', 'exception', provided was '{}'".format(if_new_item))
    #
    #     if if_new_user == "ignore":
    #         if_new_user_get_user_index = "exception"
    #     else:
    #         if_new_user_get_user_index = if_new_user
    #
    #     if if_new_item == "ignore":
    #         if_new_item_get_item_index = "exception"
    #     else:
    #         if_new_item_get_item_index = if_new_item
    #
    #
    #
    #
    #
    #     fileHandle = open(impressions_path, "r")
    #
    #     # Use array as for datasets this big lists would require more than 10GB of RAM
    #     dataBlock = 10000000
    #
    #     values = np.zeros(dataBlock)
    #     rows = np.zeros(dataBlock)
    #     cols = np.zeros(dataBlock)
    #
    #     numCells = 0
    #
    #     # Remove header
    #     fileHandle.readline()
    #
    #
    #     for line in fileHandle:
    #
    #         line = line.split(" ")
    #
    #         """
    #         Which items were shown by the existing XING job recommender to which user in which week of the year.
    #
    #         user_id     ID of the user (points to users.id)
    #         year
    #         week        of the year
    #         items       is a comma-separated list (not set) of items that were displayed to the user (point to items.id)
    #         """
    #
    #
    #
    #         user_id = line[0]
    #         year = line[1]
    #         week = line[2]
    #         item_list = line[3]
    #
    #
    #         try:
    #             user_index = self._get_user_index(user_id, if_new = if_new_user_get_user_index)
    #         except KeyError:
    #             # Go to next line
    #             print("XingChallenge2016Reader: Impressions contains user which is not in ICM: {}. Skipping...".format(user_id))
    #             continue
    #
    #
    #
    #         item_list = item_list.split(",")
    #
    #         for item_id in item_list:
    #
    #             if numCells % 1000000 == 0 and numCells!=0:
    #                 print("Processed {} cells".format(numCells))
    #
    #             try:
    #                 item_index = self._get_item_index(item_id, if_new = if_new_item_get_item_index)
    #             except KeyError:
    #                 # Go to next line
    #                 print("XingChallenge2016Reader: Impressions contains item which is not in ICM: {}. Skipping...".format(item_id))
    #                 continue
    #
    #
    #             if numCells == len(rows):
    #                 rows = np.concatenate((rows, np.zeros(dataBlock)))
    #                 cols = np.concatenate((cols, np.zeros(dataBlock)))
    #                 values = np.concatenate((values, np.zeros(dataBlock)))
    #
    #             rows[numCells] = int(user_index)
    #             cols[numCells] = int(item_index)
    #             values[numCells] = True
    #
    #             numCells += 1
    #
    #
    #     fileHandle.close()
    #
    #     return sps.csr_matrix((values[:numCells], (rows[:numCells], cols[:numCells])), dtype=np.float32)




    def _load_interactions(self, impressions_path, if_new_user ="add", if_new_item ="ignore"):


        from Data_manager.IncrementalSparseMatrix import IncrementalSparseMatrix_FilterIDs

        URM_builder = IncrementalSparseMatrix_FilterIDs(preinitialized_col_mapper = self.item_original_ID_to_index, on_new_col = if_new_item,
                                                        preinitialized_row_mapper = None, on_new_row = if_new_user)




        fileHandle = open(impressions_path, "r")

        numCells = 0

        # Remove header
        fileHandle.readline()


        for line in fileHandle:


            if numCells % 1000000 == 0 and numCells!=0:
                print("Processed {} cells".format(numCells))


            line = line.split("\t")

            """
            
            Interactions that the user performed on the job posting items. Fields:

            user_id             ID of the user who performed the interaction (points to users.id)
            item_id             ID of the item on which the interaction was performed (points to items.id)
            interaction_type    the type of interaction that was performed on the item:
                1 = the user clicked on the item
                2 = the user bookmarked the item on XING
                3 = the user clicked on the reply button or application form button that is shown on some job postings
                4 = the user deleted a recommendation from his/her list of recommendation (clicking on "x") which has the effect that the recommendation will no longer been shown to the user and that a new recommendation item will be loaded and displayed to the user
            created_at          a unix time stamp timestamp representing the time when the interaction got created
            """

            user_id = line[0]
            item_id = line[1]

            # transform negative interactions into a negative number
            interaction_type = int(line[2])
            if interaction_type == 4:
                interaction_type = -1

            created_at = line[3]

            URM_builder.add_data_lists([user_id], [item_id], [interaction_type])

            numCells += 1


        fileHandle.close()

        return URM_builder.get_SparseMatrix(), URM_builder.get_column_token_to_id_mapper(), URM_builder.get_row_token_to_id_mapper()




    def _load_ICM(self, ICM_path, if_new_item ="add"):


        from Data_manager.IncrementalSparseMatrix import IncrementalSparseMatrix_FilterIDs

        ICM_builder = IncrementalSparseMatrix_FilterIDs(preinitialized_col_mapper = None, on_new_col = "add",
                                                        preinitialized_row_mapper = None, on_new_row = if_new_item)



        fileHandle = open(ICM_path, "r")

        numCells = 0

        # Remove header
        # id	title	career_level	discipline_id	industry_id	country	region	latitude	longitude	employment	tags	created_at	active_during_test
        fileHandle.readline()


        for line in fileHandle:


            if numCells % 1000000 == 0 and numCells!=0:
                print("Processed {} cells".format(numCells))


            line = line.split("\t")

            """
            id              anonymized ID of the item (referenced as item_id in the other datasets above)
            title           concepts that have been extracted from the job title of the job posting (numeric IDs)
            career_level    career level ID (e.g. beginner, experienced, manager):
                0 = unknown
                1 = Student/Intern
                2 = Entry Level (Beginner)
                3 = Professional/Experienced
                4 = Manager (Manager/Supervisor)
                5 = Executive (VP, SVP, etc.)
                6 = Senior Executive (CEO, CFO, President)
            discipline_id   anonymized IDs represent disciplines such as "Consulting", "HR", etc.
            industry_id     anonymized IDs represent industries such as "Internet", "Automotive", "Finance", etc.
            country         code of the country in which the job is offered
            region          is specified for some users who have as country de. Meaning of the regions: see below.
            latitude        latitude information (rounded to ca. 10km)
            longitude       longitude information (rounded to ca. 10km)
            employment      the type of employment:
                0 = unknown
                1 = full-time
                2 = part-time
                3 = freelancer
                4 = intern
                5 = voluntary
            tags            concepts that have been extracted from the tags, skills or company name
            created_at      a Unix time stamp timestamp representing the time when the interaction got created
            active_during_test is 1 if the item is still active (= recommendable) during the test period and 0 if the item is not active anymore in the test period (= not recommendable)
            """


            item_id = line[0]
            job_title_id_list = line[1]
            job_title_id_list = job_title_id_list.split(",")

            career_level = line[2]

            discipline_id = line[3]
            discipline_id = discipline_id.split(",")

            industry_id = line[4]
            industry_id = industry_id.split(",")

            country = line[5]
            region = line[6]
            latitude = line[7]
            longitude = line[8]
            employment = line[9]

            tags_list = line[10]
            tags_list = tags_list.split(",")

            created_at = line[11]
            active_during_test = line[12]


            item_token_list = [*job_title_id_list, career_level, *discipline_id, *industry_id, country, region, employment, *tags_list]


            ICM_builder.add_single_row(item_id, item_token_list, data=1.0)

            numCells += 1


        fileHandle.close()

        return ICM_builder.get_SparseMatrix(), ICM_builder.get_column_token_to_id_mapper(), ICM_builder.get_row_token_to_id_mapper()

