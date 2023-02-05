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
                                    
                    
# tree code

#   <!-- <h1 style="color: black; margin-left: 268px; font-size: larger;">RESULT :</h1> -->
#   <!-- <div style = "margin-left: 500px;" class="tree">
#     <ul>
#       <li>
#         <a href="#">{&nbsp;&nbsp;&nbsp;0,0,0,0,0,0,0&nbsp;&nbsp;&nbsp;}</a>&nbsp;&nbsp;S0<br><br>
#         <a href="#">{&nbsp;&nbsp;&nbsp;sunny,warm,normal,strong,warm,same&nbsp;&nbsp;&nbsp;}</a>&nbsp;&nbsp;S1<br><br>
#         <a href="#">{&nbsp;&nbsp;&nbsp;sunny,warm,?,strong,warm,same&nbsp;&nbsp;&nbsp;}</a>&nbsp;&nbsp;S2&nbsp;S3<br><br>
#         <a href="#">{&nbsp;&nbsp;&nbsp;sunny,warm,?,strong,?,?&nbsp;&nbsp;&nbsp;}</a>&nbsp;&nbsp;S4<br><br>
#           <a href="#">{&nbsp;&nbsp;&nbsp;sunny,?,?,strong,?,?&nbsp;&nbsp;&nbsp;}</a>
#           <a href="#">{&nbsp;&nbsp;&nbsp;sunny,warm,?,?,?,?&nbsp;&nbsp;&nbsp;}</a>
#           <a href="#">{&nbsp;&nbsp;&nbsp;?,warm,?,strong,?,?&nbsp;&nbsp;&nbsp;}</a><br><br>
#           <a href="#">{&nbsp;&nbsp;&nbsp;sunny,?,?,?,?,?&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?,warm,?,?,?,?&nbsp;&nbsp;&nbsp;}</a>&nbsp;&nbsp;G4<br><br>
#           <a href="#">{&nbsp;&nbsp;&nbsp;sunny,?,?,?,?,?&nbsp;&nbsp;&nbsp;&nbsp;?,warm,?,?,?,?&nbsp;&nbsp;&nbsp;&nbsp;?,?,?,?,?,same&nbsp;&nbsp;&nbsp;}</a>&nbsp;&nbsp;G3<br><br>
#           <a href="#">{&nbsp;&nbsp;&nbsp;?,?,?,?,?,?&nbsp;&nbsp;&nbsp;}</a>&nbsp;&nbsp;G0,G1,G2
#       </li>
#     </ul>
#   </div> -->
#   <!-- Optional JavaScript -->
#   <!-- jQuery first, then Popper.js, then Bootstrap JS -->