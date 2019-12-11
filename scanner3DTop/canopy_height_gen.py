#!/usr/bin/python
import os
import subprocess
import sys

def main(plot_name,meta_data):
""" sudo ./main_python.py  path/insert_plot_name.py path/metadata.json  """



    cmd="""sudo docker run --rm -u root -v "$(pwd)":/mnt -w /mnt agpipeline/canopy_height:2.0 --working_space "/mnt/{filename}" --result print --metadata "/mnt/{filename}/{json_name}" "/mnt/{filename}/{lasname}" """
    lis_dir = [ os.path.join(os.getcwd(), name) for name in os.listdir(os.getcwd()) if os.path.isdir(os.path.join(os.getcwd(), name)) ]


    for i in lis_dir:
	
        #run.run(meta_data,clean_metadata,i.split("/")[-1])
        cmd_run_plot_name="""sudo {} {} "{}/meta_edited.json" "{}" """.format(plot_name_code,meta_data,i,i.split("/")[-1])
        p=subprocess.Popen(cmd_run_plot_name, shell =True, stdout=subprocess.PIPE)
        stdout_value = p.communicate()[0] 

        las_file=[j for j in os.listdir(i) if ".las" in j]
        json_file=[j for j in os.listdir(i) if ".json" in j]
        cmd_run_docker = cmd.format(filename=i.split("/")[-1],json_name=json_file[0],lasname=las_file[0])
        print(cmd_run_docker)
        p=subprocess.Popen(cmd_run_docker, shell =True, stdout=subprocess.PIPE)
	stdout_value = p.communicate()[0]

        
if __name__ == "__main__":
    
    plot_name_code = sys.argv[1]
    meta_data =sys.argv[2]
    main(plot_name_code,meta_data)
    
