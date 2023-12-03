def search_str(file_path, word):
    with open(file_path, 'r') as file:
        # read all content of a file
        content = file.read()
        # check if string present in a file
        if word in content:
            print('string exist in a file')
        else:
            print('string does not exist in a file')

search_str(r'D:\BMW_Repo\Entwicklung\IPM_HIL_Mxx\work\CFD_Projekte\CFD_Anwendung\ELA_SX_BF3__TEE1_Gen5WE_B1__TEE2_C1__CCU_11kW_C2__BMU_C_2020_iLD_C__BM.txt', 'BMU_Neu')