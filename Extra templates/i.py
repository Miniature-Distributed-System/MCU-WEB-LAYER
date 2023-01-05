import os, csv
with open(r"D:\Miniature Compute Unit Web Layer\MCU\CSV UPLOADS\candidate_algo.csv") as csv_file:
                                csvfile = csv.reader(csv_file,delimiter=",")
                                for row in csvfile:
                                    
                                    print(row[0])
                                    print(row[1])
                                    print(row[2])
                                    print(row[3])
                                    print(row[4])
                                    print(row[5])
                                    print(row[6])
                                    
                    
                                