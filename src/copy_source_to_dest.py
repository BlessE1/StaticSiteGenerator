import os
import shutil

def delete_dir_contents(dir):
   dir_path = os.path.abspath(dir)

   if os.path.exists(dir_path):
      shutil.rmtree(dir_path)
      os.mkdir(dir_path)
      return

   raise Exception(f"{dir} is not a directory")

def copy_source_to_dest(working_dir, source_dir, dest_dir):
   source_path = os.path.join(working_dir, source_dir)
   dest_path = os.path.join(working_dir, dest_dir)

   with os.scandir(source_path) as curr_dir:
      for item in curr_dir:
         if item.is_dir():
            new_dest_path = os.path.join(dest_dir, item.name)
            os.mkdir(new_dest_path)
            copy_source_to_dest(working_dir, item.path, new_dest_path)

         if item.is_file():
            shutil.copy(item.path, dest_path)

def copy_from_source_to_destination(wrk_dir, src_dir, dst_dir):
   delete_dir_contents(dst_dir)
   copy_source_to_dest(wrk_dir, src_dir, dst_dir)
